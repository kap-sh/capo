"""Generated from Smithy shape ``com.amazonaws.route53#CreateVPCAssociationAuthorizationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_route_53._protocol.xml import Element, SubElement
from capo_route_53.errors import DeserializationError

if TYPE_CHECKING:
    import capo_route_53.types.resource_id
    import capo_route_53.types.vpc


class CreateVPCAssociationAuthorizationResponse(TypedDict, closed=True):
    hosted_zone_id: "capo_route_53.types.resource_id.ResourceId"
    """<p>The ID of the hosted zone that you authorized associating a VPC with.</p>"""
    vpc: "capo_route_53.types.vpc.VPC"
    """<p>The VPC that you authorized associating with a hosted zone.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: CreateVPCAssociationAuthorizationResponse, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "HostedZoneId").text = str(value["hosted_zone_id"])
    import capo_route_53.types.vpc

    capo_route_53.types.vpc.serialize_xml(value["vpc"], el, "VPC")


def deserialize_xml(el: Element) -> CreateVPCAssociationAuthorizationResponse:
    out: CreateVPCAssociationAuthorizationResponse = {}  # type: ignore[typeddict-item]
    child_hosted_zone_id = el.find("HostedZoneId")
    if child_hosted_zone_id is not None:
        out["hosted_zone_id"] = str(child_hosted_zone_id.text or "")
    else:
        out["hosted_zone_id"] = ""
    child_vpc = el.find("VPC")
    if child_vpc is not None:
        import capo_route_53.types.vpc

        out["vpc"] = capo_route_53.types.vpc.deserialize_xml(child_vpc)
    else:
        raise DeserializationError(
            "CreateVPCAssociationAuthorizationResponse.vpc required"
        )
    return out
