from collections import OrderedDict

from flask import Flask, render_template

app = Flask(__name__)
dynamic_data = {"Key":"Item", "key2":"item2"}

@app.route("/")
def index():
    return render_template('index.html', data=dynamic_data)

# inputs are (company stock ticker)
# returns, ESG Rating: ,stock market sentiment: (Good/bad?), Price Trend: (up/down), Current Price: $ , fear and greed index: (),
def APIcalls(ticker):

    my_ordered_dict = OrderedDict()
    my_ordered_dict['name'] = 'John'
    my_ordered_dict['ticker'] = ticker

    with open('output.txt', 'w') as file:
        file.write(my_ordered_dict)
        file.write('\n')

    return my_ordered_dict
