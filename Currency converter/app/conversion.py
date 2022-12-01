
from flask import Flask, render_template,request,  url_for
from currency import *


app= Flask(__name__)
app.config.from_object(__name__)


@app.route('/',methods= ['GET','POST'])
def Converter():
    if request.method=="GET":
        return render_template("convert.html")

    if request.method== "POST":
        amount=request.form['amount']
        fromCurr= request.form["from"]
        toCurr= request.form["to"]
        url= MoneyConverter(amount,fromCurr,toCurr)
        for key,value in url.apiReport().items():
            results=[]
            newDict= url.apiReport()["query"]
            for x,y in newDict.items():
                fromCurr=newDict["from"]
                toCurr=newDict["to"]
                amount=newDict["amount"]
                results.append(fromCurr)
                results.append(toCurr)
                results.append(amount)
                conVert=url.apiReport()["result"]
                results.append(conVert)
        data= {'from':results[0], 'to':results[1],'amount':results[2],'convertion':results[3]}
        
        return render_template("main.html",data=data)
    
    


if __name__=="__main__":
    
    app.run(debug=True)
    

