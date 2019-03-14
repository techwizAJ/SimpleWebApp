from flask import Flask,request, render_template, url_for
from textblob import TextBlob
app = Flask(__name__)

# Todo Html File analysis Html with text field and button
# Get the field using post method and use text blob for analysis
# Pass the value from python to html for output

@app.route("/")
def home():
    return render_template('analysis.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['in']
    a = TextBlob(text)
    return render_template('result.html',posts=a)

if __name__ == '__main__':
    app.run(debug=True)
