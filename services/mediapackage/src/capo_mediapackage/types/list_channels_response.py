"""Generated from Smithy shape ``com.amazonaws.mediapackage#ListChannelsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediapackage.types.__list_of_channel
    import capo_mediapackage.types.__string


class ListChannelsResponse(TypedDict, closed=True):
    channels: NotRequired["capo_mediapackage.types.__list_of_channel.__listOfChannel"]
    """A list of Channel records."""
    next_token: NotRequired["capo_mediapackage.types.__string.__string"]
    """A token that can be used to resume pagination from the end of the collection."""


# --- restJson1 ser/de ---
def serialize_json(value: ListChannelsResponse) -> dict:
    out: dict = {}
    if "channels" in value:
        import capo_mediapackage.types.__list_of_channel

        out["channels"] = capo_mediapackage.types.__list_of_channel.serialize_json(
            value["channels"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListChannelsResponse:
    out: ListChannelsResponse = {}  # type: ignore[typeddict-item]
    if data.get("channels") is not None:
        import capo_mediapackage.types.__list_of_channel

        out["channels"] = capo_mediapackage.types.__list_of_channel.deserialize_json(
            data["channels"]
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: ListChannelsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "channels" in value:
        import capo_mediapackage.types.__list_of_channel

        out["channels"] = capo_mediapackage.types.__list_of_channel.redact_sensitive(
            value["channels"]
        )
    return out
