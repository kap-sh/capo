"""Generated from Smithy shape ``com.amazonaws.inspector2#StringFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.string_comparison
    import capo_inspector2.types.string_input


class StringFilter(TypedDict, closed=True):
    comparison: "capo_inspector2.types.string_comparison.StringComparison"
    """<p>The operator to use when comparing values in the filter.</p>"""
    value: "capo_inspector2.types.string_input.StringInput"
    """<p>The value to filter on.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StringFilter) -> dict:
    out: dict = {}
    out["comparison"] = value["comparison"]
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> StringFilter:
    out: StringFilter = {}  # type: ignore[typeddict-item]
    if data.get("comparison") is not None:
        out["comparison"] = data["comparison"]
    else:
        out["comparison"] = ""
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        out["value"] = ""
    return out
