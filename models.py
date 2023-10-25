#models
def get_user_data(user_id):
    def get_users_data():
        USERS = {
        "A4DC2287-B03D-430C-92E8-02216D828709": {
        "online_times": ["2023-09-27 19:00", "2023-09-28 15:00", "2023-09-29 14:00"],
        "page_views": [120, 80, 200],
        "purchases": [1, 0, 3],
    },

}

def get_user_online_status(user_id, date):
    if user_id not in USERS:
        return None, None, None, None
        user_data = USERS.get(user_id)
    if not user_data:
        return None, None, None, None

    was_online = date in user_data["online_times"]
    nearest_online_time = min(user_data["online_times"], key=lambda d: abs(d - date))
    page_views = sum(user_data["page_views"]) / len(user_data["page_views"])  # середнє значення переглядів
    purchases = sum(user_data["purchases"])  # загальна кількість покупок
    return was_online, nearest_online_time, page_views, purchases

def get_all_users_data(date):
    def get_users_data():
       USERS = {

    }
    return [user_data for user_id, user_data in USERS.items() if date in user_data["online_times"]]
