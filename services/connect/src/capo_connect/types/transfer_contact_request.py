"""Generated from Smithy shape ``com.amazonaws.connect#TransferContactRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.agent_resource_id
    import capo_connect.types.client_token
    import capo_connect.types.contact_flow_id
    import capo_connect.types.contact_id
    import capo_connect.types.instance_id
    import capo_connect.types.queue_id


class TransferContactRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    contact_id: "capo_connect.types.contact_id.ContactId"
    """<p>The identifier of the contact in this instance of Connect Customer. </p>"""
    queue_id: NotRequired["capo_connect.types.queue_id.QueueId"]
    """<p>The identifier for the queue.</p>"""
    user_id: NotRequired["capo_connect.types.agent_resource_id.AgentResourceId"]
    """<p>The identifier for the user. This can be the ID or the ARN of the user.</p>"""
    contact_flow_id: "capo_connect.types.contact_flow_id.ContactFlowId"
    """<p>The identifier of the flow.</p>"""
    client_token: NotRequired["capo_connect.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TransferContactRequest) -> dict:
    out: dict = {}
    out["InstanceId"] = value["instance_id"]
    out["ContactId"] = value["contact_id"]
    if "queue_id" in value:
        out["QueueId"] = value["queue_id"]
    if "user_id" in value:
        out["UserId"] = value["user_id"]
    out["ContactFlowId"] = value["contact_flow_id"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> TransferContactRequest:
    out: TransferContactRequest = {}  # type: ignore[typeddict-item]
    if data.get("InstanceId") is not None:
        out["instance_id"] = data["InstanceId"]
    else:
        raise DeserializationError("TransferContactRequest.instance_id required")
    if data.get("ContactId") is not None:
        out["contact_id"] = data["ContactId"]
    else:
        raise DeserializationError("TransferContactRequest.contact_id required")
    if data.get("QueueId") is not None:
        out["queue_id"] = data["QueueId"]
    if data.get("UserId") is not None:
        out["user_id"] = data["UserId"]
    if data.get("ContactFlowId") is not None:
        out["contact_flow_id"] = data["ContactFlowId"]
    else:
        raise DeserializationError("TransferContactRequest.contact_flow_id required")
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out
