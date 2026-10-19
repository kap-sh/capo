"""Generated from Smithy shape ``com.amazonaws.kinesis#DeleteChannelInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kinesis.types.channel_arn


class DeleteChannelInput(TypedDict, closed=True):
    channel_arn: "capo_kinesis.types.channel_arn.ChannelARN"
    """<p>The Amazon Resource Name (ARN) of the channel to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteChannelInput) -> dict:
    out: dict = {}
    out["ChannelARN"] = value["channel_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteChannelInput:
    out: DeleteChannelInput = {}  # type: ignore[typeddict-item]
    if data.get("ChannelARN") is not None:
        out["channel_arn"] = data["ChannelARN"]
    else:
        out["channel_arn"] = ""
    return out
