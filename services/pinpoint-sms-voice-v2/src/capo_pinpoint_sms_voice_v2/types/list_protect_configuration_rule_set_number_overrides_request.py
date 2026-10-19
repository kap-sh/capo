"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#ListProtectConfigurationRuleSetNumberOverridesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.list_protect_configuration_rule_set_number_override_filter
    import capo_pinpoint_sms_voice_v2.types.max_results
    import capo_pinpoint_sms_voice_v2.types.next_token
    import capo_pinpoint_sms_voice_v2.types.protect_configuration_id_or_arn


class ListProtectConfigurationRuleSetNumberOverridesRequest(TypedDict, closed=True):
    protect_configuration_id: "capo_pinpoint_sms_voice_v2.types.protect_configuration_id_or_arn.ProtectConfigurationIdOrArn"
    """<p>The unique identifier for the protect configuration.</p>"""
    filters: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.list_protect_configuration_rule_set_number_override_filter.ListProtectConfigurationRuleSetNumberOverrideFilter"
    ]
    """<p>An array of ProtectConfigurationRuleSetNumberOverrideFilterItem objects to filter the results.</p>"""
    next_token: NotRequired["capo_pinpoint_sms_voice_v2.types.next_token.NextToken"]
    """<p>The token to be used for the next set of paginated results. You don't need to supply a value for this field in the initial request.</p>"""
    max_results: NotRequired["capo_pinpoint_sms_voice_v2.types.max_results.MaxResults"]
    """<p>The maximum number of results to return per each request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: ListProtectConfigurationRuleSetNumberOverridesRequest,
) -> dict:
    out: dict = {}
    out["ProtectConfigurationId"] = value["protect_configuration_id"]
    if "filters" in value:
        import capo_pinpoint_sms_voice_v2.types.list_protect_configuration_rule_set_number_override_filter

        out["Filters"] = (
            capo_pinpoint_sms_voice_v2.types.list_protect_configuration_rule_set_number_override_filter.serialize_aws_json_1_0(
                value["filters"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> ListProtectConfigurationRuleSetNumberOverridesRequest:
    out: ListProtectConfigurationRuleSetNumberOverridesRequest = {}  # type: ignore[typeddict-item]
    if data.get("ProtectConfigurationId") is not None:
        out["protect_configuration_id"] = data["ProtectConfigurationId"]
    else:
        out["protect_configuration_id"] = ""
    if data.get("Filters") is not None:
        import capo_pinpoint_sms_voice_v2.types.list_protect_configuration_rule_set_number_override_filter

        out["filters"] = (
            capo_pinpoint_sms_voice_v2.types.list_protect_configuration_rule_set_number_override_filter.deserialize_aws_json_1_0(
                data["Filters"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
