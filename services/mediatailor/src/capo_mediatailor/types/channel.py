"""Generated from Smithy shape ``com.amazonaws.mediatailor#Channel``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_mediatailor.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mediatailor.types.__map_of__string
    import capo_mediatailor.types.__string
    import capo_mediatailor.types.__timestamp_unix
    import capo_mediatailor.types.audiences
    import capo_mediatailor.types.log_configuration_for_channel
    import capo_mediatailor.types.response_outputs
    import capo_mediatailor.types.slate_source


class Channel(TypedDict, closed=True):
    arn: "capo_mediatailor.types.__string.__string"
    """<p>The ARN of the channel.</p>"""
    channel_name: "capo_mediatailor.types.__string.__string"
    """<p>The name of the channel.</p>"""
    channel_state: "capo_mediatailor.types.__string.__string"
    """<p>Returns the state whether the channel is running or not.</p>"""
    creation_time: NotRequired[
        "capo_mediatailor.types.__timestamp_unix.__timestampUnix"
    ]
    """<p>The timestamp of when the channel was created.</p>"""
    filler_slate: NotRequired["capo_mediatailor.types.slate_source.SlateSource"]
    """<p>The slate used to fill gaps between programs in the schedule. You must configure filler slate if your channel uses the <code>LINEAR</code> <code>PlaybackMode</code>. MediaTailor doesn't support filler slate for channels using the <code>LOOP</code> <code>PlaybackMode</code>.</p>"""
    last_modified_time: NotRequired[
        "capo_mediatailor.types.__timestamp_unix.__timestampUnix"
    ]
    """<p>The timestamp of when the channel was last modified.</p>"""
    outputs: "capo_mediatailor.types.response_outputs.ResponseOutputs"
    """<p>The channel's output properties.</p>"""
    playback_mode: "capo_mediatailor.types.__string.__string"
    """<p>The type of playback mode for this channel.</p> <p> <code>LINEAR</code> - Programs play back-to-back only once.</p> <p> <code>LOOP</code> - Programs play back-to-back in an endless loop. When the last program in the schedule plays, playback loops back to the first program in the schedule.</p>"""
    tags: NotRequired["capo_mediatailor.types.__map_of__string.__mapOf__string"]
    """<p>The tags to assign to the channel. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html">Tagging AWS Elemental MediaTailor Resources</a>.</p>"""
    tier: "capo_mediatailor.types.__string.__string"
    """<p>The tier for this channel. STANDARD tier channels can contain live programs.</p>"""
    log_configuration: "capo_mediatailor.types.log_configuration_for_channel.LogConfigurationForChannel"
    """<p>The log configuration.</p>"""
    audiences: NotRequired["capo_mediatailor.types.audiences.Audiences"]
    """<p>The list of audiences defined in channel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Channel) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    out["ChannelName"] = value["channel_name"]
    out["ChannelState"] = value["channel_state"]
    if "creation_time" in value:
        import capo_mediatailor.types.__timestamp_unix

        out["CreationTime"] = capo_mediatailor.types.__timestamp_unix.serialize_json(
            value["creation_time"]
        )
    if "filler_slate" in value:
        import capo_mediatailor.types.slate_source

        out["FillerSlate"] = capo_mediatailor.types.slate_source.serialize_json(
            value["filler_slate"]
        )
    if "last_modified_time" in value:
        import capo_mediatailor.types.__timestamp_unix

        out["LastModifiedTime"] = (
            capo_mediatailor.types.__timestamp_unix.serialize_json(
                value["last_modified_time"]
            )
        )
    import capo_mediatailor.types.response_outputs

    out["Outputs"] = capo_mediatailor.types.response_outputs.serialize_json(
        value["outputs"]
    )
    out["PlaybackMode"] = value["playback_mode"]
    if "tags" in value:
        import capo_mediatailor.types.__map_of__string

        out["tags"] = capo_mediatailor.types.__map_of__string.serialize_json(
            value["tags"]
        )
    out["Tier"] = value["tier"]
    import capo_mediatailor.types.log_configuration_for_channel

    out["LogConfiguration"] = (
        capo_mediatailor.types.log_configuration_for_channel.serialize_json(
            value["log_configuration"]
        )
    )
    if "audiences" in value:
        import capo_mediatailor.types.audiences

        out["Audiences"] = capo_mediatailor.types.audiences.serialize_json(
            value["audiences"]
        )
    return out


def deserialize_json(data: dict) -> Channel:
    out: Channel = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("Channel.arn required")
    if data.get("ChannelName") is not None:
        out["channel_name"] = data["ChannelName"]
    else:
        raise DeserializationError("Channel.channel_name required")
    if data.get("ChannelState") is not None:
        out["channel_state"] = data["ChannelState"]
    else:
        raise DeserializationError("Channel.channel_state required")
    if data.get("CreationTime") is not None:
        import capo_mediatailor.types.__timestamp_unix

        out["creation_time"] = capo_mediatailor.types.__timestamp_unix.deserialize_json(
            data["CreationTime"]
        )
    if data.get("FillerSlate") is not None:
        import capo_mediatailor.types.slate_source

        out["filler_slate"] = capo_mediatailor.types.slate_source.deserialize_json(
            data["FillerSlate"]
        )
    if data.get("LastModifiedTime") is not None:
        import capo_mediatailor.types.__timestamp_unix

        out["last_modified_time"] = (
            capo_mediatailor.types.__timestamp_unix.deserialize_json(
                data["LastModifiedTime"]
            )
        )
    if data.get("Outputs") is not None:
        import capo_mediatailor.types.response_outputs

        out["outputs"] = capo_mediatailor.types.response_outputs.deserialize_json(
            data["Outputs"]
        )
    else:
        raise DeserializationError("Channel.outputs required")
    if data.get("PlaybackMode") is not None:
        out["playback_mode"] = data["PlaybackMode"]
    else:
        raise DeserializationError("Channel.playback_mode required")
    if data.get("tags") is not None:
        import capo_mediatailor.types.__map_of__string

        out["tags"] = capo_mediatailor.types.__map_of__string.deserialize_json(
            data["tags"]
        )
    if data.get("Tier") is not None:
        out["tier"] = data["Tier"]
    else:
        raise DeserializationError("Channel.tier required")
    if data.get("LogConfiguration") is not None:
        import capo_mediatailor.types.log_configuration_for_channel

        out["log_configuration"] = (
            capo_mediatailor.types.log_configuration_for_channel.deserialize_json(
                data["LogConfiguration"]
            )
        )
    else:
        raise DeserializationError("Channel.log_configuration required")
    if data.get("Audiences") is not None:
        import capo_mediatailor.types.audiences

        out["audiences"] = capo_mediatailor.types.audiences.deserialize_json(
            data["Audiences"]
        )
    return out
