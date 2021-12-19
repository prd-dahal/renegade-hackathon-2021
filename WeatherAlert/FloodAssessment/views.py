from django.shortcuts import render, redirect
from django.http import HttpResponse
from FloodAssessment.learn import MachineLearning

m = MachineLearning()
# Create your views here.
def machineLearning(request):
    if(request.method == "POST"):
        country = request.POST["country"]
        city = request.POST["city"]
        risk_factor_question = float(request.POST['risk_factor'])
        risk_factor_ml = float(m.predict()[0])
        risk_factor = (risk_factor_question + risk_factor_ml)/2
        if(risk_factor<=0.3):
            risk_value ="Low"
        elif(risk_factor>0.3 and risk_factor<=0.7):
            risk_value ="Medium"
        elif(risk_factor>0.3 and risk_factor<=1):
            risk_value ="High"
        
        return render(request,"FloodAssessment/questions.html", {"risk_factor":risk_factor, "risk_value":risk_value} )
    return render(request, "FloodAssessment/questions.html")
