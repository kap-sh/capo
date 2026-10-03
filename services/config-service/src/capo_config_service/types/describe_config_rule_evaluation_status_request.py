"""Generated from Smithy shape ``com.amazonaws.configservice#DescribeConfigRuleEvaluationStatusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.config_rule_names
    import capo_config_service.types.rule_limit
    import capo_config_service.types.string


class DescribeConfigRuleEvaluationStatusRequest(TypedDict, closed=True):
    config_rule_names: NotRequired[
        "capo_config_service.types.config_rule_names.ConfigRuleNames"
    ]
    """<p>The name of the Config managed rules for which you want status information. If you do not specify any names, Config returns status information for all Config managed rules that you use.</p>"""
    next_token: NotRequired["capo_config_service.types.string.String"]
    """<p>The <code>nextToken</code> string returned on a previous page that you use to get the next page of results in a paginated response.</p>"""
    limit: "capo_config_service.types.rule_limit.RuleLimit"
    """<p>The number of rule evaluation results that you want returned.</p> <p>This parameter is required if the rule limit for your account is more than the default of 1000 rules.</p> <p>For information about requesting a rule limit increase, see <a href="http://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html#limits_config">Config Limits</a> in the <i>Amazon Web Services General Reference Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeConfigRuleEvaluationStatusRequest) -> dict:
    out: dict = {}
    if "config_rule_names" in value:
        import capo_config_service.types.config_rule_names

        out["ConfigRuleNames"] = (
            capo_config_service.types.config_rule_names.serialize_aws_json_1_1(
                value["config_rule_names"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    out["Limit"] = value.get("limit", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeConfigRuleEvaluationStatusRequest:
    out: DescribeConfigRuleEvaluationStatusRequest = {}  # type: ignore[typeddict-item]
    if data.get("ConfigRuleNames") is not None:
        import capo_config_service.types.config_rule_names

        out["config_rule_names"] = (
            capo_config_service.types.config_rule_names.deserialize_aws_json_1_1(
                data["ConfigRuleNames"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    else:
        out["limit"] = 0
    return out
