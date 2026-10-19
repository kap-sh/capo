"""Generated from Smithy shape ``com.amazonaws.inspector2#CoverageMapFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.coverage_map_comparison
    import capo_inspector2.types.non_empty_string


class CoverageMapFilter(TypedDict, closed=True):
    comparison: "capo_inspector2.types.coverage_map_comparison.CoverageMapComparison"
    """<p>The operator to compare coverage on.</p>"""
    key: "capo_inspector2.types.non_empty_string.NonEmptyString"
    """<p>The tag key associated with the coverage map filter.</p>"""
    value: NotRequired["capo_inspector2.types.non_empty_string.NonEmptyString"]
    """<p>The tag value associated with the coverage map filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CoverageMapFilter) -> dict:
    out: dict = {}
    out["comparison"] = value["comparison"]
    out["key"] = value["key"]
    if "value" in value:
        out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> CoverageMapFilter:
    out: CoverageMapFilter = {}  # type: ignore[typeddict-item]
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
