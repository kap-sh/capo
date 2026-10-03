"""Generated from Smithy shape ``com.amazonaws.cloudwatch#InsightRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.insight_rule_definition
    import capo_cloudwatch.types.insight_rule_is_managed
    import capo_cloudwatch.types.insight_rule_name
    import capo_cloudwatch.types.insight_rule_on_transformed_logs
    import capo_cloudwatch.types.insight_rule_schema
    import capo_cloudwatch.types.insight_rule_state


class InsightRule(TypedDict, closed=True):
    name: NotRequired["capo_cloudwatch.types.insight_rule_name.InsightRuleName"]
    """<p>The name of the rule.</p>"""
    state: NotRequired["capo_cloudwatch.types.insight_rule_state.InsightRuleState"]
    """<p>Indicates whether the rule is enabled or disabled.</p>"""
    schema: NotRequired["capo_cloudwatch.types.insight_rule_schema.InsightRuleSchema"]
    """<p>For rules that you create, this is always <code>{"Name": "CloudWatchLogRule", "Version": 1}</code>. For managed rules, this is <code>{"Name": "ServiceLogRule", "Version": 1}</code> </p>"""
    definition: NotRequired[
        "capo_cloudwatch.types.insight_rule_definition.InsightRuleDefinition"
    ]
    """<p>The definition of the rule, as a JSON object. The definition contains the keywords used to define contributors, the value to aggregate on if this rule returns a sum instead of a count, and the filters. For details on the valid syntax, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContributorInsights-RuleSyntax.html">Contributor Insights Rule Syntax</a>.</p>"""
    managed_rule: NotRequired[
        "capo_cloudwatch.types.insight_rule_is_managed.InsightRuleIsManaged"
    ]
    """<p> An optional built-in rule that Amazon Web Services manages. </p>"""
    apply_on_transformed_logs: NotRequired[
        "capo_cloudwatch.types.insight_rule_on_transformed_logs.InsightRuleOnTransformedLogs"
    ]
    """<p>Displays whether the rule is evaluated on the transformed versions of logs, for log groups that have <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html">Log transformation</a> enabled. If this is <code>false</code>, log events are evaluated before they are transformed.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InsightRule) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "state" in value:
        out["State"] = value["state"]
    if "schema" in value:
        out["Schema"] = value["schema"]
    if "definition" in value:
        out["Definition"] = value["definition"]
    if "managed_rule" in value:
        out["ManagedRule"] = value["managed_rule"]
    if "apply_on_transformed_logs" in value:
        out["ApplyOnTransformedLogs"] = value["apply_on_transformed_logs"]
    return out


def deserialize_aws_json_1_0(data: dict) -> InsightRule:
    out: InsightRule = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("State") is not None:
        out["state"] = data["State"]
    if data.get("Schema") is not None:
        out["schema"] = data["Schema"]
    if data.get("Definition") is not None:
        out["definition"] = data["Definition"]
    if data.get("ManagedRule") is not None:
        out["managed_rule"] = data["ManagedRule"]
    if data.get("ApplyOnTransformedLogs") is not None:
        out["apply_on_transformed_logs"] = data["ApplyOnTransformedLogs"]
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: InsightRule, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "name" in value:
        pairs.append((f"{key_prefix}Name", str(value["name"])))
    if "state" in value:
        pairs.append((f"{key_prefix}State", str(value["state"])))
    if "schema" in value:
        pairs.append((f"{key_prefix}Schema", str(value["schema"])))
    if "definition" in value:
        pairs.append((f"{key_prefix}Definition", str(value["definition"])))
    if "managed_rule" in value:
        pairs.append(
            (f"{key_prefix}ManagedRule", "true" if value["managed_rule"] else "false")
        )
    if "apply_on_transformed_logs" in value:
        pairs.append(
            (
                f"{key_prefix}ApplyOnTransformedLogs",
                "true" if value["apply_on_transformed_logs"] else "false",
            )
        )


def deserialize_query(el: Element) -> InsightRule:
    out: InsightRule = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    child_state = el.find("State")
    if child_state is not None:
        out["state"] = str(child_state.text or "")
    child_schema = el.find("Schema")
    if child_schema is not None:
        out["schema"] = str(child_schema.text or "")
    child_definition = el.find("Definition")
    if child_definition is not None:
        out["definition"] = str(child_definition.text or "")
    child_managed_rule = el.find("ManagedRule")
    if child_managed_rule is not None:
        out["managed_rule"] = (child_managed_rule.text or "").lower() == "true"
    child_apply_on_transformed_logs = el.find("ApplyOnTransformedLogs")
    if child_apply_on_transformed_logs is not None:
        out["apply_on_transformed_logs"] = (
            child_apply_on_transformed_logs.text or ""
        ).lower() == "true"
    return out
