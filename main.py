#main
from flask import Flask, jsonify, request, abort
import models
from api import fetch_all_users_data
from last_seen_formatter import format_last_seen
from localization import translate


def validate_user_id(user_id):
    if not user_id or not isinstance(user_id, str):
        abort(400, description="Invalid user ID provided.")

def validate_date(date):
    if not date:
        abort(400, description="Date parameter is required.")

app = Flask(__name__)

@app.route('/api/stats/users', methods=['GET'])
def get_all_users_stats():
    date = request.args.get('date')
    validate_date(date)
    users_online = models.get_users_online(date)
    return jsonify({"usersOnline": users_online})

@app.route('/api/stats/user', methods=['GET'])
def get_single_user_stats():
    date = request.args.get('date')
    validate_date(date)
    user_id = request.args.get('userId')
    validate_user_id(user_id)
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
    validate_date(date)
    predicted_users = models.predict_users_online(date)
    return jsonify({"onlineUsers": predicted_users})

@app.route('/api/predictions/user', methods=['GET'])
def predict_single_user():
    date = request.args.get('date')
    validate_date(date)
    tolerance = float(request.args.get('tolerance'))
    user_id = request.args.get('userId')
    validate_user_id(user_id)
    will_be_online, online_chance = models.predict_user_online(user_id, date, tolerance)
    return jsonify({"willBeOnline": will_be_online, "onlineChance": online_chance})

from flask import jsonify, request, abort
import utils

@app.route('/api/users/last_seen', methods=['GET'])
def get_user_last_seen():
    offset = request.args.get('offset')
    if offset is None:
        abort(400, description="Offset parameter is required.")

    last_seen = utils.get_last_seen_online(offset)
    if last_seen is None:
        abort(500, description="An error occurred while retrieving data.")

    return jsonify({"lastSeenOnline": last_seen})


def fetch_users():
    return fetch_all_users_data()

def format_user_info(user, lang):
    username = user.get('nickname')
    first_name = user.get('firstName')
    last_name = user.get('lastName')
    last_seen = user.get('lastSeen')

    if last_seen is not None:
        last_seen_formatted = translate(format_last_seen(last_seen), lang)
    else:
        last_seen_formatted = translate("Never", lang)

    return f"{username} ({first_name} {last_name}) - Last seen: {last_seen_formatted}"

def display_users_info(lang):
    users_data = fetch_users()
    for user in users_data:
        print(format_user_info(user, lang))


if __name__ == '__main__':
    print("Select a language: [en] English, [uk] Українська, [ar] العربية, [fr] Français")
    lang = input("Enter the language code (e.g., en, uk, ar, fr): ").strip().lower()
    if lang not in ['en', 'uk', 'ar', 'fr']:
        print("Invalid language selection. Defaulting to English.")
        lang = 'en'
    display_users_info(lang)
    app.run(debug=True)
