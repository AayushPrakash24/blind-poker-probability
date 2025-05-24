import flask
from flask_cors import CORS
from GameElements import Card, Hand

app = flask.Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})

@app.route("/evaluate-hand", methods=["POST"])
def evaluate_hand():
    data = flask.request.json

    try:
        cards = [Card(rank=c['rank'], suit=c['suit']) for c in data["cards"]]
        hand = Hand(*cards)
        result = hand.rank()
        return flask.jsonify({'result': result})
    except Exception as e:
        return flask.jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)


