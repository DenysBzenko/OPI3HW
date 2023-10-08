
USERS = {
    "A4DC2287-B03D-430C-92E8-02216D828709": {
        "online_times": ["2023-27-09-19:00", "2023-28-09-15:00", "2023-29-09-14:00"]
    }
}

def get_users_online(date):
    # Mock: Return a random number or fetch from database
    return 34

def get_user_online_status(user_id, date):
    if user_id not in USERS:
        return None, None
    user_data = USERS[user_id]
    was_online = date in user_data["online_times"]
    nearest_online_time = min(user_data["online_times"], key=lambda d: abs(d - date))
    return was_online, nearest_online_time

