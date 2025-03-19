
import os

db_host = os.getenv('DB_HOST', 'localhost')
db_port = os.getenv('DB_PORT', 5432)
db_name = os.getenv('DB_NAME', 'task_management')
db_user = os.getenv('DB_USER', 'postgres')
db_password = os.getenv('DB_PASSWORD', 'password')

