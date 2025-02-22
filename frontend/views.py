from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
import shap
from sklearn.ensemble import RandomForestClassifier
import joblib
import numpy as np


# Load or train your model (replace with your actual model)

model = joblib.load("frontend/models/fraud_detection_model.joblib")

# Example: Train the model (replace with your actual training logic)

def home(request):
    return render(request, 'frontend/home.html')

def custom_input(request):
    if request.method == 'POST':
        # Process user input and predict fraud
        amount = float(request.POST.get('amount'))
        amount = np.log1p(amount)
        category = str(request.POST.get('category'))
        city = str(request.POST.get('city'))
        job = str(request.POST.get('job'))
        frequency = int(request.POST.get('frequency'))

        data = pd.DataFrame([{
            'merch-lat': 40.2,
            'amt_log': amount,
            'category': -2.209382,
            'city': 4.484122,
            'job': -.0305748,
            'cc_num_frequency': frequency
        }])
        prediction = model.predict(data)[0]
        result = "Fraud" if prediction == 1 else "Not Fraud"
        context = {"result": result}
        return render(request, 'frontend/result.html' , context)
    return render(request, 'frontend/custom_input.html')
0
def real_time_tracking(request):
    # Simulate real-time data and predict fraud
    data = pd.DataFrame({'amount': [150], 'age': [30]})  # Replace with real-time data
    prediction = model.predict(data)[0]
    print(prediction)
    result = "Fraud" if prediction == 1 else "Not Fraud"
    return JsonResponse({'prediction': result})

def shap_explanation(request):
    # Generate SHAP values for the model
    data = pd.DataFrame({'amount': [150], 'age': [30]})  # Example input data
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(data)
    return JsonResponse({'shap_values': shap_values[0].tolist()})

def dashboard(request):
    # Generate plots for the dashboard (replace with actual plots)
    plots = {
        'age_vs_fraud': 'age_vs_fraud.png',
        'amount_vs_fraud': 'amount_vs_fraud.png',
    }
    return render(request, 'frontend/dashboard.html', {'plots': plots})



def result(request, context):
    return render(request, 'frontend/result.html', context)
