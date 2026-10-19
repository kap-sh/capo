"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#CreateRegistrationAssociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.registration_id_or_arn
    import capo_pinpoint_sms_voice_v2.types.resource_id_or_arn


class CreateRegistrationAssociationRequest(TypedDict, closed=True):
    registration_id: (
        "capo_pinpoint_sms_voice_v2.types.registration_id_or_arn.RegistrationIdOrArn"
    )
    """<p>The unique identifier for the registration.</p>"""
    resource_id: "capo_pinpoint_sms_voice_v2.types.resource_id_or_arn.ResourceIdOrArn"
    """<p>The unique identifier for the origination identity. For example this could be a <b>PhoneNumberId</b> or <b>SenderId</b>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateRegistrationAssociationRequest) -> dict:
    out: dict = {}
    out["RegistrationId"] = value["registration_id"]
    out["ResourceId"] = value["resource_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateRegistrationAssociationRequest:
    out: CreateRegistrationAssociationRequest = {}  # type: ignore[typeddict-item]
    if data.get("RegistrationId") is not None:
        out["registration_id"] = data["RegistrationId"]
    else:
        out["registration_id"] = ""
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    else:
        out["resource_id"] = ""
    return out
