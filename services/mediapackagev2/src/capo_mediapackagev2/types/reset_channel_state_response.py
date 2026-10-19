"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#ResetChannelStateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import datetime


class ResetChannelStateResponse(TypedDict, closed=True):
    channel_group_name: "str"
    """<p>The name of the channel group that contains the channel that you just reset.</p>"""
    channel_name: "str"
    """<p>The name of the channel that you just reset.</p>"""
    arn: "str"
    """<p>The Amazon Resource Name (ARN) associated with the channel that you just reset.</p>"""
    reset_at: "datetime.datetime"
    """<p>The time that the channel was last reset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResetChannelStateResponse) -> dict:
    out: dict = {}
    out["ChannelGroupName"] = value["channel_group_name"]
    out["ChannelName"] = value["channel_name"]
    out["Arn"] = value["arn"]
    import capo_mediapackagev2.types._prelude.timestamp

    out["ResetAt"] = capo_mediapackagev2.types._prelude.timestamp.serialize_json(
        value["reset_at"]
    )
    return out


def deserialize_json(data: dict) -> ResetChannelStateResponse:
    out: ResetChannelStateResponse = {}  # type: ignore[typeddict-item]
    if data.get("ChannelGroupName") is not None:
        out["channel_group_name"] = data["ChannelGroupName"]
    else:
        out["channel_group_name"] = ""
    if data.get("ChannelName") is not None:
        out["channel_name"] = data["ChannelName"]
    else:
        out["channel_name"] = ""
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    if data.get("ResetAt") is not None:
        import capo_mediapackagev2.types._prelude.timestamp

        out["reset_at"] = capo_mediapackagev2.types._prelude.timestamp.deserialize_json(
            data["ResetAt"]
        )
    else:
        import datetime

        out["reset_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
