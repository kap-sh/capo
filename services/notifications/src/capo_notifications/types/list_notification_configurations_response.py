"""Generated from Smithy shape ``com.amazonaws.notifications#ListNotificationConfigurationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_notifications.types.next_token
    import capo_notifications.types.notification_configurations


class ListNotificationConfigurationsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_notifications.types.next_token.NextToken"]
    """<p>A pagination token. If a non-null pagination token is returned in a result, pass its value in another request to retrieve more entries.</p>"""
    notification_configurations: "capo_notifications.types.notification_configurations.NotificationConfigurations"
    """<p>The <code>NotificationConfigurations</code> in the account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListNotificationConfigurationsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_notifications.types.notification_configurations

    out["notificationConfigurations"] = (
        capo_notifications.types.notification_configurations.serialize_json(
            value["notification_configurations"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListNotificationConfigurationsResponse:
    out: ListNotificationConfigurationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("notificationConfigurations") is not None:
        import capo_notifications.types.notification_configurations

        out["notification_configurations"] = (
            capo_notifications.types.notification_configurations.deserialize_json(
                data["notificationConfigurations"]
            )
        )
    else:
        out["notification_configurations"] = []
    return out
