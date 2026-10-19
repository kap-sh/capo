"""Generated from Smithy shape ``com.amazonaws.configservice#GetAggregateConfigRuleComplianceSummaryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.config_rule_compliance_summary_filters
    import capo_config_service.types.config_rule_compliance_summary_group_key
    import capo_config_service.types.configuration_aggregator_name
    import capo_config_service.types.group_by_api_limit
    import capo_config_service.types.next_token


class GetAggregateConfigRuleComplianceSummaryRequest(TypedDict, closed=True):
    configuration_aggregator_name: "capo_config_service.types.configuration_aggregator_name.ConfigurationAggregatorName"
    """<p>The name of the configuration aggregator.</p>"""
    filters: NotRequired[
        "capo_config_service.types.config_rule_compliance_summary_filters.ConfigRuleComplianceSummaryFilters"
    ]
    """<p>Filters the results based on the ConfigRuleComplianceSummaryFilters object.</p>"""
    group_by_key: NotRequired[
        "capo_config_service.types.config_rule_compliance_summary_group_key.ConfigRuleComplianceSummaryGroupKey"
    ]
    """<p>Groups the result based on ACCOUNT_ID or AWS_REGION.</p>"""
    limit: NotRequired["capo_config_service.types.group_by_api_limit.GroupByAPILimit"]
    """<p>The maximum number of evaluation results returned on each page. The default is 1000. You cannot specify a number greater than 1000. If you specify 0, Config uses the default.</p>"""
    next_token: NotRequired["capo_config_service.types.next_token.NextToken"]
    """<p>The <code>nextToken</code> string returned on a previous page that you use to get the next page of results in a paginated response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: GetAggregateConfigRuleComplianceSummaryRequest,
) -> dict:
    out: dict = {}
    out["ConfigurationAggregatorName"] = value["configuration_aggregator_name"]
    if "filters" in value:
        import capo_config_service.types.config_rule_compliance_summary_filters

        out["Filters"] = (
            capo_config_service.types.config_rule_compliance_summary_filters.serialize_aws_json_1_1(
                value["filters"]
            )
        )
    if "group_by_key" in value:
        import capo_config_service.types.config_rule_compliance_summary_group_key

        out["GroupByKey"] = (
            capo_config_service.types.config_rule_compliance_summary_group_key.serialize_aws_json_1_1(
                value["group_by_key"]
            )
        )
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> GetAggregateConfigRuleComplianceSummaryRequest:
    out: GetAggregateConfigRuleComplianceSummaryRequest = {}  # type: ignore[typeddict-item]
    if data.get("ConfigurationAggregatorName") is not None:
        out["configuration_aggregator_name"] = data["ConfigurationAggregatorName"]
    else:
        out["configuration_aggregator_name"] = ""
    if data.get("Filters") is not None:
        import capo_config_service.types.config_rule_compliance_summary_filters

        out["filters"] = (
            capo_config_service.types.config_rule_compliance_summary_filters.deserialize_aws_json_1_1(
                data["Filters"]
            )
        )
    if data.get("GroupByKey") is not None:
        import capo_config_service.types.config_rule_compliance_summary_group_key

        out["group_by_key"] = (
            capo_config_service.types.config_rule_compliance_summary_group_key.deserialize_aws_json_1_1(
                data["GroupByKey"]
            )
        )
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
