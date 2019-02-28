import mysql.connector


# DB name phonebook
# Table name users

cnx = mysql.connector.connect(host='localhost',user='baivab',
                              password='baivab12345', database='phonebook')
my_cursor=cnx.cursor()


def insert_into(name_,email_,phone_,password_):
    sql_query=("INSERT INTO users (name,email,phone,password) VALUES (%s,%s,%s,%s)")
    data_user= (name_,email_,phone_,password_)
    my_cursor.execute(sql_query, data_user)
    cnx.commit()
    cnx.close()

# DELETE USING A PHONE NUMBER
def delete_specific(phone_):
    my_cursor.execute("DELETE FROM users WHERE phone = '%s'"%phone_)
    cnx.commit()
    cnx.close()

def login_check(phone_,passoword_):

def user_exists_check(name_,email_,phone_,password_):

def add_relation(name_,relation_):

def delete_relation(name_,relation_)

def return_specific_details(name_)

