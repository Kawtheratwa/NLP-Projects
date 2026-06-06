from flask import Flask, request, jsonify, render_template
import pandas as pd
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)

# بيانات تدريب (30 مثال)
data = {
    'Age': [22,25,30,35,40,45,50,28,32,38,42,48,29,31,36,41,46,27,33,39,44,49,26,34,37,43,47,24,23,52],
    'Monthly_Income': [2000,2500,3000,4000,5000,6000,7000,3200,3500,4500,5200,6100,3300,3600,4200,5100,6200,2800,3700,4600,5300,6400,2700,3900,4400,5400,6500,2600,2400,7200],
    'Years_With_Company': [1,2,3,5,7,10,12,2,4,6,8,11,3,4,6,9,10,2,5,7,9,11,1,6,7,8,12,1,1,13],
    'Num_Products': [1,1,2,2,3,3,4,2,2,3,3,4,2,2,3,3,4,1,2,3,3,4,1,3,3,4,4,1,1,4],
    'Credit_Score': [600,620,650,680,700,720,750,640,660,690,710,730,645,665,695,705,725,630,670,700,720,740,610,680,690,710,735,605,600,760],
    'Support_Calls': [5,4,3,2,1,1,0,3,2,2,1,0,3,2,2,1,0,4,3,2,1,0,5,2,2,1,0,5,5,0],
    'Churn': [1,1,1,0,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,0,0,0,0,1,1,0]
}

df = pd.DataFrame(data)

X = df[['Age','Monthly_Income','Years_With_Company','Num_Products','Credit_Score','Support_Calls']]
y = df['Churn']

model = LogisticRegression()
model.fit(X, y)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    new_customer = pd.DataFrame([{
        'Age': float(data['age']),
        'Monthly_Income': float(data['income']),
        'Years_With_Company': float(data['years']),
        'Num_Products': float(data['products']),
        'Credit_Score': float(data['score']),
        'Support_Calls': float(data['calls'])
    }])

    prediction = model.predict(new_customer)[0]

    result = "Leave ❌" if prediction == 1 else "Stay ✅"

    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)