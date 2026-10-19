"""Generated from Smithy shape ``com.amazonaws.route53#ListVPCAssociationAuthorizationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_route_53.types.pagination_token
    import capo_route_53.types.resource_id
    import capo_route_53.types.vp_cs


class ListVPCAssociationAuthorizationsResponse(TypedDict, closed=True):
    hosted_zone_id: "capo_route_53.types.resource_id.ResourceId"
    """<p>The ID of the hosted zone that you can associate the listed VPCs with.</p>"""
    next_token: NotRequired["capo_route_53.types.pagination_token.PaginationToken"]
    """<p>When the response includes a <code>NextToken</code> element, there are more VPCs that can be associated with the specified hosted zone. To get the next page of VPCs, submit another <code>ListVPCAssociationAuthorizations</code> request, and include the value of the <code>NextToken</code> element from the response in the <code>nexttoken</code> request parameter.</p>"""
    vp_cs: "capo_route_53.types.vp_cs.VPCs"
    """<p>The list of VPCs that are authorized to be associated with the specified hosted zone.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ListVPCAssociationAuthorizationsResponse, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "HostedZoneId").text = str(value["hosted_zone_id"])
    if "next_token" in value:
        SubElement(el, "NextToken").text = str(value["next_token"])
    import capo_route_53.types.vp_cs

    capo_route_53.types.vp_cs.serialize_xml(value["vp_cs"], el, "VPCs")


def deserialize_xml(el: Element) -> ListVPCAssociationAuthorizationsResponse:
    out: ListVPCAssociationAuthorizationsResponse = {}  # type: ignore[typeddict-item]
    child_hosted_zone_id = el.find("HostedZoneId")
    if child_hosted_zone_id is not None:
        out["hosted_zone_id"] = str(child_hosted_zone_id.text or "")
    else:
        out["hosted_zone_id"] = ""
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_vp_cs = el.find("VPCs")
    if child_vp_cs is not None:
        import capo_route_53.types.vp_cs

        out["vp_cs"] = capo_route_53.types.vp_cs.deserialize_xml(child_vp_cs)
    else:
        out["vp_cs"] = []
    return out
