"""Generated from Smithy shape ``com.amazonaws.connect#UpdateContactScheduleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.contact_id
    import capo_connect.types.instance_id
    import capo_connect.types.timestamp


class UpdateContactScheduleRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    contact_id: "capo_connect.types.contact_id.ContactId"
    """<p>The identifier of the contact.</p>"""
    scheduled_time: "capo_connect.types.timestamp.Timestamp"
    """<p>The timestamp, in Unix Epoch seconds format, at which to start running the inbound flow. The scheduled time cannot be in the past. It must be within up to 6 days in future. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateContactScheduleRequest) -> dict:
    out: dict = {}
    out["InstanceId"] = value["instance_id"]
    out["ContactId"] = value["contact_id"]
    import capo_connect.types.timestamp

    out["ScheduledTime"] = capo_connect.types.timestamp.serialize_json(
        value["scheduled_time"]
    )
    return out


def deserialize_json(data: dict) -> UpdateContactScheduleRequest:
    out: UpdateContactScheduleRequest = {}  # type: ignore[typeddict-item]
    if data.get("InstanceId") is not None:
        out["instance_id"] = data["InstanceId"]
    else:
        raise DeserializationError("UpdateContactScheduleRequest.instance_id required")
    if data.get("ContactId") is not None:
        out["contact_id"] = data["ContactId"]
    else:
        raise DeserializationError("UpdateContactScheduleRequest.contact_id required")
    if data.get("ScheduledTime") is not None:
        import capo_connect.types.timestamp

        out["scheduled_time"] = capo_connect.types.timestamp.deserialize_json(
            data["ScheduledTime"]
        )
    else:
        raise DeserializationError(
            "UpdateContactScheduleRequest.scheduled_time required"
        )
    return out
