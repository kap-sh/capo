"""Generated from Smithy shape ``com.amazonaws.ivs#GetChannelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ivs.types.channel_arn


class GetChannelRequest(TypedDict, closed=True):
    arn: "capo_ivs.types.channel_arn.ChannelArn"
    """<p>ARN of the channel for which the configuration is to be retrieved.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetChannelRequest) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> GetChannelRequest:
    out: GetChannelRequest = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    return out
