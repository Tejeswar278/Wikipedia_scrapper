from flask import Flask,request

app = Flask(__name__)

@app.route("/members")
def member():
    return {"members":["mem1","mem2","mem3"]}

@app.route("/scrape",methods=['POST'])
def scrape():
    data = request.get_json()
    print(data,"data.............")
    url = data['url']

    return {"scrape":["scrape1","scrape2","scrape3"]}

if __name__ == "__main__":
    app.run(debug=True)
