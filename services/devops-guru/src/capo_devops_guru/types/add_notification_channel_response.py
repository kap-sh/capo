"""Generated from Smithy shape ``com.amazonaws.devopsguru#AddNotificationChannelResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_devops_guru.types.notification_channel_id


class AddNotificationChannelResponse(TypedDict, closed=True):
    id: "capo_devops_guru.types.notification_channel_id.NotificationChannelId"
    """<p> The ID of the added notification channel. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AddNotificationChannelResponse) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    return out


def deserialize_json(data: dict) -> AddNotificationChannelResponse:
    out: AddNotificationChannelResponse = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = ""
    return out
