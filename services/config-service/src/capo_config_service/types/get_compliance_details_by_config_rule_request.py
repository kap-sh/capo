"""Generated from Smithy shape ``com.amazonaws.configservice#GetComplianceDetailsByConfigRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.compliance_types
    import capo_config_service.types.limit
    import capo_config_service.types.next_token
    import capo_config_service.types.string_with_char_limit64


class GetComplianceDetailsByConfigRuleRequest(TypedDict, closed=True):
    config_rule_name: (
        "capo_config_service.types.string_with_char_limit64.StringWithCharLimit64"
    )
    """<p>The name of the Config rule for which you want compliance information.</p>"""
    compliance_types: NotRequired[
        "capo_config_service.types.compliance_types.ComplianceTypes"
    ]
    """<p>Filters the results by compliance.</p> <p> <code>INSUFFICIENT_DATA</code> is a valid <code>ComplianceType</code> that is returned when an Config rule cannot be evaluated. However, <code>INSUFFICIENT_DATA</code> cannot be used as a <code>ComplianceType</code> for filtering results.</p>"""
    limit: NotRequired["capo_config_service.types.limit.Limit"]
    """<p>The maximum number of evaluation results returned on each page. The default is 10. You cannot specify a number greater than 100. If you specify 0, Config uses the default.</p>"""
    next_token: NotRequired["capo_config_service.types.next_token.NextToken"]
    """<p>The <code>nextToken</code> string returned on a previous page that you use to get the next page of results in a paginated response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetComplianceDetailsByConfigRuleRequest) -> dict:
    out: dict = {}
    out["ConfigRuleName"] = value["config_rule_name"]
    if "compliance_types" in value:
        import capo_config_service.types.compliance_types

        out["ComplianceTypes"] = (
            capo_config_service.types.compliance_types.serialize_aws_json_1_1(
                value["compliance_types"]
            )
        )
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetComplianceDetailsByConfigRuleRequest:
    out: GetComplianceDetailsByConfigRuleRequest = {}  # type: ignore[typeddict-item]
    if data.get("ConfigRuleName") is not None:
        out["config_rule_name"] = data["ConfigRuleName"]
    else:
        out["config_rule_name"] = ""
    if data.get("ComplianceTypes") is not None:
        import capo_config_service.types.compliance_types

        out["compliance_types"] = (
            capo_config_service.types.compliance_types.deserialize_aws_json_1_1(
                data["ComplianceTypes"]
            )
        )
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
