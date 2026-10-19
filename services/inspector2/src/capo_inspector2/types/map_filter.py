"""Generated from Smithy shape ``com.amazonaws.inspector2#MapFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.map_comparison
    import capo_inspector2.types.map_key
    import capo_inspector2.types.map_value


class MapFilter(TypedDict, closed=True):
    comparison: "capo_inspector2.types.map_comparison.MapComparison"
    """<p>The operator to use when comparing values in the filter.</p>"""
    key: "capo_inspector2.types.map_key.MapKey"
    """<p>The tag key used in the filter.</p>"""
    value: NotRequired["capo_inspector2.types.map_value.MapValue"]
    """<p>The tag value used in the filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MapFilter) -> dict:
    out: dict = {}
    out["comparison"] = value["comparison"]
    out["key"] = value["key"]
    if "value" in value:
        out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> MapFilter:
    out: MapFilter = {}  # type: ignore[typeddict-item]
    if data.get("comparison") is not None:
        out["comparison"] = data["comparison"]
    else:
        out["comparison"] = ""
    if data.get("key") is not None:
        out["key"] = data["key"]
    else:
        out["key"] = ""
    if data.get("value") is not None:
        out["value"] = data["value"]
    return out
