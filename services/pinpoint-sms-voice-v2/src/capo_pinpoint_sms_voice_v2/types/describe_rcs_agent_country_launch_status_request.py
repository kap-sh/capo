"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#DescribeRcsAgentCountryLaunchStatusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.country_launch_status_filter_list
    import capo_pinpoint_sms_voice_v2.types.iso_country_code_list
    import capo_pinpoint_sms_voice_v2.types.max_results
    import capo_pinpoint_sms_voice_v2.types.next_token
    import capo_pinpoint_sms_voice_v2.types.rcs_agent_id_or_arn


class DescribeRcsAgentCountryLaunchStatusRequest(TypedDict, closed=True):
    rcs_agent_id: "capo_pinpoint_sms_voice_v2.types.rcs_agent_id_or_arn.RcsAgentIdOrArn"
    """<p>The unique identifier of the RCS agent. You can use either the RcsAgentId or RcsAgentArn.</p>"""
    iso_country_codes: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.iso_country_code_list.IsoCountryCodeList"
    ]
    """<p>An array of two-character ISO country codes, in ISO 3166-1 alpha-2 format, to filter the results.</p>"""
    filters: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.country_launch_status_filter_list.CountryLaunchStatusFilterList"
    ]
    """<p>An array of CountryLaunchStatusFilter objects to filter the results.</p>"""
    max_results: NotRequired["capo_pinpoint_sms_voice_v2.types.max_results.MaxResults"]
    """<p>The maximum number of results to return per each request.</p>"""
    next_token: NotRequired["capo_pinpoint_sms_voice_v2.types.next_token.NextToken"]
    """<p>The token to be used for the next set of paginated results. You don't need to supply a value for this field in the initial request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeRcsAgentCountryLaunchStatusRequest) -> dict:
    out: dict = {}
    out["RcsAgentId"] = value["rcs_agent_id"]
    if "iso_country_codes" in value:
        import capo_pinpoint_sms_voice_v2.types.iso_country_code_list

        out["IsoCountryCodes"] = (
            capo_pinpoint_sms_voice_v2.types.iso_country_code_list.serialize_aws_json_1_0(
                value["iso_country_codes"]
            )
        )
    if "filters" in value:
        import capo_pinpoint_sms_voice_v2.types.country_launch_status_filter_list

        out["Filters"] = (
            capo_pinpoint_sms_voice_v2.types.country_launch_status_filter_list.serialize_aws_json_1_0(
                value["filters"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeRcsAgentCountryLaunchStatusRequest:
    out: DescribeRcsAgentCountryLaunchStatusRequest = {}  # type: ignore[typeddict-item]
    if data.get("RcsAgentId") is not None:
        out["rcs_agent_id"] = data["RcsAgentId"]
    else:
        out["rcs_agent_id"] = ""
    if data.get("IsoCountryCodes") is not None:
        import capo_pinpoint_sms_voice_v2.types.iso_country_code_list

        out["iso_country_codes"] = (
            capo_pinpoint_sms_voice_v2.types.iso_country_code_list.deserialize_aws_json_1_0(
                data["IsoCountryCodes"]
            )
        )
    if data.get("Filters") is not None:
        import capo_pinpoint_sms_voice_v2.types.country_launch_status_filter_list

        out["filters"] = (
            capo_pinpoint_sms_voice_v2.types.country_launch_status_filter_list.deserialize_aws_json_1_0(
                data["Filters"]
            )
        )
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
