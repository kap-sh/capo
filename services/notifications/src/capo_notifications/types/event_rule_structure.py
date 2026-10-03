"""Generated from Smithy shape ``com.amazonaws.notifications#EventRuleStructure``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_notifications.errors import DeserializationError

if TYPE_CHECKING:
    import capo_notifications.types.creation_time
    import capo_notifications.types.event_rule_arn
    import capo_notifications.types.event_rule_event_pattern
    import capo_notifications.types.event_type
    import capo_notifications.types.managed_rule_arns
    import capo_notifications.types.notification_configuration_arn
    import capo_notifications.types.regions
    import capo_notifications.types.source
    import capo_notifications.types.status_summary_by_region


class EventRuleStructure(TypedDict, closed=True):
    arn: "capo_notifications.types.event_rule_arn.EventRuleArn"
    """<p>The Amazon Resource Name (ARN) of the <code>EventRule</code>. CloudFormation stack generates this ARN and then uses this ARN to associate with the <code>NotificationConfiguration</code>.</p>"""
    notification_configuration_arn: "capo_notifications.types.notification_configuration_arn.NotificationConfigurationArn"
    """<p>The ARN for the <code>NotificationConfiguration</code> associated with this <code>EventRule</code>.</p>"""
    creation_time: "capo_notifications.types.creation_time.CreationTime"
    """<p>The creation time of the <code>EventRule</code>.</p>"""
    source: "capo_notifications.types.source.Source"
    """<p>The event source this rule should match with the EventBridge event sources. It must match with atleast one of the valid EventBridge event sources. Only Amazon Web Services service sourced events are supported. For example, <code>aws.ec2</code> and <code>aws.cloudwatch</code>. For more information, see <a href="https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event.html#eb-service-event-delivery-level">Event delivery from Amazon Web Services services</a> in the <i> Amazon EventBridge User Guide</i>.</p>"""
    event_type: "capo_notifications.types.event_type.EventType"
    """<p>The event type this rule should match with the EventBridge events. It must match with atleast one of the valid EventBridge event types. For example, Amazon EC2 Instance State change Notification and Amazon CloudWatch State Change. For more information, see <a href="https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event.html#eb-service-event-delivery-level">Event delivery from Amazon Web Services services</a> in the <i> Amazon EventBridge User Guide</i>.</p>"""
    event_pattern: (
        "capo_notifications.types.event_rule_event_pattern.EventRuleEventPattern"
    )
    """<p>An additional event pattern used to further filter the events this <code>EventRule</code> receives.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html">Amazon EventBridge event patterns</a> in the <i>Amazon EventBridge User Guide.</i> </p>"""
    regions: "capo_notifications.types.regions.Regions"
    """<p>A list of Amazon Web Services Regions that send events to this <code>EventRule</code>.</p>"""
    managed_rules: "capo_notifications.types.managed_rule_arns.ManagedRuleArns"
    """<p>A list of Amazon EventBridge Managed Rule ARNs associated with this <code>EventRule</code>.</p> <note> <p>These are created by User Notifications within your account so your <code>EventRules</code> can function.</p> </note>"""
    status_summary_by_region: (
        "capo_notifications.types.status_summary_by_region.StatusSummaryByRegion"
    )
    """<p>A list of an <code>EventRule</code>'s status by Region. Regions are mapped to <code>EventRuleStatusSummary</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EventRuleStructure) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["notificationConfigurationArn"] = value["notification_configuration_arn"]
    import capo_notifications.types.creation_time

    out["creationTime"] = capo_notifications.types.creation_time.serialize_json(
        value["creation_time"]
    )
    out["source"] = value["source"]
    out["eventType"] = value["event_type"]
    out["eventPattern"] = value["event_pattern"]
    import capo_notifications.types.regions

    out["regions"] = capo_notifications.types.regions.serialize_json(value["regions"])
    import capo_notifications.types.managed_rule_arns

    out["managedRules"] = capo_notifications.types.managed_rule_arns.serialize_json(
        value["managed_rules"]
    )
    import capo_notifications.types.status_summary_by_region

    out["statusSummaryByRegion"] = (
        capo_notifications.types.status_summary_by_region.serialize_json(
            value["status_summary_by_region"]
        )
    )
    return out


def deserialize_json(data: dict) -> EventRuleStructure:
    out: EventRuleStructure = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("EventRuleStructure.arn required")
    if data.get("notificationConfigurationArn") is not None:
        out["notification_configuration_arn"] = data["notificationConfigurationArn"]
    else:
        raise DeserializationError(
            "EventRuleStructure.notification_configuration_arn required"
        )
    if data.get("creationTime") is not None:
        import capo_notifications.types.creation_time

        out["creation_time"] = capo_notifications.types.creation_time.deserialize_json(
            data["creationTime"]
        )
    else:
        raise DeserializationError("EventRuleStructure.creation_time required")
    if data.get("source") is not None:
        out["source"] = data["source"]
    else:
        raise DeserializationError("EventRuleStructure.source required")
    if data.get("eventType") is not None:
        out["event_type"] = data["eventType"]
    else:
        raise DeserializationError("EventRuleStructure.event_type required")
    if data.get("eventPattern") is not None:
        out["event_pattern"] = data["eventPattern"]
    else:
        raise DeserializationError("EventRuleStructure.event_pattern required")
    if data.get("regions") is not None:
        import capo_notifications.types.regions

        out["regions"] = capo_notifications.types.regions.deserialize_json(
            data["regions"]
        )
    else:
        raise DeserializationError("EventRuleStructure.regions required")
    if data.get("managedRules") is not None:
        import capo_notifications.types.managed_rule_arns

        out["managed_rules"] = (
            capo_notifications.types.managed_rule_arns.deserialize_json(
                data["managedRules"]
            )
        )
    else:
        raise DeserializationError("EventRuleStructure.managed_rules required")
    if data.get("statusSummaryByRegion") is not None:
        import capo_notifications.types.status_summary_by_region

        out["status_summary_by_region"] = (
            capo_notifications.types.status_summary_by_region.deserialize_json(
                data["statusSummaryByRegion"]
            )
        )
    else:
        raise DeserializationError(
            "EventRuleStructure.status_summary_by_region required"
        )
    return out
