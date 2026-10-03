"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#DeleteRegistrationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_pinpoint_sms_voice_v2.types.registration_status
    import capo_pinpoint_sms_voice_v2.types.registration_type
    import capo_pinpoint_sms_voice_v2.types.registration_version_number
    import capo_pinpoint_sms_voice_v2.types.string_map


class DeleteRegistrationResult(TypedDict, closed=True):
    registration_arn: "str"
    """<p>The Amazon Resource Name (ARN) for the registration.</p>"""
    registration_id: "str"
    """<p>The unique identifier for the registration.</p>"""
    registration_type: (
        "capo_pinpoint_sms_voice_v2.types.registration_type.RegistrationType"
    )
    """<p>The type of registration form. The list of <b>RegistrationTypes</b> can be found using the <a>DescribeRegistrationTypeDefinitions</a> action.</p>"""
    registration_status: (
        "capo_pinpoint_sms_voice_v2.types.registration_status.RegistrationStatus"
    )
    """<p>The status of the registration.</p> <ul> <li> <p> <code>CLOSED</code>: The phone number or sender ID has been deleted and you must also delete the registration for the number.</p> </li> <li> <p> <code>CREATED</code>: Your registration is created but not submitted.</p> </li> <li> <p> <code>COMPLETE</code>: Your registration has been approved and your origination identity has been created.</p> </li> <li> <p> <code>DELETED</code>: The registration has been deleted.</p> </li> <li> <p> <code>PROVISIONING</code>: Your registration has been approved and your origination identity is being created.</p> </li> <li> <p> <code>REQUIRES_AUTHENTICATION</code>: You need to complete email authentication.</p> </li> <li> <p> <code>REQUIRES_UPDATES</code>: You must fix your registration and resubmit it.</p> </li> <li> <p> <code>REVIEWING</code>: Your registration has been accepted and is being reviewed.</p> </li> <li> <p> <code>SUBMITTED</code>: Your registration has been submitted and is awaiting review.</p> </li> </ul>"""
    current_version_number: "capo_pinpoint_sms_voice_v2.types.registration_version_number.RegistrationVersionNumber"
    """<p>The current version number of the registration.</p>"""
    approved_version_number: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.registration_version_number.RegistrationVersionNumber"
    ]
    """<p>The version number of the registration that was approved.</p>"""
    latest_denied_version_number: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.registration_version_number.RegistrationVersionNumber"
    ]
    """<p>The latest version number of the registration that was denied.</p>"""
    additional_attributes: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.string_map.StringMap"
    ]
    """<p>Metadata about a given registration which is specific to that registration type.</p>"""
    created_timestamp: "datetime.datetime"
    """<p>The time when the registration was created, in <a href="https://www.epochconverter.com/">UNIX epoch time</a> format.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteRegistrationResult) -> dict:
    out: dict = {}
    out["RegistrationArn"] = value["registration_arn"]
    out["RegistrationId"] = value["registration_id"]
    out["RegistrationType"] = value["registration_type"]
    out["RegistrationStatus"] = value["registration_status"]
    out["CurrentVersionNumber"] = value["current_version_number"]
    if "approved_version_number" in value:
        out["ApprovedVersionNumber"] = value["approved_version_number"]
    if "latest_denied_version_number" in value:
        out["LatestDeniedVersionNumber"] = value["latest_denied_version_number"]
    if "additional_attributes" in value:
        import capo_pinpoint_sms_voice_v2.types.string_map

        out["AdditionalAttributes"] = (
            capo_pinpoint_sms_voice_v2.types.string_map.serialize_aws_json_1_0(
                value["additional_attributes"]
            )
        )
    import capo_pinpoint_sms_voice_v2.types._prelude.timestamp

    out["CreatedTimestamp"] = (
        capo_pinpoint_sms_voice_v2.types._prelude.timestamp.serialize_aws_json_1_0(
            value["created_timestamp"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteRegistrationResult:
    out: DeleteRegistrationResult = {}  # type: ignore[typeddict-item]
    if data.get("RegistrationArn") is not None:
        out["registration_arn"] = data["RegistrationArn"]
    else:
        raise DeserializationError("DeleteRegistrationResult.registration_arn required")
    if data.get("RegistrationId") is not None:
        out["registration_id"] = data["RegistrationId"]
    else:
        raise DeserializationError("DeleteRegistrationResult.registration_id required")
    if data.get("RegistrationType") is not None:
        out["registration_type"] = data["RegistrationType"]
    else:
        raise DeserializationError(
            "DeleteRegistrationResult.registration_type required"
        )
    if data.get("RegistrationStatus") is not None:
        out["registration_status"] = data["RegistrationStatus"]
    else:
        raise DeserializationError(
            "DeleteRegistrationResult.registration_status required"
        )
    if data.get("CurrentVersionNumber") is not None:
        out["current_version_number"] = data["CurrentVersionNumber"]
    else:
        raise DeserializationError(
            "DeleteRegistrationResult.current_version_number required"
        )
    if data.get("ApprovedVersionNumber") is not None:
        out["approved_version_number"] = data["ApprovedVersionNumber"]
    if data.get("LatestDeniedVersionNumber") is not None:
        out["latest_denied_version_number"] = data["LatestDeniedVersionNumber"]
    if data.get("AdditionalAttributes") is not None:
        import capo_pinpoint_sms_voice_v2.types.string_map

        out["additional_attributes"] = (
            capo_pinpoint_sms_voice_v2.types.string_map.deserialize_aws_json_1_0(
                data["AdditionalAttributes"]
            )
        )
    if data.get("CreatedTimestamp") is not None:
        import capo_pinpoint_sms_voice_v2.types._prelude.timestamp

        out["created_timestamp"] = (
            capo_pinpoint_sms_voice_v2.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["CreatedTimestamp"]
            )
        )
    else:
        raise DeserializationError(
            "DeleteRegistrationResult.created_timestamp required"
        )
    return out
