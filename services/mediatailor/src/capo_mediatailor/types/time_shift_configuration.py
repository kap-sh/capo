"""Generated from Smithy shape ``com.amazonaws.mediatailor#TimeShiftConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mediatailor.types.__integer


class TimeShiftConfiguration(TypedDict, closed=True):
    max_time_delay_seconds: "capo_mediatailor.types.__integer.__integer"
    """<p> The maximum time delay for time-shifted viewing. The minimum allowed maximum time delay is 0 seconds, and the maximum allowed maximum time delay is 21600 seconds (6 hours). </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TimeShiftConfiguration) -> dict:
    out: dict = {}
    out["MaxTimeDelaySeconds"] = value["max_time_delay_seconds"]
    return out


def deserialize_json(data: dict) -> TimeShiftConfiguration:
    out: TimeShiftConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("MaxTimeDelaySeconds") is not None:
        out["max_time_delay_seconds"] = data["MaxTimeDelaySeconds"]
    else:
        out["max_time_delay_seconds"] = 0
    return out
