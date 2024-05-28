from flask import Flask,render_template,url_for,redirect,request,send_from_directory
import pickle
import numpy as np
# from sklearn.externals import joblib
from ml_deploy import predict_salary_api,predict_status_api

# model = joblib.load('model.pkl')

# # dropdown_options = ["ssc", "Cbse"]

# model1 = joblib.load('salary.pkl')

app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')
@app.route('/bot')
def bot():
    return render_template('bot.html')
# @app.route('/main')
# def main():
#     return render_template('main.html')
@app.route('/trend')
def trend():
    return render_template('Clgtrend.html')
@app.route('/input', methods=["POST", "GET"])
def input():
    if request.method == "POST":
        #   {% comment %} <script src="{{url_for('static',filename='Javas/input.js')}}"></script> {% endcomment %}
        gender = int(request.form.get('gender'))  # Assuming gender is represented as an integer (e.g., 0 for male, 1 for female)
        School = int(request.form.get('drop'))  # Assuming 'drop' is a numerical identifier for schools
        schoolp = float(request.form.get('schoolPercentage'))
        Interb = int(request.form.get('Iboard'))  # Assuming 'Iboard' is a numerical identifier for intermediate boards
        Interg = int(request.form.get('Interg'))  # Assuming 'Interg' is a numerical identifier for intermediate groups
        Interp = float(request.form.get('Iper'))
        Degreeb = int(request.form.get('Dbranch'))  # Assuming 'Dbranch' is a numerical identifier for degree branches
        Interns = int(request.form.get('Ist'))
        Cgpa = float(request.form.get('Cgpa'))
        skill = int(request.form.get('skills'))
        print(gender)
        print(Interns)
        if(schoolp<=35 or Interp<=35 or Cgpa<=35):
            return render_template('result.html')
        else:
            inputarray=np.array([[gender,schoolp,School,Interp,Interb,Interg,Degreeb,Interns,Cgpa,skill]])
            # print( "sataus ",model.predict(inputarray))

            predictions = predict_status_api((inputarray).tolist())
            print('predictions: ',predictions)
           
            # data11=model.predict(inputarray)
            d2 = predictions[0]
            if d2 == 0:
                return render_template('result.html')
            else:
            
                data11 = np.array([[gender,schoolp,School,Interp,Interb,Interg,Degreeb,Interns,Cgpa,skill,d2]])
                salary = predict_salary_api((data11).tolist())
                resu=salary[0]
                print(salary)
                return render_template('results.html', data=resu)
    else:
        return render_template('main1.html')
# @app.route('/<sscs>')
# def sample(sscs):
#     return f"<h1>{sscs}</h1>"
# @app.route('/reg')
# def reg():
#     reg=1
#     return redirect(url_for('login'))
@app.route('/main')
def main():
    return render_template('main1.html')
@app.route('/college')
def college():
    return render_template('Clgtrend.html')
@app.route('/cse')
def cse():
    return render_template('Cse.html')
@app.route('/ece')
def ece():
    return render_template('Ece.html')
@app.route('/me')
def me():
    return render_template('Me.html')
@app.route('/favicon.ico')
def favicon():
    return send_from_directory('static', 'favicon.ico')
if __name__=='__main__':
    app.run(debug=True)