"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#SubmitRegistrationVersionResult``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.registration_version_number
    import capo_pinpoint_sms_voice_v2.types.registration_version_status
    import capo_pinpoint_sms_voice_v2.types.registration_version_status_history


class SubmitRegistrationVersionResult(TypedDict, closed=True):
    registration_arn: "str"
    """<p>The Amazon Resource Name (ARN) for the registration.</p>"""
    registration_id: "str"
    """<p>The unique identifier for the registration.</p>"""
    version_number: "capo_pinpoint_sms_voice_v2.types.registration_version_number.RegistrationVersionNumber"
    """<p>The version number of the registration.</p>"""
    registration_version_status: "capo_pinpoint_sms_voice_v2.types.registration_version_status.RegistrationVersionStatus"
    """<p>The status of the registration version.</p> <ul> <li> <p> <code>APPROVED</code>: Your registration has been approved.</p> </li> <li> <p> <code>ARCHIVED</code>: Your previously approved registration version moves into this status when a more recently submitted version is approved.</p> </li> <li> <p> <code>DENIED</code>: You must fix your registration and resubmit it.</p> </li> <li> <p> <code>DISCARDED</code>: You've abandon this version of their registration to start over with a new version. </p> </li> <li> <p> <code>DRAFT</code>: The initial status of a registration version after it’s created.</p> </li> <li> <p> <code>REQUIRES_AUTHENTICATION</code>: You need to complete email authentication.</p> </li> <li> <p> <code>REVIEWING</code>: Your registration has been accepted and is being reviewed.</p> </li> <li> <p> <code>REVOKED</code>: Your previously approved registration has been revoked.</p> </li> <li> <p> <code>SUBMITTED</code>: Your registration has been submitted.</p> </li> </ul>"""
    registration_version_status_history: "capo_pinpoint_sms_voice_v2.types.registration_version_status_history.RegistrationVersionStatusHistory"
    """<p>The <b>RegistrationVersionStatusHistory</b> object contains the time stamps for when the reservations status changes.</p>"""
    aws_review: "bool"
    """<p>Indicates whether AWS review was requested for this registration submission.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SubmitRegistrationVersionResult) -> dict:
    out: dict = {}
    out["RegistrationArn"] = value["registration_arn"]
    out["RegistrationId"] = value["registration_id"]
    out["VersionNumber"] = value["version_number"]
    out["RegistrationVersionStatus"] = value["registration_version_status"]
    import capo_pinpoint_sms_voice_v2.types.registration_version_status_history

    out["RegistrationVersionStatusHistory"] = (
        capo_pinpoint_sms_voice_v2.types.registration_version_status_history.serialize_aws_json_1_0(
            value["registration_version_status_history"]
        )
    )
    out["AwsReview"] = value.get("aws_review", False)
    return out


def deserialize_aws_json_1_0(data: dict) -> SubmitRegistrationVersionResult:
    out: SubmitRegistrationVersionResult = {}  # type: ignore[typeddict-item]
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
    if data.get("RegistrationVersionStatus") is not None:
        out["registration_version_status"] = data["RegistrationVersionStatus"]
    else:
        out["registration_version_status"] = ""
    if data.get("RegistrationVersionStatusHistory") is not None:
        import capo_pinpoint_sms_voice_v2.types.registration_version_status_history

        out["registration_version_status_history"] = (
            capo_pinpoint_sms_voice_v2.types.registration_version_status_history.deserialize_aws_json_1_0(
                data["RegistrationVersionStatusHistory"]
            )
        )
    else:
        raise DeserializationError(
            "SubmitRegistrationVersionResult.registration_version_status_history required"
        )
    if data.get("AwsReview") is not None:
        out["aws_review"] = data["AwsReview"]
    else:
        out["aws_review"] = False
    return out
