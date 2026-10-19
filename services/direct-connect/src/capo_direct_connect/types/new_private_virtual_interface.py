"""Generated from Smithy shape ``com.amazonaws.directconnect#NewPrivateVirtualInterface``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_direct_connect.types.address_family
    import capo_direct_connect.types.amazon_address
    import capo_direct_connect.types.asn
    import capo_direct_connect.types.bgp_auth_key
    import capo_direct_connect.types.customer_address
    import capo_direct_connect.types.direct_connect_gateway_id
    import capo_direct_connect.types.enable_site_link
    import capo_direct_connect.types.long_asn
    import capo_direct_connect.types.mtu
    import capo_direct_connect.types.prefix_pool_allocated_count
    import capo_direct_connect.types.rate_limit
    import capo_direct_connect.types.tag_list
    import capo_direct_connect.types.virtual_gateway_id
    import capo_direct_connect.types.virtual_interface_name
    import capo_direct_connect.types.vlan


class NewPrivateVirtualInterface(TypedDict, closed=True):
    virtual_interface_name: (
        "capo_direct_connect.types.virtual_interface_name.VirtualInterfaceName"
    )
    """<p>The name of the virtual interface assigned by the customer network. The name has a maximum of 100 characters. The following are valid characters: a-z, 0-9 and a hyphen (-).</p>"""
    vlan: "capo_direct_connect.types.vlan.VLAN"
    """<p>The ID of the VLAN.</p>"""
    asn: "capo_direct_connect.types.asn.ASN"
    """<p>The autonomous system number (ASN). The valid range is from 1 to 2147483646 for Border Gateway Protocol (BGP) configuration. If you provide a number greater than the maximum, an error is returned. Use <code>asnLong</code> instead.</p> <ul> <li> <p>You can use <code>asnLong</code> or <code>asn</code>, but not both. We recommend using <code>asnLong</code> as it supports a greater pool of numbers. </p> </li> <li> <p>If you provide a value in the same API call for both <code>asn</code> and <code>asnLong</code>, the API will only accept the value for <code>asnLong</code>. </p> </li> <li> <p>If you enter a 4-byte ASN for the <code>asn</code> parameter, the API returns an error. </p> </li> <li> <p>If you are using a 2-byte ASN, the API response will include the 2-byte value for both the <code>asn</code> and <code>asnLong</code> fields.</p> </li> </ul> <p>The valid values are 1-2147483646.</p>"""
    asn_long: NotRequired["capo_direct_connect.types.long_asn.LongAsn"]
    """<p>The long ASN for a new private virtual interface. The valid range is from 1 to 4294967294 for BGP configuration.</p> <p>Note the following limitations when using <code>asnLong</code>:</p> <ul> <li> <p>You can use <code>asnLong</code> or <code>asn</code>, but not both. We recommend using <code>asnLong</code> as it supports a greater pool of numbers. </p> </li> <li> <p> <code>asnLong</code> accepts any valid ASN value, regardless if it's 2-byte or 4-byte. </p> </li> <li> <p>When using a 4-byte <code>asnLong</code>, the API response returns <code>0</code> for the legacy <code>asn</code> attribute since 4-byte ASN values exceed the maximum supported value of 2,147,483,647.</p> </li> <li> <p>If you are using a 2-byte ASN, the API response will include the 2-byte value for both the <code>asn</code> and <code>asnLong</code> fields.</p> </li> <li> <p>If you provide a value in the same API call for both <code>asn</code> and <code>asnLong</code>, the API will only accept the value for <code>asnLong</code>.</p> </li> </ul>"""
    mtu: NotRequired["capo_direct_connect.types.mtu.MTU"]
    """<p>The maximum transmission unit (MTU), in bytes. The supported values are 1500 and 8500. The default value is 1500.</p>"""
    auth_key: NotRequired["capo_direct_connect.types.bgp_auth_key.BGPAuthKey"]
    """<p>The authentication key for BGP configuration. This string has a minimum length of 6 characters and and a maximun lenth of 80 characters.</p>"""
    amazon_address: NotRequired[
        "capo_direct_connect.types.amazon_address.AmazonAddress"
    ]
    """<p>The IP address assigned to the Amazon interface.</p>"""
    customer_address: NotRequired[
        "capo_direct_connect.types.customer_address.CustomerAddress"
    ]
    """<p>The IP address assigned to the customer interface.</p>"""
    address_family: NotRequired[
        "capo_direct_connect.types.address_family.AddressFamily"
    ]
    """<p>The address family for the BGP peer.</p>"""
    virtual_gateway_id: NotRequired[
        "capo_direct_connect.types.virtual_gateway_id.VirtualGatewayId"
    ]
    """<p>The ID of the virtual private gateway.</p>"""
    direct_connect_gateway_id: NotRequired[
        "capo_direct_connect.types.direct_connect_gateway_id.DirectConnectGatewayId"
    ]
    """<p>The ID of the Direct Connect gateway.</p>"""
    tags: NotRequired["capo_direct_connect.types.tag_list.TagList"]
    """<p>The tags associated with the private virtual interface.</p>"""
    enable_site_link: NotRequired[
        "capo_direct_connect.types.enable_site_link.EnableSiteLink"
    ]
    """<p>Indicates whether to enable or disable SiteLink.</p>"""
    prefix_pool_allocated_count_ipv4: NotRequired[
        "capo_direct_connect.types.prefix_pool_allocated_count.PrefixPoolAllocatedCount"
    ]
    """<p>The number of inbound IPv4 route prefixes to allocate to the virtual interface.</p>"""
    prefix_pool_allocated_count_ipv6: NotRequired[
        "capo_direct_connect.types.prefix_pool_allocated_count.PrefixPoolAllocatedCount"
    ]
    """<p>The number of inbound IPv6 route prefixes to allocate to the virtual interface.</p>"""
    rate_limit: NotRequired["capo_direct_connect.types.rate_limit.RateLimit"]
    """<p>The rate limit (bandwidth allocation) to apply to the virtual interface. The rate limit restricts the maximum bandwidth that the virtual interface can use on the parent connection.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NewPrivateVirtualInterface) -> dict:
    out: dict = {}
    out["virtualInterfaceName"] = value["virtual_interface_name"]
    out["vlan"] = value.get("vlan", 0)
    out["asn"] = value.get("asn", 0)
    if "asn_long" in value:
        out["asnLong"] = value["asn_long"]
    if "mtu" in value:
        out["mtu"] = value["mtu"]
    if "auth_key" in value:
        out["authKey"] = value["auth_key"]
    if "amazon_address" in value:
        out["amazonAddress"] = value["amazon_address"]
    if "customer_address" in value:
        out["customerAddress"] = value["customer_address"]
    if "address_family" in value:
        import capo_direct_connect.types.address_family

        out["addressFamily"] = (
            capo_direct_connect.types.address_family.serialize_aws_json_1_1(
                value["address_family"]
            )
        )
    if "virtual_gateway_id" in value:
        out["virtualGatewayId"] = value["virtual_gateway_id"]
    if "direct_connect_gateway_id" in value:
        out["directConnectGatewayId"] = value["direct_connect_gateway_id"]
    if "tags" in value:
        import capo_direct_connect.types.tag_list

        out["tags"] = capo_direct_connect.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "enable_site_link" in value:
        out["enableSiteLink"] = value["enable_site_link"]
    if "prefix_pool_allocated_count_ipv4" in value:
        out["prefixPoolAllocatedCountIpv4"] = value["prefix_pool_allocated_count_ipv4"]
    if "prefix_pool_allocated_count_ipv6" in value:
        out["prefixPoolAllocatedCountIpv6"] = value["prefix_pool_allocated_count_ipv6"]
    if "rate_limit" in value:
        out["rateLimit"] = value["rate_limit"]
    return out


def deserialize_aws_json_1_1(data: dict) -> NewPrivateVirtualInterface:
    out: NewPrivateVirtualInterface = {}  # type: ignore[typeddict-item]
    if data.get("virtualInterfaceName") is not None:
        out["virtual_interface_name"] = data["virtualInterfaceName"]
    else:
        out["virtual_interface_name"] = ""
    if data.get("vlan") is not None:
        out["vlan"] = data["vlan"]
    else:
        out["vlan"] = 0
    if data.get("asn") is not None:
        out["asn"] = data["asn"]
    else:
        out["asn"] = 0
    if data.get("asnLong") is not None:
        out["asn_long"] = data["asnLong"]
    if data.get("mtu") is not None:
        out["mtu"] = data["mtu"]
    if data.get("authKey") is not None:
        out["auth_key"] = data["authKey"]
    if data.get("amazonAddress") is not None:
        out["amazon_address"] = data["amazonAddress"]
    if data.get("customerAddress") is not None:
        out["customer_address"] = data["customerAddress"]
    if data.get("addressFamily") is not None:
        import capo_direct_connect.types.address_family

        out["address_family"] = (
            capo_direct_connect.types.address_family.deserialize_aws_json_1_1(
                data["addressFamily"]
            )
        )
    if data.get("virtualGatewayId") is not None:
        out["virtual_gateway_id"] = data["virtualGatewayId"]
    if data.get("directConnectGatewayId") is not None:
        out["direct_connect_gateway_id"] = data["directConnectGatewayId"]
    if data.get("tags") is not None:
        import capo_direct_connect.types.tag_list

        out["tags"] = capo_direct_connect.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    if data.get("enableSiteLink") is not None:
        out["enable_site_link"] = data["enableSiteLink"]
    if data.get("prefixPoolAllocatedCountIpv4") is not None:
        out["prefix_pool_allocated_count_ipv4"] = data["prefixPoolAllocatedCountIpv4"]
    if data.get("prefixPoolAllocatedCountIpv6") is not None:
        out["prefix_pool_allocated_count_ipv6"] = data["prefixPoolAllocatedCountIpv6"]
    if data.get("rateLimit") is not None:
        out["rate_limit"] = data["rateLimit"]
    return out
