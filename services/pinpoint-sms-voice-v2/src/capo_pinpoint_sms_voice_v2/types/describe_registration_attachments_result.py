"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#DescribeRegistrationAttachmentsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.next_token
    import capo_pinpoint_sms_voice_v2.types.registration_attachments_information_list


class DescribeRegistrationAttachmentsResult(TypedDict, closed=True):
    registration_attachments: "capo_pinpoint_sms_voice_v2.types.registration_attachments_information_list.RegistrationAttachmentsInformationList"
    """<p>An array of <b>RegistrationAttachments</b> objects that contain the details for the requested registration attachments. </p>"""
    next_token: NotRequired["capo_pinpoint_sms_voice_v2.types.next_token.NextToken"]
    """<p>The token to be used for the next set of paginated results. You don't need to supply a value for this field in the initial request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeRegistrationAttachmentsResult) -> dict:
    out: dict = {}
    import capo_pinpoint_sms_voice_v2.types.registration_attachments_information_list

    out["RegistrationAttachments"] = (
        capo_pinpoint_sms_voice_v2.types.registration_attachments_information_list.serialize_aws_json_1_0(
            value["registration_attachments"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeRegistrationAttachmentsResult:
    out: DescribeRegistrationAttachmentsResult = {}  # type: ignore[typeddict-item]
    if data.get("RegistrationAttachments") is not None:
        import capo_pinpoint_sms_voice_v2.types.registration_attachments_information_list

        out["registration_attachments"] = (
            capo_pinpoint_sms_voice_v2.types.registration_attachments_information_list.deserialize_aws_json_1_0(
                data["RegistrationAttachments"]
            )
        )
    else:
        out["registration_attachments"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
