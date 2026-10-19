"""Generated from Smithy shape ``com.amazonaws.route53#CidrRoutingConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_route_53.types.cidr_location_name_default_allowed
    import capo_route_53.types.uuid


class CidrRoutingConfig(TypedDict, closed=True):
    collection_id: "capo_route_53.types.uuid.UUID"
    """<p>The CIDR collection ID.</p>"""
    location_name: "capo_route_53.types.cidr_location_name_default_allowed.CidrLocationNameDefaultAllowed"
    """<p>The CIDR collection location name.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: CidrRoutingConfig, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "CollectionId").text = str(value["collection_id"])
    SubElement(el, "LocationName").text = str(value["location_name"])


def deserialize_xml(el: Element) -> CidrRoutingConfig:
    out: CidrRoutingConfig = {}  # type: ignore[typeddict-item]
    child_collection_id = el.find("CollectionId")
    if child_collection_id is not None:
        out["collection_id"] = str(child_collection_id.text or "")
    else:
        out["collection_id"] = ""
    child_location_name = el.find("LocationName")
    if child_location_name is not None:
        out["location_name"] = str(child_location_name.text or "")
    else:
        out["location_name"] = ""
    return out
