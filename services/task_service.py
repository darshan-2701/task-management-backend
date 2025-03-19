import task_details


class TaskCls:
    def __init__(self):
        pass

    def create_task(self, payload):
        try:
             result = task_details.TaskDetailsCls().create_task(payload)
             return result
        except Exception as e:
            print(str(e))

    def get_task(self):
        try:
            result = task_details.TaskDetailsCls().get_task()
            return result
        except Exception as e:
            print(str(e))

    def delete_task(self, payload):
        try:
            result = task_details.TaskDetailsCls().delete_task(payload)
            return result
        except Exception as e:
            print(str(e))

    def update_task(self, payload):
        try:
            result = task_details.TaskDetailsCls().update_task(payload)
            return result
        except Exception as e:
            print(str(e))
