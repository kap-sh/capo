"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#ListAutomationRulesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer_automation.types.automation_rules
    import capo_compute_optimizer_automation.types.next_token


class ListAutomationRulesResponse(TypedDict, closed=True):
    automation_rules: NotRequired[
        "capo_compute_optimizer_automation.types.automation_rules.AutomationRules"
    ]
    """<p> The list of automation rules that match the specified criteria. </p>"""
    next_token: NotRequired[
        "capo_compute_optimizer_automation.types.next_token.NextToken"
    ]
    """<p>A token used for pagination. If present, indicates there are more results available and can be used in subsequent requests.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListAutomationRulesResponse) -> dict:
    out: dict = {}
    if "automation_rules" in value:
        import capo_compute_optimizer_automation.types.automation_rules

        out["automationRules"] = (
            capo_compute_optimizer_automation.types.automation_rules.serialize_aws_json_1_0(
                value["automation_rules"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListAutomationRulesResponse:
    out: ListAutomationRulesResponse = {}  # type: ignore[typeddict-item]
    if data.get("automationRules") is not None:
        import capo_compute_optimizer_automation.types.automation_rules

        out["automation_rules"] = (
            capo_compute_optimizer_automation.types.automation_rules.deserialize_aws_json_1_0(
                data["automationRules"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListAutomationRulesResponse) -> dict:
    out: dict = {}
    if "automation_rules" in value:
        import capo_compute_optimizer_automation.types.automation_rules

        out["automationRules"] = (
            capo_compute_optimizer_automation.types.automation_rules.serialize_cbor(
                value["automation_rules"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListAutomationRulesResponse:
    out: ListAutomationRulesResponse = {}  # type: ignore[typeddict-item]
    if data.get("automationRules") is not None:
        import capo_compute_optimizer_automation.types.automation_rules

        out["automation_rules"] = (
            capo_compute_optimizer_automation.types.automation_rules.deserialize_cbor(
                data["automationRules"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
