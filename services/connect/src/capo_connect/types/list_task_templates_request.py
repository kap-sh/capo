"""Generated from Smithy shape ``com.amazonaws.connect#ListTaskTemplatesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.instance_id
    import capo_connect.types.max_result100
    import capo_connect.types.next_token
    import capo_connect.types.task_template_name
    import capo_connect.types.task_template_status


class ListTaskTemplatesRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    next_token: NotRequired["capo_connect.types.next_token.NextToken"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p> <important> <p>It is not expected that you set this because the value returned in the previous response is always null.</p> </important>"""
    max_results: NotRequired["capo_connect.types.max_result100.MaxResult100"]
    """<p>The maximum number of results to return per page.</p> <important> <p>It is not expected that you set this.</p> </important>"""
    status: NotRequired["capo_connect.types.task_template_status.TaskTemplateStatus"]
    """<p>Marks a template as <code>ACTIVE</code> or <code>INACTIVE</code> for a task to refer to it. Tasks can only be created from <code>ACTIVE</code> templates. If a template is marked as <code>INACTIVE</code>, then a task that refers to this template cannot be created.</p>"""
    name: NotRequired["capo_connect.types.task_template_name.TaskTemplateName"]
    """<p>The name of the task template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTaskTemplatesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTaskTemplatesRequest:
    out: ListTaskTemplatesRequest = {}  # type: ignore[typeddict-item]
    return out
