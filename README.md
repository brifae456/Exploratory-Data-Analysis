# EDA Project

For this project, you’ll work with data from Instacart.

Instacart is a grocery delivery platform where customers can place a grocery order and have it delivered to them, similar to how Uber Eats and Door Dash work. This particular dataset was publicly released by Instacart in 2017 for a Kaggle competition. Although the original dataset is no longer available on the Instacart website, we’ve created CSV files that contain a modified version of that data. Download these files and use them for your project.

The dataset we've provided for you has been modified from the original. We've reduced the size of the dataset so that your calculations run faster and we’ve introduced missing and duplicate values. We were also careful to preserve the distributions of the original data when we made our changes.

Your mission is to clean up the data and prepare a report that gives insight into the shopping habits of Instacart customers.

## Data dictionary
There are five tables in the dataset, and you’ll need to use all of them to do your data preprocessing and EDA. Below is a data dictionary that lists the columns in each table and describes that data that hold.

`instacart_orders.csv`: each row corresponds to one order on the Instacart app
- **order_id**: ID number that uniquely identifies each order
- **user_id**: ID number that uniquely identifies each customer account
- **order_number**: the number of times this customer has placed an order
- **order_dow**: day of the week that the order placed (which day is 0 is uncertain)
- **order_hour_of_day**: hour of the day that the order was placed
- **days_since_prior_order**: number of days since this customer placed their previous order

`products.csv`: each row corresponds to a unique product that customers can buy
- **product_id**: ID number that uniquely identifies each product
- **product_name**: name of the product
- **aisle_id**: ID number that uniquely identifies each grocery aisle category
- **department_id**: ID number that uniquely identifies each grocery department category

`order_products.csv`: each row corresponds to one item placed in an order
- **order_id**: ID number that uniquely identifies each order
- **product_id**: ID number that uniquely identifies each product
- **add_to_cart_order**: the sequential order in which each item was placed in the cart
- **reordered**: 0 if the customer has never ordered this product before, 1 if they have

`aisles.csv`:
- **aisle_id**: ID number that uniquely identifies each grocery aisle category
- **aisle**: name of the aisle

`departments.csv`:
- **department_id**: ID number that uniquely identifies each grocery department category
- **department**: name of the department

## Stages
Your project will consist of three stages:
 1) Open the data files 
 2) Preprocess the data
 3) Perform analysis on the data
