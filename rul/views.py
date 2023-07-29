from django.shortcuts import render 
import pickle

# Create your views here.
def home(request):
    return render(request,"home.html")

def result(request):
    if request.method == "POST":

         # Ambient_temperature
        ambient_temperature =float(request.POST.get("ambient_temperature"))
        voltage_measured= float(request.POST.get("voltage_measured"))
        current_measured = float(request.POST.get("current_measured"))
        temperature_measured= float(request.POST.get("temperature_measured"))
        voltage_load= float(request.POST.get("voltage_load"))
        current_load= float(request.POST.get("current_load"))
        time = float(request.POST.get("time(sec)"))
     
        
        model=pickle.load(open("rul.pkl","rb"))
        prediction=model.predict([[ambient_temperature,voltage_measured,current_measured,temperature_measured,voltage_load,current_load,time]])

        result = { "RUL": int(prediction[0])}
        
        return render(request,'home.html',{ 'prediction_text':f'The predicted Remaining Useful Life of Battery is {result["RUL"]} cycles'})
