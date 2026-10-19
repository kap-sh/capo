"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#DescribeRegistrationVersionsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.next_token
    import capo_pinpoint_sms_voice_v2.types.registration_version_information_list


class DescribeRegistrationVersionsResult(TypedDict, closed=True):
    registration_arn: "str"
    """<p>The Amazon Resource Name (ARN) for the registration.</p>"""
    registration_id: "str"
    """<p>The unique identifier for the registration.</p>"""
    registration_versions: "capo_pinpoint_sms_voice_v2.types.registration_version_information_list.RegistrationVersionInformationList"
    """<p>An array of RegistrationVersions objects.</p>"""
    next_token: NotRequired["capo_pinpoint_sms_voice_v2.types.next_token.NextToken"]
    """<p>The token to be used for the next set of paginated results. You don't need to supply a value for this field in the initial request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeRegistrationVersionsResult) -> dict:
    out: dict = {}
    out["RegistrationArn"] = value["registration_arn"]
    out["RegistrationId"] = value["registration_id"]
    import capo_pinpoint_sms_voice_v2.types.registration_version_information_list

    out["RegistrationVersions"] = (
        capo_pinpoint_sms_voice_v2.types.registration_version_information_list.serialize_aws_json_1_0(
            value["registration_versions"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeRegistrationVersionsResult:
    out: DescribeRegistrationVersionsResult = {}  # type: ignore[typeddict-item]
    if data.get("RegistrationArn") is not None:
        out["registration_arn"] = data["RegistrationArn"]
    else:
        out["registration_arn"] = ""
    if data.get("RegistrationId") is not None:
        out["registration_id"] = data["RegistrationId"]
    else:
        out["registration_id"] = ""
    if data.get("RegistrationVersions") is not None:
        import capo_pinpoint_sms_voice_v2.types.registration_version_information_list

        out["registration_versions"] = (
            capo_pinpoint_sms_voice_v2.types.registration_version_information_list.deserialize_aws_json_1_0(
                data["RegistrationVersions"]
            )
        )
    else:
        out["registration_versions"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
