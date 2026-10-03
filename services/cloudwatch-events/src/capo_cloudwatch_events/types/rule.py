"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#Rule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_events.types.event_bus_name
    import capo_cloudwatch_events.types.event_pattern
    import capo_cloudwatch_events.types.managed_by
    import capo_cloudwatch_events.types.role_arn
    import capo_cloudwatch_events.types.rule_arn
    import capo_cloudwatch_events.types.rule_description
    import capo_cloudwatch_events.types.rule_name
    import capo_cloudwatch_events.types.rule_state
    import capo_cloudwatch_events.types.schedule_expression


class Rule(TypedDict, closed=True):
    name: NotRequired["capo_cloudwatch_events.types.rule_name.RuleName"]
    """<p>The name of the rule.</p>"""
    arn: NotRequired["capo_cloudwatch_events.types.rule_arn.RuleArn"]
    """<p>The Amazon Resource Name (ARN) of the rule.</p>"""
    event_pattern: NotRequired[
        "capo_cloudwatch_events.types.event_pattern.EventPattern"
    ]
    """<p>The event pattern of the rule. For more information, see <a href="https://docs.aws.amazon.com/eventbridge/latest/userguide/eventbridge-and-event-patterns.html">Events and Event Patterns</a> in the <i>Amazon EventBridge User Guide</i>.</p>"""
    state: NotRequired["capo_cloudwatch_events.types.rule_state.RuleState"]
    """<p>The state of the rule.</p>"""
    description: NotRequired[
        "capo_cloudwatch_events.types.rule_description.RuleDescription"
    ]
    """<p>The description of the rule.</p>"""
    schedule_expression: NotRequired[
        "capo_cloudwatch_events.types.schedule_expression.ScheduleExpression"
    ]
    """<p>The scheduling expression. For example, "cron(0 20 * * ? *)", "rate(5 minutes)". For more information, see <a href="https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-create-rule-schedule.html">Creating an Amazon EventBridge rule that runs on a schedule</a>.</p>"""
    role_arn: NotRequired["capo_cloudwatch_events.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the role that is used for target invocation.</p> <p>If you're setting an event bus in another account as the target and that account granted permission to your account through an organization instead of directly by the account ID, you must specify a <code>RoleArn</code> with proper permissions in the <code>Target</code> structure, instead of here in this parameter.</p>"""
    managed_by: NotRequired["capo_cloudwatch_events.types.managed_by.ManagedBy"]
    """<p>If the rule was created on behalf of your account by an Amazon Web Services service, this field displays the principal name of the service that created the rule.</p>"""
    event_bus_name: NotRequired[
        "capo_cloudwatch_events.types.event_bus_name.EventBusName"
    ]
    """<p>The name or ARN of the event bus associated with the rule. If you omit this, the default event bus is used.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Rule) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "event_pattern" in value:
        out["EventPattern"] = value["event_pattern"]
    if "state" in value:
        import capo_cloudwatch_events.types.rule_state

        out["State"] = capo_cloudwatch_events.types.rule_state.serialize_aws_json_1_1(
            value["state"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "schedule_expression" in value:
        out["ScheduleExpression"] = value["schedule_expression"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "managed_by" in value:
        out["ManagedBy"] = value["managed_by"]
    if "event_bus_name" in value:
        out["EventBusName"] = value["event_bus_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Rule:
    out: Rule = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("EventPattern") is not None:
        out["event_pattern"] = data["EventPattern"]
    if data.get("State") is not None:
        import capo_cloudwatch_events.types.rule_state

        out["state"] = capo_cloudwatch_events.types.rule_state.deserialize_aws_json_1_1(
            data["State"]
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("ScheduleExpression") is not None:
        out["schedule_expression"] = data["ScheduleExpression"]
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    if data.get("ManagedBy") is not None:
        out["managed_by"] = data["ManagedBy"]
    if data.get("EventBusName") is not None:
        out["event_bus_name"] = data["EventBusName"]
    return out
