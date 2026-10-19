"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#DeleteRegistrationFieldValueRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.field_path
    import capo_pinpoint_sms_voice_v2.types.registration_id_or_arn


class DeleteRegistrationFieldValueRequest(TypedDict, closed=True):
    registration_id: (
        "capo_pinpoint_sms_voice_v2.types.registration_id_or_arn.RegistrationIdOrArn"
    )
    """<p>The unique identifier for the registration.</p>"""
    field_path: "capo_pinpoint_sms_voice_v2.types.field_path.FieldPath"
    """<p>The path to the registration form field. You can use <a>DescribeRegistrationFieldDefinitions</a> for a list of <b>FieldPaths</b>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteRegistrationFieldValueRequest) -> dict:
    out: dict = {}
    out["RegistrationId"] = value["registration_id"]
    out["FieldPath"] = value["field_path"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteRegistrationFieldValueRequest:
    out: DeleteRegistrationFieldValueRequest = {}  # type: ignore[typeddict-item]
    if data.get("RegistrationId") is not None:
        out["registration_id"] = data["RegistrationId"]
    else:
        out["registration_id"] = ""
    if data.get("FieldPath") is not None:
        out["field_path"] = data["FieldPath"]
    else:
        out["field_path"] = ""
    return out
