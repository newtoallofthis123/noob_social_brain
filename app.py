from db.connect import NoobSocialDB
from dotenv import load_dotenv
import os

from model.classify import classify_tags

load_dotenv()


db = NoobSocialDB(os.environ.get("DB_USER"), os.environ.get("DB_PASSWORD"))
assert(db.check_connection())

contents = db.fetch_posts()
posts = [r[1] for r in contents]

tags = ["Politics", "PopCulture", "Sports", "Tech", "Science", "General", "Comment", "Review"]

for post in posts:
    x = classify_tags(post, tags)
    print(f"Post: {post} Tags: {x}")
