"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#DeleteAutomationRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer_automation.types.client_token
    import capo_compute_optimizer_automation.types.rule_arn


class DeleteAutomationRuleRequest(TypedDict, closed=True):
    rule_arn: "capo_compute_optimizer_automation.types.rule_arn.RuleArn"
    """<p> The ARN of the rule to delete. </p>"""
    rule_revision: "int"
    """<p> The revision number of the rule to delete. </p>"""
    client_token: NotRequired[
        "capo_compute_optimizer_automation.types.client_token.ClientToken"
    ]
    """<p> A unique identifier to ensure idempotency of the request. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteAutomationRuleRequest) -> dict:
    out: dict = {}
    out["ruleArn"] = value["rule_arn"]
    out["ruleRevision"] = value["rule_revision"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteAutomationRuleRequest:
    out: DeleteAutomationRuleRequest = {}  # type: ignore[typeddict-item]
    if data.get("ruleArn") is not None:
        out["rule_arn"] = data["ruleArn"]
    else:
        out["rule_arn"] = ""
    if data.get("ruleRevision") is not None:
        out["rule_revision"] = data["ruleRevision"]
    else:
        out["rule_revision"] = 0
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
