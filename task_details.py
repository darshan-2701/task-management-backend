from queries import general
from utils import postgres


class TaskDetailsCls:
    def __init__(self):
        pass

    def create_task(self, payload):
        try:
            db_obj = postgres.PostgresCls()
            db_obj.db_connect()

            title = payload.get('title')
            description = payload.get('description', '')
            status = payload.get('status', 'Pending')
            query = general.create_task_in_db
            params = {'?1': title, '?2': description,
                      '?3': status}
            db_obj.cursor.execute(query, params)
            db_obj.commit_changes()
            db_obj.db_disconnect()
            return {'message': 'Task created successfully'}
        except Exception as e:
            print(str(e))
            return {'error': str(e)}

    def get_task(self):
        try:
            db_obj = postgres.PostgresCls()
            db_obj.db_connect()

            task_details = {}
            query = general.get_all_task_from_db
            db_obj.cursor.execute(query)
            result = db_obj.cursor.fetchall()
            db_obj.db_disconnect()
            for row in result:
                id = row[0]
                title = row[1]
                description = row[2]
                status = row[3]
                task_details[id] = [title, description, status]
            return {'message': 'Getting all tasks',
                    'tasks': task_details}
        except Exception as e:
            print(str(e))
            return {'error': str(e)}

    def delete_task(self, payload):
        try:
            db_obj = postgres.PostgresCls()
            db_obj.db_connect()

            task_id = payload.get('id')
            query = general.delete_task_from_db
            params = {'?1': task_id}
            db_obj.cursor.execute(query, params)
            db_obj.commit_changes()
            db_obj.db_disconnect()
            return {'message': 'Task deleted successfully'}
        except Exception as e:
            print(str(e))
            return {'error': str(e)}

    def update_task(self, payload):
        try:
            db_obj = postgres.PostgresCls()
            db_obj.db_connect()

            task_id = payload.get('id')
            title = payload.get('title')
            description = payload.get('description', '')
            status = payload.get('status', 'Pending')
            query = general.update_task_in_db
            params = {'?1': task_id, '?2': title,
                      '?3': description, '?4': status}
            db_obj.cursor.execute(query, params)
            db_obj.commit_changes()
            db_obj.db_disconnect()
            return {'message': 'Task updated successfully'}
        except Exception as e:
            print(str(e))
            return {'error': str(e)}
