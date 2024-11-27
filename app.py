from web.routes import app

#
# contents = db.fetch_posts()
# tags = db.fetch_tags()
# posts = [r[1] for r in contents]
# tags = [r[1] for r in tags]
#
# for post in posts:
#     x = classify_tags(post, tags)
#     print(f"Post: {post} Tags: {x}")


if __name__ == '__main__':
    app.run(debug=True)
