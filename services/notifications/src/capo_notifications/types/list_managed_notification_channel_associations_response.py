"""Generated from Smithy shape ``com.amazonaws.notifications#ListManagedNotificationChannelAssociationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_notifications.types.managed_notification_channel_associations
    import capo_notifications.types.next_token


class ListManagedNotificationChannelAssociationsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_notifications.types.next_token.NextToken"]
    """<p>A pagination token. If a non-null pagination token is returned in a result, pass its value in another request to retrieve more entries.</p>"""
    channel_associations: "capo_notifications.types.managed_notification_channel_associations.ManagedNotificationChannelAssociations"
    """<p>A list that contains the following information about a channel association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListManagedNotificationChannelAssociationsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_notifications.types.managed_notification_channel_associations

    out["channelAssociations"] = (
        capo_notifications.types.managed_notification_channel_associations.serialize_json(
            value["channel_associations"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListManagedNotificationChannelAssociationsResponse:
    out: ListManagedNotificationChannelAssociationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("channelAssociations") is not None:
        import capo_notifications.types.managed_notification_channel_associations

        out["channel_associations"] = (
            capo_notifications.types.managed_notification_channel_associations.deserialize_json(
                data["channelAssociations"]
            )
        )
    else:
        out["channel_associations"] = []
    return out
