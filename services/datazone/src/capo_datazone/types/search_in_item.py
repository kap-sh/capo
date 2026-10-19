"""Generated from Smithy shape ``com.amazonaws.datazone#SearchInItem``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.attribute


class SearchInItem(TypedDict, closed=True):
    attribute: "capo_datazone.types.attribute.Attribute"
    """<p>The search attribute.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchInItem) -> dict:
    out: dict = {}
    out["attribute"] = value["attribute"]
    return out


def deserialize_json(data: dict) -> SearchInItem:
    out: SearchInItem = {}  # type: ignore[typeddict-item]
    if data.get("attribute") is not None:
        out["attribute"] = data["attribute"]
    else:
        out["attribute"] = ""
    return out
