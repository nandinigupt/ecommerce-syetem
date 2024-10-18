# Simplified ecommerce-syetem

## Overview
This project is a simplified e-commerce system designed to handle users, products, orders, and payments. It includes a system design with a class diagram, business logic for inventory management, and SQL queries for database operations. The project is modular, scalable, and follows clean coding practices.

## Project Structure
The project is divided into three parts:
1. **System Design**: A class diagram that represents the relationships between users, products, orders, and payments.
2. **Business Logic Implementation**: Functions for processing orders and managing inventory.
3. **Database Query Writing**: SQL queries to handle common operations in a relational database for an online bookstore.

## System Design
The system includes four main components:
- **User**: A user can create, view, and manage orders.
- **Product**: Products are available for purchase, and each has a price and stock level.
- **Order**: An order can contain multiple products, and each order has a status (pending, completed, shipped, etc.).
- **Payment**: A payment is made for each order.

The relationships are shown in the provided class diagram (`class_diagram.png`).

### Class Diagram:
The class diagram outlines the relationships between:
- **User**: Can have multiple orders.
- **Order**: Can contain multiple products and has one associated payment.
- **Product**: Managed with stock levels.
- **Payment**: Made for an order and contains payment details.

Check the diagram file `class_diagram.png` in the repository for a visual representation.

## Business Logic Implementation
Two key functions handle inventory management:
1. **process_orders(products, sales_orders)**:
    - Takes a list of products with their current stock levels and a list of incoming sales orders.
    - Reduces the stock levels based on the orders.
    - Triggers a restock alert if any product’s stock drops below a defined threshold (e.g., 10 units).
    
2. **restock_items(products_to_restock)**:
    - Takes a list of products and their required quantities.
    - Updates stock levels accordingly.

### Error Handling:
- Invalid inputs, such as trying to process an order when the product is out of stock, are handled.

## Database Query Writing
The SQL queries are designed for a relational database schema for an online bookstore. Here are the SQL queries provided:

1. **Top 5 customers who purchased the most books in the last year**
2. **Total revenue generated from book sales by each author**
3. **Books that have been ordered more than 10 times**

 Setup and Running the Project
Prerequisites
Git: Make sure you have Git installed on your machine.
MySQL or any RDBMS: You need a relational database setup like MySQL, PostgreSQL, etc.
SQLTools Plugin: Use SQLTools in VSCode for running queries.
Visual Studio Code or any preferred IDE for coding.
Steps
Clone the Repository:
git clone https://github.com/your-username/your-repository.git
cd your-repository
Set Up the Database:

Connect to your MySQL/PostgreSQL database using a tool like MySQL Workbench or pgAdmin.
Run the provided SQL queries to test the functionality.
Run the Code:

Implement the business logic by running the scripts provided in your preferred language.
For SQL queries, use an IDE or terminal to connect to the database and execute the queries.
Push to GitHub (for future changes):

bash
Copy code
git add .
git commit -m "Updated project with SQL queries and business logic"
git push origin master
Assumptions
The e-commerce system is designed to be scalable and modular.
Error handling is in place for invalid orders.
A MySQL database is used for the SQL queries, but it can be adapted to other RDBMS. 
