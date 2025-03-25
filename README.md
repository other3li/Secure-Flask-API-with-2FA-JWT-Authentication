# Secure Flask API with 2FA & JWT Authentication

## 🚀 Project Overview
This project is a **Flask-based REST API** that implements secure authentication using **JWT Tokens** and **Two-Factor Authentication (2FA)** via **Google Authenticator**. The API allows user registration, login, and CRUD operations on a `Products` database table.

---

## 👨‍💻 Developed by
This project was created by **[Ali Mohamed Abdelmonem Ekab 😎😎😎]**.

---

## 📂 Features
✅ **User Registration** (with hashed passwords & 2FA secret generation)  
✅ **Google Authenticator 2FA Setup** (QR Code generation)  
✅ **Login with Username, Password & 2FA**  
✅ **JWT Authentication** for secure API access  
✅ **CRUD operations on Products** (Create, Read, Update, Delete)  
✅ **MySQL Database Integration**  

---

## 🛠️ Setup Instructions

### 1️⃣ Install Required Dependencies
Run the following command to install all required dependencies:
```bash
pip install Flask Flask-MySQLdb Flask-JWT-Extended bcrypt pyotp qrcode Pillow
```

### 2️⃣ Configure Database (MySQL)
Ensure you have MySQL installed and create a database:
```sql
CREATE DATABASE secure_api;
USE secure_api;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(256) NOT NULL,
    twofa_secret VARCHAR(256) NOT NULL
);

CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    description VARCHAR(255),
    price DECIMAL(10,2),
    quantity INT
);
```

### 3️⃣ Run the Flask Server
```bash
python app.py
```
If everything is set up correctly, Flask will run on:
```
http://127.0.0.1:5000/
```

---

## 📌 API Endpoints

### 🟢 User Authentication

#### **1️⃣ Register a new user**
```http
POST /auth/register
```
**Body (JSON):**
```json
{
    "username": "testuser",
    "password": "securepassword"
}
```

#### **2️⃣ Generate QR Code for Google Authenticator**
```http
GET /auth/generate_qr/testuser
```

#### **3️⃣ Login with Username & Password**
```http
POST /auth/login
```
**Body (JSON):**
```json
{
    "username": "testuser",
    "password": "securepassword"
}
```

#### **4️⃣ Login with 2FA Code to Get JWT Token**
```http
POST /auth/login
```
**Body (JSON):**
```json
{
    "username": "testuser",
    "password": "securepassword",
    "code": "123456"
}
```

---

### 🔒 Secured CRUD Operations (Requires JWT Token)

#### **5️⃣ Create a Product**
```http
POST /api/products
```
**Headers:**
```
Authorization: Bearer YOUR_JWT_TOKEN
```
**Body (JSON):**
```json
{
    "name": "Gaming Laptop",
    "description": "Powerful laptop for gaming",
    "price": 2000.00,
    "quantity": 5
}
```

#### **6️⃣ Get All Products**
```http
GET /api/products
```
**Headers:**
```
Authorization: Bearer YOUR_JWT_TOKEN
```

---

## 🎯 Next Steps
- ✅ Improve token expiration handling
- ✅ Add role-based access control (RBAC)
- ✅ Implement refresh tokens

---

## 💡 Contributing
Feel free to fork this repo, create a new branch, and submit a PR. Contributions are always welcome! 🎉

---

## 📜 License
This project is licensed under the MIT License.

