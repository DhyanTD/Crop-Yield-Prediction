from flask import Flask, redirect, render_template
from flask import request
from numpy import append
import temp

app = Flask(__name__)

attributes = []
res=0

@app.route("/")
def hello_world():
    list = ["Bagalkot","Bangalore Rural","Bangalore Urban","Belgaum","Bellary","Bidar","Vijayapura","Chamarajanagar","Chikkaballapur","Chikkamagaluru","Chitradurga","Dakshina Kannada","Davanagere","Dharwad","Gadag","Gulbarga","Hassan","Haveri","Kodagu","Kolar","Koppal","Mandya","Mysore","Raichur","Ramanagara","Shivamogga","Tumkur","Udupi","Uttara Kannada","Yadgir"]
    return render_template("index.html", list=list)

@app.route("/gettemp", methods=["GET", "POST"])
def gettemp():
    # if(request.method == 'GET'):
    #     city = request.form.get('city')
    city = request.form.get("city")
    city = city+" weather"
    global res
    res = temp.weather(city)
    global attributes
    attributes.clear()
    attributes.append(res)
    # res=0
    return redirect("/data")

@app.route("/data", methods=['GET', 'POST'])
def data():
    global attributes
    global res
    
    if request.method == 'POST':
        attributes.clear()
        attributes.append(res)
        attributes.append(request.form.get('season'))
        attributes.append(request.form.get('crop'))
        attributes.append(request.form.get('N'))
        attributes.append(request.form.get('P'))
        attributes.append(request.form.get('K'))
        attributes.append(request.form.get('ph'))
        attributes.append(request.form.get('area'))
        

        for i in attributes:
            print(i)

        
        return redirect("/finaldata")
    return render_template('data.html')

@app.route("/finaldata", methods=['GET', 'POST']) 
def prediction():
    global attributes
    global res
    for i in attributes:
        print(i)
    import random
    r=random.randint(1,30)
    print(r)
    return render_template('finaldata.html',attributes=attributes, r=r) 


    
app.run(debug=True)

