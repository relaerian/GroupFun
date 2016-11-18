
from system.core.model import Model

class User(Model):
    def __init__(self):
        super(User, self).__init__()


    def create(self, info):
        query = "INSERT INTO users (name, email, created_at) VALUES (:name, :email, NOW())"
        data = {
            'name' : info['name'],
            'email' : info['email']
        }
        return self.db.query_db(query, data)

    def get_users(self):
        return self.db.query_db("SELECT * FROM users")

    def get_user_by_id(self, id):
        query = "SELECT * FROM users WHERE id = :id"
        data = {'id' : id}
        return self.db.query_db(query,data)

    def update(self, info, id):
        query = "UPDATE users SET name = :name, email = :email, updated_at = NOW() WHERE id = :id"
        data = {
            'name' : info['name'],
            'email' : info['email'],
            'id' : id
        }
        return self.db.query_db(query, data)

    def destroy(self, id):
        query = "DELETE FROM users WHERE id = :id"
        data = {'id' : id}
        return self.db.query_db(query, data)
