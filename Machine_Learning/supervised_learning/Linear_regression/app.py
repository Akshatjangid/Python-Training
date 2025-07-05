from flask import Flask, render_template,url_for

app = Flask(__name__)

@app.route('/')
def home():             ## we make fuction with same file name
    return render_template('home.html')

#
@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)