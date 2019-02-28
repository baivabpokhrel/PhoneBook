import mysql.connector


# DB name phonebook
# Table name users
# cannpt have two same phone numbers

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

def login_check(phone_,password_):
    pass


def user_exists_check(phone_):
    pass

def add_relation(name_,relation_):
    pass
#change based on phone_numbr

def delete_relation(name_,relation_):
    pass
# change based on phone_number

def return_specific_details(name_):
    pass

