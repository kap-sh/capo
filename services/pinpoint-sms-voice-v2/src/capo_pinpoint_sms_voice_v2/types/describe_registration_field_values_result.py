"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#DescribeRegistrationFieldValuesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.next_token
    import capo_pinpoint_sms_voice_v2.types.registration_field_value_information_list
    import capo_pinpoint_sms_voice_v2.types.registration_version_number


class DescribeRegistrationFieldValuesResult(TypedDict, closed=True):
    registration_arn: "str"
    """<p>The Amazon Resource Name (ARN) for the registration.</p>"""
    registration_id: "str"
    """<p>The unique identifier for the registration.</p>"""
    version_number: "capo_pinpoint_sms_voice_v2.types.registration_version_number.RegistrationVersionNumber"
    """<p>The current version of the registration.</p>"""
    registration_field_values: "capo_pinpoint_sms_voice_v2.types.registration_field_value_information_list.RegistrationFieldValueInformationList"
    """<p>An array of RegistrationFieldValues objects that contain the values for the requested registration. </p>"""
    next_token: NotRequired["capo_pinpoint_sms_voice_v2.types.next_token.NextToken"]
    """<p>The token to be used for the next set of paginated results. You don't need to supply a value for this field in the initial request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeRegistrationFieldValuesResult) -> dict:
    out: dict = {}
    out["RegistrationArn"] = value["registration_arn"]
    out["RegistrationId"] = value["registration_id"]
    out["VersionNumber"] = value["version_number"]
    import capo_pinpoint_sms_voice_v2.types.registration_field_value_information_list

    out["RegistrationFieldValues"] = (
        capo_pinpoint_sms_voice_v2.types.registration_field_value_information_list.serialize_aws_json_1_0(
            value["registration_field_values"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeRegistrationFieldValuesResult:
    out: DescribeRegistrationFieldValuesResult = {}  # type: ignore[typeddict-item]
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
    if data.get("RegistrationFieldValues") is not None:
        import capo_pinpoint_sms_voice_v2.types.registration_field_value_information_list

        out["registration_field_values"] = (
            capo_pinpoint_sms_voice_v2.types.registration_field_value_information_list.deserialize_aws_json_1_0(
                data["RegistrationFieldValues"]
            )
        )
    else:
        out["registration_field_values"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
