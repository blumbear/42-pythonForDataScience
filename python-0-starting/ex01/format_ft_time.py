import datetime as dt

today = dt.datetime.now()

month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

print("Seconds since January 1, 1970:",
      f"{today.timestamp():,}",
      "or", f"{today.timestamp():.2e}",
      "in scientific notation")

print(month[today.month - 1], today.day, today.year)
