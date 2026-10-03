"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#PutRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch_events.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudwatch_events.types.event_bus_name_or_arn
    import capo_cloudwatch_events.types.event_pattern
    import capo_cloudwatch_events.types.role_arn
    import capo_cloudwatch_events.types.rule_description
    import capo_cloudwatch_events.types.rule_name
    import capo_cloudwatch_events.types.rule_state
    import capo_cloudwatch_events.types.schedule_expression
    import capo_cloudwatch_events.types.tag_list


class PutRuleRequest(TypedDict, closed=True):
    name: "capo_cloudwatch_events.types.rule_name.RuleName"
    """<p>The name of the rule that you are creating or updating.</p>"""
    schedule_expression: NotRequired[
        "capo_cloudwatch_events.types.schedule_expression.ScheduleExpression"
    ]
    """<p>The scheduling expression. For example, "cron(0 20 * * ? *)" or "rate(5 minutes)".</p>"""
    event_pattern: NotRequired[
        "capo_cloudwatch_events.types.event_pattern.EventPattern"
    ]
    """<p>The event pattern. For more information, see <a href="https://docs.aws.amazon.com/eventbridge/latest/userguide/eventbridge-and-event-patterns.html">Events and Event Patterns</a> in the <i>Amazon EventBridge User Guide</i>.</p>"""
    state: NotRequired["capo_cloudwatch_events.types.rule_state.RuleState"]
    """<p>Indicates whether the rule is enabled or disabled.</p>"""
    description: NotRequired[
        "capo_cloudwatch_events.types.rule_description.RuleDescription"
    ]
    """<p>A description of the rule.</p>"""
    role_arn: NotRequired["capo_cloudwatch_events.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the IAM role associated with the rule.</p> <p>If you're setting an event bus in another account as the target and that account granted permission to your account through an organization instead of directly by the account ID, you must specify a <code>RoleArn</code> with proper permissions in the <code>Target</code> structure, instead of here in this parameter.</p>"""
    tags: NotRequired["capo_cloudwatch_events.types.tag_list.TagList"]
    """<p>The list of key-value pairs to associate with the rule.</p>"""
    event_bus_name: NotRequired[
        "capo_cloudwatch_events.types.event_bus_name_or_arn.EventBusNameOrArn"
    ]
    """<p>The name or ARN of the event bus to associate with this rule. If you omit this, the default event bus is used.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutRuleRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "schedule_expression" in value:
        out["ScheduleExpression"] = value["schedule_expression"]
    if "event_pattern" in value:
        out["EventPattern"] = value["event_pattern"]
    if "state" in value:
        import capo_cloudwatch_events.types.rule_state

        out["State"] = capo_cloudwatch_events.types.rule_state.serialize_aws_json_1_1(
            value["state"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "tags" in value:
        import capo_cloudwatch_events.types.tag_list

        out["Tags"] = capo_cloudwatch_events.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "event_bus_name" in value:
        out["EventBusName"] = value["event_bus_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutRuleRequest:
    out: PutRuleRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("PutRuleRequest.name required")
    if data.get("ScheduleExpression") is not None:
        out["schedule_expression"] = data["ScheduleExpression"]
    if data.get("EventPattern") is not None:
        out["event_pattern"] = data["EventPattern"]
    if data.get("State") is not None:
        import capo_cloudwatch_events.types.rule_state

        out["state"] = capo_cloudwatch_events.types.rule_state.deserialize_aws_json_1_1(
            data["State"]
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    if data.get("Tags") is not None:
        import capo_cloudwatch_events.types.tag_list

        out["tags"] = capo_cloudwatch_events.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if data.get("EventBusName") is not None:
        out["event_bus_name"] = data["EventBusName"]
    return out
