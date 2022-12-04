
from flask import Flask, render_template,request,  url_for
from currency import *
from weather import *
from finance import * 


app= Flask(__name__)
app.config.from_object(__name__)


@app.route('/',methods= ['GET','POST'])
def Converter():
    if request.method=="GET":
        data=Weather().report()
        finance= FinanceNews().newsData()
        return render_template("convert.html",data=data,finance=finance)

        

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
                results.append(round(conVert))
        data= {'from':results[0], 'to':results[1],'amount':results[2],'convertion':results[3]}
        report=Weather().report()
        return render_template("main.html",data=data,report=report)









if __name__=="__main__":
    
    app.run(debug=True)
    

