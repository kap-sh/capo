"""Generated from Smithy shape ``com.amazonaws.eventbridge#DisableRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridge.types.event_bus_name_or_arn
    import capo_eventbridge.types.rule_name


class DisableRuleRequest(TypedDict, closed=True):
    name: "capo_eventbridge.types.rule_name.RuleName"
    """<p>The name of the rule.</p>"""
    event_bus_name: NotRequired[
        "capo_eventbridge.types.event_bus_name_or_arn.EventBusNameOrArn"
    ]
    """<p>The name or ARN of the event bus associated with the rule. If you omit this, the default event bus is used.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisableRuleRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "event_bus_name" in value:
        out["EventBusName"] = value["event_bus_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DisableRuleRequest:
    out: DisableRuleRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("EventBusName") is not None:
        out["event_bus_name"] = data["EventBusName"]
    return out
