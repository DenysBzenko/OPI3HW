def predict_users_online(date):
    # Mock: Return a random number or use some prediction algorithm based on historical data
    return 31

def predict_user_online(user_id, date, tolerance):
    if user_id not in USERS:
        return None, None
    user_data = USERS[user_id]
    weekday = date.weekday()
    online_weekdays = [d.weekday() for d in user_data["online_times"]]
    online_chance = online_weekdays.count(weekday) / len(online_weekdays)
    will_be_online = online_chance > tolerance
    return will_be_online, online_chance
