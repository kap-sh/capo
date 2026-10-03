"""Generated from Smithy shape ``com.amazonaws.geoplaces#OpeningHoursComponents``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_places.types.sensitive_string


class OpeningHoursComponents(TypedDict, closed=True):
    open_time: NotRequired["capo_geo_places.types.sensitive_string.SensitiveString"]
    """<p>String which represents the opening hours, such as <code>"T070000"</code>.</p>"""
    open_duration: NotRequired["capo_geo_places.types.sensitive_string.SensitiveString"]
    """<p>String which represents the duration of the opening period, such as <code>"PT12H00M"</code>.</p>"""
    recurrence: NotRequired["capo_geo_places.types.sensitive_string.SensitiveString"]
    """<p>Days or periods when the provided opening hours are in affect. </p> <p>Example: <code>FREQ:DAILY;BYDAY:MO,TU,WE,TH,SU</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OpeningHoursComponents) -> dict:
    out: dict = {}
    if "open_time" in value:
        out["OpenTime"] = value["open_time"]
    if "open_duration" in value:
        out["OpenDuration"] = value["open_duration"]
    if "recurrence" in value:
        out["Recurrence"] = value["recurrence"]
    return out


def deserialize_json(data: dict) -> OpeningHoursComponents:
    out: OpeningHoursComponents = {}  # type: ignore[typeddict-item]
    if data.get("OpenTime") is not None:
        out["open_time"] = data["OpenTime"]
    if data.get("OpenDuration") is not None:
        out["open_duration"] = data["OpenDuration"]
    if data.get("Recurrence") is not None:
        out["recurrence"] = data["Recurrence"]
    return out
