"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#RegistrationVersionInformation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.registration_denied_reason_information_list
    import capo_pinpoint_sms_voice_v2.types.registration_version_number
    import capo_pinpoint_sms_voice_v2.types.registration_version_status
    import capo_pinpoint_sms_voice_v2.types.registration_version_status_history


class RegistrationVersionInformation(TypedDict, closed=True):
    version_number: "capo_pinpoint_sms_voice_v2.types.registration_version_number.RegistrationVersionNumber"
    """<p>The version number of the registration.</p>"""
    registration_version_status: "capo_pinpoint_sms_voice_v2.types.registration_version_status.RegistrationVersionStatus"
    """<p>The status of the registration.</p> <ul> <li> <p> <code>APPROVED</code>: Your registration has been approved.</p> </li> <li> <p> <code>ARCHIVED</code>: Your previously approved registration version moves into this status when a more recently submitted version is approved.</p> </li> <li> <p> <code>DENIED</code>: You must fix your registration and resubmit it.</p> </li> <li> <p> <code>DISCARDED</code>: You've abandon this version of their registration to start over with a new version. </p> </li> <li> <p> <code>DRAFT</code>: The initial status of a registration version after it’s created.</p> </li> <li> <p> <code>REQUIRES_AUTHENTICATION</code>: You need to complete email authentication.</p> </li> <li> <p> <code>REVIEWING</code>: Your registration has been accepted and is being reviewed.</p> </li> <li> <p> <code>REVOKED</code>: Your previously approved registration has been revoked.</p> </li> <li> <p> <code>SUBMITTED</code>: Your registration has been submitted.</p> </li> </ul>"""
    registration_version_status_history: "capo_pinpoint_sms_voice_v2.types.registration_version_status_history.RegistrationVersionStatusHistory"
    """<p>The <b>RegistrationVersionStatusHistory</b> object contains the time stamps for when the reservations status changes.</p>"""
    denied_reasons: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.registration_denied_reason_information_list.RegistrationDeniedReasonInformationList"
    ]
    """<p>An array of RegistrationDeniedReasonInformation objects. </p>"""
    feedback: NotRequired["str"]
    """<p>Generative AI feedback information provided during the registration review process. This includes comments, suggestions, or additional requirements.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RegistrationVersionInformation) -> dict:
    out: dict = {}
    out["VersionNumber"] = value["version_number"]
    out["RegistrationVersionStatus"] = value["registration_version_status"]
    import capo_pinpoint_sms_voice_v2.types.registration_version_status_history

    out["RegistrationVersionStatusHistory"] = (
        capo_pinpoint_sms_voice_v2.types.registration_version_status_history.serialize_aws_json_1_0(
            value["registration_version_status_history"]
        )
    )
    if "denied_reasons" in value:
        import capo_pinpoint_sms_voice_v2.types.registration_denied_reason_information_list

        out["DeniedReasons"] = (
            capo_pinpoint_sms_voice_v2.types.registration_denied_reason_information_list.serialize_aws_json_1_0(
                value["denied_reasons"]
            )
        )
    if "feedback" in value:
        out["Feedback"] = value["feedback"]
    return out


def deserialize_aws_json_1_0(data: dict) -> RegistrationVersionInformation:
    out: RegistrationVersionInformation = {}  # type: ignore[typeddict-item]
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
            "RegistrationVersionInformation.registration_version_status_history required"
        )
    if data.get("DeniedReasons") is not None:
        import capo_pinpoint_sms_voice_v2.types.registration_denied_reason_information_list

        out["denied_reasons"] = (
            capo_pinpoint_sms_voice_v2.types.registration_denied_reason_information_list.deserialize_aws_json_1_0(
                data["DeniedReasons"]
            )
        )
    if data.get("Feedback") is not None:
        out["feedback"] = data["Feedback"]
    return out
