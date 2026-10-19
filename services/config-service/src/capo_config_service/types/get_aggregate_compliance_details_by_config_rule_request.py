"""Generated from Smithy shape ``com.amazonaws.configservice#GetAggregateComplianceDetailsByConfigRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.account_id
    import capo_config_service.types.aws_region
    import capo_config_service.types.compliance_type
    import capo_config_service.types.config_rule_name
    import capo_config_service.types.configuration_aggregator_name
    import capo_config_service.types.limit
    import capo_config_service.types.next_token


class GetAggregateComplianceDetailsByConfigRuleRequest(TypedDict, closed=True):
    configuration_aggregator_name: "capo_config_service.types.configuration_aggregator_name.ConfigurationAggregatorName"
    """<p>The name of the configuration aggregator.</p>"""
    config_rule_name: "capo_config_service.types.config_rule_name.ConfigRuleName"
    """<p>The name of the Config rule for which you want compliance information.</p>"""
    account_id: "capo_config_service.types.account_id.AccountId"
    """<p>The 12-digit account ID of the source account.</p>"""
    aws_region: "capo_config_service.types.aws_region.AwsRegion"
    """<p>The source region from where the data is aggregated.</p>"""
    compliance_type: NotRequired[
        "capo_config_service.types.compliance_type.ComplianceType"
    ]
    """<p>The resource compliance status.</p> <note> <p>For the <code>GetAggregateComplianceDetailsByConfigRuleRequest</code> data type, Config supports only the <code>COMPLIANT</code> and <code>NON_COMPLIANT</code>. Config does not support the <code>NOT_APPLICABLE</code> and <code>INSUFFICIENT_DATA</code> values.</p> </note>"""
    limit: NotRequired["capo_config_service.types.limit.Limit"]
    """<p>The maximum number of evaluation results returned on each page. The default is 50. You cannot specify a number greater than 100. If you specify 0, Config uses the default.</p>"""
    next_token: NotRequired["capo_config_service.types.next_token.NextToken"]
    """<p>The <code>nextToken</code> string returned on a previous page that you use to get the next page of results in a paginated response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: GetAggregateComplianceDetailsByConfigRuleRequest,
) -> dict:
    out: dict = {}
    out["ConfigurationAggregatorName"] = value["configuration_aggregator_name"]
    out["ConfigRuleName"] = value["config_rule_name"]
    out["AccountId"] = value["account_id"]
    out["AwsRegion"] = value["aws_region"]
    if "compliance_type" in value:
        import capo_config_service.types.compliance_type

        out["ComplianceType"] = (
            capo_config_service.types.compliance_type.serialize_aws_json_1_1(
                value["compliance_type"]
            )
        )
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> GetAggregateComplianceDetailsByConfigRuleRequest:
    out: GetAggregateComplianceDetailsByConfigRuleRequest = {}  # type: ignore[typeddict-item]
    if data.get("ConfigurationAggregatorName") is not None:
        out["configuration_aggregator_name"] = data["ConfigurationAggregatorName"]
    else:
        out["configuration_aggregator_name"] = ""
    if data.get("ConfigRuleName") is not None:
        out["config_rule_name"] = data["ConfigRuleName"]
    else:
        out["config_rule_name"] = ""
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    else:
        out["account_id"] = ""
    if data.get("AwsRegion") is not None:
        out["aws_region"] = data["AwsRegion"]
    else:
        out["aws_region"] = ""
    if data.get("ComplianceType") is not None:
        import capo_config_service.types.compliance_type

        out["compliance_type"] = (
            capo_config_service.types.compliance_type.deserialize_aws_json_1_1(
                data["ComplianceType"]
            )
        )
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
