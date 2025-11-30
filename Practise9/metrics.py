# metrika_week_report_FIXED.py
import os
import requests
import csv
from datetime import date, timedelta
from tabulate import tabulate
from dotenv import load_dotenv

load_dotenv()
counter_id = os.getenv("YANDEX_METRIKA_COUNTER_ID", "").strip()
token = os.getenv("YANDEX_METRIKA_OAUTH_TOKEN", "").strip()

if not counter_id or not token:
    raise SystemExit("❌ .env: проверьте COUNTER_ID и TOKEN")

end = date.today()
start = end - timedelta(days=6)
date1 = start.strftime("%Y-%m-%d")
date2 = end.strftime("%Y-%m-%d")


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

if response.status_code != 200:
    print(f"❌ Ошибка {response.status_code}: {response.text}")
    exit(1)

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
        round(pageviews / visits, 2) if visits else 0
    ])

all_dates = [(start + timedelta(days=i)).strftime("%Y-%m-%d") for i in range(7)]
full_rows = []
seen = {r[0] for r in rows}
for d in all_dates:
    if d in seen:
        row = next(r for r in rows if r[0] == d)
    else:
        row = [d, 0, 0, 0, 0.0]
    full_rows.append(row)

# Вывод
headers = ["Дата", "Визиты", "Просмотры", "Уникальные", "П/В"]
print("\n" + "="*60)
print("Отчёт за 7 дней")
print("="*60)
print(tabulate(full_rows, headers=headers, tablefmt="fancy_grid", stralign="right"))

# CSV
with open("metrika_report.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    for r in full_rows:
        writer.writerow([r[0], r[1], r[2], r[3], f"{r[4]:.2f}"])

print("\nСохранено: metrika_report.csv")