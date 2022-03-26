from flask import Flask, render_template, request
import requests
import urllib.parse
import pandas
app = Flask(__name__)

address = 'Shivaji Nagar, Bangalore, KA 560001'
url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(address) +'?format=json'

response = requests.get(url).json()
# print(response[0]["lat"])
# print(response[0]["lon"])



@app.route('/', methods=["POST","GET"])
def success():
    if request.method=='POST':
        f=request.files['file_upload']
        # print(f.filename)
        f.save(f.filename)
        if f.filename:
            df=pandas.read_csv(f.filename)
            df["Ankush"] = 1
            print(df)
        # with open(f.filename) as file:
        #     print(file.readlines)

            return render_template('index.html',tables=[df.to_html(classes='data')], titles=df.columns.values)
    else:
        return render_template('index.html')


if __name__=="__main__":
    app.run(debug=True)
