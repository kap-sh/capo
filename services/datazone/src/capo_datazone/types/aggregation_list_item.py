"""Generated from Smithy shape ``com.amazonaws.datazone#AggregationListItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.aggregation_display_value
    import capo_datazone.types.attribute


class AggregationListItem(TypedDict, closed=True):
    attribute: "capo_datazone.types.attribute.Attribute"
    """<p>An attribute on which to compute aggregations.</p>"""
    display_value: NotRequired[
        "capo_datazone.types.aggregation_display_value.AggregationDisplayValue"
    ]
    """<p>The display value of the aggregation list item. Supported values include <code>value</code> and <code>glossaryTerm.name</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AggregationListItem) -> dict:
    out: dict = {}
    out["attribute"] = value["attribute"]
    if "display_value" in value:
        out["displayValue"] = value["display_value"]
    return out


def deserialize_json(data: dict) -> AggregationListItem:
    out: AggregationListItem = {}  # type: ignore[typeddict-item]
    if data.get("attribute") is not None:
        out["attribute"] = data["attribute"]
    else:
        out["attribute"] = ""
    if data.get("displayValue") is not None:
        out["display_value"] = data["displayValue"]
    return out
