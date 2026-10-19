"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#PutRegistrationFieldValueRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.field_path
    import capo_pinpoint_sms_voice_v2.types.registration_attachment_id_or_arn
    import capo_pinpoint_sms_voice_v2.types.registration_id_or_arn
    import capo_pinpoint_sms_voice_v2.types.select_choice_list
    import capo_pinpoint_sms_voice_v2.types.text_value


class PutRegistrationFieldValueRequest(TypedDict, closed=True):
    registration_id: (
        "capo_pinpoint_sms_voice_v2.types.registration_id_or_arn.RegistrationIdOrArn"
    )
    """<p>The unique identifier for the registration.</p>"""
    field_path: "capo_pinpoint_sms_voice_v2.types.field_path.FieldPath"
    """<p>The path to the registration form field. You can use <a>DescribeRegistrationFieldDefinitions</a> for a list of <b>FieldPaths</b>.</p>"""
    select_choices: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.select_choice_list.SelectChoiceList"
    ]
    """<p>An array of values for the form field.</p>"""
    text_value: NotRequired["capo_pinpoint_sms_voice_v2.types.text_value.TextValue"]
    """<p>The text data for a free form field.</p>"""
    registration_attachment_id: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.registration_attachment_id_or_arn.RegistrationAttachmentIdOrArn"
    ]
    """<p>The unique identifier for the registration attachment.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PutRegistrationFieldValueRequest) -> dict:
    out: dict = {}
    out["RegistrationId"] = value["registration_id"]
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


def deserialize_aws_json_1_0(data: dict) -> PutRegistrationFieldValueRequest:
    out: PutRegistrationFieldValueRequest = {}  # type: ignore[typeddict-item]
    if data.get("RegistrationId") is not None:
        out["registration_id"] = data["RegistrationId"]
    else:
        out["registration_id"] = ""
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
