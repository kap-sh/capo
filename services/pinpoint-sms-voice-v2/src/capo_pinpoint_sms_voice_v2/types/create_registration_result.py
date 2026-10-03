"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#CreateRegistrationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_pinpoint_sms_voice_v2.types.registration_status
    import capo_pinpoint_sms_voice_v2.types.registration_type
    import capo_pinpoint_sms_voice_v2.types.registration_version_number
    import capo_pinpoint_sms_voice_v2.types.string_map
    import capo_pinpoint_sms_voice_v2.types.tag_list


class CreateRegistrationResult(TypedDict, closed=True):
    registration_arn: "str"
    """<p>The Amazon Resource Name (ARN) for the registration.</p>"""
    registration_id: "str"
    """<p>The unique identifier for the registration.</p>"""
    registration_type: (
        "capo_pinpoint_sms_voice_v2.types.registration_type.RegistrationType"
    )
    """<p>The type of registration form to create. The list of <b>RegistrationTypes</b> can be found using the <a>DescribeRegistrationTypeDefinitions</a> action.</p>"""
    registration_status: (
        "capo_pinpoint_sms_voice_v2.types.registration_status.RegistrationStatus"
    )
    """<p>The status of the registration.</p> <ul> <li> <p> <code>CLOSED</code>: The phone number or sender ID has been deleted and you must also delete the registration for the number.</p> </li> <li> <p> <code>CREATED</code>: Your registration is created but not submitted.</p> </li> <li> <p> <code>COMPLETE</code>: Your registration has been approved and your origination identity has been created.</p> </li> <li> <p> <code>DELETED</code>: The registration has been deleted.</p> </li> <li> <p> <code>PROVISIONING</code>: Your registration has been approved and your origination identity is being created.</p> </li> <li> <p> <code>REQUIRES_AUTHENTICATION</code>: You need to complete email authentication.</p> </li> <li> <p> <code>REQUIRES_UPDATES</code>: You must fix your registration and resubmit it.</p> </li> <li> <p> <code>REVIEWING</code>: Your registration has been accepted and is being reviewed.</p> </li> <li> <p> <code>SUBMITTED</code>: Your registration has been submitted and is awaiting review.</p> </li> </ul>"""
    current_version_number: "capo_pinpoint_sms_voice_v2.types.registration_version_number.RegistrationVersionNumber"
    """<p>The current version number of the registration.</p>"""
    additional_attributes: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.string_map.StringMap"
    ]
    """<p>Metadata about a given registration which is specific to that registration type.</p>"""
    tags: NotRequired["capo_pinpoint_sms_voice_v2.types.tag_list.TagList"]
    """<p>An array of tags (key and value pairs) to associate with the registration.</p>"""
    created_timestamp: "datetime.datetime"
    """<p>The time when the registration was created, in <a href="https://www.epochconverter.com/">UNIX epoch time</a> format.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateRegistrationResult) -> dict:
    out: dict = {}
    out["RegistrationArn"] = value["registration_arn"]
    out["RegistrationId"] = value["registration_id"]
    out["RegistrationType"] = value["registration_type"]
    out["RegistrationStatus"] = value["registration_status"]
    out["CurrentVersionNumber"] = value["current_version_number"]
    if "additional_attributes" in value:
        import capo_pinpoint_sms_voice_v2.types.string_map

        out["AdditionalAttributes"] = (
            capo_pinpoint_sms_voice_v2.types.string_map.serialize_aws_json_1_0(
                value["additional_attributes"]
            )
        )
    if "tags" in value:
        import capo_pinpoint_sms_voice_v2.types.tag_list

        out["Tags"] = capo_pinpoint_sms_voice_v2.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    import capo_pinpoint_sms_voice_v2.types._prelude.timestamp

    out["CreatedTimestamp"] = (
        capo_pinpoint_sms_voice_v2.types._prelude.timestamp.serialize_aws_json_1_0(
            value["created_timestamp"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateRegistrationResult:
    out: CreateRegistrationResult = {}  # type: ignore[typeddict-item]
    if data.get("RegistrationArn") is not None:
        out["registration_arn"] = data["RegistrationArn"]
    else:
        raise DeserializationError("CreateRegistrationResult.registration_arn required")
    if data.get("RegistrationId") is not None:
        out["registration_id"] = data["RegistrationId"]
    else:
        raise DeserializationError("CreateRegistrationResult.registration_id required")
    if data.get("RegistrationType") is not None:
        out["registration_type"] = data["RegistrationType"]
    else:
        raise DeserializationError(
            "CreateRegistrationResult.registration_type required"
        )
    if data.get("RegistrationStatus") is not None:
        out["registration_status"] = data["RegistrationStatus"]
    else:
        raise DeserializationError(
            "CreateRegistrationResult.registration_status required"
        )
    if data.get("CurrentVersionNumber") is not None:
        out["current_version_number"] = data["CurrentVersionNumber"]
    else:
        raise DeserializationError(
            "CreateRegistrationResult.current_version_number required"
        )
    if data.get("AdditionalAttributes") is not None:
        import capo_pinpoint_sms_voice_v2.types.string_map

        out["additional_attributes"] = (
            capo_pinpoint_sms_voice_v2.types.string_map.deserialize_aws_json_1_0(
                data["AdditionalAttributes"]
            )
        )
    if data.get("Tags") is not None:
        import capo_pinpoint_sms_voice_v2.types.tag_list

        out["tags"] = (
            capo_pinpoint_sms_voice_v2.types.tag_list.deserialize_aws_json_1_0(
                data["Tags"]
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
            "CreateRegistrationResult.created_timestamp required"
        )
    return out
