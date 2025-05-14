def generate_time_series(data_points, interval_minutes=5):
    from datetime import datetime, timedelta
    base_time = datetime.now()
    return [
        {"time": (base_time - timedelta(minutes=i*interval_minutes)).isoformat(), "value": v}
        for i, v in enumerate(reversed(data_points))
    ]