"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#ListTargetsByRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_events.types.event_bus_name_or_arn
    import capo_cloudwatch_events.types.limit_max100
    import capo_cloudwatch_events.types.next_token
    import capo_cloudwatch_events.types.rule_name


class ListTargetsByRuleRequest(TypedDict, closed=True):
    rule: "capo_cloudwatch_events.types.rule_name.RuleName"
    """<p>The name of the rule.</p>"""
    event_bus_name: NotRequired[
        "capo_cloudwatch_events.types.event_bus_name_or_arn.EventBusNameOrArn"
    ]
    """<p>The name or ARN of the event bus associated with the rule. If you omit this, the default event bus is used.</p>"""
    next_token: NotRequired["capo_cloudwatch_events.types.next_token.NextToken"]
    """<p>The token returned by a previous call to retrieve the next set of results.</p>"""
    limit: NotRequired["capo_cloudwatch_events.types.limit_max100.LimitMax100"]
    """<p>The maximum number of results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTargetsByRuleRequest) -> dict:
    out: dict = {}
    out["Rule"] = value["rule"]
    if "event_bus_name" in value:
        out["EventBusName"] = value["event_bus_name"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "limit" in value:
        out["Limit"] = value["limit"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTargetsByRuleRequest:
    out: ListTargetsByRuleRequest = {}  # type: ignore[typeddict-item]
    if data.get("Rule") is not None:
        out["rule"] = data["Rule"]
    else:
        out["rule"] = ""
    if data.get("EventBusName") is not None:
        out["event_bus_name"] = data["EventBusName"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    return out
