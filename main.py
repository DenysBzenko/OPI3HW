from flask import Flask, jsonify, request
import models

app = Flask(__name__)

@app.route('/api/stats/users', methods=['GET'])
def get_all_users_stats():
    date = request.args.get('date')
    users_online = models.get_users_online(date)
    return jsonify({"usersOnline": users_online})

@app.route('/api/stats/user', methods=['GET'])
def get_single_user_stats():
    date = request.args.get('date')
    user_id = request.args.get('userId')
    was_online, nearest_online_time, page_views, purchases = models.get_user_online_status(user_id, date)
    return jsonify({
        "wasUserOnline": was_online,
        "nearestOnlineTime": nearest_online_time,
        "pageViews": page_views,
        "purchases": purchases
    })

@app.route('/api/predictions/users', methods=['GET'])
def predict_all_users():
    date = request.args.get('date')
    predicted_users = models.predict_users_online(date)
    return jsonify({"onlineUsers": predicted_users})

@app.route('/api/predictions/user', methods=['GET'])
def predict_single_user():
    date = request.args.get('date')
    tolerance = float(request.args.get('tolerance'))
    user_id = request.args.get('userId')
    will_be_online, online_chance = models.predict_user_online(user_id, date, tolerance)
    return jsonify({"willBeOnline": will_be_online, "onlineChance": online_chance})

if __name__ == '__main__':
    app.run(debug=True)
