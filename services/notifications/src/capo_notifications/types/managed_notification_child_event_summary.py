"""Generated from Smithy shape ``com.amazonaws.notifications#ManagedNotificationChildEventSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_notifications.errors import DeserializationError

if TYPE_CHECKING:
    import capo_notifications.types.aggregation_detail
    import capo_notifications.types.event_status
    import capo_notifications.types.managed_source_event_metadata_summary
    import capo_notifications.types.message_components_summary
    import capo_notifications.types.notification_type
    import capo_notifications.types.schema_version


class ManagedNotificationChildEventSummary(TypedDict, closed=True):
    schema_version: "capo_notifications.types.schema_version.SchemaVersion"
    """<p>The schema version of the <code>ManagedNotificationChildEvent</code>.</p>"""
    source_event_metadata: "capo_notifications.types.managed_source_event_metadata_summary.ManagedSourceEventMetadataSummary"
    """<p>Contains all event metadata present identically across all <code>NotificationEvents</code>. All fields are present in Source Events via Eventbridge.</p>"""
    message_components: (
        "capo_notifications.types.message_components_summary.MessageComponentsSummary"
    )
    aggregation_detail: "capo_notifications.types.aggregation_detail.AggregationDetail"
    """<p>Provides detailed information about the dimensions used for event summarization and aggregation.</p>"""
    event_status: "capo_notifications.types.event_status.EventStatus"
    """<p>The perceived nature of the event.</p> <ul> <li> <p>Values:</p> <ul> <li> <p> <code>HEALTHY</code> </p> <ul> <li> <p>All EventRules are <code>ACTIVE</code> and any call can be run.</p> </li> </ul> </li> <li> <p> <code>UNHEALTHY</code> </p> <ul> <li> <p>Some EventRules are <code>ACTIVE</code> and some are <code>INACTIVE</code>. Any call can be run.</p> </li> </ul> </li> </ul> </li> </ul>"""
    notification_type: "capo_notifications.types.notification_type.NotificationType"
    """<p>The Type of the event causing this notification.</p> <ul> <li> <p>Values:</p> <ul> <li> <p> <code>ALERT</code> </p> <ul> <li> <p>A notification about an event where something was triggered, initiated, reopened, deployed, or a threshold was breached.</p> </li> </ul> </li> <li> <p> <code>WARNING</code> </p> <ul> <li> <p>A notification about an event where an issue is about to arise. For example, something is approaching a threshold.</p> </li> </ul> </li> <li> <p> <code>ANNOUNCEMENT</code> </p> <ul> <li> <p>A notification about an important event. For example, a step in a workflow or escalation path or that a workflow was updated.</p> </li> </ul> </li> <li> <p> <code>INFORMATIONAL</code> </p> <ul> <li> <p>A notification about informational messages. For example, recommendations, service announcements, or reminders.</p> </li> </ul> </li> </ul> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: ManagedNotificationChildEventSummary) -> dict:
    out: dict = {}
    out["schemaVersion"] = value["schema_version"]
    import capo_notifications.types.managed_source_event_metadata_summary

    out["sourceEventMetadata"] = (
        capo_notifications.types.managed_source_event_metadata_summary.serialize_json(
            value["source_event_metadata"]
        )
    )
    import capo_notifications.types.message_components_summary

    out["messageComponents"] = (
        capo_notifications.types.message_components_summary.serialize_json(
            value["message_components"]
        )
    )
    import capo_notifications.types.aggregation_detail

    out["aggregationDetail"] = (
        capo_notifications.types.aggregation_detail.serialize_json(
            value["aggregation_detail"]
        )
    )
    out["eventStatus"] = value["event_status"]
    out["notificationType"] = value["notification_type"]
    return out


def deserialize_json(data: dict) -> ManagedNotificationChildEventSummary:
    out: ManagedNotificationChildEventSummary = {}  # type: ignore[typeddict-item]
    if data.get("schemaVersion") is not None:
        out["schema_version"] = data["schemaVersion"]
    else:
        out["schema_version"] = ""
    if data.get("sourceEventMetadata") is not None:
        import capo_notifications.types.managed_source_event_metadata_summary

        out["source_event_metadata"] = (
            capo_notifications.types.managed_source_event_metadata_summary.deserialize_json(
                data["sourceEventMetadata"]
            )
        )
    else:
        raise DeserializationError(
            "ManagedNotificationChildEventSummary.source_event_metadata required"
        )
    if data.get("messageComponents") is not None:
        import capo_notifications.types.message_components_summary

        out["message_components"] = (
            capo_notifications.types.message_components_summary.deserialize_json(
                data["messageComponents"]
            )
        )
    else:
        raise DeserializationError(
            "ManagedNotificationChildEventSummary.message_components required"
        )
    if data.get("aggregationDetail") is not None:
        import capo_notifications.types.aggregation_detail

        out["aggregation_detail"] = (
            capo_notifications.types.aggregation_detail.deserialize_json(
                data["aggregationDetail"]
            )
        )
    else:
        raise DeserializationError(
            "ManagedNotificationChildEventSummary.aggregation_detail required"
        )
    if data.get("eventStatus") is not None:
        out["event_status"] = data["eventStatus"]
    else:
        out["event_status"] = ""
    if data.get("notificationType") is not None:
        out["notification_type"] = data["notificationType"]
    else:
        out["notification_type"] = ""
    return out
