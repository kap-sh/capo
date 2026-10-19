"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#GetAutomationRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer_automation.types.rule_arn


class GetAutomationRuleRequest(TypedDict, closed=True):
    rule_arn: "capo_compute_optimizer_automation.types.rule_arn.RuleArn"
    """<p> The ARN of the rule to retrieve. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetAutomationRuleRequest) -> dict:
    out: dict = {}
    out["ruleArn"] = value["rule_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetAutomationRuleRequest:
    out: GetAutomationRuleRequest = {}  # type: ignore[typeddict-item]
    if data.get("ruleArn") is not None:
        out["rule_arn"] = data["ruleArn"]
    else:
        out["rule_arn"] = ""
    return out
