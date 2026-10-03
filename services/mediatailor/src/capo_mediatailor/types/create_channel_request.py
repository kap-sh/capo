"""Generated from Smithy shape ``com.amazonaws.mediatailor#CreateChannelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_mediatailor.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mediatailor.types.__map_of__string
    import capo_mediatailor.types.__string
    import capo_mediatailor.types.audiences
    import capo_mediatailor.types.playback_mode
    import capo_mediatailor.types.request_outputs
    import capo_mediatailor.types.slate_source
    import capo_mediatailor.types.tier
    import capo_mediatailor.types.time_shift_configuration


class CreateChannelRequest(TypedDict, closed=True):
    channel_name: "capo_mediatailor.types.__string.__string"
    """<p>The name of the channel.</p>"""
    filler_slate: NotRequired["capo_mediatailor.types.slate_source.SlateSource"]
    """<p>The slate used to fill gaps between programs in the schedule. You must configure filler slate if your channel uses the <code>LINEAR</code> <code>PlaybackMode</code>. MediaTailor doesn't support filler slate for channels using the <code>LOOP</code> <code>PlaybackMode</code>.</p>"""
    outputs: "capo_mediatailor.types.request_outputs.RequestOutputs"
    """<p>The channel's output properties.</p>"""
    playback_mode: "capo_mediatailor.types.playback_mode.PlaybackMode"
    """<p>The type of playback mode to use for this channel.</p> <p> <code>LINEAR</code> - The programs in the schedule play once back-to-back in the schedule.</p> <p> <code>LOOP</code> - The programs in the schedule play back-to-back in an endless loop. When the last program in the schedule stops playing, playback loops back to the first program in the schedule.</p>"""
    tags: NotRequired["capo_mediatailor.types.__map_of__string.__mapOf__string"]
    """<p>The tags to assign to the channel. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html">Tagging AWS Elemental MediaTailor Resources</a>.</p>"""
    tier: NotRequired["capo_mediatailor.types.tier.Tier"]
    """<p>The tier of the channel.</p>"""
    time_shift_configuration: NotRequired[
        "capo_mediatailor.types.time_shift_configuration.TimeShiftConfiguration"
    ]
    """<p> The time-shifted viewing configuration you want to associate to the channel. </p>"""
    audiences: NotRequired["capo_mediatailor.types.audiences.Audiences"]
    """<p>The list of audiences defined in channel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateChannelRequest) -> dict:
    out: dict = {}
    if "filler_slate" in value:
        import capo_mediatailor.types.slate_source

        out["FillerSlate"] = capo_mediatailor.types.slate_source.serialize_json(
            value["filler_slate"]
        )
    import capo_mediatailor.types.request_outputs

    out["Outputs"] = capo_mediatailor.types.request_outputs.serialize_json(
        value["outputs"]
    )
    import capo_mediatailor.types.playback_mode

    out["PlaybackMode"] = capo_mediatailor.types.playback_mode.serialize_json(
        value["playback_mode"]
    )
    if "tags" in value:
        import capo_mediatailor.types.__map_of__string

        out["tags"] = capo_mediatailor.types.__map_of__string.serialize_json(
            value["tags"]
        )
    if "tier" in value:
        import capo_mediatailor.types.tier

        out["Tier"] = capo_mediatailor.types.tier.serialize_json(value["tier"])
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


def deserialize_json(data: dict) -> CreateChannelRequest:
    out: CreateChannelRequest = {}  # type: ignore[typeddict-item]
    if data.get("FillerSlate") is not None:
        import capo_mediatailor.types.slate_source

        out["filler_slate"] = capo_mediatailor.types.slate_source.deserialize_json(
            data["FillerSlate"]
        )
    if data.get("Outputs") is not None:
        import capo_mediatailor.types.request_outputs

        out["outputs"] = capo_mediatailor.types.request_outputs.deserialize_json(
            data["Outputs"]
        )
    else:
        raise DeserializationError("CreateChannelRequest.outputs required")
    if data.get("PlaybackMode") is not None:
        import capo_mediatailor.types.playback_mode

        out["playback_mode"] = capo_mediatailor.types.playback_mode.deserialize_json(
            data["PlaybackMode"]
        )
    else:
        raise DeserializationError("CreateChannelRequest.playback_mode required")
    if data.get("tags") is not None:
        import capo_mediatailor.types.__map_of__string

        out["tags"] = capo_mediatailor.types.__map_of__string.deserialize_json(
            data["tags"]
        )
    if data.get("Tier") is not None:
        import capo_mediatailor.types.tier

        out["tier"] = capo_mediatailor.types.tier.deserialize_json(data["Tier"])
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
