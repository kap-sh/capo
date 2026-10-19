"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#DeleteRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch_events.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudwatch_events.types.boolean
    import capo_cloudwatch_events.types.event_bus_name_or_arn
    import capo_cloudwatch_events.types.rule_name


class DeleteRuleRequest(TypedDict, closed=True):
    name: "capo_cloudwatch_events.types.rule_name.RuleName"
    """<p>The name of the rule.</p>"""
    event_bus_name: NotRequired[
        "capo_cloudwatch_events.types.event_bus_name_or_arn.EventBusNameOrArn"
    ]
    """<p>The name or ARN of the event bus associated with the rule. If you omit this, the default event bus is used.</p>"""
    force: NotRequired["capo_cloudwatch_events.types.boolean.Boolean"]
    """<p>If this is a managed rule, created by an Amazon Web Services service on your behalf, you must specify <code>Force</code> as <code>True</code> to delete the rule. This parameter is ignored for rules that are not managed rules. You can check whether a rule is a managed rule by using <code>DescribeRule</code> or <code>ListRules</code> and checking the <code>ManagedBy</code> field of the response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteRuleRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "event_bus_name" in value:
        out["EventBusName"] = value["event_bus_name"]
    if "force" in value:
        out["Force"] = value["force"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteRuleRequest:
    out: DeleteRuleRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("DeleteRuleRequest.name required")
    if data.get("EventBusName") is not None:
        out["event_bus_name"] = data["EventBusName"]
    if data.get("Force") is not None:
        out["force"] = data["Force"]
    return out
