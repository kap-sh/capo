"""Generated from Smithy shape ``com.amazonaws.connect#UpdateQueueMaxContactsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.instance_id
    import capo_connect.types.queue_id
    import capo_connect.types.queue_max_contacts


class UpdateQueueMaxContactsRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    queue_id: "capo_connect.types.queue_id.QueueId"
    """<p>The identifier for the queue.</p>"""
    max_contacts: NotRequired["capo_connect.types.queue_max_contacts.QueueMaxContacts"]
    """<p>The maximum number of contacts that can be in the queue before it is considered full.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateQueueMaxContactsRequest) -> dict:
    out: dict = {}
    if "max_contacts" in value:
        out["MaxContacts"] = value["max_contacts"]
    return out


def deserialize_json(data: dict) -> UpdateQueueMaxContactsRequest:
    out: UpdateQueueMaxContactsRequest = {}  # type: ignore[typeddict-item]
    if data.get("MaxContacts") is not None:
        out["max_contacts"] = data["MaxContacts"]
    return out
