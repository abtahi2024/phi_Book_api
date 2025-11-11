# 📚 PhiBook Management API

A complete RESTful API built with **Django + Django REST Framework + Djoser + JWT** for managing users, books, carts, and orders.  
This project also includes Swagger documentation at [`/swagger/`](http://127.0.0.1:8000/swagger/).

---

## 🚀 Features

- ✅ User registration, login, and profile management (with image upload)
- 🛒 Shopping cart and order management
- 📚 Book and category management
- 🔐 JWT-based authentication
- 🧾 Auto-generated API docs via Swagger (`drf_yasg`)
- 🧰 Built-in admin dashboard

---

## 🧩 Tech Stack

- **Backend:** Django, Django REST Framework  
- **Auth:** JWT + Djoser  
- **Database:** SQLite (default, easily switchable to PostgreSQL/MySQL)  
- **Docs:** Swagger (drf_yasg)

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone https://github.com/yourusername/phi-book-management.git
cd phi-book-management

python -m venv venv
venv\Scripts\activate 
`````
🧾 Admin Credentials (example)

- ****email: admin@admin.com****
- ****password: 1234****

# 🔐 Authentication & User Management API

## Endpoints for user registration, authentication (JWT), profile management, and password/email handling.
## Authentication system: Djoser + JWT (SimpleJWT)
### Base URL: /auth/ 
| Method   | Endpoint             | Description                              | Swagger Operation         |
| :------- | :------------------- | :--------------------------------------- | :------------------------ |
| **POST** | `/auth/jwt/create/`  | Obtain JWT access and refresh tokens     | `auth_jwt_create_create`  |
| **POST** | `/auth/jwt/refresh/` | Refresh access token using refresh token | `auth_jwt_refresh_create` |
| **POST** | `/auth/jwt/verify/`  | Verify if JWT token is valid             | `auth_jwt_verify_create`  |
### 👤 User Registration & Profile
| Method     | Endpoint            | Description                           | Swagger Operation           |
| :--------- | :------------------ | :------------------------------------ | :-------------------------- |
| **GET**    | `/auth/users/`      | Admin can list all users              | `auth_users_list`           |
| **POST**   | `/auth/users/`      | Register a new user                   | `auth_users_create`         |
| **GET**    | `/auth/users/{id}/` | Retrieve a specific user (Admin only) | `auth_users_read`           |
| **PUT**    | `/auth/users/{id}/` | Fully update user (Admin only)        | `auth_users_update`         |
| **PATCH**  | `/auth/users/{id}/` | Partially update user (Admin only)    | `auth_users_partial_update` |
| **DELETE** | `/auth/users/{id}/` | Delete user (Admin only)              | `auth_users_delete`         |
### 🙋 Current Authenticated User (/me/)
| Method     | Endpoint          | Description                                                | Swagger Operation              |
| :--------- | :---------------- | :--------------------------------------------------------- | :----------------------------- |
| **GET**    | `/auth/users/me/` | Get details of the currently logged-in user                | `auth_users_me_read`           |
| **PUT**    | `/auth/users/me/` | Update current user profile                                | `auth_users_me_update`         |
| **PATCH**  | `/auth/users/me/` | Partially update current user profile (e.g. profile image) | `auth_users_me_partial_update` |
| **DELETE** | `/auth/users/me/` | Delete user account                                        | `auth_users_me_delete`         |
### 📧 Account Activation & Resend
| Method   | Endpoint                         | Description                              | Swagger Operation              |
| :------- | :------------------------------- | :--------------------------------------- | :----------------------------- |
| **POST** | `/auth/users/activation/`        | Activate user account after registration | `auth_users_activation`        |
| **POST** | `/auth/users/resend_activation/` | Resend activation email                  | `auth_users_resend_activation` |

### 🔁 Email Management
| Method   | Endpoint                           | Description                                | Swagger Operation                   |
| :------- | :--------------------------------- | :----------------------------------------- | :---------------------------------- |
| **POST** | `/auth/users/set_email/`           | Set a new email for the authenticated user | `auth_users_set_username`           |
| **POST** | `/auth/users/reset_email/`         | Send email reset confirmation link         | `auth_users_reset_username`         |
| **POST** | `/auth/users/reset_email_confirm/` | Confirm email reset with token             | `auth_users_reset_username_confirm` |

### 🔒 Password Management
| Method   | Endpoint                              | Description                        | Swagger Operation                   |
| :------- | :------------------------------------ | :--------------------------------- | :---------------------------------- |
| **POST** | `/auth/users/set_password/`           | Change current password            | `auth_users_set_password`           |
| **POST** | `/auth/users/reset_password/`         | Request password reset email       | `auth_users_reset_password`         |
| **POST** | `/auth/users/reset_password_confirm/` | Confirm password reset using token | `auth_users_reset_password_confirm` |

# 📚 Books API

Endpoints related to Books, Book Images, and Book Reviews.
` Base URL: /books/ `

📖 Book 
| Method     | Endpoint       | Description                       | Swagger Operation      |
| :--------- | :------------- | :-------------------------------- | :--------------------- |
| **GET**    | `/books/`      | Everyone can view all books       | `books_list`           |
| **POST**   | `/books/`      | Admin can create a new book       | `books_create`         |
| **GET**    | `/books/{id}/` | View a single book by ID          | `books_read`           |
| **PUT**    | `/books/{id}/` | Admin can fully update a book     | `books_update`         |
| **PATCH**  | `/books/{id}/` | Admin can partially update a book | `books_partial_update` |
| **DELETE** | `/books/{id}/` | Admin can delete a book           | `books_delete`         |

🖼️ Book Images
| Method     | Endpoint                        | Description                            | Swagger Operation             |
| :--------- | :------------------------------ | :------------------------------------- | :---------------------------- |
| **GET**    | `/books/{book_pk}/images/`      | Everyone can view all images of a book | `books_images_list`           |
| **POST**   | `/books/{book_pk}/images/`      | Admin can upload and manage images     | `books_images_create`         |
| **GET**    | `/books/{book_pk}/images/{id}/` | View a specific book image             | `books_images_read`           |
| **PUT**    | `/books/{book_pk}/images/{id}/` | Admin can update an image              | `books_images_update`         |
| **PATCH**  | `/books/{book_pk}/images/{id}/` | Admin can partially edit an image      | `books_images_partial_update` |
| **DELETE** | `/books/{book_pk}/images/{id}/` | Admin can delete a book image          | `books_images_delete`         |

📝 Book Reviews
| Method     | Endpoint                         | Description                         | Swagger Operation              |
| :--------- | :------------------------------- | :---------------------------------- | :----------------------------- |
| **GET**    | `/books/{book_pk}/reviews/`      | Anyone can view reviews of a book   | `books_reviews_list`           |
| **POST**   | `/books/{book_pk}/reviews/`      | Admin can post and manage reviews   | `books_reviews_create`         |
| **GET**    | `/books/{book_pk}/reviews/{id}/` | View a single review by ID          | `books_reviews_read`           |
| **PUT**    | `/books/{book_pk}/reviews/{id}/` | Admin can fully update a review     | `books_reviews_update`         |
| **PATCH**  | `/books/{book_pk}/reviews/{id}/` | Admin can partially update a review | `books_reviews_partial_update` |
| **DELETE** | `/books/{book_pk}/reviews/{id}/` | Admin can delete a review           | `books_reviews_delete`         |


# 🛒 Cart API
Endpoints related to Carts and Cart Items.
`Base URL: /carts/`

🧺 Carts
| Method     | Endpoint       | Description                                   | Swagger Operation |
| :--------- | :------------- | :-------------------------------------------- | :---------------- |
| **GET**    | `/carts/`      | Everyone can view all carts                   | `carts_list`      |
| **POST**   | `/carts/`      | Authenticated users can create or add to cart | `carts_create`    |
| **GET**    | `/carts/{id}/` | View a single cart by ID                      | `carts_read`      |
| **DELETE** | `/carts/{id}/` | User can delete a specific cart               | `carts_delete`    |

🧾 Cart Items
| Method     | Endpoint                       | Description                               | Swagger Operation            |
| :--------- | :----------------------------- | :---------------------------------------- | :--------------------------- |
| **GET**    | `/carts/{cart_pk}/items/`      | View items in a specific cart             | `carts_items_list`           |
| **POST**   | `/carts/{cart_pk}/items/`      | User can add items to a cart              | `carts_items_create`         |
| **GET**    | `/carts/{cart_pk}/items/{id}/` | View details of a specific cart item      | `carts_items_read`           |
| **PATCH**  | `/carts/{cart_pk}/items/{id}/` | Update quantity or details of a cart item | `carts_items_partial_update` |
| **DELETE** | `/carts/{cart_pk}/items/{id}/` | Remove an item from the cart              | `carts_items_delete`         |


# 📦 Order API
| Method    | Endpoint                      | Description                   | Swagger Operation       |
| :-------- | :---------------------------- | :---------------------------- | :---------------------- |
| **GET**   | `/orders/`                    | Everyone can see the orders   | `orders_list`           |
| **POST**  | `/orders/`                    | Cart order ID POST            | `orders_create`         |
| **GET**   | `/orders/{id}/`               | View a specific order by ID   | `orders_read`           |
| **PATCH** | `/orders/{id}/`               | Update a specific order       | `orders_partial_update` |
| **POST**  | `/orders/{id}/cancel/`        | User can cancel their order   | `orders_cancel`         |
| **PATCH** | `/orders/{id}/update_status/` | Admin can update order status | `orders_update_status`  |

# 🏷️ Category API

## Endpoints for managing book categories.
### Permissions:

👀 Any user can view categories

🧑‍💼 Only admin users can create, edit, or delete categories
| Method     | Endpoint            | Access           | Description                      | Swagger Operation           |
| :--------- | :------------------ | :--------------- | :------------------------------- | :-------------------------- |
| **GET**    | `/categories/`      | Everyone 👥      | Retrieve all categories          | `categories_list`           |
| **POST**   | `/categories/`      | Admin only 🧑‍💼 | Create a new category            | `categories_create`         |
| **GET**    | `/categories/{id}/` | Everyone 👥      | Retrieve a single category by ID | `categories_read`           |
| **PUT**    | `/categories/{id}/` | Admin only 🧑‍💼 | Fully update a category          | `categories_update`         |
| **PATCH**  | `/categories/{id}/` | Admin only 🧑‍💼 | Partially update a category      | `categories_partial_update` |
| **DELETE** | `/categories/{id}/` | Admin only 🧑‍💼 | Delete a category                | `categories_delete`         |
