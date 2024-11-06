from django.shortcuts import render
import pandas as pd
import pickle
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# Create your views here.
def home_view(request):
    return render(request ,"home.html", {})


model = pickle.load(open("model.sav", "rb"))
df_1 = pd.read_csv("customer_service.csv")
@csrf_exempt

def data_view(request):
 
 df_1 = pd.read_csv('customer_service.csv')  # Read the data from the Excel file
 data_rows = df_1.head(5)  # Retrieve the first 10 rows

# Machine Learning Code
 if request.method == 'POST':
        # Get form input values
        input_query1 = request.POST.get('query1')
        input_query2 = request.POST.get('query2')
        input_query3 = request.POST.get('query3')
        input_query4 = request.POST.get('query4')
        input_query5 = request.POST.get('query5')
        input_query6 = request.POST.get('query6')
        input_query7 = request.POST.get('query7')
        input_query8 = request.POST.get('query8')
        input_query9 = request.POST.get('query9')
        input_query10 = request.POST.get('query10')
        input_query11 = request.POST.get('query11')
        input_query12 = request.POST.get('query12')
        input_query13 = request.POST.get('query13')
        input_query14 = request.POST.get('query14')
        input_query15 = request.POST.get('query15')
        input_query16 = request.POST.get('query16')
        input_query17 = request.POST.get('query17')
        input_query18 = request.POST.get('query18')
        input_query19 = request.POST.get('query19')



        data = [[input_query1, input_query2, input_query3, input_query4, input_query5, input_query6, input_query7,
                 input_query8, input_query9, input_query10, input_query11, input_query12, input_query13, input_query14,
                 input_query15, input_query16, input_query17, input_query18, input_query19]]

        new_df = pd.DataFrame(data, columns=['SeniorCitizen', 'MonthlyCharges', 'TotalCharges', 'gender',
                                             'Partner', 'Dependents', 'PhoneService', 'MultipleLines',
                                             'InternetService', 'OnlineSecurity', 'OnlineBackup',
                                             'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies',
                                             'Contract', 'PaperlessBilling', 'PaymentMethod', 'tenure'])

        df_2 = pd.concat([df_1, new_df], ignore_index=True)
        # Group the tenure in bins of 12 months
        labels = ["{0} - {1}".format(i, i + 11) for i in range(1, 72, 12)]

        df_2['tenure_group'] = pd.cut(df_2.tenure.astype(int), range(1, 80, 12), right=False, labels=labels)
        # Drop column customerID and tenure
        df_2.drop(columns=['tenure'], axis=1, inplace=True)

        new_df_dummies = pd.get_dummies(df_2[['gender', 'Partner', 'Dependents', 'PhoneService',
                                      'MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup',
                                      'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies',
                                      'Contract', 'PaperlessBilling', 'PaymentMethod', 'tenure_group']],
                               prefix=['gender', 'Partner', 'Dependents', 'PhoneService',
                                       'MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup',
                                       'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies',
                                       'Contract', 'PaperlessBilling', 'PaymentMethod', 'tenure_group'],
                               prefix_sep='_')
        
        new_df_dummies.insert(0, 'SeniorCitizen', df_2['SeniorCitizen'])
        new_df_dummies.insert(1, 'MonthlyCharges', df_2['MonthlyCharges'])
        new_df_dummies.insert(2, 'TotalCharges', df_2['TotalCharges'])

        single = model.predict(new_df_dummies.tail(1))
        probability = model.predict_proba(new_df_dummies.tail(1))[:, 1]
        
        if single == 1:
            output1 = "This customer is likely to be churned!"
            output2 = "Confidence: {}".format(probability * 100)
        else:
            output1 = "This customer is likely to continue!"
            output2 = "Confidence: {}".format(probability * 100)

        response = {
            'output1': output1,
            'output2': output2
        }

        return JsonResponse(response)

        
 
 return render(request ,"data.html", {'data_rows': data_rows })

    

