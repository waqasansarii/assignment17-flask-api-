import db
from query import add_category,get_category,get_product,add_prdoucts,update_product,delete_product,get_products_with_category,product_count
from flask import Flask,request

app = Flask(__name__)
db_conn = db.mysqlconnect()

# add new category endpoint 
@app.route('/category/', methods=['POST'])
def create_category():
    body = request.get_json()
    if 'name' in body:
        name = body['name']
        add_category(db_conn , name)
        return {
            "message": f"{name} category has been added"
        }
    else:
        return {
            "message":"name field is required!"
        }    



# add new product endpoint 
@app.route('/product/', methods=['POST'])
def create_product():
    body = request.get_json()
    if 'name' not in body or 'cat_id' not in body:
        return {
            "message": "Both 'name' and 'cat_id' fields are required."
        }
    try:
        cat_id = int(body['cat_id'])
    except ValueError as e:
        # print(e)
        return {
            "message": "invalid category id"
        }    
    name = body['name']
    categories = get_category(db_conn)
    is_cat_exists = next((cat for cat in categories if int(cat['id']) == cat_id), None)
    if is_cat_exists:
        add_prdoucts(db_conn , name,cat_id)
        return{
            "message": f"{name} has been added"
        }
    else:
        return{
            "message":"category id is not exists"
        }    


# update product with path params endpoint 
@app.route('/product/<id>', methods=['PUT'])
def update_products(id):
    body = request.get_json()
    if 'name' not in body:
        return {
            "message": " name is required."
        }
    try:
        id = int(id)
    except ValueError as e:
        # print(e)
        return {
            "message": "invalid product id"
        }    
    name = body['name']
    products = get_product(db_conn)
    is_product_exists = next((product for product in products if int(product['id']) == id), None)
    if is_product_exists:
        update_product(db_conn ,name,id)
        return{
            "message": f"{name} has been updated"
        }
    else:
        return{
            "message":"product id is not exists"
        }    



# delete product endpoint 
@app.route('/product/<id>', methods=['DELETE'])
def delete_products(id):
    try:
        id = int(id)
    except ValueError as e:
        # print(e)
        return {
            "message": "invalid product id"
        }    
    products = get_product(db_conn)
    is_product_exists = next((product for product in products if int(product['id']) == id), None)
    if is_product_exists:
        delete_product(db_conn ,id)
        return{
            "message": f"{is_product_exists['name']} has been deleted"
        }
    else:
        return{
            "message":"product id is not exists"
        }    


# get all products endpoint 
@app.route('/products/', methods=['GET'])
def get_all_products():
    products = get_product(db_conn)
    return{
        "message":"products fetched successfully",
        "data" : products
    }   


# get category endpoint 
@app.route('/category/', methods=['GET'])
def get_all_category():
    categories = get_category(db_conn)
    return{
        "message":"categories fetched successfully",
        "data" : categories
    }   


# get products with category name endpoint 
@app.route('/combined_product/', methods=['GET'])
def get_category_product():
    data = get_products_with_category(db_conn)
    return{
        "message":"combined product with category fetched successfully",
        "data" : data
    }   


# getting number of products endpoint 
@app.route('/product_count/', methods=['GET'])
def count_product():
    data = product_count(db_conn)
    return{
        "message":f"Total {data[0]['total_products']} products available",
        "data" : data
    }   

    
app.run(
    debug=True,
    port=5000
)   