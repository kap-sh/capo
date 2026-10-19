"""Generated from Smithy shape ``com.amazonaws.notifications#ListManagedNotificationConfigurationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_notifications.types.managed_notification_configurations
    import capo_notifications.types.next_token


class ListManagedNotificationConfigurationsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_notifications.types.next_token.NextToken"]
    """<p>A pagination token. If a non-null pagination token is returned in a result, pass its value in another request to retrieve more entries.</p>"""
    managed_notification_configurations: "capo_notifications.types.managed_notification_configurations.ManagedNotificationConfigurations"
    """<p>A list of Managed Notification Configurations matching the request criteria.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListManagedNotificationConfigurationsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_notifications.types.managed_notification_configurations

    out["managedNotificationConfigurations"] = (
        capo_notifications.types.managed_notification_configurations.serialize_json(
            value["managed_notification_configurations"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListManagedNotificationConfigurationsResponse:
    out: ListManagedNotificationConfigurationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("managedNotificationConfigurations") is not None:
        import capo_notifications.types.managed_notification_configurations

        out["managed_notification_configurations"] = (
            capo_notifications.types.managed_notification_configurations.deserialize_json(
                data["managedNotificationConfigurations"]
            )
        )
    else:
        out["managed_notification_configurations"] = []
    return out
