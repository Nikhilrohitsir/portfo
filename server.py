from flask import Flask, render_template, request
from werkzeug.utils import redirect
import csv

app = Flask(__name__)
print(__name__)


@app.route('/index.html')
def hello_world():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    my_file = open("database.txt", "r")
    content_list = my_file.readlines()
    print(content_list)

    print("data")
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        print(email)
        print(subject)
        print(message)
        file = database.write(f'/n {email}, {subject},{message}')
        print(file)


def write_to_csv(data):

    print("data")
    with open('database.csv',newline='', mode='a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        print(email)
        print(subject)
        print(message)
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])
        print(csv_writer)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        # write_to_file(data)
        # write_to_file(data)
        write_to_csv(data)
        return redirect('/thank-you.html')
    else:
        return 'Error'
