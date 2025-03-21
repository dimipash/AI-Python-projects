from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/orders", methods=["POST"])
def get_orders():
    return jsonify(
        {
            "order_number": "1",
            "customer_name": "John Doe",
            "order_date": "2021-01-01",
            "total_amount": 100.00,
            "status": "pending",
            "shipping_adress": "123 Main St, New York, NY 10001",
        }
    )
