from pymongo import MongoClient

client = MongoClient('mongodb://admin:admin@ds021182.mlab.com:21182/c4e')

db = client.get_default_database()

posts = db['posts']

new_post = {
    'title': 'Kêu ca - By Hương',
    'content': 'Rất mong các lớp C4E sau sẽ có nhiều bạn nữ để không phải cảm thấy buồn thê lương như em'
}
posts.insert_one(new_post)
