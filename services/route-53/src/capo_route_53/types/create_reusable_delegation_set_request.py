"""Generated from Smithy shape ``com.amazonaws.route53#CreateReusableDelegationSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_route_53.types.nonce
    import capo_route_53.types.resource_id


class CreateReusableDelegationSetRequest(TypedDict, closed=True):
    caller_reference: "capo_route_53.types.nonce.Nonce"
    """<p>A unique string that identifies the request, and that allows you to retry failed <code>CreateReusableDelegationSet</code> requests without the risk of executing the operation twice. You must use a unique <code>CallerReference</code> string every time you submit a <code>CreateReusableDelegationSet</code> request. <code>CallerReference</code> can be any unique string, for example a date/time stamp.</p>"""
    hosted_zone_id: NotRequired["capo_route_53.types.resource_id.ResourceId"]
    """<p>If you want to mark the delegation set for an existing hosted zone as reusable, the ID for that hosted zone.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: CreateReusableDelegationSetRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "CallerReference").text = str(value["caller_reference"])
    if "hosted_zone_id" in value:
        SubElement(el, "HostedZoneId").text = str(value["hosted_zone_id"])


def deserialize_xml(el: Element) -> CreateReusableDelegationSetRequest:
    out: CreateReusableDelegationSetRequest = {}  # type: ignore[typeddict-item]
    child_caller_reference = el.find("CallerReference")
    if child_caller_reference is not None:
        out["caller_reference"] = str(child_caller_reference.text or "")
    else:
        out["caller_reference"] = ""
    child_hosted_zone_id = el.find("HostedZoneId")
    if child_hosted_zone_id is not None:
        out["hosted_zone_id"] = str(child_hosted_zone_id.text or "")
    return out
