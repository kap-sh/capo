"""Generated from Smithy shape ``com.amazonaws.repostspace#ListChannelsOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_repostspace.errors import DeserializationError

if TYPE_CHECKING:
    import capo_repostspace.types.channels_list


class ListChannelsOutput(TypedDict, closed=True):
    channels: "capo_repostspace.types.channels_list.ChannelsList"
    """<p>An array of structures that contain some information about the channels in the private re:Post.</p>"""
    next_token: NotRequired["str"]
    """<p>The token that you use when you request the next set of channels.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListChannelsOutput) -> dict:
    out: dict = {}
    import capo_repostspace.types.channels_list

    out["channels"] = capo_repostspace.types.channels_list.serialize_json(
        value["channels"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListChannelsOutput:
    out: ListChannelsOutput = {}  # type: ignore[typeddict-item]
    if data.get("channels") is not None:
        import capo_repostspace.types.channels_list

        out["channels"] = capo_repostspace.types.channels_list.deserialize_json(
            data["channels"]
        )
    else:
        raise DeserializationError("ListChannelsOutput.channels required")
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: ListChannelsOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "channels" in value:
        import capo_repostspace.types.channels_list

        out["channels"] = capo_repostspace.types.channels_list.redact_sensitive(
            value["channels"]
        )
    return out
