"""Generated from Smithy shape ``com.amazonaws.notifications#DeregisterNotificationHubResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_notifications.errors import DeserializationError

if TYPE_CHECKING:
    import capo_notifications.types.notification_hub_status_summary
    import capo_notifications.types.region


class DeregisterNotificationHubResponse(TypedDict, closed=True):
    notification_hub_region: "capo_notifications.types.region.Region"
    """<p>The <code>NotificationHub</code> Region.</p>"""
    status_summary: "capo_notifications.types.notification_hub_status_summary.NotificationHubStatusSummary"
    """<p> <code>NotificationHub</code> status information.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeregisterNotificationHubResponse) -> dict:
    out: dict = {}
    out["notificationHubRegion"] = value["notification_hub_region"]
    import capo_notifications.types.notification_hub_status_summary

    out["statusSummary"] = (
        capo_notifications.types.notification_hub_status_summary.serialize_json(
            value["status_summary"]
        )
    )
    return out


def deserialize_json(data: dict) -> DeregisterNotificationHubResponse:
    out: DeregisterNotificationHubResponse = {}  # type: ignore[typeddict-item]
    if data.get("notificationHubRegion") is not None:
        out["notification_hub_region"] = data["notificationHubRegion"]
    else:
        out["notification_hub_region"] = ""
    if data.get("statusSummary") is not None:
        import capo_notifications.types.notification_hub_status_summary

        out["status_summary"] = (
            capo_notifications.types.notification_hub_status_summary.deserialize_json(
                data["statusSummary"]
            )
        )
    else:
        raise DeserializationError(
            "DeregisterNotificationHubResponse.status_summary required"
        )
    return out
