from fastapi import FastAPI, Depends, Request, HTTPException, status
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db, engine
from app import models, schemas, crud, database, security

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="ShopFast E-Commerce Platform",
    description="Full-stack E-Commerce Web Application built with FastAPI, PostgreSQL, Jinja2, and Tailwind CSS",
    version="1.0.0"
)

# Mount static files and setup Jinja2 template directory
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

from app.routers import auth as auth_router
app.include_router(auth_router.router)

from app.routers import pages
app.include_router(pages.router)


# ==========================================
# 1. FRONTEND HTML ROUTE CONTROLLERS
# ==========================================

@app.get("/", response_class=HTMLResponse)
def render_home_page(request: Request, db: Session = Depends(database.get_db)):
    products = db.query(models.Product).all()
    return templates.TemplateResponse(request, "index.html", {"products": products})



from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

'''
# Cart Page Route
@app.get("/cart-page", response_class=HTMLResponse)
def render_cart_page(request: Request):
    return templates.TemplateResponse("cart.html", {"request": request})

# Login Page Route
@app.get("/login-page")
def login_page(request: Request):
    return templates.TemplateResponse(request, "login.html")

@app.get("/register-page")
def register_page(request: Request):
    return templates.TemplateResponse(request, "register.html")

'''

# ==========================================
# 2. BACKEND REST API ENDPOINTS
# ==========================================

@app.get("/api/products", response_model=List[schemas.ProductResponse])
def get_all_products(db: Session = Depends(get_db)):
    """Public API endpoint returning the product catalog."""
    return crud.get_products(db)

@app.post("/api/products", response_model=schemas.ProductResponse, status_code=status.HTTP_201_CREATED)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    """Admin endpoint to seed/create new products in the catalog."""
    return crud.create_product(db, product)
