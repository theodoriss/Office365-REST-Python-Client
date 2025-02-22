import sys

from office365.sharepoint.client_context import ClientContext
from office365.sharepoint.fields.field_lookup_value import FieldLookupValue
from tests import test_team_site_url, test_client_credentials

ctx = ClientContext(test_team_site_url).with_credentials(test_client_credentials)

list_tasks = ctx.web.lists.get_by_title("Tasks")
items = list_tasks.items.get().top(2).execute_query()
if len(items) != 2:
    sys.exit("Not enough items were found")

task_id = items[0].get_property("Id")
lookup_field_value = FieldLookupValue(task_id)
items[1].set_property("ParentTask", lookup_field_value).update().execute_query()
print("Item has been updated")


