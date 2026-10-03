"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#DeleteRegistrationAttachmentResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_pinpoint_sms_voice_v2.types.attachment_status
    import capo_pinpoint_sms_voice_v2.types.attachment_upload_error_reason


class DeleteRegistrationAttachmentResult(TypedDict, closed=True):
    registration_attachment_arn: "str"
    """<p>The Amazon Resource Name (ARN) for the registration attachment.</p>"""
    registration_attachment_id: "str"
    """<p>The unique identifier for the registration attachment.</p>"""
    attachment_status: (
        "capo_pinpoint_sms_voice_v2.types.attachment_status.AttachmentStatus"
    )
    """<p>The status of the registration attachment. </p> <ul> <li> <p> <code>UPLOAD_IN_PROGRESS</code> The attachment is being uploaded.</p> </li> <li> <p> <code>UPLOAD_COMPLETE</code> The attachment has been uploaded.</p> </li> <li> <p> <code>UPLOAD_FAILED</code> The attachment failed to uploaded.</p> </li> <li> <p> <code>DELETED</code> The attachment has been deleted..</p> </li> </ul>"""
    attachment_upload_error_reason: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.attachment_upload_error_reason.AttachmentUploadErrorReason"
    ]
    """<p>The error message if the upload failed.</p>"""
    created_timestamp: "datetime.datetime"
    """<p>The time when the registration attachment was created, in <a href="https://www.epochconverter.com/">UNIX epoch time</a> format.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteRegistrationAttachmentResult) -> dict:
    out: dict = {}
    out["RegistrationAttachmentArn"] = value["registration_attachment_arn"]
    out["RegistrationAttachmentId"] = value["registration_attachment_id"]
    out["AttachmentStatus"] = value["attachment_status"]
    if "attachment_upload_error_reason" in value:
        out["AttachmentUploadErrorReason"] = value["attachment_upload_error_reason"]
    import capo_pinpoint_sms_voice_v2.types._prelude.timestamp

    out["CreatedTimestamp"] = (
        capo_pinpoint_sms_voice_v2.types._prelude.timestamp.serialize_aws_json_1_0(
            value["created_timestamp"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteRegistrationAttachmentResult:
    out: DeleteRegistrationAttachmentResult = {}  # type: ignore[typeddict-item]
    if data.get("RegistrationAttachmentArn") is not None:
        out["registration_attachment_arn"] = data["RegistrationAttachmentArn"]
    else:
        raise DeserializationError(
            "DeleteRegistrationAttachmentResult.registration_attachment_arn required"
        )
    if data.get("RegistrationAttachmentId") is not None:
        out["registration_attachment_id"] = data["RegistrationAttachmentId"]
    else:
        raise DeserializationError(
            "DeleteRegistrationAttachmentResult.registration_attachment_id required"
        )
    if data.get("AttachmentStatus") is not None:
        out["attachment_status"] = data["AttachmentStatus"]
    else:
        raise DeserializationError(
            "DeleteRegistrationAttachmentResult.attachment_status required"
        )
    if data.get("AttachmentUploadErrorReason") is not None:
        out["attachment_upload_error_reason"] = data["AttachmentUploadErrorReason"]
    if data.get("CreatedTimestamp") is not None:
        import capo_pinpoint_sms_voice_v2.types._prelude.timestamp

        out["created_timestamp"] = (
            capo_pinpoint_sms_voice_v2.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["CreatedTimestamp"]
            )
        )
    else:
        raise DeserializationError(
            "DeleteRegistrationAttachmentResult.created_timestamp required"
        )
    return out
