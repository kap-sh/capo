"""Generated from Smithy shape ``com.amazonaws.notifications#ListManagedNotificationEventsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_notifications.types.managed_notification_events
    import capo_notifications.types.next_token


class ListManagedNotificationEventsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_notifications.types.next_token.NextToken"]
    """<p>A pagination token. If a non-null pagination token is returned in a result, pass its value in another request to retrieve more entries.</p>"""
    managed_notification_events: (
        "capo_notifications.types.managed_notification_events.ManagedNotificationEvents"
    )
    """<p>A list of Managed Notification Events matching the request criteria.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListManagedNotificationEventsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_notifications.types.managed_notification_events

    out["managedNotificationEvents"] = (
        capo_notifications.types.managed_notification_events.serialize_json(
            value["managed_notification_events"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListManagedNotificationEventsResponse:
    out: ListManagedNotificationEventsResponse = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("managedNotificationEvents") is not None:
        import capo_notifications.types.managed_notification_events

        out["managed_notification_events"] = (
            capo_notifications.types.managed_notification_events.deserialize_json(
                data["managedNotificationEvents"]
            )
        )
    else:
        out["managed_notification_events"] = []
    return out
