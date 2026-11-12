from app.database import SessionLocal, engine
from app import models

def seed_data():
    db = SessionLocal()
    
    # Check if products already exist to avoid duplicate entries
    existing_products = db.query(models.Product).first()
    if existing_products:
        print("Database already contains data!")
        db.close()
        return

    # 1. Create Sample Categories
    tech = models.Category(name="Electronics")
    fashion = models.Category(name="Fashion")
    db.add_all([tech, fashion])
    db.commit()

    # 2. Create Sample Products
    p1 = models.Product(
        title="Wireless Noise-Canceling Headphones",
        description="High-fidelity audio with active noise cancellation and 30-hour battery life.",
        price=120.00,
        stock=15,
        category_id=tech.id
    )
    p2 = models.Product(
        title="Developer Mechanical Keyboard",
        description="Tactile mechanical switches with customizable RGB lighting and ergonomic build.",
        price=85.50,
        stock=25,
        category_id=tech.id
    )
    p3 = models.Product(
        title="Minimalist Laptop Backpack",
        description="Water-resistant 15.6-inch laptop bag with built-in USB charging port.",
        price=45.00,
        stock=40,
        category_id=fashion.id
    )

    db.add_all([p1, p2, p3])
    db.commit()
    db.close()
    print("Database successfully seeded with sample categories and products!")

if __name__ == "__main__":
    seed_data()
