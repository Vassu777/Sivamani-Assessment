# Sivamani-Assessment

# Django RESTful API for Product Catalog

## Overview

This project is a Django-based RESTful API for managing a product catalog with basic user authentication. It includes endpoints to register a user, list products, add a new product, and get product details.

## Django Models

### Product Model

The `Product` model represents product data in the system.

- **Fields:**
  - `name`: Name of the product (CharField, max length 255).
  - `description`: Description of the product (TextField).
  - `price`: Price of the product (DecimalField, max digits 10, decimal places 2).

### UserProfile Model

The `UserProfile` model extends the built-in `User` model to include additional user profile information.

- **Fields:**
  - `user`: One-to-One relationship with the built-in `User` model.

## API Endpoints

### User Endpoints

- **GET /api/users/**: List all users
- **POST /api/users/**: Register a new user
- **GET /api/users/{id}/**: Get user details by ID
- **PUT /api/users/{id}/**: Update user details by ID
- **DELETE /api/users/{id}/**: Delete a user by ID

### Product Endpoints

- **GET /api/products/**: List all products
- **POST /api/products/**: Add a new product
- **GET /api/products/{id}/**: Get product details by ID
- **PUT /api/products/{id}/**: Update product details by ID
- **DELETE /api/products/{id}/**: Delete a product by ID

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Vassu777/Sivamani-Assessment.git
cd Sivamani-Assessment
