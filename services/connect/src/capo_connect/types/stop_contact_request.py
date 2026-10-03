"""Generated from Smithy shape ``com.amazonaws.connect#StopContactRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.contact_id
    import capo_connect.types.disconnect_reason
    import capo_connect.types.instance_id


class StopContactRequest(TypedDict, closed=True):
    contact_id: "capo_connect.types.contact_id.ContactId"
    """<p>The ID of the contact.</p>"""
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    disconnect_reason: NotRequired[
        "capo_connect.types.disconnect_reason.DisconnectReason"
    ]
    """<p>The reason a contact can be disconnected. Only Connect Customer outbound campaigns can provide this field. For a list and description of all the possible disconnect reasons by channel (including outbound campaign voice contacts) see DisconnectReason under <a href="https://docs.aws.amazon.com/connect/latest/adminguide/ctr-data-model.html#ctr-ContactTraceRecord">ContactTraceRecord</a> in the <i>Connect Customer Administrator Guide</i>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopContactRequest) -> dict:
    out: dict = {}
    out["ContactId"] = value["contact_id"]
    out["InstanceId"] = value["instance_id"]
    if "disconnect_reason" in value:
        import capo_connect.types.disconnect_reason

        out["DisconnectReason"] = capo_connect.types.disconnect_reason.serialize_json(
            value["disconnect_reason"]
        )
    return out


def deserialize_json(data: dict) -> StopContactRequest:
    out: StopContactRequest = {}  # type: ignore[typeddict-item]
    if data.get("ContactId") is not None:
        out["contact_id"] = data["ContactId"]
    else:
        raise DeserializationError("StopContactRequest.contact_id required")
    if data.get("InstanceId") is not None:
        out["instance_id"] = data["InstanceId"]
    else:
        raise DeserializationError("StopContactRequest.instance_id required")
    if data.get("DisconnectReason") is not None:
        import capo_connect.types.disconnect_reason

        out["disconnect_reason"] = (
            capo_connect.types.disconnect_reason.deserialize_json(
                data["DisconnectReason"]
            )
        )
    return out
