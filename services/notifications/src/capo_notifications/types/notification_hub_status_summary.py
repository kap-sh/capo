"""Generated from Smithy shape ``com.amazonaws.notifications#NotificationHubStatusSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_notifications.types.notification_hub_status
    import capo_notifications.types.notification_hub_status_reason


class NotificationHubStatusSummary(TypedDict, closed=True):
    status: "capo_notifications.types.notification_hub_status.NotificationHubStatus"
    """<p>Status information about the <code>NotificationHub</code>.</p> <ul> <li> <p>Values:</p> <ul> <li> <p> <code>ACTIVE</code> </p> <ul> <li> <p>Incoming <code>NotificationEvents</code> are replicated to this <code>NotificationHub</code>.</p> </li> </ul> </li> <li> <p> <code>REGISTERING</code> </p> <ul> <li> <p>The <code>NotificationConfiguration</code> is initializing. A <code>NotificationConfiguration</code> with this status can't be deregistered.</p> </li> </ul> </li> <li> <p> <code>DEREGISTERING</code> </p> <ul> <li> <p>The <code>NotificationConfiguration</code> is being deleted. You can't register additional <code>NotificationHubs</code> in the same Region as a <code>NotificationConfiguration</code> with this status.</p> </li> </ul> </li> </ul> </li> </ul>"""
    reason: "capo_notifications.types.notification_hub_status_reason.NotificationHubStatusReason"
    """<p>An explanation for the current status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NotificationHubStatusSummary) -> dict:
    out: dict = {}
    out["status"] = value["status"]
    out["reason"] = value["reason"]
    return out


def deserialize_json(data: dict) -> NotificationHubStatusSummary:
    out: NotificationHubStatusSummary = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        out["status"] = ""
    if data.get("reason") is not None:
        out["reason"] = data["reason"]
    else:
        out["reason"] = ""
    return out
