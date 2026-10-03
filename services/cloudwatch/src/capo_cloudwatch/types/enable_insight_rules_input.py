"""Generated from Smithy shape ``com.amazonaws.cloudwatch#EnableInsightRulesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.insight_rule_names


class EnableInsightRulesInput(TypedDict, closed=True):
    rule_names: NotRequired["capo_cloudwatch.types.insight_rule_names.InsightRuleNames"]
    """<p>An array of the rule names to enable. If you need to find out the names of your rules, use <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DescribeInsightRules.html">DescribeInsightRules</a>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EnableInsightRulesInput) -> dict:
    out: dict = {}
    if "rule_names" in value:
        import capo_cloudwatch.types.insight_rule_names

        out["RuleNames"] = (
            capo_cloudwatch.types.insight_rule_names.serialize_aws_json_1_0(
                value["rule_names"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> EnableInsightRulesInput:
    out: EnableInsightRulesInput = {}  # type: ignore[typeddict-item]
    if data.get("RuleNames") is not None:
        import capo_cloudwatch.types.insight_rule_names

        out["rule_names"] = (
            capo_cloudwatch.types.insight_rule_names.deserialize_aws_json_1_0(
                data["RuleNames"]
            )
        )
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: EnableInsightRulesInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "rule_names" in value:
        import capo_cloudwatch.types.insight_rule_names

        capo_cloudwatch.types.insight_rule_names.serialize_query(
            value["rule_names"], pairs, f"{key_prefix}RuleNames"
        )


def deserialize_query(el: Element) -> EnableInsightRulesInput:
    out: EnableInsightRulesInput = {}  # type: ignore[typeddict-item]
    child_rule_names = el.find("RuleNames")
    if child_rule_names is not None:
        import capo_cloudwatch.types.insight_rule_names

        out["rule_names"] = capo_cloudwatch.types.insight_rule_names.deserialize_query(
            child_rule_names
        )
    return out
