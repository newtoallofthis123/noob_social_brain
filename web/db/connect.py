import uuid
import psycopg


class NoobSocialDB:
    def __init__(
        self, username, password, dbname="noob_social", host="localhost", port="5432"
    ):
        self.engine = NoobSocialDB.create_engine(username, password, dbname, host, port)
        if self.engine is None:
            raise Exception("Could not connect to database")

    @staticmethod
    def create_engine(username, password, dbname, host, port):
        conn = psycopg.connect(
            dbname=dbname, user=username, password=password, host=host, port=port
        )

        return conn

    def check_connection(self):
        cursor = self.engine.cursor()

        cursor.execute("SELECT 1")
        result = cursor.fetchone() or [0]

        cursor.close()

        return result[0] == 1

    def get_conn(self):
        return self.engine
    
    def fetch_tags(self):
        tags = []
        cursor = self.engine.cursor()
        cursor.execute("SELECT * FROM tags")

        for row in cursor.fetchall():
            tags.append((row[0], row[1]))

        cursor.close()

        return tags 

    def fetch_posts(self):
        contents = []
        cursor = self.engine.cursor()
        cursor.execute("SELECT * FROM contents")

        for row in cursor.fetchall():
            contents.append((row[0], row[1], row[2]))

        cursor.close()

        return contents

    def fetch_content_by_id(self, post_id):
        cursor = self.engine.cursor()
        cursor.execute("SELECT * FROM posts WHERE id = %s", (post_id,))
        row = cursor.fetchone()
        if row is None:
            return None

        content_id = row[2]
        cursor.execute("SELECT * FROM contents WHERE id = %s", (content_id,))
        row = cursor.fetchone()
        if row is None:
            return None

        cursor.close()

        return (row[0], row[1], row[2])

    def add_tag(self, content_id, tag_id):
        cursor = self.engine.cursor()
        cursor.execute("INSERT INTO content_tags (id, content_id, tag_id, created_at) VALUES (%s, %s, %s, NOW())", (uuid.uuid4(), content_id, tag_id))
        self.engine.commit()
        cursor.close()


    def get_tags_for_post(self, post_id):
        tags = []
        cursor = self.engine.cursor()
        cursor.execute("SELECT * FROM posts WHERE id = %s", (post_id,))
        row = cursor.fetchone()

        if row is None:
            return None

        content_id = row[2]
        cursor.execute("SELECT tag_id from content_tags where content_id = %s", (content_id,))
        rows = cursor.fetchall()

        for row in rows:
            tags.append(row[0])

        cursor.close()

        return tags

    def fetch_posts_of_tag(self, tag_id):
        posts = []
        cursor = self.engine.cursor()
        cursor.execute("SELECT * FROM content_tags WHERE tag_id = %s", (tag_id,))
        rows = cursor.fetchall()

        for row in rows:
            cursor.execute("SELECT * FROM contents INNER JOIN posts ON contents.id = posts.content WHERE contents.id = %s", (row[1],))
            post = cursor.fetchone()
            if post is not None:
                print(post)
                posts.append((post[0], post[1], post[2]))

        cursor.close()

        return posts
