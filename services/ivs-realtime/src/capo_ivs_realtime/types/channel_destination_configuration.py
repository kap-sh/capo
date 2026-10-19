"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#ChannelDestinationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ivs_realtime.types.channel_arn
    import capo_ivs_realtime.types.encoder_configuration_arn


class ChannelDestinationConfiguration(TypedDict, closed=True):
    channel_arn: "capo_ivs_realtime.types.channel_arn.ChannelArn"
    """<p>ARN of the channel to use for broadcasting. The channel and stage resources must be in the same AWS account and region. The channel must be offline (not broadcasting).</p>"""
    encoder_configuration_arn: NotRequired[
        "capo_ivs_realtime.types.encoder_configuration_arn.EncoderConfigurationArn"
    ]
    """<p>ARN of the <a>EncoderConfiguration</a> resource. The encoder configuration and stage resources must be in the same AWS account and region.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChannelDestinationConfiguration) -> dict:
    out: dict = {}
    out["channelArn"] = value["channel_arn"]
    if "encoder_configuration_arn" in value:
        out["encoderConfigurationArn"] = value["encoder_configuration_arn"]
    return out


def deserialize_json(data: dict) -> ChannelDestinationConfiguration:
    out: ChannelDestinationConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("channelArn") is not None:
        out["channel_arn"] = data["channelArn"]
    else:
        out["channel_arn"] = ""
    if data.get("encoderConfigurationArn") is not None:
        out["encoder_configuration_arn"] = data["encoderConfigurationArn"]
    return out
