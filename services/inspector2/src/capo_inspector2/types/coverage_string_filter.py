"""Generated from Smithy shape ``com.amazonaws.inspector2#CoverageStringFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.coverage_string_comparison
    import capo_inspector2.types.coverage_string_input


class CoverageStringFilter(TypedDict, closed=True):
    comparison: (
        "capo_inspector2.types.coverage_string_comparison.CoverageStringComparison"
    )
    """<p>The operator to compare strings on.</p>"""
    value: "capo_inspector2.types.coverage_string_input.CoverageStringInput"
    """<p>The value to compare strings on.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CoverageStringFilter) -> dict:
    out: dict = {}
    out["comparison"] = value["comparison"]
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> CoverageStringFilter:
    out: CoverageStringFilter = {}  # type: ignore[typeddict-item]
    if data.get("comparison") is not None:
        out["comparison"] = data["comparison"]
    else:
        out["comparison"] = ""
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        out["value"] = ""
    return out
