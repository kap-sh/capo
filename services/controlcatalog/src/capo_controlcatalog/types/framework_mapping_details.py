"""Generated from Smithy shape ``com.amazonaws.controlcatalog#FrameworkMappingDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_controlcatalog.types.framework_item
    import capo_controlcatalog.types.framework_name


class FrameworkMappingDetails(TypedDict, closed=True):
    name: "capo_controlcatalog.types.framework_name.FrameworkName"
    """<p>The name of the compliance framework that the control maps to.</p>"""
    item: "capo_controlcatalog.types.framework_item.FrameworkItem"
    """<p>The specific item or requirement within the framework that the control maps to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FrameworkMappingDetails) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Item"] = value["item"]
    return out


def deserialize_json(data: dict) -> FrameworkMappingDetails:
    out: FrameworkMappingDetails = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Item") is not None:
        out["item"] = data["Item"]
    else:
        out["item"] = ""
    return out
