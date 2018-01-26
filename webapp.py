import os
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session

app = Flask(__name__)

# In order to use "sessions",you need a "secret key".
# This is something random you generate.
# See: http://flask.pocoo.org/docs/0.10/quickstart/#sessions

app.secret_key=os.environ["SECRET_KEY"]; #This is an environment variable.
                                     #The value should be set in Heroku (Settings->Config Vars).

@app.route('/')
def renderMain():
    return render_template('index.html')

@app.route('/startOver')
def startOver():
    #clear variable values and create a new session
    session.clear()
    return redirect(url_for('renderMain')) # url_for('renderMain') could be replaced with '/'

@app.route('/index',methods=['GET','POST'])
def renderIndex():

    if "first_question" in request.form &&
    first_question = request.form["first_question"]
    second_question = request.form["second_question"]
    third_question = request.form["third_question"]
    fourth_question = request.form["fourth_question"]
    corect_questions = 0
    question_info = {}

    if first_question == "-sinx":
        question_info["first_question"] = "Correct"
        correct_questions += 1
    else:
        question_info["first_question"] = "Incorrect"

    if second_question == "cosx":
        question_info["second_question"] = "Correct"
        correct_questions += 1
    else:
        question_info["second_question"] = "Incorrect"

    if third_question == "n(x^(n-1))":
        question_info["third_question"] = "Correct"
        correct_questions += 1
    else:
        question_info["first_question"] = "Incorrect"

    if fourth_question == "sec^2(x)":
        question_info["fourth_question"] = "Correct"
        correct_questions += 1
    else:
        question_info["fourth_question"] = "Incorrect"


    return render_template('index.html', response_question_info = question_info, response_correct_questions = correct_questions)

if __name__=="__main__":
    app.run(debug=False)
