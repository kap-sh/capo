"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#CreateSignalingChannelInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_video.types.channel_name
    import capo_kinesis_video.types.channel_type
    import capo_kinesis_video.types.single_master_configuration
    import capo_kinesis_video.types.tag_on_create_list


class CreateSignalingChannelInput(TypedDict, closed=True):
    channel_name: "capo_kinesis_video.types.channel_name.ChannelName"
    """<p>A name for the signaling channel that you are creating. It must be unique for each Amazon Web Services account and Amazon Web Services Region.</p>"""
    channel_type: NotRequired["capo_kinesis_video.types.channel_type.ChannelType"]
    """<p>A type of the signaling channel that you are creating. Currently, <code>SINGLE_MASTER</code> is the only supported channel type. </p>"""
    single_master_configuration: NotRequired[
        "capo_kinesis_video.types.single_master_configuration.SingleMasterConfiguration"
    ]
    """<p>A structure containing the configuration for the <code>SINGLE_MASTER</code> channel type. The default configuration for the channel message's time to live is 60 seconds (1 minute).</p>"""
    tags: NotRequired["capo_kinesis_video.types.tag_on_create_list.TagOnCreateList"]
    """<p>A set of tags (key-value pairs) that you want to associate with this channel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSignalingChannelInput) -> dict:
    out: dict = {}
    out["ChannelName"] = value["channel_name"]
    if "channel_type" in value:
        import capo_kinesis_video.types.channel_type

        out["ChannelType"] = capo_kinesis_video.types.channel_type.serialize_json(
            value["channel_type"]
        )
    if "single_master_configuration" in value:
        import capo_kinesis_video.types.single_master_configuration

        out["SingleMasterConfiguration"] = (
            capo_kinesis_video.types.single_master_configuration.serialize_json(
                value["single_master_configuration"]
            )
        )
    if "tags" in value:
        import capo_kinesis_video.types.tag_on_create_list

        out["Tags"] = capo_kinesis_video.types.tag_on_create_list.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateSignalingChannelInput:
    out: CreateSignalingChannelInput = {}  # type: ignore[typeddict-item]
    if data.get("ChannelName") is not None:
        out["channel_name"] = data["ChannelName"]
    else:
        out["channel_name"] = ""
    if data.get("ChannelType") is not None:
        import capo_kinesis_video.types.channel_type

        out["channel_type"] = capo_kinesis_video.types.channel_type.deserialize_json(
            data["ChannelType"]
        )
    if data.get("SingleMasterConfiguration") is not None:
        import capo_kinesis_video.types.single_master_configuration

        out["single_master_configuration"] = (
            capo_kinesis_video.types.single_master_configuration.deserialize_json(
                data["SingleMasterConfiguration"]
            )
        )
    if data.get("Tags") is not None:
        import capo_kinesis_video.types.tag_on_create_list

        out["tags"] = capo_kinesis_video.types.tag_on_create_list.deserialize_json(
            data["Tags"]
        )
    return out
