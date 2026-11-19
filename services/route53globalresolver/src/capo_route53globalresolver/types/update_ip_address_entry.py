"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#UpdateIpAddressEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53globalresolver.types.dns_label
    import capo_route53globalresolver.types.i_pv4_address
    import capo_route53globalresolver.types.i_pv6_address
    import capo_route53globalresolver.types.region_scope_type
    import capo_route53globalresolver.types.regions
    import capo_route53globalresolver.types.update_ip_address_operation


class UpdateIpAddressEntry(TypedDict, closed=True):
    operation: "capo_route53globalresolver.types.update_ip_address_operation.UpdateIpAddressOperation"
    """<p>The operation to perform on the IP address. Valid values are <code>ADD</code>, <code>REMOVE</code>, and <code>UPDATE</code>.</p>"""
    ipv4_address: NotRequired[
        "capo_route53globalresolver.types.i_pv4_address.IPv4Address"
    ]
    """<p>The IPv4 address that the operation acts on.</p>"""
    ipv6_address: NotRequired[
        "capo_route53globalresolver.types.i_pv6_address.IPv6Address"
    ]
    """<p>The IPv6 address that the operation acts on.</p>"""
    dns_label: NotRequired["capo_route53globalresolver.types.dns_label.DnsLabel"]
    """<p>The DNS label associated with the IP address.</p>"""
    region_scope: NotRequired[
        "capo_route53globalresolver.types.region_scope_type.RegionScopeType"
    ]
    """<p>Indicates whether the IP address applies to all Amazon Web Services Regions or only to the specific Regions that you identify. When the value is <code>REGIONAL</code>, the Regions are listed in the <code>regions</code> field.</p>"""
    regions: NotRequired["capo_route53globalresolver.types.regions.Regions"]
    """<p>The Amazon Web Services Regions in which the IP address applies when the region scope is <code>REGIONAL</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateIpAddressEntry) -> dict:
    out: dict = {}
    import capo_route53globalresolver.types.update_ip_address_operation

    out["operation"] = (
        capo_route53globalresolver.types.update_ip_address_operation.serialize_json(
            value["operation"]
        )
    )
    if "ipv4_address" in value:
        out["ipv4Address"] = value["ipv4_address"]
    if "ipv6_address" in value:
        out["ipv6Address"] = value["ipv6_address"]
    if "dns_label" in value:
        out["dnsLabel"] = value["dns_label"]
    if "region_scope" in value:
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


def deserialize_json(data: dict) -> UpdateIpAddressEntry:
    out: UpdateIpAddressEntry = {}  # type: ignore[typeddict-item]
    if data.get("operation") is not None:
        import capo_route53globalresolver.types.update_ip_address_operation

        out["operation"] = (
            capo_route53globalresolver.types.update_ip_address_operation.deserialize_json(
                data["operation"]
            )
        )
    else:
        import typing

        out["operation"] = typing.cast(
            "capo_route53globalresolver.types.update_ip_address_operation.UpdateIpAddressOperation",
            "",
        )
    if data.get("ipv4Address") is not None:
        out["ipv4_address"] = data["ipv4Address"]
    if data.get("ipv6Address") is not None:
        out["ipv6_address"] = data["ipv6Address"]
    if data.get("dnsLabel") is not None:
        out["dns_label"] = data["dnsLabel"]
    if data.get("regionScope") is not None:
        import capo_route53globalresolver.types.region_scope_type

        out["region_scope"] = (
            capo_route53globalresolver.types.region_scope_type.deserialize_json(
                data["regionScope"]
            )
        )
    if data.get("regions") is not None:
        import capo_route53globalresolver.types.regions

        out["regions"] = capo_route53globalresolver.types.regions.deserialize_json(
            data["regions"]
        )
    return out
