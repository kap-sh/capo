"""Generated from Smithy shape ``com.amazonaws.inspector2#ResourceMapFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.non_empty_string
    import capo_inspector2.types.resource_map_comparison


class ResourceMapFilter(TypedDict, closed=True):
    comparison: "capo_inspector2.types.resource_map_comparison.ResourceMapComparison"
    """<p>The filter's comparison.</p>"""
    key: "capo_inspector2.types.non_empty_string.NonEmptyString"
    """<p>The filter's key.</p>"""
    value: NotRequired["capo_inspector2.types.non_empty_string.NonEmptyString"]
    """<p>The filter's value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceMapFilter) -> dict:
    out: dict = {}
    out["comparison"] = value["comparison"]
    out["key"] = value["key"]
    if "value" in value:
        out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> ResourceMapFilter:
    out: ResourceMapFilter = {}  # type: ignore[typeddict-item]
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
