from flask import Flask,render_template,request
import requests
import json
# app=Flask(__name__)
# @app.route("/")
# def index():
#     # return render_template("./index.html")
#     return render_template('hello.html')
# app.run(host="0.0.0.0",port=81)
app = Flask(__name__)  
def number_d(number):
    import phonenumbers
    # number= "+917011643631"
    from phonenumbers import geocoder
    from phonenumbers import carrier
    ch_number=phonenumbers.parse(number,"CH")
    location=geocoder.description_for_number(ch_number,"en")
    service_number=phonenumbers.parse(number,"RO")
    carrier_n=carrier.name_for_number(service_number,"en")
    return location,carrier_n

# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods =["GET", "POST"])
def no_inp():
    if request.method == "POST":
       # getting input with name = fname in HTML form
       countr_code = request.form.get("cc")
       # getting input with name = lname in HTML form
       ph_no = request.form.get("number")
       a=str(countr_code)
       b=str(ph_no)
       loc,car=  number_d(a+b)
       if(loc==None or car==None):
           return a+b +"is invalid"
       return render_template("post.html",loca=loc,carr=car)
    return render_template("index.html")
 
if __name__=='__main__':
   app.run(host="0.0.0.0",port=81)