"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#StreamChannelDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.channel_definitions
    import capo_chime_sdk_media_pipelines.types.number_of_channels


class StreamChannelDefinition(TypedDict, closed=True):
    number_of_channels: (
        "capo_chime_sdk_media_pipelines.types.number_of_channels.NumberOfChannels"
    )
    """<p>The number of channels in a streaming channel.</p>"""
    channel_definitions: NotRequired[
        "capo_chime_sdk_media_pipelines.types.channel_definitions.ChannelDefinitions"
    ]
    """<p>The definitions of the channels in a streaming channel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StreamChannelDefinition) -> dict:
    out: dict = {}
    out["NumberOfChannels"] = value["number_of_channels"]
    if "channel_definitions" in value:
        import capo_chime_sdk_media_pipelines.types.channel_definitions

        out["ChannelDefinitions"] = (
            capo_chime_sdk_media_pipelines.types.channel_definitions.serialize_json(
                value["channel_definitions"]
            )
        )
    return out


def deserialize_json(data: dict) -> StreamChannelDefinition:
    out: StreamChannelDefinition = {}  # type: ignore[typeddict-item]
    if data.get("NumberOfChannels") is not None:
        out["number_of_channels"] = data["NumberOfChannels"]
    else:
        out["number_of_channels"] = 0
    if data.get("ChannelDefinitions") is not None:
        import capo_chime_sdk_media_pipelines.types.channel_definitions

        out["channel_definitions"] = (
            capo_chime_sdk_media_pipelines.types.channel_definitions.deserialize_json(
                data["ChannelDefinitions"]
            )
        )
    return out
