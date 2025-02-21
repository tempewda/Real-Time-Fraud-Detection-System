from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
import shap
from sklearn.ensemble import RandomForestClassifier

# Load or train your model (replace with your actual model)
model = RandomForestClassifier()
# Example: Train the model (replace with your actual training logic)
X_train = pd.DataFrame({'amount': [100, 200, 300], 'age': [25, 35, 45]})
y_train = [0, 1, 0]  # 0 = Not Fraud, 1 = Fraud
model.fit(X_train, y_train)

def home(request):
    return render(request, 'frontend/home.html')

def custom_input(request):
    if request.method == 'POST':
        # Process user input and predict fraud
        amount = float(request.POST.get('amount'))
        age = int(request.POST.get('age'))
        data = pd.DataFrame({'amount': [amount], 'age': [age]})
        prediction = model.predict(data)[0]
        result = "Fraud" if prediction == 1 else "Not Fraud"
        return JsonResponse({'prediction': result})
    return render(request, 'frontend/custom_input.html')

def real_time_tracking(request):
    # Simulate real-time data and predict fraud
    data = pd.DataFrame({'amount': [150], 'age': [30]})  # Replace with real-time data
    prediction = model.predict(data)[0]
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