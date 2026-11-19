"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#CoreNetworkEndpointDnsIpItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53globalresolver.types.dns_label
    import capo_route53globalresolver.types.dns_name
    import capo_route53globalresolver.types.i_pv4_address
    import capo_route53globalresolver.types.i_pv6_address
    import capo_route53globalresolver.types.region_scope_type
    import capo_route53globalresolver.types.regions


class CoreNetworkEndpointDnsIpItem(TypedDict, closed=True):
    ipv4_address: NotRequired[
        "capo_route53globalresolver.types.i_pv4_address.IPv4Address"
    ]
    """<p>The IPv4 address that the core network endpoint uses to receive DNS queries.</p>"""
    ipv6_address: NotRequired[
        "capo_route53globalresolver.types.i_pv6_address.IPv6Address"
    ]
    """<p>The IPv6 address that the core network endpoint uses to receive DNS queries.</p>"""
    dns_label: "capo_route53globalresolver.types.dns_label.DnsLabel"
    """<p>The DNS label associated with the IP address.</p>"""
    dns_name: NotRequired["capo_route53globalresolver.types.dns_name.DnsName"]
    """<p>The fully qualified DNS name associated with the IP address.</p>"""
    region_scope: "capo_route53globalresolver.types.region_scope_type.RegionScopeType"
    """<p>Indicates whether the IP address applies to all Amazon Web Services Regions or only to the specific Regions that you identify. When the value is <code>REGIONAL</code>, the Regions are listed in the <code>regions</code> field.</p>"""
    regions: NotRequired["capo_route53globalresolver.types.regions.Regions"]
    """<p>The Amazon Web Services Regions in which the IP address applies when the region scope is <code>REGIONAL</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CoreNetworkEndpointDnsIpItem) -> dict:
    out: dict = {}
    if "ipv4_address" in value:
        out["ipv4Address"] = value["ipv4_address"]
    if "ipv6_address" in value:
        out["ipv6Address"] = value["ipv6_address"]
    out["dnsLabel"] = value["dns_label"]
    if "dns_name" in value:
        out["dnsName"] = value["dns_name"]
    import capo_route53globalresolver.types.region_scope_type

    out["regionScope"] = (
        capo_route53globalresolver.types.region_scope_type.serialize_json(
            value["region_scope"]
        )
    )
    if "regions" in value:
        import capo_route53globalresolver.types.regions

        out["regions"] = capo_route53globalresolver.types.regions.serialize_json(
            value["regions"]
        )
    return out


def deserialize_json(data: dict) -> CoreNetworkEndpointDnsIpItem:
    out: CoreNetworkEndpointDnsIpItem = {}  # type: ignore[typeddict-item]
    if data.get("ipv4Address") is not None:
        out["ipv4_address"] = data["ipv4Address"]
    if data.get("ipv6Address") is not None:
        out["ipv6_address"] = data["ipv6Address"]
    if data.get("dnsLabel") is not None:
        out["dns_label"] = data["dnsLabel"]
    else:
        out["dns_label"] = ""
    if data.get("dnsName") is not None:
        out["dns_name"] = data["dnsName"]
    if data.get("regionScope") is not None:
        import capo_route53globalresolver.types.region_scope_type

        out["region_scope"] = (
            capo_route53globalresolver.types.region_scope_type.deserialize_json(
                data["regionScope"]
            )
        )
    else:
        import typing

        out["region_scope"] = typing.cast(
            "capo_route53globalresolver.types.region_scope_type.RegionScopeType", ""
        )
    if data.get("regions") is not None:
        import capo_route53globalresolver.types.regions

        out["regions"] = capo_route53globalresolver.types.regions.deserialize_json(
            data["regions"]
        )
    return out
