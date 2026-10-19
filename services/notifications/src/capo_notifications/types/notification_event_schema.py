"""Generated from Smithy shape ``com.amazonaws.notifications#NotificationEventSchema``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_notifications.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_notifications.types.aggregation_event_type
    import capo_notifications.types.aggregation_summary
    import capo_notifications.types.event_status
    import capo_notifications.types.media
    import capo_notifications.types.message_components
    import capo_notifications.types.notification_event_arn
    import capo_notifications.types.notification_event_id
    import capo_notifications.types.notification_type
    import capo_notifications.types.organizational_unit_id
    import capo_notifications.types.schema_version
    import capo_notifications.types.source_event_metadata
    import capo_notifications.types.text_parts
    import capo_notifications.types.url


class NotificationEventSchema(TypedDict, closed=True):
    schema_version: "capo_notifications.types.schema_version.SchemaVersion"
    """<p>The schema version of the Notification Event.</p>"""
    id: "capo_notifications.types.notification_event_id.NotificationEventId"
    """<p>The unique identifier for a <code>NotificationEvent</code>.</p>"""
    source_event_metadata: (
        "capo_notifications.types.source_event_metadata.SourceEventMetadata"
    )
    """<p>The source event metadata.</p>"""
    message_components: "capo_notifications.types.message_components.MessageComponents"
    source_event_detail_url: NotRequired["capo_notifications.types.url.Url"]
    """<p>The source event URL.</p>"""
    source_event_detail_url_display_text: NotRequired["str"]
    """<p>The detailed URL for the source event.</p>"""
    notification_type: "capo_notifications.types.notification_type.NotificationType"
    """<p>The type of event causing the notification.</p> <ul> <li> <p>Values:</p> <ul> <li> <p> <code>ALERT</code> </p> <ul> <li> <p>A notification about an event where something was triggered, initiated, reopened, deployed, or a threshold was breached.</p> </li> </ul> </li> <li> <p> <code>WARNING</code> </p> <ul> <li> <p>A notification about an event where an issue is about to arise. For example, something is approaching a threshold.</p> </li> </ul> </li> <li> <p> <code>ANNOUNCEMENT</code> </p> <ul> <li> <p>A notification about an important event. For example, a step in a workflow or escalation path or that a workflow was updated.</p> </li> </ul> </li> <li> <p> <code>INFORMATIONAL</code> </p> <ul> <li> <p>A notification about informational messages. For example, recommendations, service announcements, or reminders.</p> </li> </ul> </li> </ul> </li> </ul>"""
    event_status: NotRequired["capo_notifications.types.event_status.EventStatus"]
    """<p>The assessed nature of the event.</p> <ul> <li> <p>Values:</p> <ul> <li> <p> <code>HEALTHY</code> </p> <ul> <li> <p>All <code>EventRules</code> are <code>ACTIVE</code> and any call can be run.</p> </li> </ul> </li> <li> <p> <code>UNHEALTHY</code> </p> <ul> <li> <p>Some <code>EventRules</code> are <code>ACTIVE</code> and some are <code>INACTIVE</code>. Any call can be run.</p> </li> </ul> </li> </ul> </li> </ul>"""
    aggregation_event_type: NotRequired[
        "capo_notifications.types.aggregation_event_type.AggregationEventType"
    ]
    """<p>The aggregation type of the <code>NotificationConfiguration</code>.</p> <ul> <li> <p>Values:</p> <ul> <li> <p> <code>AGGREGATE</code> </p> <ul> <li> <p>The notification event is an aggregate notification. Aggregate notifications summarize grouped events over a specified time period.</p> </li> </ul> </li> <li> <p> <code>CHILD</code> </p> <ul> <li> <p>Some <code>EventRules</code> are <code>ACTIVE</code> and some are <code>INACTIVE</code>. Any call can be run.</p> </li> </ul> </li> <li> <p> <code>NONE</code> </p> <ul> <li> <p>The notification isn't aggregated.</p> </li> </ul> </li> </ul> </li> </ul>"""
    aggregate_notification_event_arn: NotRequired[
        "capo_notifications.types.notification_event_arn.NotificationEventArn"
    ]
    """<p>If the value of <code>aggregationEventType</code> is not <code>NONE</code>, this is the Amazon Resource Event (ARN) of the parent aggregate notification.</p> <p>This is omitted if notification isn't aggregated.</p>"""
    aggregation_summary: NotRequired[
        "capo_notifications.types.aggregation_summary.AggregationSummary"
    ]
    """<p>Provides additional information about how multiple notifications are grouped.</p>"""
    start_time: NotRequired["datetime.datetime"]
    """<p>The notification event start time.</p>"""
    end_time: NotRequired["datetime.datetime"]
    """<p>The end time of the event.</p>"""
    text_parts: "capo_notifications.types.text_parts.TextParts"
    """<p>A list of text values.</p>"""
    media: "capo_notifications.types.media.Media"
    """<p>A list of media elements.</p>"""
    organizational_unit_id: NotRequired[
        "capo_notifications.types.organizational_unit_id.OrganizationalUnitId"
    ]
    """<p>The unique identifier of the organizational unit associated with the notification event.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NotificationEventSchema) -> dict:
    out: dict = {}
    out["schemaVersion"] = value["schema_version"]
    out["id"] = value["id"]
    import capo_notifications.types.source_event_metadata

    out["sourceEventMetadata"] = (
        capo_notifications.types.source_event_metadata.serialize_json(
            value["source_event_metadata"]
        )
    )
    import capo_notifications.types.message_components

    out["messageComponents"] = (
        capo_notifications.types.message_components.serialize_json(
            value["message_components"]
        )
    )
    if "source_event_detail_url" in value:
        out["sourceEventDetailUrl"] = value["source_event_detail_url"]
    if "source_event_detail_url_display_text" in value:
        out["sourceEventDetailUrlDisplayText"] = value[
            "source_event_detail_url_display_text"
        ]
    out["notificationType"] = value["notification_type"]
    if "event_status" in value:
        out["eventStatus"] = value["event_status"]
    if "aggregation_event_type" in value:
        out["aggregationEventType"] = value["aggregation_event_type"]
    if "aggregate_notification_event_arn" in value:
        out["aggregateNotificationEventArn"] = value["aggregate_notification_event_arn"]
    if "aggregation_summary" in value:
        import capo_notifications.types.aggregation_summary

        out["aggregationSummary"] = (
            capo_notifications.types.aggregation_summary.serialize_json(
                value["aggregation_summary"]
            )
        )
    if "start_time" in value:
        import capo_notifications._protocol.serialize

        out["startTime"] = capo_notifications._protocol.serialize.fmt_date_time(
            value["start_time"]
        )
    if "end_time" in value:
        import capo_notifications._protocol.serialize

        out["endTime"] = capo_notifications._protocol.serialize.fmt_date_time(
            value["end_time"]
        )
    import capo_notifications.types.text_parts

    out["textParts"] = capo_notifications.types.text_parts.serialize_json(
        value["text_parts"]
    )
    import capo_notifications.types.media

    out["media"] = capo_notifications.types.media.serialize_json(value["media"])
    if "organizational_unit_id" in value:
        out["organizationalUnitId"] = value["organizational_unit_id"]
    return out


def deserialize_json(data: dict) -> NotificationEventSchema:
    out: NotificationEventSchema = {}  # type: ignore[typeddict-item]
    if data.get("schemaVersion") is not None:
        out["schema_version"] = data["schemaVersion"]
    else:
        out["schema_version"] = ""
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("sourceEventMetadata") is not None:
        import capo_notifications.types.source_event_metadata

        out["source_event_metadata"] = (
            capo_notifications.types.source_event_metadata.deserialize_json(
                data["sourceEventMetadata"]
            )
        )
    else:
        raise DeserializationError(
            "NotificationEventSchema.source_event_metadata required"
        )
    if data.get("messageComponents") is not None:
        import capo_notifications.types.message_components

        out["message_components"] = (
            capo_notifications.types.message_components.deserialize_json(
                data["messageComponents"]
            )
        )
    else:
        raise DeserializationError(
            "NotificationEventSchema.message_components required"
        )
    if data.get("sourceEventDetailUrl") is not None:
        out["source_event_detail_url"] = data["sourceEventDetailUrl"]
    if data.get("sourceEventDetailUrlDisplayText") is not None:
        out["source_event_detail_url_display_text"] = data[
            "sourceEventDetailUrlDisplayText"
        ]
    if data.get("notificationType") is not None:
        out["notification_type"] = data["notificationType"]
    else:
        out["notification_type"] = ""
    if data.get("eventStatus") is not None:
        out["event_status"] = data["eventStatus"]
    if data.get("aggregationEventType") is not None:
        out["aggregation_event_type"] = data["aggregationEventType"]
    if data.get("aggregateNotificationEventArn") is not None:
        out["aggregate_notification_event_arn"] = data["aggregateNotificationEventArn"]
    if data.get("aggregationSummary") is not None:
        import capo_notifications.types.aggregation_summary

        out["aggregation_summary"] = (
            capo_notifications.types.aggregation_summary.deserialize_json(
                data["aggregationSummary"]
            )
        )
    if data.get("startTime") is not None:
        import datetime

        out["start_time"] = datetime.datetime.fromisoformat(
            data["startTime"].replace("Z", "+00:00")
        )
    if data.get("endTime") is not None:
        import datetime

        out["end_time"] = datetime.datetime.fromisoformat(
            data["endTime"].replace("Z", "+00:00")
        )
    if data.get("textParts") is not None:
        import capo_notifications.types.text_parts

        out["text_parts"] = capo_notifications.types.text_parts.deserialize_json(
            data["textParts"]
        )
    else:
        out["text_parts"] = {}
    if data.get("media") is not None:
        import capo_notifications.types.media

        out["media"] = capo_notifications.types.media.deserialize_json(data["media"])
    else:
        out["media"] = []
    if data.get("organizationalUnitId") is not None:
        out["organizational_unit_id"] = data["organizationalUnitId"]
    return out
