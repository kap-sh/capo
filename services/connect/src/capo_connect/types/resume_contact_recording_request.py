"""Generated from Smithy shape ``com.amazonaws.connect#ResumeContactRecordingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.contact_id
    import capo_connect.types.contact_recording_type
    import capo_connect.types.instance_id


class ResumeContactRecordingRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    contact_id: "capo_connect.types.contact_id.ContactId"
    """<p>The identifier of the contact.</p>"""
    initial_contact_id: "capo_connect.types.contact_id.ContactId"
    """<p>The identifier of the contact. This is the identifier of the contact associated with the first interaction with the contact center.</p>"""
    contact_recording_type: NotRequired[
        "capo_connect.types.contact_recording_type.ContactRecordingType"
    ]
    """<p>The type of recording being operated on.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResumeContactRecordingRequest) -> dict:
    out: dict = {}
    out["InstanceId"] = value["instance_id"]
    out["ContactId"] = value["contact_id"]
    out["InitialContactId"] = value["initial_contact_id"]
    if "contact_recording_type" in value:
        import capo_connect.types.contact_recording_type

        out["ContactRecordingType"] = (
            capo_connect.types.contact_recording_type.serialize_json(
                value["contact_recording_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> ResumeContactRecordingRequest:
    out: ResumeContactRecordingRequest = {}  # type: ignore[typeddict-item]
    if data.get("InstanceId") is not None:
        out["instance_id"] = data["InstanceId"]
    else:
        raise DeserializationError("ResumeContactRecordingRequest.instance_id required")
    if data.get("ContactId") is not None:
        out["contact_id"] = data["ContactId"]
    else:
        raise DeserializationError("ResumeContactRecordingRequest.contact_id required")
    if data.get("InitialContactId") is not None:
        out["initial_contact_id"] = data["InitialContactId"]
    else:
        raise DeserializationError(
            "ResumeContactRecordingRequest.initial_contact_id required"
        )
    if data.get("ContactRecordingType") is not None:
        import capo_connect.types.contact_recording_type

        out["contact_recording_type"] = (
            capo_connect.types.contact_recording_type.deserialize_json(
                data["ContactRecordingType"]
            )
        )
    return out
