
from flask import Flask, request, session, redirect, url_for, \
     abort, render_template, flash,json

app =Flask(__name__)
@app.route('/')
def post_user():
    return render_template('output.html')






if __name__ == "__main__":
    app.run();
    #app.run(debug=True, host='0.0.0.0', port=5000);

