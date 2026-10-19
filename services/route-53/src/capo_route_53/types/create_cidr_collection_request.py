"""Generated from Smithy shape ``com.amazonaws.route53#CreateCidrCollectionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_route_53.types.cidr_nonce
    import capo_route_53.types.collection_name


class CreateCidrCollectionRequest(TypedDict, closed=True):
    name: "capo_route_53.types.collection_name.CollectionName"
    """<p>A unique identifier for the account that can be used to reference the collection from other API calls.</p>"""
    caller_reference: "capo_route_53.types.cidr_nonce.CidrNonce"
    """<p>A client-specific token that allows requests to be securely retried so that the intended outcome will only occur once, retries receive a similar response, and there are no additional edge cases to handle.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: CreateCidrCollectionRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Name").text = str(value["name"])
    SubElement(el, "CallerReference").text = str(value["caller_reference"])


def deserialize_xml(el: Element) -> CreateCidrCollectionRequest:
    out: CreateCidrCollectionRequest = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    else:
        out["name"] = ""
    child_caller_reference = el.find("CallerReference")
    if child_caller_reference is not None:
        out["caller_reference"] = str(child_caller_reference.text or "")
    else:
        out["caller_reference"] = ""
    return out
