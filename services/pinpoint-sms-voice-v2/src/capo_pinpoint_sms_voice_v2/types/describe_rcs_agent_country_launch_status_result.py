"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#DescribeRcsAgentCountryLaunchStatusResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.country_launch_status_information_list
    import capo_pinpoint_sms_voice_v2.types.next_token


class DescribeRcsAgentCountryLaunchStatusResult(TypedDict, closed=True):
    rcs_agent_id: "str"
    """<p>The unique identifier for the RCS agent.</p>"""
    rcs_agent_arn: "str"
    """<p>The Amazon Resource Name (ARN) of the RCS agent.</p>"""
    country_launch_status: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.country_launch_status_information_list.CountryLaunchStatusInformationList"
    ]
    """<p>An array of CountryLaunchStatusInformation objects that contain the per-country launch status details.</p>"""
    next_token: NotRequired["capo_pinpoint_sms_voice_v2.types.next_token.NextToken"]
    """<p>The token to be used for the next set of paginated results. If this field is empty then there are no more results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeRcsAgentCountryLaunchStatusResult) -> dict:
    out: dict = {}
    out["RcsAgentId"] = value["rcs_agent_id"]
    out["RcsAgentArn"] = value["rcs_agent_arn"]
    if "country_launch_status" in value:
        import capo_pinpoint_sms_voice_v2.types.country_launch_status_information_list

        out["CountryLaunchStatus"] = (
            capo_pinpoint_sms_voice_v2.types.country_launch_status_information_list.serialize_aws_json_1_0(
                value["country_launch_status"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeRcsAgentCountryLaunchStatusResult:
    out: DescribeRcsAgentCountryLaunchStatusResult = {}  # type: ignore[typeddict-item]
    if data.get("RcsAgentId") is not None:
        out["rcs_agent_id"] = data["RcsAgentId"]
    else:
        out["rcs_agent_id"] = ""
    if data.get("RcsAgentArn") is not None:
        out["rcs_agent_arn"] = data["RcsAgentArn"]
    else:
        out["rcs_agent_arn"] = ""
    if data.get("CountryLaunchStatus") is not None:
        import capo_pinpoint_sms_voice_v2.types.country_launch_status_information_list

        out["country_launch_status"] = (
            capo_pinpoint_sms_voice_v2.types.country_launch_status_information_list.deserialize_aws_json_1_0(
                data["CountryLaunchStatus"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
