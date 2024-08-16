from flask import Flask,request,jsonify
import requests
app=Flask(__name__)

@app.route('/',methods=['POST'])
def index():
    data=request.get_json()
    source_currency=data['queryResult']['parameters']['unit-currency']['currency']
    amount=data['queryResult']['parameters']['unit-currency']['amount']
    target_currency =data['queryResult']['parameters']['currency-name']
    print(source_currency)
    print(amount)
    print(target_currency)
    #return str(source_currency)+" "+str(amount)+" "+str(target_currency)
    cf=fetch_conversion_factor(target_currency,source_currency)
    final_amount=round(amount*cf,2)
    print(final_amount)
    response={
        'fulfillmentText':"{} {} is {} {}".format(amount,source_currency,final_amount,target_currency)
    }
    return jsonify(response)
def fetch_conversion_factor(source,target):
    url="https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_XvRqBpH5h7MIFnNTwG9zAjCGpae0Mvouu4iWWvdc&currencies={}&base_currency={}".format(source,target)
    response=requests.get(url)
    response=response.json()
    print(response['data'])
    print(response['data'])
    return response['data']['{}'.format(source)]

if __name__ =="__main__":
    app.run(debug=True)
