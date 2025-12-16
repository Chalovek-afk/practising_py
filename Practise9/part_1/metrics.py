import os
import sys
import csv
from datetime import datetime, timedelta
import argparse

import requests
from dotenv import load_dotenv
from tabulate import tabulate

# --- Аргументы CLI ---
parser = argparse.ArgumentParser()
parser.add_argument("--from", "-f", dest="date_from")
parser.add_argument("--to", "-t", dest="date_to")
parser.add_argument("--output", "-o", default="metrika_report.csv")
args = parser.parse_args()

load_dotenv()
counter_id = os.getenv("YANDEX_METRIKA_COUNTER_ID", "")
token = os.getenv("YANDEX_METRIKA_OAUTH_TOKEN", "")


# --- Ошибки .env ---
if not counter_id:
    print("ERROR: YANDEX_METRIKA_COUNTER_ID is not set in .env", file=sys.stderr)
    sys.exit(1)
if not token:
    print("ERROR: YANDEX_METRIKA_OAUTH_TOKEN is not set in .env", file=sys.stderr)
    sys.exit(1)

# --- Даты ---
try:
    if args.date_from and args.date_to:
        date1 = datetime.strptime(args.date_from, "%Y-%m-%d").date()
        date2 = datetime.strptime(args.date_to, "%Y-%m-%d").date()
        if date1 > date2:
            print("ERROR: start date must not be later than end date", file=sys.stderr)
            sys.exit(1)
    elif args.date_from or args.date_to:
        print("ERROR: both --from and --to must be specified", file=sys.stderr)
        sys.exit(1)
    else:
        date2 = datetime.today().date()
        date1 = date2 - timedelta(days=6)

    date1_str = date1.strftime("%Y-%m-%d")
    date2_str = date2.strftime("%Y-%m-%d")
    print(f"Period: {date1_str} to {date2_str}")

except ValueError:
    print("ERROR: invalid date format. Use YYYY-MM-DD", file=sys.stderr)
    sys.exit(1)

# --- Запрос ---
try:
    response = requests.get(
        "https://api-metrika.yandex.net/stat/v1/data",
        params={
            "ids": counter_id,
            "metrics": "ym:s:visits,ym:s:pageviews,ym:s:users",
            "date1": date1,
            "date2": date2,
            "dimensions": "ym:s:date",
        },
        headers={"Authorization": f"OAuth {token}"}
    )
except Exception as e:
    print(f"ERROR: {e}", file=sys.stderr)
    sys.exit(1)

# --- Обработка ошибок ---
if response.status_code != 200:
    msg = f"API error {response.status_code}"
    try:
        err = response.json().get("message", "")
        if "token" in err.lower():
            msg = "ERROR: invalid or expired OAuth token"
        elif "counter" in err.lower():
            msg = f"ERROR: no access to counter {counter_id}"
    except:
        pass
    print(msg, file=sys.stderr)
    sys.exit(1)

# --- Данные ---
data = response.json()
rows = []
for item in data.get("data", []):
    dt = item["dimensions"][0]["name"]
    visits, pageviews, users = item["metrics"]
    rows.append([
        dt,
        int(visits),
        int(pageviews),
        int(users),
        round(pageviews / visits, 2) if visits else 0.0
    ])

# Заполнение дней
if (date2 - date1).days <= 31:
    all_dates = [
        (date1 + timedelta(days=i)).strftime("%Y-%m-%d")
        for i in range((date2 - date1).days + 1)
    ]
    result = []
    seen = {r[0] for r in rows}
    for d in all_dates:
        if d in seen:
            row = next(r for r in rows if r[0] == d)
        else:
            row = [d, 0, 0, 0, 0.0]
        result.append(row)
else:
    result = rows

# --- Вывод ---
headers = ["Date", "Visits", "Pageviews", "Users", "PV/V"]
print(tabulate(result, headers=headers, tablefmt="plain"))

# --- CSV ---
output = args.output
if os.path.dirname(output) and not os.path.exists(os.path.dirname(output)):
    os.makedirs(os.path.dirname(output))
with open(output, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    for r in result:
        writer.writerow([r[0], r[1], r[2], r[3], f"{r[4]:.2f}"])
print(f"\nSaved to: {os.path.abspath(output)}")