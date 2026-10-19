"""Generated from Smithy shape ``com.amazonaws.inspector2#ResourceStringFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.resource_string_comparison
    import capo_inspector2.types.resource_string_input


class ResourceStringFilter(TypedDict, closed=True):
    comparison: (
        "capo_inspector2.types.resource_string_comparison.ResourceStringComparison"
    )
    """<p>The filter's comparison.</p>"""
    value: "capo_inspector2.types.resource_string_input.ResourceStringInput"
    """<p>The filter's value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceStringFilter) -> dict:
    out: dict = {}
    out["comparison"] = value["comparison"]
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> ResourceStringFilter:
    out: ResourceStringFilter = {}  # type: ignore[typeddict-item]
    if data.get("comparison") is not None:
        out["comparison"] = data["comparison"]
    else:
        out["comparison"] = ""
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        out["value"] = ""
    return out
