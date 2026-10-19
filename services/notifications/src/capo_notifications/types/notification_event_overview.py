"""Generated from Smithy shape ``com.amazonaws.notifications#NotificationEventOverview``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_notifications.errors import DeserializationError

if TYPE_CHECKING:
    import capo_notifications.types.account_id
    import capo_notifications.types.aggregation_event_type
    import capo_notifications.types.aggregation_summary
    import capo_notifications.types.creation_time
    import capo_notifications.types.notification_configuration_arn
    import capo_notifications.types.notification_event_arn
    import capo_notifications.types.notification_event_summary
    import capo_notifications.types.organizational_unit_id


class NotificationEventOverview(TypedDict, closed=True):
    arn: "capo_notifications.types.notification_event_arn.NotificationEventArn"
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""
    notification_configuration_arn: "capo_notifications.types.notification_configuration_arn.NotificationConfigurationArn"
    """<p>The ARN of the <code>NotificationConfiguration</code>.</p>"""
    related_account: "capo_notifications.types.account_id.AccountId"
    """<p>The account name containing the <code>NotificationHub</code>.</p>"""
    creation_time: "capo_notifications.types.creation_time.CreationTime"
    """<p>The creation time of the <code>NotificationEvent</code>.</p>"""
    notification_event: (
        "capo_notifications.types.notification_event_summary.NotificationEventSummary"
    )
    """<p>Refers to a <code>NotificationEventSummary</code> object.</p> <p>Similar in structure to <code>content</code> in the <code>GetNotificationEvent</code> response.</p>"""
    aggregation_event_type: NotRequired[
        "capo_notifications.types.aggregation_event_type.AggregationEventType"
    ]
    """<p>The <code>NotificationConfiguration</code>'s aggregation type.</p> <ul> <li> <p>Values:</p> <ul> <li> <p> <code>AGGREGATE</code> </p> <ul> <li> <p>The notification event is an aggregate notification. Aggregate notifications summarize grouped events over a specified time period.</p> </li> </ul> </li> <li> <p> <code>CHILD</code> </p> <ul> <li> <p>Some <code>EventRules</code> are <code>ACTIVE</code> and some are <code>INACTIVE</code>. Any call can be run.</p> </li> </ul> </li> <li> <p> <code>NONE</code> </p> <ul> <li> <p>The notification isn't aggregated.</p> </li> </ul> </li> </ul> </li> </ul>"""
    aggregate_notification_event_arn: NotRequired[
        "capo_notifications.types.notification_event_arn.NotificationEventArn"
    ]
    """<p>The ARN of the <code>aggregatedNotificationEventArn</code> to match.</p>"""
    aggregation_summary: NotRequired[
        "capo_notifications.types.aggregation_summary.AggregationSummary"
    ]
    """<p>Provides an aggregated summary data for notification events.</p>"""
    organizational_unit_id: NotRequired[
        "capo_notifications.types.organizational_unit_id.OrganizationalUnitId"
    ]
    """<p>The unique identifier of the organizational unit in the notification event overview.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NotificationEventOverview) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["notificationConfigurationArn"] = value["notification_configuration_arn"]
    out["relatedAccount"] = value["related_account"]
    import capo_notifications.types.creation_time

    out["creationTime"] = capo_notifications.types.creation_time.serialize_json(
        value["creation_time"]
    )
    import capo_notifications.types.notification_event_summary

    out["notificationEvent"] = (
        capo_notifications.types.notification_event_summary.serialize_json(
            value["notification_event"]
        )
    )
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
    if "organizational_unit_id" in value:
        out["organizationalUnitId"] = value["organizational_unit_id"]
    return out


def deserialize_json(data: dict) -> NotificationEventOverview:
    out: NotificationEventOverview = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("notificationConfigurationArn") is not None:
        out["notification_configuration_arn"] = data["notificationConfigurationArn"]
    else:
        out["notification_configuration_arn"] = ""
    if data.get("relatedAccount") is not None:
        out["related_account"] = data["relatedAccount"]
    else:
        out["related_account"] = ""
    if data.get("creationTime") is not None:
        import capo_notifications.types.creation_time

        out["creation_time"] = capo_notifications.types.creation_time.deserialize_json(
            data["creationTime"]
        )
    else:
        import datetime

        out["creation_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("notificationEvent") is not None:
        import capo_notifications.types.notification_event_summary

        out["notification_event"] = (
            capo_notifications.types.notification_event_summary.deserialize_json(
                data["notificationEvent"]
            )
        )
    else:
        raise DeserializationError(
            "NotificationEventOverview.notification_event required"
        )
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
    if data.get("organizationalUnitId") is not None:
        out["organizational_unit_id"] = data["organizationalUnitId"]
    return out
