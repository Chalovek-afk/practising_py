from datetime import datetime
import json
import os

from dotenv import load_dotenv
import vk_api

load_dotenv()

VK_TOKEN = os.getenv("VK_TOKEN", "")

OWNER_ID = -185939737
POST_ID  = 1459

vk = vk_api.VkApi(token=VK_TOKEN).get_api()

try:
    likes = vk.likes.getList(
        type='post',
        owner_id=OWNER_ID,
        item_id=POST_ID,
    )
    user_ids = likes['items']
    print(f"   Найдено {likes['count']} лайков")
except Exception as e:
    print(f"Ошибка получения лайков: {e}")
    exit()

if not user_ids:
    print("Нет лайков или доступ запрещён.")
    exit()

try:
    users = vk.users.get(
        user_ids=user_ids,
        fields='sex,bdate'
    )
except Exception as e:
    print(f"Ошибка получения данных пользователей: {e}")
    exit()

age_stats = {"0-18": 0, "19-35": 0, "36-50": 0, ">50": 0, "unknown": 0}
sex_stats = {"male": 0, "female": 0, "unknown": 0}

for user in users:
    sex = user.get('sex')
    if sex == 1:
        sex_stats["female"] += 1
    elif sex == 2:
        sex_stats["male"] += 1
    else:
        sex_stats["unknown"] += 1

    bdate = user.get('bdate', '')
    if bdate.count('.') == 2:
        try:
            year = int(bdate.split('.')[2])
            age = datetime.now().year - year
            if age <= 18:
                age_stats["0-18"] += 1
            elif 19 <= age <= 35:
                age_stats["19-35"] += 1
            elif 36 <= age <= 50:
                age_stats["36-50"] += 1
            elif age > 50:
                age_stats[">50"] += 1
            else:
                age_stats["unknown"] += 1
        except:
            age_stats["unknown"] += 1
    else:
        age_stats["unknown"] += 1

result = {
    "post_id": POST_ID,
    "age": age_stats,
    "sex": sex_stats
}

print(json.dumps(result, ensure_ascii=False, indent=2))