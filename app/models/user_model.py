from app.dynamodb import dynamodb
from app.dynamodb import Key
from boto3.dynamodb.conditions import Key
import uuid

class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email

    @staticmethod
    def get_users():
        table = dynamodb.Table('Users')
        response = table.scan().get('Items', [])
        return response

    @staticmethod
    def get_user_by_id(user_id):
        table = dynamodb.Table('Users')
        response = table.get_item(
            Key={'user_id': user_id}
        )
        return response
    
    @staticmethod
    def create_user(name, email):
        table = dynamodb.Table('Users')
        user_id = str(uuid.uuid4())
        table.put_item(
            Item={
                'user_id': user_id,
                'name': name,
                'email': email
            }
        )
        return {'user_id': user_id, 'name': name, 'email': email}