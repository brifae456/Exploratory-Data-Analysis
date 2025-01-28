#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd #library
import matplotlib.pyplot as plt #library


# In[2]:


# loading datasets
orders = pd.read_csv('/datasets/instacart_orders.csv', sep=';') 
products = pd.read_csv('/datasets/products.csv', sep=';')
order_products = pd.read_csv('/datasets/order_products.csv', sep=';')
aisles = pd.read_csv('/datasets/aisles.csv', sep=';')
departments = pd.read_csv('/datasets/departments.csv', sep=';')


# ## Find and remove duplicate values (and describe why you make your choices)

# ### `orders` data frame

# In[3]:


# Check for duplicated orders
orders.duplicated().sum()


# In[4]:


# Check for all orders placed Wednesday at 2:00 AM
#'order_dow' helps to narrow to give the day of the week, assuming Sunday=0 and Wednesday=3
orders[(orders['order_dow'] == 3) & (orders['order_hour_of_day'] == 2)]


# In[5]:


# Remove duplicate orders
orders = orders.drop_duplicates()


# In[6]:


# Double check for duplicate rows
orders.duplicated().sum()


# In[7]:


# Double check for duplicate order IDs only
orders['order_id'].duplicated().sum()


# ### `products` data frame

# In[8]:


# Check for fully duplicate rows
products.duplicated().sum()


# In[9]:


# Check for just duplicate product IDs
products['product_id'].duplicated().sum()


# In[10]:


# Check for just duplicate product names (convert names to lowercase to compare better)
products['product_name'].str.lower().duplicated().sum()


# In[11]:


# Check for duplicate product names that aren't missing
products[products['product_name'].str.lower().duplicated(keep=False)].sort_values('product_name').head(10)


# ### `departments` data frame

# In[12]:


departments.duplicated().sum()


# In[13]:


departments['department_id'].duplicated().sum()


# ### `aisles` data frame

# In[14]:


aisles.duplicated().sum()


# In[15]:


aisles['aisle_id'].duplicated().sum()


# ### `order_products` data frame

# In[16]:


# Check for fullly duplicate rows
order_products.duplicated().sum()


# In[17]:


# Double check for any other tricky duplicates
order_products[['order_id', 'product_id']].duplicated().sum()


# ## Find and remove missing values
# 

# ### `products` data frame

# In[18]:


products.info(), products.isnull().sum()


# In[19]:


# Are all of the missing product names associated with aisle ID 100?
products[products['product_name'].isnull()]['aisle_id'].value_counts()


# In[20]:


# Are all of the missing product names associated with department ID 21?
products[products['product_name'].isnull()]['department_id'].value_counts()


# In[21]:


# What is this ailse and department?
display(aisles[aisles['aisle_id'] == 100])
display(departments[departments['department_id'] == 21])


# In[22]:


# Fill missing product names with 'Unknown'
products['product_name'] = products['product_name'].fillna('Unknown')


# ### `orders` data frame

# In[23]:


orders.info()


# In[24]:


# Are there any missing values where it's not a customer's first order?
orders[orders['days_since_prior_order'].isnull() & (orders['order_number'] > 1)]


# ### `order_products` data frame

# In[25]:


order_products.info()


# In[26]:


# What are the min and max values in this column?
order_products['add_to_cart_order'].min(), order_products['add_to_cart_order']


# In[27]:


# Save all order IDs with at least one missing value in 'add_to_cart_order'
missing_cart_order = order_products[order_products['add_to_cart_order'].isnull()]['order_id']


# In[28]:


# Do all orders with missing values have more than 64 products?
display(order_products[order_products['order_id'].isin(missing_cart_order)]['order_id'].value_counts().head(10))
order_products[order_products['order_id'].isin(missing_cart_order)]['order_id'].value_counts().min()


# In[29]:


# Replace missing values with 999 and convert column to integer type
order_products['add_to_cart_order'] = order_products['add_to_cart_order'].fillna(999).astype(int)


# ##  Verify that the `'order_hour_of_day'` and `'order_dow'` values in the `orders` tables are sensible (i.e. `'order_hour_of_day'` ranges from 0 to 23 and `'order_dow'` ranges from 0 to 6)

# In[30]:


orders['order_hour_of_day'].value_counts().sort_index()


# In[31]:


orders['order_dow'].value_counts().sort_index()


# ### [A2] What time of day do people shop for groceries?

# In[32]:


orders['order_hour_of_day'].value_counts().sort_index().plot.bar(figsize = (10, 5))
plt.xlabel('Hour of Day')
plt.ylabel('Number of Orders')
plt.title('Number of Orders by Hour of Day')
plt.show()


# ##  What day of the week do people shop for groceries?

# In[33]:


orders['order_dow'].value_counts().sort_index().plot.bar(figsize = (10, 5))
plt.xlabel('Day of Week')
plt.ylabel('Number of Orders')
plt.title('Number of Orders by Day of Week')
plt.show()


# ### [A4] How long do people wait until placing another order?

# In[34]:


orders['days_since_prior_order'].min(), orders['days_since_prior_order'].max()


# 

# In[35]:


# Charting Number of Orders by Days Since Prior Order
orders['days_since_prior_order'].value_counts().sort_index().plot.bar(figsize = (10, 5))
plt.xlabel('Days Since Prior Order')
plt.ylabel('Number of Orders')
plt.title('Number of Orders by Days Since Prior Order')
plt.show()


# # [B] Medium (must complete all to pass)

# ### [B1] Is there a difference in `'order_hour_of_day'` distributions on Wednesdays and Saturdays? Plot the histograms for both days and describe the differences that you see.

# In[36]:


# Plotting Wed. and Sat.
b, bins, patches = plt.hist(
    [orders[orders['order_dow'] == 3]['order_hour_of_day'], orders[orders['order_dow'] == 6]['order_hour_of_day']],
    bins = 24,
    label = ['Wednesday', 'Saturday'],
)
plt.legend()
plt.xlabel('Hour of Day')
plt.ylabel('Number of Orders')
plt.title('Number of Orders by Hour of Day on Wednesdays and Saturdays')
plt.show()


# 

# ### [B2] What's the distribution for the number of orders per customer?

# In[37]:


display(orders.groupby('user_id')['order_number'].max().value_counts().head(5))
display(orders.groupby('user_id')['order_number'].max().mean())


# In[38]:


# Plot the distribution
orders.groupby('user_id')['order_id'].nunique().plot.hist(bins = 25, figsize = (10, 5))
plt.xlabel('Number of Orders')
plt.ylabel('Number of Customers')
plt.title('Number of Orders per Customer')
plt.show()


# ## What are the top 20 popular products (display their id and name)?

# In[39]:


# Merge data frames
merged_products = pd.merge(order_products, products, on = 'product_id', how = 'left')
merged_products.head(20)


# In[40]:


# Find the count of the product_name
merged_products.groupby(['product_name', 'product_id'])['product_name'].count().sort_values(ascending = False).head(20)


# 

# # Hard (must complete at least two to pass)

# ### [C1] How many items do people typically buy in one order? What does the distribution look like?

# In[41]:


# Merge the data frames
order_frequency = pd.merge(orders, order_products, on = 'order_id', how = 'left')
order_frequency.reset_index()
display(order_frequency.head(20))


# In[42]:


# Getting the mean
order_frequency['order_id'].value_counts().mean()


# In[43]:


# Chart that shows number of items and orders. 
order_frequency['order_id'].value_counts().plot.hist(bins = 20, figsize = (10, 5))
plt.xlabel('Number of Items')
plt.ylabel('Number of Orders')
plt.title('Number of Items per Order')
plt.show()


# ## What are the top 20 items that are reordered most frequently (display their names and product IDs)?

# In[44]:


# Finding the total or sum of reorders
merged_products.groupby(['product_name', 'product_id'])['reordered'].sum().sort_values(ascending = False).head(20)


# 

# ## What are the top 20 items that people put in their carts first? 

# In[45]:


# Find the first item people put into carts first
merged_products=merged_products[merged_products['add_to_cart_order'] == 1]


# In[46]:


merged_products.groupby(['product_id', 'product_name'])['add_to_cart_order'].count().sort_values(ascending = False).head(20)


# 
