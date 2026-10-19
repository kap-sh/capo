"""Generated from Smithy shape ``com.amazonaws.ivs#BatchGetChannelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ivs.types.channel_arn_list


class BatchGetChannelRequest(TypedDict, closed=True):
    arns: "capo_ivs.types.channel_arn_list.ChannelArnList"
    """<p>Array of ARNs, one per channel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetChannelRequest) -> dict:
    out: dict = {}
    import capo_ivs.types.channel_arn_list

    out["arns"] = capo_ivs.types.channel_arn_list.serialize_json(value["arns"])
    return out


def deserialize_json(data: dict) -> BatchGetChannelRequest:
    out: BatchGetChannelRequest = {}  # type: ignore[typeddict-item]
    if data.get("arns") is not None:
        import capo_ivs.types.channel_arn_list

        out["arns"] = capo_ivs.types.channel_arn_list.deserialize_json(data["arns"])
    else:
        out["arns"] = []
    return out
