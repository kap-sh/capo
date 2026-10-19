"""Generated from Smithy shape ``com.amazonaws.notifications#ListNotificationHubsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_notifications.types.next_token
    import capo_notifications.types.notification_hubs


class ListNotificationHubsResponse(TypedDict, closed=True):
    notification_hubs: "capo_notifications.types.notification_hubs.NotificationHubs"
    """<p>The <code>NotificationHubs</code> in the account.</p>"""
    next_token: NotRequired["capo_notifications.types.next_token.NextToken"]
    """<p>A pagination token. If a non-null pagination token is returned in a result, pass its value in another request to retrieve more entries.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListNotificationHubsResponse) -> dict:
    out: dict = {}
    import capo_notifications.types.notification_hubs

    out["notificationHubs"] = capo_notifications.types.notification_hubs.serialize_json(
        value["notification_hubs"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListNotificationHubsResponse:
    out: ListNotificationHubsResponse = {}  # type: ignore[typeddict-item]
    if data.get("notificationHubs") is not None:
        import capo_notifications.types.notification_hubs

        out["notification_hubs"] = (
            capo_notifications.types.notification_hubs.deserialize_json(
                data["notificationHubs"]
            )
        )
    else:
        out["notification_hubs"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
