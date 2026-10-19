"""Generated from Smithy shape ``com.amazonaws.notifications#ListNotificationEventsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_notifications.types.next_token
    import capo_notifications.types.notification_events


class ListNotificationEventsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_notifications.types.next_token.NextToken"]
    """<p>A pagination token. If a non-null pagination token is returned in a result, pass its value in another request to retrieve more entries.</p>"""
    notification_events: (
        "capo_notifications.types.notification_events.NotificationEvents"
    )
    """<p>The list of notification events.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListNotificationEventsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_notifications.types.notification_events

    out["notificationEvents"] = (
        capo_notifications.types.notification_events.serialize_json(
            value["notification_events"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListNotificationEventsResponse:
    out: ListNotificationEventsResponse = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("notificationEvents") is not None:
        import capo_notifications.types.notification_events

        out["notification_events"] = (
            capo_notifications.types.notification_events.deserialize_json(
                data["notificationEvents"]
            )
        )
    else:
        out["notification_events"] = []
    return out
