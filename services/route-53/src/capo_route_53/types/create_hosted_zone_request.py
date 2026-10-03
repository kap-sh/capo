"""Generated from Smithy shape ``com.amazonaws.route53#CreateHostedZoneRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_route_53._protocol.xml import Element, SubElement
from capo_route_53.errors import DeserializationError

if TYPE_CHECKING:
    import capo_route_53.types.dns_name
    import capo_route_53.types.hosted_zone_config
    import capo_route_53.types.nonce
    import capo_route_53.types.resource_id
    import capo_route_53.types.vpc


class CreateHostedZoneRequest(TypedDict, closed=True):
    name: "capo_route_53.types.dns_name.DNSName"
    """<p>The name of the domain. Specify a fully qualified domain name, for example, <i>www.example.com</i>. The trailing dot is optional; Amazon Route 53 assumes that the domain name is fully qualified. This means that Route 53 treats <i>www.example.com</i> (without a trailing dot) and <i>www.example.com.</i> (with a trailing dot) as identical.</p> <p>If you're creating a public hosted zone, this is the name you have registered with your DNS registrar. If your domain name is registered with a registrar other than Route 53, change the name servers for your domain to the set of <code>NameServers</code> that <code>CreateHostedZone</code> returns in <code>DelegationSet</code>.</p>"""
    vpc: NotRequired["capo_route_53.types.vpc.VPC"]
    """<p>(Private hosted zones only) A complex type that contains information about the Amazon VPC that you're associating with this hosted zone.</p> <p>You can specify only one Amazon VPC when you create a private hosted zone. If you are associating a VPC with a hosted zone with this request, the paramaters <code>VPCId</code> and <code>VPCRegion</code> are also required.</p> <p>To associate additional Amazon VPCs with the hosted zone, use <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_AssociateVPCWithHostedZone.html">AssociateVPCWithHostedZone</a> after you create a hosted zone.</p>"""
    caller_reference: "capo_route_53.types.nonce.Nonce"
    """<p>A unique string that identifies the request and that allows failed <code>CreateHostedZone</code> requests to be retried without the risk of executing the operation twice. You must use a unique <code>CallerReference</code> string every time you submit a <code>CreateHostedZone</code> request. <code>CallerReference</code> can be any unique string, for example, a date/time stamp.</p>"""
    hosted_zone_config: NotRequired[
        "capo_route_53.types.hosted_zone_config.HostedZoneConfig"
    ]
    """<p>(Optional) A complex type that contains the following optional values:</p> <ul> <li> <p>For public and private hosted zones, an optional comment</p> </li> <li> <p>For private hosted zones, an optional <code>PrivateZone</code> element</p> </li> </ul> <p>If you don't specify a comment or the <code>PrivateZone</code> element, omit <code>HostedZoneConfig</code> and the other elements.</p>"""
    delegation_set_id: NotRequired["capo_route_53.types.resource_id.ResourceId"]
    """<p>If you want to associate a reusable delegation set with this hosted zone, the ID that Amazon Route 53 assigned to the reusable delegation set when you created it. For more information about reusable delegation sets, see <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_CreateReusableDelegationSet.html">CreateReusableDelegationSet</a>.</p> <p>If you are using a reusable delegation set to create a public hosted zone for a subdomain, make sure that the parent hosted zone doesn't use one or more of the same name servers. If you have overlapping nameservers, the operation will cause a <code>ConflictingDomainsExist</code> error.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: CreateHostedZoneRequest, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Name").text = str(value["name"])
    if "vpc" in value:
        import capo_route_53.types.vpc

        capo_route_53.types.vpc.serialize_xml(value["vpc"], el, "VPC")
    SubElement(el, "CallerReference").text = str(value["caller_reference"])
    if "hosted_zone_config" in value:
        import capo_route_53.types.hosted_zone_config

        capo_route_53.types.hosted_zone_config.serialize_xml(
            value["hosted_zone_config"], el, "HostedZoneConfig"
        )
    if "delegation_set_id" in value:
        SubElement(el, "DelegationSetId").text = str(value["delegation_set_id"])


def deserialize_xml(el: Element) -> CreateHostedZoneRequest:
    out: CreateHostedZoneRequest = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    else:
        raise DeserializationError("CreateHostedZoneRequest.name required")
    child_vpc = el.find("VPC")
    if child_vpc is not None:
        import capo_route_53.types.vpc

        out["vpc"] = capo_route_53.types.vpc.deserialize_xml(child_vpc)
    child_caller_reference = el.find("CallerReference")
    if child_caller_reference is not None:
        out["caller_reference"] = str(child_caller_reference.text or "")
    else:
        raise DeserializationError("CreateHostedZoneRequest.caller_reference required")
    child_hosted_zone_config = el.find("HostedZoneConfig")
    if child_hosted_zone_config is not None:
        import capo_route_53.types.hosted_zone_config

        out["hosted_zone_config"] = (
            capo_route_53.types.hosted_zone_config.deserialize_xml(
                child_hosted_zone_config
            )
        )
    child_delegation_set_id = el.find("DelegationSetId")
    if child_delegation_set_id is not None:
        out["delegation_set_id"] = str(child_delegation_set_id.text or "")
    return out
