"""Generated from Smithy shape ``com.amazonaws.route53#DelegationSet``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_route_53.types.delegation_set_name_servers
    import capo_route_53.types.nonce
    import capo_route_53.types.resource_id


class DelegationSet(TypedDict, closed=True):
    id: NotRequired["capo_route_53.types.resource_id.ResourceId"]
    """<p>The ID that Amazon Route 53 assigns to a reusable delegation set.</p>"""
    caller_reference: NotRequired["capo_route_53.types.nonce.Nonce"]
    """<p>The value that you specified for <code>CallerReference</code> when you created the reusable delegation set.</p>"""
    name_servers: (
        "capo_route_53.types.delegation_set_name_servers.DelegationSetNameServers"
    )
    """<p>A complex type that contains a list of the authoritative name servers for a hosted zone or for a reusable delegation set.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: DelegationSet, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "id" in value:
        SubElement(el, "Id").text = str(value["id"])
    if "caller_reference" in value:
        SubElement(el, "CallerReference").text = str(value["caller_reference"])
    import capo_route_53.types.delegation_set_name_servers

    capo_route_53.types.delegation_set_name_servers.serialize_xml(
        value["name_servers"], el, "NameServers"
    )


def deserialize_xml(el: Element) -> DelegationSet:
    out: DelegationSet = {}  # type: ignore[typeddict-item]
    child_id = el.find("Id")
    if child_id is not None:
        out["id"] = str(child_id.text or "")
    child_caller_reference = el.find("CallerReference")
    if child_caller_reference is not None:
        out["caller_reference"] = str(child_caller_reference.text or "")
    child_name_servers = el.find("NameServers")
    if child_name_servers is not None:
        import capo_route_53.types.delegation_set_name_servers

        out["name_servers"] = (
            capo_route_53.types.delegation_set_name_servers.deserialize_xml(
                child_name_servers
            )
        )
    else:
        out["name_servers"] = []
    return out
