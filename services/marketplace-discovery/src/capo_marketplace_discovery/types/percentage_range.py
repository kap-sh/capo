"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#PercentageRange``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.bounded_string


class PercentageRange(TypedDict, closed=True):
    minimum_value: "capo_marketplace_discovery.types.bounded_string.BoundedString"
    """<p>The minimum percentage by which the price can increase at each renewal cycle.</p>"""
    maximum_value: "capo_marketplace_discovery.types.bounded_string.BoundedString"
    """<p>The maximum percentage by which the price can increase at each renewal cycle.</p>"""
    default_value: "capo_marketplace_discovery.types.bounded_string.BoundedString"
    """<p>The percentage increase applied by default when no other value is finalized before the adjustment deadline. Falls between <code>minimumValue</code> and <code>maximumValue</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PercentageRange) -> dict:
    out: dict = {}
    out["minimumValue"] = value["minimum_value"]
    out["maximumValue"] = value["maximum_value"]
    out["defaultValue"] = value["default_value"]
    return out


def deserialize_json(data: dict) -> PercentageRange:
    out: PercentageRange = {}  # type: ignore[typeddict-item]
    if data.get("minimumValue") is not None:
        out["minimum_value"] = data["minimumValue"]
    else:
        out["minimum_value"] = ""
    if data.get("maximumValue") is not None:
        out["maximum_value"] = data["maximumValue"]
    else:
        out["maximum_value"] = ""
    if data.get("defaultValue") is not None:
        out["default_value"] = data["defaultValue"]
    else:
        out["default_value"] = ""
    return out
