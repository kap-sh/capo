"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#PutRegistrationFieldValueResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.field_path
    import capo_pinpoint_sms_voice_v2.types.registration_version_number
    import capo_pinpoint_sms_voice_v2.types.select_choice_list
    import capo_pinpoint_sms_voice_v2.types.text_value


class PutRegistrationFieldValueResult(TypedDict, closed=True):
    registration_arn: "str"
    """<p>The Amazon Resource Name (ARN) for the registration.</p>"""
    registration_id: "str"
    """<p>The unique identifier for the registration.</p>"""
    version_number: "capo_pinpoint_sms_voice_v2.types.registration_version_number.RegistrationVersionNumber"
    """<p>The version number of the registration.</p>"""
    field_path: "capo_pinpoint_sms_voice_v2.types.field_path.FieldPath"
    """<p>The path to the registration form field. You can use <a>DescribeRegistrationFieldDefinitions</a> for a list of <b>FieldPaths</b>.</p>"""
    select_choices: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.select_choice_list.SelectChoiceList"
    ]
    """<p>An array of values for the form field.</p>"""
    text_value: NotRequired["capo_pinpoint_sms_voice_v2.types.text_value.TextValue"]
    """<p>The text data for a free form field.</p>"""
    registration_attachment_id: NotRequired["str"]
    """<p>The unique identifier for the registration attachment.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PutRegistrationFieldValueResult) -> dict:
    out: dict = {}
    out["RegistrationArn"] = value["registration_arn"]
    out["RegistrationId"] = value["registration_id"]
    out["VersionNumber"] = value["version_number"]
    out["FieldPath"] = value["field_path"]
    if "select_choices" in value:
        import capo_pinpoint_sms_voice_v2.types.select_choice_list

        out["SelectChoices"] = (
            capo_pinpoint_sms_voice_v2.types.select_choice_list.serialize_aws_json_1_0(
                value["select_choices"]
            )
        )
    if "text_value" in value:
        out["TextValue"] = value["text_value"]
    if "registration_attachment_id" in value:
        out["RegistrationAttachmentId"] = value["registration_attachment_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> PutRegistrationFieldValueResult:
    out: PutRegistrationFieldValueResult = {}  # type: ignore[typeddict-item]
    if data.get("RegistrationArn") is not None:
        out["registration_arn"] = data["RegistrationArn"]
    else:
        out["registration_arn"] = ""
    if data.get("RegistrationId") is not None:
        out["registration_id"] = data["RegistrationId"]
    else:
        out["registration_id"] = ""
    if data.get("VersionNumber") is not None:
        out["version_number"] = data["VersionNumber"]
    else:
        out["version_number"] = 0
    if data.get("FieldPath") is not None:
        out["field_path"] = data["FieldPath"]
    else:
        out["field_path"] = ""
    if data.get("SelectChoices") is not None:
        import capo_pinpoint_sms_voice_v2.types.select_choice_list

        out["select_choices"] = (
            capo_pinpoint_sms_voice_v2.types.select_choice_list.deserialize_aws_json_1_0(
                data["SelectChoices"]
            )
        )
    if data.get("TextValue") is not None:
        out["text_value"] = data["TextValue"]
    if data.get("RegistrationAttachmentId") is not None:
        out["registration_attachment_id"] = data["RegistrationAttachmentId"]
    return out
