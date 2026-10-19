"""Generated from Smithy shape ``com.amazonaws.notifications#ManagedNotificationEventOverview``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_notifications.errors import DeserializationError

if TYPE_CHECKING:
    import capo_notifications.types.account_id
    import capo_notifications.types.aggregated_notification_regions
    import capo_notifications.types.aggregation_event_type
    import capo_notifications.types.aggregation_summary
    import capo_notifications.types.creation_time
    import capo_notifications.types.managed_notification_configuration_os_arn
    import capo_notifications.types.managed_notification_event_arn
    import capo_notifications.types.managed_notification_event_summary
    import capo_notifications.types.organizational_unit_id


class ManagedNotificationEventOverview(TypedDict, closed=True):
    arn: "capo_notifications.types.managed_notification_event_arn.ManagedNotificationEventArn"
    """<p>The Amazon Resource Name (ARN) of the ManagedNotificationEvent.</p>"""
    managed_notification_configuration_arn: "capo_notifications.types.managed_notification_configuration_os_arn.ManagedNotificationConfigurationOsArn"
    """<p>The Amazon Resource Name (ARN) of the <code>ManagedNotificationConfiguration</code>.</p>"""
    related_account: "capo_notifications.types.account_id.AccountId"
    """<p>The account that related to the <code>ManagedNotificationEvent</code>.</p>"""
    creation_time: "capo_notifications.types.creation_time.CreationTime"
    """<p>The creation time of the <code>ManagedNotificationEvent</code>.</p>"""
    notification_event: "capo_notifications.types.managed_notification_event_summary.ManagedNotificationEventSummary"
    """<p/>"""
    aggregation_event_type: NotRequired[
        "capo_notifications.types.aggregation_event_type.AggregationEventType"
    ]
    """<p>The notifications aggregation type.</p> <ul> <li> <p>Values:</p> <ul> <li> <p> <code>AGGREGATE</code> </p> <ul> <li> <p>The notification event is an aggregate notification. Aggregate notifications summarize grouped events over a specified time period.</p> </li> </ul> </li> <li> <p> <code>CHILD</code> </p> <ul> <li> <p>Some <code>EventRules</code> are <code>ACTIVE</code> and some are <code>INACTIVE</code>. Any call can be run.</p> </li> </ul> </li> <li> <p> <code>NONE</code> </p> <ul> <li> <p>The notification isn't aggregated.</p> </li> </ul> </li> </ul> </li> </ul>"""
    organizational_unit_id: NotRequired[
        "capo_notifications.types.organizational_unit_id.OrganizationalUnitId"
    ]
    """<p>The Organizational Unit Id that an Amazon Web Services account belongs to.</p>"""
    aggregation_summary: NotRequired[
        "capo_notifications.types.aggregation_summary.AggregationSummary"
    ]
    aggregated_notification_regions: NotRequired[
        "capo_notifications.types.aggregated_notification_regions.AggregatedNotificationRegions"
    ]
    """<p>The list of the regions where the aggregated notifications in this <code>NotificationEvent</code> originated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ManagedNotificationEventOverview) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["managedNotificationConfigurationArn"] = value[
        "managed_notification_configuration_arn"
    ]
    out["relatedAccount"] = value["related_account"]
    import capo_notifications.types.creation_time

    out["creationTime"] = capo_notifications.types.creation_time.serialize_json(
        value["creation_time"]
    )
    import capo_notifications.types.managed_notification_event_summary

    out["notificationEvent"] = (
        capo_notifications.types.managed_notification_event_summary.serialize_json(
            value["notification_event"]
        )
    )
    if "aggregation_event_type" in value:
        out["aggregationEventType"] = value["aggregation_event_type"]
    if "organizational_unit_id" in value:
        out["organizationalUnitId"] = value["organizational_unit_id"]
    if "aggregation_summary" in value:
        import capo_notifications.types.aggregation_summary

        out["aggregationSummary"] = (
            capo_notifications.types.aggregation_summary.serialize_json(
                value["aggregation_summary"]
            )
        )
    if "aggregated_notification_regions" in value:
        import capo_notifications.types.aggregated_notification_regions

        out["aggregatedNotificationRegions"] = (
            capo_notifications.types.aggregated_notification_regions.serialize_json(
                value["aggregated_notification_regions"]
            )
        )
    return out


def deserialize_json(data: dict) -> ManagedNotificationEventOverview:
    out: ManagedNotificationEventOverview = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("managedNotificationConfigurationArn") is not None:
        out["managed_notification_configuration_arn"] = data[
            "managedNotificationConfigurationArn"
        ]
    else:
        out["managed_notification_configuration_arn"] = ""
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
        import capo_notifications.types.managed_notification_event_summary

        out["notification_event"] = (
            capo_notifications.types.managed_notification_event_summary.deserialize_json(
                data["notificationEvent"]
            )
        )
    else:
        raise DeserializationError(
            "ManagedNotificationEventOverview.notification_event required"
        )
    if data.get("aggregationEventType") is not None:
        out["aggregation_event_type"] = data["aggregationEventType"]
    if data.get("organizationalUnitId") is not None:
        out["organizational_unit_id"] = data["organizationalUnitId"]
    if data.get("aggregationSummary") is not None:
        import capo_notifications.types.aggregation_summary

        out["aggregation_summary"] = (
            capo_notifications.types.aggregation_summary.deserialize_json(
                data["aggregationSummary"]
            )
        )
    if data.get("aggregatedNotificationRegions") is not None:
        import capo_notifications.types.aggregated_notification_regions

        out["aggregated_notification_regions"] = (
            capo_notifications.types.aggregated_notification_regions.deserialize_json(
                data["aggregatedNotificationRegions"]
            )
        )
    return out
