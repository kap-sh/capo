"""Generated from Smithy shape ``com.amazonaws.eventbridge#PutRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_eventbridge.errors import DeserializationError

if TYPE_CHECKING:
    import capo_eventbridge.types.event_bus_name_or_arn
    import capo_eventbridge.types.event_pattern
    import capo_eventbridge.types.role_arn
    import capo_eventbridge.types.rule_description
    import capo_eventbridge.types.rule_name
    import capo_eventbridge.types.rule_state
    import capo_eventbridge.types.schedule_expression
    import capo_eventbridge.types.tag_list


class PutRuleRequest(TypedDict, closed=True):
    name: "capo_eventbridge.types.rule_name.RuleName"
    """<p>The name of the rule that you are creating or updating.</p>"""
    schedule_expression: NotRequired[
        "capo_eventbridge.types.schedule_expression.ScheduleExpression"
    ]
    """<p>The scheduling expression. For example, "cron(0 20 * * ? *)" or "rate(5 minutes)".</p>"""
    event_pattern: NotRequired["capo_eventbridge.types.event_pattern.EventPattern"]
    """<p>The event pattern. For more information, see <a href="https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html">Amazon EventBridge event patterns</a> in the <i> <i>Amazon EventBridge User Guide</i> </i>.</p>"""
    state: NotRequired["capo_eventbridge.types.rule_state.RuleState"]
    """<p>The state of the rule.</p> <p>Valid values include:</p> <ul> <li> <p> <code>DISABLED</code>: The rule is disabled. EventBridge does not match any events against the rule.</p> </li> <li> <p> <code>ENABLED</code>: The rule is enabled. EventBridge matches events against the rule, <i>except</i> for Amazon Web Services management events delivered through CloudTrail.</p> </li> <li> <p> <code>ENABLED_WITH_ALL_CLOUDTRAIL_MANAGEMENT_EVENTS</code>: The rule is enabled for all events, including Amazon Web Services management events delivered through CloudTrail.</p> <p>Management events provide visibility into management operations that are performed on resources in your Amazon Web Services account. These are also known as control plane operations. For more information, see <a href="https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.html#logging-management-events">Logging management events</a> in the <i>CloudTrail User Guide</i>, and <a href="https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event.html#eb-service-event-cloudtrail">Filtering management events from Amazon Web Services services</a> in the <i> <i>Amazon EventBridge User Guide</i> </i>.</p> <p>This value is only valid for rules on the <a href="https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is-how-it-works-concepts.html#eb-bus-concepts-buses">default</a> event bus or <a href="https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-create-event-bus.html">custom event buses</a>. It does not apply to <a href="https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-saas.html">partner event buses</a>.</p> </li> </ul>"""
    description: NotRequired["capo_eventbridge.types.rule_description.RuleDescription"]
    """<p>A description of the rule.</p>"""
    role_arn: NotRequired["capo_eventbridge.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the IAM role associated with the rule.</p> <p>If you're setting an event bus in another account as the target and that account granted permission to your account through an organization instead of directly by the account ID, you must specify a <code>RoleArn</code> with proper permissions in the <code>Target</code> structure, instead of here in this parameter.</p>"""
    tags: NotRequired["capo_eventbridge.types.tag_list.TagList"]
    """<p>The list of key-value pairs to associate with the rule.</p>"""
    event_bus_name: NotRequired[
        "capo_eventbridge.types.event_bus_name_or_arn.EventBusNameOrArn"
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
        import capo_eventbridge.types.rule_state

        out["State"] = capo_eventbridge.types.rule_state.serialize_aws_json_1_1(
            value["state"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "tags" in value:
        import capo_eventbridge.types.tag_list

        out["Tags"] = capo_eventbridge.types.tag_list.serialize_aws_json_1_1(
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
        import capo_eventbridge.types.rule_state

        out["state"] = capo_eventbridge.types.rule_state.deserialize_aws_json_1_1(
            data["State"]
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    if data.get("Tags") is not None:
        import capo_eventbridge.types.tag_list

        out["tags"] = capo_eventbridge.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if data.get("EventBusName") is not None:
        out["event_bus_name"] = data["EventBusName"]
    return out
