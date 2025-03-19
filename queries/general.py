create_task_in_db = """
insert into darshan.task_details ( title, description, status ) values ( %(?1)s, %(?2)s, %(?3)s )
"""

get_all_task_from_db = """
select id, title, description, status from darshan.task_details
"""

update_task_in_db = """
update darshan.task_details set title = %(?2)s, description = %(?3)s, status = %(?4)s
where id = %(?1)s
"""

delete_task_from_db = """
delete from darshan.task_details where id = %(?1)s
"""