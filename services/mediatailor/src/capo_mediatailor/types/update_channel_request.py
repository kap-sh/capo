"""Generated from Smithy shape ``com.amazonaws.mediatailor#UpdateChannelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediatailor.types.__string
    import capo_mediatailor.types.audiences
    import capo_mediatailor.types.request_outputs
    import capo_mediatailor.types.slate_source
    import capo_mediatailor.types.time_shift_configuration


class UpdateChannelRequest(TypedDict, closed=True):
    channel_name: "capo_mediatailor.types.__string.__string"
    """<p>The name of the channel.</p>"""
    filler_slate: NotRequired["capo_mediatailor.types.slate_source.SlateSource"]
    """<p>The slate used to fill gaps between programs in the schedule. You must configure filler slate if your channel uses the <code>LINEAR</code> <code>PlaybackMode</code>. MediaTailor doesn't support filler slate for channels using the <code>LOOP</code> <code>PlaybackMode</code>.</p>"""
    outputs: "capo_mediatailor.types.request_outputs.RequestOutputs"
    """<p>The channel's output properties.</p>"""
    time_shift_configuration: NotRequired[
        "capo_mediatailor.types.time_shift_configuration.TimeShiftConfiguration"
    ]
    """<p> The time-shifted viewing configuration you want to associate to the channel. </p>"""
    audiences: NotRequired["capo_mediatailor.types.audiences.Audiences"]
    """<p>The list of audiences defined in channel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateChannelRequest) -> dict:
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


def deserialize_json(data: dict) -> UpdateChannelRequest:
    out: UpdateChannelRequest = {}  # type: ignore[typeddict-item]
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
        out["outputs"] = []
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
