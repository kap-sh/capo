"""Generated from Smithy shape ``com.amazonaws.configservice#DescribeConfigRulesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.config_rule_names
    import capo_config_service.types.describe_config_rules_filters
    import capo_config_service.types.string


class DescribeConfigRulesRequest(TypedDict, closed=True):
    config_rule_names: NotRequired[
        "capo_config_service.types.config_rule_names.ConfigRuleNames"
    ]
    """<p>The names of the Config rules for which you want details. If you do not specify any names, Config returns details for all your rules.</p>"""
    filters: NotRequired[
        "capo_config_service.types.describe_config_rules_filters.DescribeConfigRulesFilters"
    ]
    """<p>Returns a list of Detective or Proactive Config rules. By default, this API returns an unfiltered list. For more information on Detective or Proactive Config rules, see <a href="https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config-rules.html"> <b>Evaluation Mode</b> </a> in the <i>Config Developer Guide</i>.</p>"""
    next_token: NotRequired["capo_config_service.types.string.String"]
    """<p>The <code>nextToken</code> string returned on a previous page that you use to get the next page of results in a paginated response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeConfigRulesRequest) -> dict:
    out: dict = {}
    if "config_rule_names" in value:
        import capo_config_service.types.config_rule_names

        out["ConfigRuleNames"] = (
            capo_config_service.types.config_rule_names.serialize_aws_json_1_1(
                value["config_rule_names"]
            )
        )
    if "filters" in value:
        import capo_config_service.types.describe_config_rules_filters

        out["Filters"] = (
            capo_config_service.types.describe_config_rules_filters.serialize_aws_json_1_1(
                value["filters"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeConfigRulesRequest:
    out: DescribeConfigRulesRequest = {}  # type: ignore[typeddict-item]
    if data.get("ConfigRuleNames") is not None:
        import capo_config_service.types.config_rule_names

        out["config_rule_names"] = (
            capo_config_service.types.config_rule_names.deserialize_aws_json_1_1(
                data["ConfigRuleNames"]
            )
        )
    if data.get("Filters") is not None:
        import capo_config_service.types.describe_config_rules_filters

        out["filters"] = (
            capo_config_service.types.describe_config_rules_filters.deserialize_aws_json_1_1(
                data["Filters"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
