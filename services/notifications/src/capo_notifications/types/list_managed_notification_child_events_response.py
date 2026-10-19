"""Generated from Smithy shape ``com.amazonaws.notifications#ListManagedNotificationChildEventsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_notifications.types.managed_notification_child_events
    import capo_notifications.types.next_token


class ListManagedNotificationChildEventsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_notifications.types.next_token.NextToken"]
    """<p>A pagination token. If a non-null pagination token is returned in a result, pass its value in another request to retrieve more entries.</p>"""
    managed_notification_child_events: "capo_notifications.types.managed_notification_child_events.ManagedNotificationChildEvents"
    """<p>A pagination token. If a non-null pagination token is returned in a result, pass its value in another request to retrieve more entries.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListManagedNotificationChildEventsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_notifications.types.managed_notification_child_events

    out["managedNotificationChildEvents"] = (
        capo_notifications.types.managed_notification_child_events.serialize_json(
            value["managed_notification_child_events"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListManagedNotificationChildEventsResponse:
    out: ListManagedNotificationChildEventsResponse = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("managedNotificationChildEvents") is not None:
        import capo_notifications.types.managed_notification_child_events

        out["managed_notification_child_events"] = (
            capo_notifications.types.managed_notification_child_events.deserialize_json(
                data["managedNotificationChildEvents"]
            )
        )
    else:
        out["managed_notification_child_events"] = []
    return out
