from w2.utils.database import DB
from w2.utils.response_model import ProcessStatus

db = DB()

# db.insert(process_id=1, start_time=1)

# db.update_percentage(process_id=1, percentage=10)

# process_statuses = []
#
# for record in db.read_all():
#     ps = ProcessStatus(**record)
#     process_statuses.append(ps)

process_statuses = [ProcessStatus(**record) for record in db.read_all()]


for process_status in process_statuses:
    print(process_status)


