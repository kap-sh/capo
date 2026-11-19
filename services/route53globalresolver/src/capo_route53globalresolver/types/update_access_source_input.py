"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#UpdateAccessSourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53globalresolver.types.cidr
    import capo_route53globalresolver.types.dns_protocol
    import capo_route53globalresolver.types.ip_address_type
    import capo_route53globalresolver.types.resource_id
    import capo_route53globalresolver.types.resource_name_short


class UpdateAccessSourceInput(TypedDict, closed=True):
    access_source_id: "capo_route53globalresolver.types.resource_id.ResourceId"
    """<p>The unique identifier of the access source to update.</p>"""
    cidr: NotRequired["capo_route53globalresolver.types.cidr.Cidr"]
    """<p>The CIDR block for the access source.</p>"""
    dns_view_id: NotRequired["capo_route53globalresolver.types.resource_id.ResourceId"]
    """<p>The ID of the DNS view to associate with this access source.</p>"""
    ip_address_type: NotRequired[
        "capo_route53globalresolver.types.ip_address_type.IpAddressType"
    ]
    """<p>The IP address type for the access source.</p>"""
    name: NotRequired[
        "capo_route53globalresolver.types.resource_name_short.ResourceNameShort"
    ]
    """<p>The name of the access source.</p>"""
    protocol: NotRequired["capo_route53globalresolver.types.dns_protocol.DnsProtocol"]
    """<p>The protocol for the access source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAccessSourceInput) -> dict:
    out: dict = {}
    if "cidr" in value:
        out["cidr"] = value["cidr"]
    if "dns_view_id" in value:
        out["dnsViewId"] = value["dns_view_id"]
    if "ip_address_type" in value:
        import capo_route53globalresolver.types.ip_address_type

        out["ipAddressType"] = (
            capo_route53globalresolver.types.ip_address_type.serialize_json(
                value["ip_address_type"]
            )
        )
    if "name" in value:
        out["name"] = value["name"]
    if "protocol" in value:
        import capo_route53globalresolver.types.dns_protocol

        out["protocol"] = capo_route53globalresolver.types.dns_protocol.serialize_json(
            value["protocol"]
        )
    return out


def deserialize_json(data: dict) -> UpdateAccessSourceInput:
    out: UpdateAccessSourceInput = {}  # type: ignore[typeddict-item]
    if data.get("cidr") is not None:
        out["cidr"] = data["cidr"]
    if data.get("dnsViewId") is not None:
        out["dns_view_id"] = data["dnsViewId"]
    if data.get("ipAddressType") is not None:
        import capo_route53globalresolver.types.ip_address_type

        out["ip_address_type"] = (
            capo_route53globalresolver.types.ip_address_type.deserialize_json(
                data["ipAddressType"]
            )
        )
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("protocol") is not None:
        import capo_route53globalresolver.types.dns_protocol

        out["protocol"] = (
            capo_route53globalresolver.types.dns_protocol.deserialize_json(
                data["protocol"]
            )
        )
    return out
