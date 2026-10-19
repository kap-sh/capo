"""Generated from Smithy shape ``com.amazonaws.directconnect#UpdateVirtualInterfaceAttributesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_direct_connect.types.enable_site_link
    import capo_direct_connect.types.mtu
    import capo_direct_connect.types.prefix_pool_allocated_count
    import capo_direct_connect.types.rate_limit
    import capo_direct_connect.types.virtual_interface_id
    import capo_direct_connect.types.virtual_interface_name


class UpdateVirtualInterfaceAttributesRequest(TypedDict, closed=True):
    virtual_interface_id: (
        "capo_direct_connect.types.virtual_interface_id.VirtualInterfaceId"
    )
    """<p>The ID of the virtual private interface.</p>"""
    mtu: NotRequired["capo_direct_connect.types.mtu.MTU"]
    """<p>The maximum transmission unit (MTU), in bytes. The supported values are 1500 and 8500. The default value is 1500.</p>"""
    enable_site_link: NotRequired[
        "capo_direct_connect.types.enable_site_link.EnableSiteLink"
    ]
    """<p>Indicates whether to enable or disable SiteLink.</p>"""
    virtual_interface_name: NotRequired[
        "capo_direct_connect.types.virtual_interface_name.VirtualInterfaceName"
    ]
    """<p>The name of the virtual private interface.</p>"""
    prefix_pool_allocated_count_ipv4: NotRequired[
        "capo_direct_connect.types.prefix_pool_allocated_count.PrefixPoolAllocatedCount"
    ]
    """<p>The number of inbound IPv4 route prefixes to allocate to the virtual interface. Not applicable to public virtual interfaces.</p>"""
    prefix_pool_allocated_count_ipv6: NotRequired[
        "capo_direct_connect.types.prefix_pool_allocated_count.PrefixPoolAllocatedCount"
    ]
    """<p>The number of inbound IPv6 route prefixes to allocate to the virtual interface. Not applicable to public virtual interfaces.</p>"""
    rate_limit: NotRequired["capo_direct_connect.types.rate_limit.RateLimit"]
    """<p>The rate limit (bandwidth allocation) to apply to the virtual interface. Use this to update the bandwidth allocation on an existing virtual interface.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateVirtualInterfaceAttributesRequest) -> dict:
    out: dict = {}
    out["virtualInterfaceId"] = value["virtual_interface_id"]
    if "mtu" in value:
        out["mtu"] = value["mtu"]
    if "enable_site_link" in value:
        out["enableSiteLink"] = value["enable_site_link"]
    if "virtual_interface_name" in value:
        out["virtualInterfaceName"] = value["virtual_interface_name"]
    if "prefix_pool_allocated_count_ipv4" in value:
        out["prefixPoolAllocatedCountIpv4"] = value["prefix_pool_allocated_count_ipv4"]
    if "prefix_pool_allocated_count_ipv6" in value:
        out["prefixPoolAllocatedCountIpv6"] = value["prefix_pool_allocated_count_ipv6"]
    if "rate_limit" in value:
        out["rateLimit"] = value["rate_limit"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateVirtualInterfaceAttributesRequest:
    out: UpdateVirtualInterfaceAttributesRequest = {}  # type: ignore[typeddict-item]
    if data.get("virtualInterfaceId") is not None:
        out["virtual_interface_id"] = data["virtualInterfaceId"]
    else:
        out["virtual_interface_id"] = ""
    if data.get("mtu") is not None:
        out["mtu"] = data["mtu"]
    if data.get("enableSiteLink") is not None:
        out["enable_site_link"] = data["enableSiteLink"]
    if data.get("virtualInterfaceName") is not None:
        out["virtual_interface_name"] = data["virtualInterfaceName"]
    if data.get("prefixPoolAllocatedCountIpv4") is not None:
        out["prefix_pool_allocated_count_ipv4"] = data["prefixPoolAllocatedCountIpv4"]
    if data.get("prefixPoolAllocatedCountIpv6") is not None:
        out["prefix_pool_allocated_count_ipv6"] = data["prefixPoolAllocatedCountIpv6"]
    if data.get("rateLimit") is not None:
        out["rate_limit"] = data["rateLimit"]
    return out
