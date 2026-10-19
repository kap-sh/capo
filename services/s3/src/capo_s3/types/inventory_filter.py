"""Generated from Smithy shape ``com.amazonaws.s3#InventoryFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.prefix


class InventoryFilter(TypedDict, closed=True):
    prefix: "capo_s3.types.prefix.Prefix"
    """<p>The prefix that an object must have to be included in the inventory results.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: InventoryFilter, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Prefix").text = str(value["prefix"])


def deserialize_xml(el: Element) -> InventoryFilter:
    out: InventoryFilter = {}  # type: ignore[typeddict-item]
    child_prefix = el.find("Prefix")
    if child_prefix is not None:
        out["prefix"] = str(child_prefix.text or "")
    else:
        out["prefix"] = ""
    return out
