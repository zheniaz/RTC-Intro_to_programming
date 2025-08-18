# here is the plan:
#
# we will read commands from terminal:
#
# add_task(title, status)
# remove_task(task_id)
# edit_task(task_id, new_title, new_status)
# get_tasks(status=None) → Optional filter by status
#
# Also we need to write logic for reading/writing to JSON file tasks.json.
# load_tasks() → Reads tasks from JSON file (creates file if missing).
# save_tasks(tasks) → Writes updated task list to JSON.

