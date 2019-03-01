import mysql.connector


# DB name phonebook
# Table name : users and user-relation
# cannot have two same phone numbers
global cnx,my_cursor
cnx = mysql.connector.connect(host='localhost',user='baivab',
                              password='baivab12345', database='phonebook')
my_cursor=cnx.cursor()


def insert_into(name_,email_,phone_,password_):
    sql_query=("INSERT INTO users (name,email,phone,password) VALUES (%s,%s,%s,%s)")
    data_user= (name_,email_,phone_,password_)
    my_cursor.execute(sql_query, data_user)
    cnx.commit()


# DELETE USING A PHONE NUMBER
def delete_specific(phone_):
    my_cursor.execute("DELETE FROM users WHERE phone = '%s'"%phone_)
    cnx.commit()


def login_check(phone_,password_):
    password=''
    my_cursor.execute("SELECT password FROM users WHERE phone = {}".format(phone_))
    for i in my_cursor:
        password= i
    if(password[0]==password_):
        return True
    else:
        return False



def user_exists_check(phone_):
    if(get_name(phone_)=='NULL'):
        return False
    else:
        return True

def add_relation(user_phone,relation_phone):
    pass
#change based on phone_numbr

def delete_relation(user_phone,relation_phone):
    pass
# change based on phone_number

def return_details(phone_):
    pass


def get_name(phone_):
    name=''

    my_cursor.execute("SELECT name FROM users WHERE phone = {}".format(phone_))


    for i in my_cursor:
        name= i

    #clean_name = name.replace("'","").replace(",","").replace(")","").replace("(","")
    if(name):
        return name[0]
    else:
        return 'NULL'



def check_valid_phone(phone_):
    if(phone_.isdigit()==True and len(phone_)==10):
        return True
    else:
        return False


def close_connection():
    cnx.close()
    print("Database Connection Successfully Closed")

#print(login_check('9179824044','Aforapple'))
