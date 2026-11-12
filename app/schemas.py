from pydantic import BaseModel, EmailStr
from typing import Optional, List

# --- Category Schemas ---
class CategoryBase(BaseModel):
    name: str

class CategoryResponse(CategoryBase):
    id: int

    class Config:
        from_attributes = True


# --- Product Schemas ---
class ProductCreate(BaseModel):
    title: str
    description: Optional[str] = None
    price: float
    stock: int
    category_id: int

class ProductResponse(ProductCreate):
    id: int
    category: Optional[CategoryResponse] = None

    class Config:
        from_attributes = True


# --- User Schemas ---
class UserCreate(BaseModel):
    full_name: str
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    email: str
    full_name: str
    is_active: bool

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str
