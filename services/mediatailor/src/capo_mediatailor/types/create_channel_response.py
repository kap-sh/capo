"""Generated from Smithy shape ``com.amazonaws.mediatailor#CreateChannelResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediatailor.types.__map_of__string
    import capo_mediatailor.types.__string
    import capo_mediatailor.types.__timestamp_unix
    import capo_mediatailor.types.audiences
    import capo_mediatailor.types.channel_state
    import capo_mediatailor.types.response_outputs
    import capo_mediatailor.types.slate_source
    import capo_mediatailor.types.time_shift_configuration


class CreateChannelResponse(TypedDict, closed=True):
    arn: NotRequired["capo_mediatailor.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) to assign to the channel.</p>"""
    channel_name: NotRequired["capo_mediatailor.types.__string.__string"]
    """<p>The name to assign to the channel.</p>"""
    channel_state: NotRequired["capo_mediatailor.types.channel_state.ChannelState"]
    """<p>Indicates whether the channel is in a running state or not.</p>"""
    creation_time: NotRequired[
        "capo_mediatailor.types.__timestamp_unix.__timestampUnix"
    ]
    """<p>The timestamp of when the channel was created.</p>"""
    filler_slate: NotRequired["capo_mediatailor.types.slate_source.SlateSource"]
    """<p>Contains information about the slate used to fill gaps between programs in the schedule.</p>"""
    last_modified_time: NotRequired[
        "capo_mediatailor.types.__timestamp_unix.__timestampUnix"
    ]
    """<p>The timestamp of when the channel was last modified.</p>"""
    outputs: NotRequired["capo_mediatailor.types.response_outputs.ResponseOutputs"]
    """<p>The output properties to assign to the channel.</p>"""
    playback_mode: NotRequired["capo_mediatailor.types.__string.__string"]
    """<p>The playback mode to assign to the channel.</p>"""
    tags: NotRequired["capo_mediatailor.types.__map_of__string.__mapOf__string"]
    """<p>The tags to assign to the channel. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html">Tagging AWS Elemental MediaTailor Resources</a>.</p>"""
    tier: NotRequired["capo_mediatailor.types.__string.__string"]
    """<p>The tier of the channel.</p>"""
    time_shift_configuration: NotRequired[
        "capo_mediatailor.types.time_shift_configuration.TimeShiftConfiguration"
    ]
    """<p> The time-shifted viewing configuration assigned to the channel. </p>"""
    audiences: NotRequired["capo_mediatailor.types.audiences.Audiences"]
    """<p>The list of audiences defined in channel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateChannelResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "channel_name" in value:
        out["ChannelName"] = value["channel_name"]
    if "channel_state" in value:
        import capo_mediatailor.types.channel_state

        out["ChannelState"] = capo_mediatailor.types.channel_state.serialize_json(
            value["channel_state"]
        )
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
    if "outputs" in value:
        import capo_mediatailor.types.response_outputs

        out["Outputs"] = capo_mediatailor.types.response_outputs.serialize_json(
            value["outputs"]
        )
    if "playback_mode" in value:
        out["PlaybackMode"] = value["playback_mode"]
    if "tags" in value:
        import capo_mediatailor.types.__map_of__string

        out["tags"] = capo_mediatailor.types.__map_of__string.serialize_json(
            value["tags"]
        )
    if "tier" in value:
        out["Tier"] = value["tier"]
    if "time_shift_configuration" in value:
        import capo_mediatailor.types.time_shift_configuration

        out["TimeShiftConfiguration"] = (
            capo_mediatailor.types.time_shift_configuration.serialize_json(
                value["time_shift_configuration"]
            )
        )
    if "audiences" in value:
        import capo_mediatailor.types.audiences

        out["Audiences"] = capo_mediatailor.types.audiences.serialize_json(
            value["audiences"]
        )
    return out


def deserialize_json(data: dict) -> CreateChannelResponse:
    out: CreateChannelResponse = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("ChannelName") is not None:
        out["channel_name"] = data["ChannelName"]
    if data.get("ChannelState") is not None:
        import capo_mediatailor.types.channel_state

        out["channel_state"] = capo_mediatailor.types.channel_state.deserialize_json(
            data["ChannelState"]
        )
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
    if data.get("PlaybackMode") is not None:
        out["playback_mode"] = data["PlaybackMode"]
    if data.get("tags") is not None:
        import capo_mediatailor.types.__map_of__string

        out["tags"] = capo_mediatailor.types.__map_of__string.deserialize_json(
            data["tags"]
        )
    if data.get("Tier") is not None:
        out["tier"] = data["Tier"]
    if data.get("TimeShiftConfiguration") is not None:
        import capo_mediatailor.types.time_shift_configuration

        out["time_shift_configuration"] = (
            capo_mediatailor.types.time_shift_configuration.deserialize_json(
                data["TimeShiftConfiguration"]
            )
        )
    if data.get("Audiences") is not None:
        import capo_mediatailor.types.audiences

        out["audiences"] = capo_mediatailor.types.audiences.deserialize_json(
            data["Audiences"]
        )
    return out
