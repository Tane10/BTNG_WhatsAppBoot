#from pymongo import MongoClient
#
#client = MongoClient()
#client = MongoClient('mongodb://localhost:27017')
#
#db = client['pymongo_test']


TESTLOAN = "Name: Susin\r\n" \
           "Age: 24 \r\n" \
           "Date of Birth: 06-06-1995 \r\n" \
           "Contact Number: +234-832-55657-1 >\r\n" \
           "Breif: Hair dressers \r\n" \
           "Address: 5, Tomary Close, Zone 3,Wuse,Abuja\r\n" \
           "Zip Code: 900288 \r\n" \
           "Amount Required: 2197705.60 \r\n"



def addloans(loandetail):
    loan_application = loandetail.splitlines()
    emptyObj = {
        "name": "" ,
        "Age": "" ,
        "Date": "" ,
        "Contact": "" ,
        "Breif": "" ,
        "Address": "" ,
        "Zip Code": "" ,
        "Amount": "" ,
        "Required": ""
    }
    for i in loan_application:
        split_deatil = i.split(":")
        del split_deatil[0]


addloans(TESTLOAN)
#posts = db.posts
#post_data = {
#    'title': 'Python and MongoDB',
#    'content': 'PyMongo is fun, you guys',
#    'author': 'Scott'
#}
#result = posts.insert_one(post_data)
#print('One post: {0}'.format(result.inserted_id))