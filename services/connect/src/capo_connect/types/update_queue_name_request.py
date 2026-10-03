"""Generated from Smithy shape ``com.amazonaws.connect#UpdateQueueNameRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.common_name_length127
    import capo_connect.types.instance_id
    import capo_connect.types.queue_description
    import capo_connect.types.queue_id


class UpdateQueueNameRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    queue_id: "capo_connect.types.queue_id.QueueId"
    """<p>The identifier for the queue.</p>"""
    name: NotRequired["capo_connect.types.common_name_length127.CommonNameLength127"]
    """<p>The name of the queue.</p>"""
    description: NotRequired["capo_connect.types.queue_description.QueueDescription"]
    """<p>The description of the queue.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateQueueNameRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_json(data: dict) -> UpdateQueueNameRequest:
    out: UpdateQueueNameRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    return out
