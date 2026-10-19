"""Generated from Smithy shape ``com.amazonaws.notifications#NotificationConfigurationStructure``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_notifications.types.aggregation_duration
    import capo_notifications.types.creation_time
    import capo_notifications.types.notification_configuration_arn
    import capo_notifications.types.notification_configuration_description
    import capo_notifications.types.notification_configuration_name
    import capo_notifications.types.notification_configuration_status
    import capo_notifications.types.notification_configuration_subtype


class NotificationConfigurationStructure(TypedDict, closed=True):
    arn: "capo_notifications.types.notification_configuration_arn.NotificationConfigurationArn"
    """<p>The Amazon Resource Name (ARN) of the <code>NotificationConfiguration</code> resource.</p>"""
    name: "capo_notifications.types.notification_configuration_name.NotificationConfigurationName"
    """<p>The name of the <code>NotificationConfiguration</code>. Supports RFC 3986's unreserved characters.</p>"""
    description: "capo_notifications.types.notification_configuration_description.NotificationConfigurationDescription"
    """<p>The description of the <code>NotificationConfiguration</code>.</p>"""
    status: "capo_notifications.types.notification_configuration_status.NotificationConfigurationStatus"
    """<p>The current status of the <code>NotificationConfiguration</code>.</p>"""
    creation_time: "capo_notifications.types.creation_time.CreationTime"
    """<p>The creation time of the <code>NotificationConfiguration</code>.</p>"""
    aggregation_duration: NotRequired[
        "capo_notifications.types.aggregation_duration.AggregationDuration"
    ]
    """<p>The aggregation preference of the <code>NotificationConfiguration</code>.</p> <ul> <li> <p>Values:</p> <ul> <li> <p> <code>LONG</code> </p> <ul> <li> <p>Aggregate notifications for long periods of time (12 hours).</p> </li> </ul> </li> <li> <p> <code>SHORT</code> </p> <ul> <li> <p>Aggregate notifications for short periods of time (5 minutes).</p> </li> </ul> </li> <li> <p> <code>NONE</code> </p> <ul> <li> <p>Don't aggregate notifications.</p> </li> </ul> </li> </ul> </li> </ul>"""
    subtype: NotRequired[
        "capo_notifications.types.notification_configuration_subtype.NotificationConfigurationSubtype"
    ]
    """<p>The subtype of the notification configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NotificationConfigurationStructure) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["name"] = value["name"]
    out["description"] = value["description"]
    out["status"] = value["status"]
    import capo_notifications.types.creation_time

    out["creationTime"] = capo_notifications.types.creation_time.serialize_json(
        value["creation_time"]
    )
    if "aggregation_duration" in value:
        out["aggregationDuration"] = value["aggregation_duration"]
    if "subtype" in value:
        out["subtype"] = value["subtype"]
    return out


def deserialize_json(data: dict) -> NotificationConfigurationStructure:
    out: NotificationConfigurationStructure = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    else:
        out["description"] = ""
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        out["status"] = ""
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
    if data.get("aggregationDuration") is not None:
        out["aggregation_duration"] = data["aggregationDuration"]
    if data.get("subtype") is not None:
        out["subtype"] = data["subtype"]
    return out
