from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/login")
def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@router.get("/register")
def register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@router.get("/cart-page", response_class=HTMLResponse)
def render_cart_page(request: Request):
    return templates.TemplateResponse(request, "cart.html", {"request": request})





