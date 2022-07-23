from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def home_view():
        return "<h1>This is Flask API for Manychat <br> Just send json data and it will convertd for you</h1>"

@app.route('/', methods=['POST'])
def process_json():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        num = len(json["products"])
        cardnum = 3
        manychat = {"version": "v2","content": {"messages": [],"actions": [],"quick_replies": []}}
        x =1
        for i in range (num//cardnum):
            manychat["content"]["messages"].append({"type": "cards","elements": [],"image_aspect_ratio": "horizontal"})
            x = i
            for j in range(cardnum):
                manychat["content"]["messages"][i]["elements"].append({"title": json["products"][(i*cardnum)+j]["name"],"subtitle": json["products"][(i*cardnum)+j]["description"],"image_url": json["products"][(i*cardnum)+j]["image"],"action_url": "https://manychat.com","buttons": []})
        if (num%cardnum > 0):
            for i in range(x+1,x+2):
                manychat["content"]["messages"].append({"type": "cards","elements": [],"image_aspect_ratio": "horizontal"})
                for j in range(num%cardnum):
                    manychat["content"]["messages"][i]["elements"].append({"title": json["products"][(i*cardnum)+j]["name"],"subtitle": json["products"][(i*cardnum)+j]["description"],"image_url": json["products"][(i*cardnum)+j]["image"],"action_url": "https://manychat.com","buttons": []})
        return manychat
    else:
        return 'Content-Type not supported!'
if __name__ == "__main__":
    app.run()
