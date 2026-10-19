"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#PutTargetsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_events.types.event_bus_name_or_arn
    import capo_cloudwatch_events.types.rule_name
    import capo_cloudwatch_events.types.target_list


class PutTargetsRequest(TypedDict, closed=True):
    rule: "capo_cloudwatch_events.types.rule_name.RuleName"
    """<p>The name of the rule.</p>"""
    event_bus_name: NotRequired[
        "capo_cloudwatch_events.types.event_bus_name_or_arn.EventBusNameOrArn"
    ]
    """<p>The name or ARN of the event bus associated with the rule. If you omit this, the default event bus is used.</p>"""
    targets: "capo_cloudwatch_events.types.target_list.TargetList"
    """<p>The targets to update or add to the rule.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutTargetsRequest) -> dict:
    out: dict = {}
    out["Rule"] = value["rule"]
    if "event_bus_name" in value:
        out["EventBusName"] = value["event_bus_name"]
    import capo_cloudwatch_events.types.target_list

    out["Targets"] = capo_cloudwatch_events.types.target_list.serialize_aws_json_1_1(
        value["targets"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutTargetsRequest:
    out: PutTargetsRequest = {}  # type: ignore[typeddict-item]
    if data.get("Rule") is not None:
        out["rule"] = data["Rule"]
    else:
        out["rule"] = ""
    if data.get("EventBusName") is not None:
        out["event_bus_name"] = data["EventBusName"]
    if data.get("Targets") is not None:
        import capo_cloudwatch_events.types.target_list

        out["targets"] = (
            capo_cloudwatch_events.types.target_list.deserialize_aws_json_1_1(
                data["Targets"]
            )
        )
    else:
        out["targets"] = []
    return out
