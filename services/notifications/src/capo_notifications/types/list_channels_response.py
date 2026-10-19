"""Generated from Smithy shape ``com.amazonaws.notifications#ListChannelsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_notifications.types.channels
    import capo_notifications.types.next_token


class ListChannelsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_notifications.types.next_token.NextToken"]
    """<p>A pagination token. If a non-null pagination token is returned in a result, pass its value in another request to retrieve more entries.</p>"""
    channels: "capo_notifications.types.channels.Channels"
    """<p>A list of Channels.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListChannelsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_notifications.types.channels

    out["channels"] = capo_notifications.types.channels.serialize_json(
        value["channels"]
    )
    return out


def deserialize_json(data: dict) -> ListChannelsResponse:
    out: ListChannelsResponse = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("channels") is not None:
        import capo_notifications.types.channels

        out["channels"] = capo_notifications.types.channels.deserialize_json(
            data["channels"]
        )
    else:
        out["channels"] = []
    return out
