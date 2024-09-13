
def get_category(db_conn):
    cur = db_conn.cursor()
    query = 'select * from category'
    cur.execute(query)
    return cur.fetchall()


def get_product(db_conn):
    cur = db_conn.cursor()
    query = 'select * from product'
    cur.execute(query)
    return cur.fetchall()


def add_category(db_conn,name):
    cur = db_conn.cursor()
    query = f'''INSERT INTO category (name) VALUES 
        ('{name}')
        '''
    cur.execute(query)
    db_conn.commit()

def add_prdoucts(db_conn,name,cat_id):
    cur = db_conn.cursor()
    query = f'''INSERT INTO product (name,cat_id) VALUES ('{name}','{cat_id}')     
        '''
    cur.execute(query)
    db_conn.commit()
    

def update_product (db_conn,newVal,id):
    cur = db_conn.cursor()
    query = f'''UPDATE product SET name='{newVal}' WHERE id ='{id}'     
        '''
    try:
        cur.execute(query)
        db_conn.commit()
        print("Product updated successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")    


def delete_product(db_conn,value):
    cur = db_conn.cursor()
    query = f'''
        delete from product where id = '{value}';
    '''
    try:
        cur.execute(query)
        db_conn.commit()
        print("Product deleted successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")         



def product_count (db_conn):
    cur = db_conn.cursor()
    query = 'select count(*) as total_products from product'  
    cur.execute(query)
    return cur.fetchall()    

        
def get_products_with_category(db_conn):
    cur = db_conn.cursor()
    query = '''
               select
                  p.id as p_id, p.name as product_name,p.cat_id,c.name as category_name
               from
                  product as p 
               inner join
                  category as c 
                on
                  p.cat_id = c.id
                ''' 
    try:
        cur.execute(query)
        return cur.fetchall()
    except Exception as e:
        print(f"An error occurred: {e}")       