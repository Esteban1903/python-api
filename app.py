from flask import Flask, jsonify, abort

days = [
    {"id": 1, "name": "Monday"},
    {"id": 2, "name": "Tuesday"},
    {"id": 3, "name": "Wednesday"},
    {"id": 4, "name": "Thursday"},
    {"id": 5, "name": "Friday"},
    {"id": 6, "name": "Saturday"},
    {"id": 7, "name": "Sunday"},
]

app = Flask(__name__)


@app.route("/", methods=["GET"])
def get_days():
    return jsonify(days)


@app.route("/<int:day_id>", methods=["GET"])
def get_day(day_id):
    day = [day for day in days if day["id"] == day_id]
    if len(day) == 0:
        abort(404)
    return jsonify({"day": day[0]})

@app.route("/", methods=["POST"])
def post_days():
    return jsonify({"success": True}), 201

# NUEVO GET:
@app.route("/status", methods=["GET"])
def get_status():
    return jsonify({"status": "API funcionando correctamente"})

# NUEVO POST:
@app.route("/add-day", methods=["POST"])
def add_day():
    new_day = {"id": len(days) + 1, "name": "Nuevo día"}
    days.append(new_day)
    return jsonify({"message": "Día agregado", "day": new_day}), 201


if __name__ == "__main__":
    app.run(debug=True)
