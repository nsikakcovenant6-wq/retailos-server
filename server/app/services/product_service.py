# server/app/services/product_service.py
from flask import request
from server.app.utils.response import Response
from server.app.extensions import db
from server.app.models.product import Product

class ProductService:
    def __init__(self):
        pass

    def get_user_store(self):
        pass

    def create_product(self):
        # Get request data
        data = request.get_json()

        # Validate request data
        if data is None:
            code = "VALIDATION_ERROR"
            message = "Invalid input data"
            fields = {
                "name": "Product name must be a string",
                "price": "Product price must be a number",
                "stock": "Product stock must be an integer",
                "low_stock_threshold": "Low stock threshold must be an integer"
            }
            return Response.error_response(code, message, fields), 400

        # Get authenticated user
        name = data.get("name")
        price = data.get("price")
        stock_quantity = data.get("stock_quantity")
        low_stock_threshold = data.get("low_stock_threshold")

        if not isinstance(name, str) or not isinstance(price, (int, float)) or not isinstance(stock_quantity, int) or not isinstance(low_stock_threshold, int):
            code = "VALIDATION_ERROR"
            message = "Invalid input data"
            fields = {
                "name": "Product name must be a string",
                "price": "Product price must be a number",
                "stock_quantity": "Product stock must be an integer",
                "low_stock_threshold": "Low stock threshold must be an integer"
            }
            return Response.error_response(code, message, fields), 400

        # Get user's store
        store = self.get_user_store()

        # Validate product data
        if name.isalnum():
            if price >= 0:
                if stock_quantity >= 0:
                    if low_stock_threshold >= 0 and low_stock_threshold < stock_quantity:
                        # Create product
                        product = Product(
                            name=name,
                            price=price,
                            stock_quantity=stock_quantity,
                            low_stock_threshold=low_stock_threshold,
                            store_id=store.id
                        )

                        # Save product
                        db.session.add(product)
                        db.session.flush()
                        db.session.commit()

                        # Build response data
                        data = {
                            "product": {
                                "id": product.id,
                                "name": product.name,
                                "price": product.price,
                                "stock_quantity": product.stock_quantity,
                                "low_stock_threshold": product.low_stock_threshold,
                                "created_at": product.created_at.isoformat()
                            }
                        }

                        # Return success response
                        message = "PRODUCT_CREATION_SUCCESSFUL"
                        return Response.success_response(message, data), 201

    def get_products(self):
        # Get authenticated user

        # Get user's store

        # Get products belonging to store

        # Build response data

        # Return success response


    def get_product(self, product_id):
        # Get authenticated user

        # Get user's store

        # Find product belonging to store

        # Check if product exists

        # Build response data

        # Return success response


    def update_product(self, product_id):
        # Get request data

        # Validate request data

        # Get authenticated user

        # Get user's store

        # Find product belonging to store

        # Check if product exists

        # Update allowed fields

        # Save changes

        # Build response data

        # Return success response


    def delete_product(self, product_id):
        # Get authenticated user

        # Get user's store

        # Find product belonging to store

        # Check if product exists

        # Delete product

        # Save changes

        # Return success response


    def adjust_stock(self, product_id):
        # Get request data

        # Validate quantity

        # Get authenticated user

        # Get user's store

        # Find product belonging to store

        # Check if product exists

        # Calculate new stock quantity

        # Prevent negative stock

        # Update stock

        # Save changes

        # Build response data

        # Return success response