from collections import OrderedDict
from flask import Flask, request, render_template

import apiFunctions
import hellDiver

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    dynamic_data = {" ": " "}
    newsData = {" ": " "}
    if request.method == 'POST':
        data_from_form = request.form['submit']

        dynamic_data = hellDiver.esgAPI(data_from_form)
        newsData = apiFunctions.newsAPICall(data_from_form)
        print(newsData)
        print()
        print(newsData[data_from_form.upper()])
        return render_template('index.html', dynamic_data=dynamic_data, newsData=newsData[data_from_form.upper()])
        # Process the data (e.g., save it, perform an action, etc.)
    return render_template('index.html', dynamic_data=dynamic_data, newsData=newsData)



