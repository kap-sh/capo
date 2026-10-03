"""Generated from Smithy shape ``com.amazonaws.eventbridge#DescribeRuleResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridge.types.created_by
    import capo_eventbridge.types.event_bus_name
    import capo_eventbridge.types.event_pattern
    import capo_eventbridge.types.managed_by
    import capo_eventbridge.types.role_arn
    import capo_eventbridge.types.rule_arn
    import capo_eventbridge.types.rule_description
    import capo_eventbridge.types.rule_name
    import capo_eventbridge.types.rule_state
    import capo_eventbridge.types.schedule_expression


class DescribeRuleResponse(TypedDict, closed=True):
    name: NotRequired["capo_eventbridge.types.rule_name.RuleName"]
    """<p>The name of the rule.</p>"""
    arn: NotRequired["capo_eventbridge.types.rule_arn.RuleArn"]
    """<p>The Amazon Resource Name (ARN) of the rule.</p>"""
    event_pattern: NotRequired["capo_eventbridge.types.event_pattern.EventPattern"]
    """<p>The event pattern. For more information, see <a href="https://docs.aws.amazon.com/eventbridge/latest/userguide/eventbridge-and-event-patterns.html">Events and Event Patterns</a> in the <i> <i>Amazon EventBridge User Guide</i> </i>.</p>"""
    schedule_expression: NotRequired[
        "capo_eventbridge.types.schedule_expression.ScheduleExpression"
    ]
    """<p>The scheduling expression. For example, "cron(0 20 * * ? *)", "rate(5 minutes)".</p>"""
    state: NotRequired["capo_eventbridge.types.rule_state.RuleState"]
    """<p>Specifies whether the rule is enabled or disabled.</p>"""
    description: NotRequired["capo_eventbridge.types.rule_description.RuleDescription"]
    """<p>The description of the rule.</p>"""
    role_arn: NotRequired["capo_eventbridge.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the IAM role associated with the rule.</p>"""
    managed_by: NotRequired["capo_eventbridge.types.managed_by.ManagedBy"]
    """<p>If this is a managed rule, created by an Amazon Web Services service on your behalf, this field displays the principal name of the Amazon Web Services service that created the rule.</p>"""
    event_bus_name: NotRequired["capo_eventbridge.types.event_bus_name.EventBusName"]
    """<p>The name of the event bus associated with the rule.</p>"""
    created_by: NotRequired["capo_eventbridge.types.created_by.CreatedBy"]
    """<p>The account ID of the user that created the rule. If you use <code>PutRule</code> to put a rule on an event bus in another account, the other account is the owner of the rule, and the rule ARN includes the account ID for that account. However, the value for <code>CreatedBy</code> is the account ID as the account that created the rule in the other account.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeRuleResponse) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "event_pattern" in value:
        out["EventPattern"] = value["event_pattern"]
    if "schedule_expression" in value:
        out["ScheduleExpression"] = value["schedule_expression"]
    if "state" in value:
        import capo_eventbridge.types.rule_state

        out["State"] = capo_eventbridge.types.rule_state.serialize_aws_json_1_1(
            value["state"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "managed_by" in value:
        out["ManagedBy"] = value["managed_by"]
    if "event_bus_name" in value:
        out["EventBusName"] = value["event_bus_name"]
    if "created_by" in value:
        out["CreatedBy"] = value["created_by"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeRuleResponse:
    out: DescribeRuleResponse = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("EventPattern") is not None:
        out["event_pattern"] = data["EventPattern"]
    if data.get("ScheduleExpression") is not None:
        out["schedule_expression"] = data["ScheduleExpression"]
    if data.get("State") is not None:
        import capo_eventbridge.types.rule_state

        out["state"] = capo_eventbridge.types.rule_state.deserialize_aws_json_1_1(
            data["State"]
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    if data.get("ManagedBy") is not None:
        out["managed_by"] = data["ManagedBy"]
    if data.get("EventBusName") is not None:
        out["event_bus_name"] = data["EventBusName"]
    if data.get("CreatedBy") is not None:
        out["created_by"] = data["CreatedBy"]
    return out
