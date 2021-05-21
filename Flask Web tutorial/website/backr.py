from flask import Flask
from flask import Blueprint, render_template, request, flash, redirect, url_for

app=Flask(__name__)


@app.route('/index')
def rome():
    return render_template("index.html")


if __name__ == '__main__':
     app.run(debug=True)