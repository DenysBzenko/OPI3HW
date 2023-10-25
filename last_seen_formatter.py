from datetime import datetime, timedelta

def format_last_seen(last_seen_timestamp):
    current_time = datetime.now()
    last_seen_time = datetime.fromtimestamp(last_seen_timestamp)
    difference = current_time - last_seen_time

    if difference.total_seconds() < 30:
        return "just now"
    elif difference.total_seconds() < 60:
        return "less than a minute ago"
    elif difference.total_seconds() < 3600:
        return "couple of minutes ago"
    elif difference.total_seconds() < 7200:
        return "hour ago"
    elif last_seen_time.date() == current_time.date():
        return "today"
    elif last_seen_time.date() == current_time.date() - timedelta(days=1):
        return "yesterday"
    elif difference.total_seconds() < 604800:
        return "this week"
    else:
        return "long time ago"
