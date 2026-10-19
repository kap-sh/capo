"""Generated from Smithy shape ``com.amazonaws.cloudfront#ConnectionFunctionAssociation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.resource_id


class ConnectionFunctionAssociation(TypedDict, closed=True):
    id: "capo_cloudfront.types.resource_id.ResourceId"
    """<p>The association's ID.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ConnectionFunctionAssociation, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Id").text = str(value["id"])


def deserialize_xml(el: Element) -> ConnectionFunctionAssociation:
    out: ConnectionFunctionAssociation = {}  # type: ignore[typeddict-item]
    child_id = el.find("Id")
    if child_id is not None:
        out["id"] = str(child_id.text or "")
    else:
        out["id"] = ""
    return out
