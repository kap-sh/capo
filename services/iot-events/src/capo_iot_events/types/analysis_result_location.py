"""Generated from Smithy shape ``com.amazonaws.iotevents#AnalysisResultLocation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_events.types.analysis_result_location_path


class AnalysisResultLocation(TypedDict, closed=True):
    path: NotRequired[
        "capo_iot_events.types.analysis_result_location_path.AnalysisResultLocationPath"
    ]
    """<p>A <a href="https://github.com/json-path/JsonPath">JsonPath</a> expression that identifies the error field in your detector model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnalysisResultLocation) -> dict:
    out: dict = {}
    if "path" in value:
        out["path"] = value["path"]
    return out


def deserialize_json(data: dict) -> AnalysisResultLocation:
    out: AnalysisResultLocation = {}  # type: ignore[typeddict-item]
    if data.get("path") is not None:
        out["path"] = data["path"]
    return out
