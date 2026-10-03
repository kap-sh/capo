"""Generated from Smithy shape ``com.amazonaws.medialive#TimecodeConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__integer_min1_max1000000
    import capo_medialive.types.timecode_config_source


class TimecodeConfig(TypedDict, closed=True):
    source: NotRequired[
        "capo_medialive.types.timecode_config_source.TimecodeConfigSource"
    ]
    """Identifies the source for the timecode that will be associated with the events outputs. -Embedded (embedded): Initialize the output timecode with timecode from the the source. If no embedded timecode is detected in the source, the system falls back to using "Start at 0" (zerobased). -System Clock (systemclock): Use the UTC time. -Start at 0 (zerobased): The time of the first frame of the event will be 00:00:00:00."""
    sync_threshold: NotRequired[
        "capo_medialive.types.__integer_min1_max1000000.__integerMin1Max1000000"
    ]
    """Threshold in frames beyond which output timecode is resynchronized to the input timecode. Discrepancies below this threshold are permitted to avoid unnecessary discontinuities in the output timecode. No timecode sync when this is not specified."""


# --- restJson1 ser/de ---
def serialize_json(value: TimecodeConfig) -> dict:
    out: dict = {}
    if "source" in value:
        import capo_medialive.types.timecode_config_source

        out["source"] = capo_medialive.types.timecode_config_source.serialize_json(
            value["source"]
        )
    if "sync_threshold" in value:
        out["syncThreshold"] = value["sync_threshold"]
    return out


def deserialize_json(data: dict) -> TimecodeConfig:
    out: TimecodeConfig = {}  # type: ignore[typeddict-item]
    if data.get("source") is not None:
        import capo_medialive.types.timecode_config_source

        out["source"] = capo_medialive.types.timecode_config_source.deserialize_json(
            data["source"]
        )
    if data.get("syncThreshold") is not None:
        out["sync_threshold"] = data["syncThreshold"]
    return out
