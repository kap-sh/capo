"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#OrderBy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iottwinmaker.types.order
    import capo_iottwinmaker.types.string


class OrderBy(TypedDict, closed=True):
    order: NotRequired["capo_iottwinmaker.types.order.Order"]
    """<p>The set order that filters results.</p>"""
    property_name: "capo_iottwinmaker.types.string.String"
    """<p>The property name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OrderBy) -> dict:
    out: dict = {}
    if "order" in value:
        out["order"] = value["order"]
    out["propertyName"] = value["property_name"]
    return out


def deserialize_json(data: dict) -> OrderBy:
    out: OrderBy = {}  # type: ignore[typeddict-item]
    if data.get("order") is not None:
        out["order"] = data["order"]
    if data.get("propertyName") is not None:
        out["property_name"] = data["propertyName"]
    else:
        out["property_name"] = ""
    return out
