"""Generated from Smithy shape ``com.amazonaws.connect#StopContactStreamingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.contact_id
    import capo_connect.types.instance_id
    import capo_connect.types.streaming_id


class StopContactStreamingRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    contact_id: "capo_connect.types.contact_id.ContactId"
    """<p>The identifier of the contact. This is the identifier of the contact that is associated with the first interaction with the contact center.</p>"""
    streaming_id: "capo_connect.types.streaming_id.StreamingId"
    """<p>The identifier of the streaming configuration enabled. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopContactStreamingRequest) -> dict:
    out: dict = {}
    out["InstanceId"] = value["instance_id"]
    out["ContactId"] = value["contact_id"]
    out["StreamingId"] = value["streaming_id"]
    return out


def deserialize_json(data: dict) -> StopContactStreamingRequest:
    out: StopContactStreamingRequest = {}  # type: ignore[typeddict-item]
    if data.get("InstanceId") is not None:
        out["instance_id"] = data["InstanceId"]
    else:
        out["instance_id"] = ""
    if data.get("ContactId") is not None:
        out["contact_id"] = data["ContactId"]
    else:
        out["contact_id"] = ""
    if data.get("StreamingId") is not None:
        out["streaming_id"] = data["StreamingId"]
    else:
        out["streaming_id"] = ""
    return out
