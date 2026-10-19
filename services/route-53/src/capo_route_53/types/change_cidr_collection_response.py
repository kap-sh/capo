"""Generated from Smithy shape ``com.amazonaws.route53#ChangeCidrCollectionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_route_53.types.change_id


class ChangeCidrCollectionResponse(TypedDict, closed=True):
    id: "capo_route_53.types.change_id.ChangeId"
    """<p>The ID that is returned by <code>ChangeCidrCollection</code>. You can use it as input to <code>GetChange</code> to see if a CIDR collection change has propagated or not.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ChangeCidrCollectionResponse, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Id").text = str(value["id"])


def deserialize_xml(el: Element) -> ChangeCidrCollectionResponse:
    out: ChangeCidrCollectionResponse = {}  # type: ignore[typeddict-item]
    child_id = el.find("Id")
    if child_id is not None:
        out["id"] = str(child_id.text or "")
    else:
        out["id"] = ""
    return out
