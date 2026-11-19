"""Generated from Smithy shape ``com.amazonaws.directconnect#VirtualInterface``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_direct_connect.types.address_family
    import capo_direct_connect.types.amazon_address
    import capo_direct_connect.types.asn
    import capo_direct_connect.types.aws_device_v2
    import capo_direct_connect.types.aws_logical_device_id
    import capo_direct_connect.types.bgp_auth_key
    import capo_direct_connect.types.bgp_peer_list
    import capo_direct_connect.types.connection_id
    import capo_direct_connect.types.customer_address
    import capo_direct_connect.types.direct_connect_gateway_id
    import capo_direct_connect.types.jumbo_frame_capable
    import capo_direct_connect.types.location_code
    import capo_direct_connect.types.long_asn
    import capo_direct_connect.types.mtu
    import capo_direct_connect.types.owner_account
    import capo_direct_connect.types.prefix_pool_allocated_count
    import capo_direct_connect.types.rate_limit
    import capo_direct_connect.types.region
    import capo_direct_connect.types.route_filter_prefix_list
    import capo_direct_connect.types.router_config
    import capo_direct_connect.types.site_link_enabled
    import capo_direct_connect.types.tag_list
    import capo_direct_connect.types.virtual_gateway_id
    import capo_direct_connect.types.virtual_interface_id
    import capo_direct_connect.types.virtual_interface_name
    import capo_direct_connect.types.virtual_interface_state
    import capo_direct_connect.types.virtual_interface_type
    import capo_direct_connect.types.vlan


class VirtualInterface(TypedDict, closed=True):
    owner_account: NotRequired["capo_direct_connect.types.owner_account.OwnerAccount"]
    """<p>The ID of the Amazon Web Services account that owns the virtual interface.</p>"""
    virtual_interface_id: NotRequired[
        "capo_direct_connect.types.virtual_interface_id.VirtualInterfaceId"
    ]
    """<p>The ID of the virtual interface.</p>"""
    location: NotRequired["capo_direct_connect.types.location_code.LocationCode"]
    """<p>The location of the connection.</p>"""
    connection_id: NotRequired["capo_direct_connect.types.connection_id.ConnectionId"]
    """<p>The ID of the connection.</p>"""
    virtual_interface_type: NotRequired[
        "capo_direct_connect.types.virtual_interface_type.VirtualInterfaceType"
    ]
    """<p>The type of virtual interface. The possible values are <code>private</code>, <code>public</code> and <code>transit</code>.</p>"""
    virtual_interface_name: NotRequired[
        "capo_direct_connect.types.virtual_interface_name.VirtualInterfaceName"
    ]
    """<p>The name of the virtual interface assigned by the customer network. The name has a maximum of 100 characters. The following are valid characters: a-z, 0-9 and a hyphen (-).</p>"""
    vlan: "capo_direct_connect.types.vlan.VLAN"
    """<p>The ID of the VLAN.</p>"""
    asn: "capo_direct_connect.types.asn.ASN"
    """<p>The autonomous system number (ASN). The valid range is from 1 to 2147483646 for Border Gateway Protocol (BGP) configuration. If you provide a number greater than the maximum, an error is returned. Use <code>asnLong</code> instead.</p> <ul> <li> <p>You can use <code>asnLong</code> or <code>asn</code>, but not both. We recommend using <code>asnLong</code> as it supports a greater pool of numbers. </p> </li> <li> <p>If you provide a value in the same API call for both <code>asn</code> and <code>asnLong</code>, the API will only accept the value for <code>asnLong</code>. </p> </li> <li> <p>If you enter a 4-byte ASN for the <code>asn</code> parameter, the API returns an error. </p> </li> <li> <p>If you are using a 2-byte ASN, the API response will include the 2-byte value for both the <code>asn</code> and <code>asnLong</code> fields.</p> </li> </ul>"""
    asn_long: NotRequired["capo_direct_connect.types.long_asn.LongAsn"]
    """<p>The long ASN for the virtual interface. The valid range is from 1 to 4294967294 for BGP configuration.</p> <p>Note the following limitations when using <code>asnLong</code>:</p> <ul> <li> <p>You can use <code>asnLong</code> or <code>asn</code>, but not both. We recommend using <code>asnLong</code> as it supports a greater pool of numbers. </p> </li> <li> <p> <code>asnLong</code> accepts any valid ASN value, regardless if it's 2-byte or 4-byte. </p> </li> <li> <p>When using a 4-byte <code>asnLong</code>, the API response returns <code>0</code> for the legacy <code>asn</code> attribute since 4-byte ASN values exceed the maximum supported value of 2,147,483,647.</p> </li> <li> <p>If you are using a 2-byte ASN, the API response will include the 2-byte value for both the <code>asn</code> and <code>asnLong</code> fields.</p> </li> <li> <p>If you provide a value in the same API call for both <code>asn</code> and <code>asnLong</code>, the API will only accept the value for <code>asnLong</code>.</p> </li> </ul>"""
    amazon_side_asn: NotRequired["capo_direct_connect.types.long_asn.LongAsn"]
    """<p>The autonomous system number (AS) for the Amazon side of the connection.</p>"""
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
    virtual_interface_state: NotRequired[
        "capo_direct_connect.types.virtual_interface_state.VirtualInterfaceState"
    ]
    """<p>The state of the virtual interface. The following are the possible values:</p> <ul> <li> <p> <code>confirming</code>: The creation of the virtual interface is pending confirmation from the virtual interface owner. If the owner of the virtual interface is different from the owner of the connection on which it is provisioned, then the virtual interface will remain in this state until it is confirmed by the virtual interface owner.</p> </li> <li> <p> <code>verifying</code>: This state only applies to public virtual interfaces. Each public virtual interface needs validation before the virtual interface can be created.</p> </li> <li> <p> <code>pending</code>: A virtual interface is in this state from the time that it is created until the virtual interface is ready to forward traffic.</p> </li> <li> <p> <code>available</code>: A virtual interface that is able to forward traffic.</p> </li> <li> <p> <code>down</code>: A virtual interface that is BGP down.</p> </li> <li> <p> <code>testing</code>: A virtual interface is in this state immediately after calling <a>StartBgpFailoverTest</a> and remains in this state during the duration of the test.</p> </li> <li> <p> <code>deleting</code>: A virtual interface is in this state immediately after calling <a>DeleteVirtualInterface</a> until it can no longer forward traffic.</p> </li> <li> <p> <code>deleted</code>: A virtual interface that cannot forward traffic.</p> </li> <li> <p> <code>rejected</code>: The virtual interface owner has declined creation of the virtual interface. If a virtual interface in the <code>Confirming</code> state is deleted by the virtual interface owner, the virtual interface enters the <code>Rejected</code> state.</p> </li> <li> <p> <code>unknown</code>: The state of the virtual interface is not available.</p> </li> </ul>"""
    customer_router_config: NotRequired[
        "capo_direct_connect.types.router_config.RouterConfig"
    ]
    """<p>The customer router configuration.</p>"""
    mtu: NotRequired["capo_direct_connect.types.mtu.MTU"]
    """<p>The maximum transmission unit (MTU), in bytes. The supported values are 1500 and 8500. The default value is 1500</p>"""
    jumbo_frame_capable: NotRequired[
        "capo_direct_connect.types.jumbo_frame_capable.JumboFrameCapable"
    ]
    """<p>Indicates whether jumbo frames are supported.</p>"""
    virtual_gateway_id: NotRequired[
        "capo_direct_connect.types.virtual_gateway_id.VirtualGatewayId"
    ]
    """<p>The ID of the virtual private gateway. Applies only to private virtual interfaces.</p>"""
    direct_connect_gateway_id: NotRequired[
        "capo_direct_connect.types.direct_connect_gateway_id.DirectConnectGatewayId"
    ]
    """<p>The ID of the Direct Connect gateway.</p>"""
    route_filter_prefixes: NotRequired[
        "capo_direct_connect.types.route_filter_prefix_list.RouteFilterPrefixList"
    ]
    """<p>The routes to be advertised to the Amazon Web Services network in this Region. Applies to public virtual interfaces.</p>"""
    bgp_peers: NotRequired["capo_direct_connect.types.bgp_peer_list.BGPPeerList"]
    """<p>The BGP peers configured on this virtual interface.</p>"""
    region: NotRequired["capo_direct_connect.types.region.Region"]
    """<p>The Amazon Web Services Region where the virtual interface is located.</p>"""
    aws_device_v2: NotRequired["capo_direct_connect.types.aws_device_v2.AwsDeviceV2"]
    """<p>The Direct Connect endpoint that terminates the physical connection.</p>"""
    aws_logical_device_id: NotRequired[
        "capo_direct_connect.types.aws_logical_device_id.AwsLogicalDeviceId"
    ]
    """<p>The Direct Connect endpoint that terminates the logical connection. This device might be different than the device that terminates the physical connection.</p>"""
    tags: NotRequired["capo_direct_connect.types.tag_list.TagList"]
    """<p>The tags associated with the virtual interface.</p>"""
    site_link_enabled: NotRequired[
        "capo_direct_connect.types.site_link_enabled.SiteLinkEnabled"
    ]
    """<p>Indicates whether SiteLink is enabled.</p>"""
    prefix_pool_allocated_count_ipv4: NotRequired[
        "capo_direct_connect.types.prefix_pool_allocated_count.PrefixPoolAllocatedCount"
    ]
    """<p>The number of inbound IPv4 route prefixes allocated to the virtual interface. Not applicable to public virtual interfaces.</p>"""
    prefix_pool_allocated_count_ipv6: NotRequired[
        "capo_direct_connect.types.prefix_pool_allocated_count.PrefixPoolAllocatedCount"
    ]
    """<p>The number of inbound IPv6 route prefixes allocated to the virtual interface. Not applicable to public virtual interfaces.</p>"""
    rate_limit: NotRequired["capo_direct_connect.types.rate_limit.RateLimit"]
    """<p>The rate limit (bandwidth allocation) applied to the virtual interface. The value must be one of the supported bandwidth values and cannot exceed the bandwidth of the parent connection or LAG. Supported values: <code>50Mbps</code>, <code>100Mbps</code>, <code>200Mbps</code>, <code>300Mbps</code>, <code>400Mbps</code>, <code>500Mbps</code>, <code>600Mbps</code>, <code>700Mbps</code>, <code>800Mbps</code>, <code>900Mbps</code>, <code>1Gbps</code>, <code>1.2Gbps</code>, <code>1.5Gbps</code>, <code>1.8Gbps</code>, <code>2Gbps</code>, <code>2.1Gbps</code>, <code>2.4Gbps</code>, <code>2.7Gbps</code>, <code>3Gbps</code>, <code>3.2Gbps</code>, <code>3.6Gbps</code>, <code>4Gbps</code>, <code>5Gbps</code>, <code>6Gbps</code>, <code>7Gbps</code>, <code>8Gbps</code>, <code>9Gbps</code>, <code>10Gbps</code>, <code>12Gbps</code>, <code>15Gbps</code>, <code>18Gbps</code>, <code>20Gbps</code>, <code>21Gbps</code>, <code>24Gbps</code>, <code>27Gbps</code>, <code>30Gbps</code>, <code>32Gbps</code>, <code>36Gbps</code>, <code>40Gbps</code>, <code>50Gbps</code>, <code>60Gbps</code>, <code>70Gbps</code>, <code>80Gbps</code>, <code>100Gbps</code>, <code>120Gbps</code>, <code>150Gbps</code>, <code>180Gbps</code>, <code>200Gbps</code>, <code>210Gbps</code>, <code>240Gbps</code>, <code>270Gbps</code>, <code>300Gbps</code>, <code>320Gbps</code>, <code>360Gbps</code>, <code>400Gbps</code>, <code>450Gbps</code>, <code>480Gbps</code>, <code>500Gbps</code>, <code>540Gbps</code>, <code>600Gbps</code>, <code>700Gbps</code>, <code>800Gbps</code>, <code>900Gbps</code>, <code>1Tbps</code>, <code>1.1Tbps</code>, <code>1.2Tbps</code>, <code>1.3Tbps</code>, <code>1.4Tbps</code>, <code>1.5Tbps</code>, <code>1.6Tbps</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VirtualInterface) -> dict:
    out: dict = {}
    if "owner_account" in value:
        out["ownerAccount"] = value["owner_account"]
    if "virtual_interface_id" in value:
        out["virtualInterfaceId"] = value["virtual_interface_id"]
    if "location" in value:
        out["location"] = value["location"]
    if "connection_id" in value:
        out["connectionId"] = value["connection_id"]
    if "virtual_interface_type" in value:
        out["virtualInterfaceType"] = value["virtual_interface_type"]
    if "virtual_interface_name" in value:
        out["virtualInterfaceName"] = value["virtual_interface_name"]
    out["vlan"] = value.get("vlan", 0)
    out["asn"] = value.get("asn", 0)
    if "asn_long" in value:
        out["asnLong"] = value["asn_long"]
    if "amazon_side_asn" in value:
        out["amazonSideAsn"] = value["amazon_side_asn"]
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
    if "virtual_interface_state" in value:
        import capo_direct_connect.types.virtual_interface_state

        out["virtualInterfaceState"] = (
            capo_direct_connect.types.virtual_interface_state.serialize_aws_json_1_1(
                value["virtual_interface_state"]
            )
        )
    if "customer_router_config" in value:
        out["customerRouterConfig"] = value["customer_router_config"]
    if "mtu" in value:
        out["mtu"] = value["mtu"]
    if "jumbo_frame_capable" in value:
        out["jumboFrameCapable"] = value["jumbo_frame_capable"]
    if "virtual_gateway_id" in value:
        out["virtualGatewayId"] = value["virtual_gateway_id"]
    if "direct_connect_gateway_id" in value:
        out["directConnectGatewayId"] = value["direct_connect_gateway_id"]
    if "route_filter_prefixes" in value:
        import capo_direct_connect.types.route_filter_prefix_list

        out["routeFilterPrefixes"] = (
            capo_direct_connect.types.route_filter_prefix_list.serialize_aws_json_1_1(
                value["route_filter_prefixes"]
            )
        )
    if "bgp_peers" in value:
        import capo_direct_connect.types.bgp_peer_list

        out["bgpPeers"] = (
            capo_direct_connect.types.bgp_peer_list.serialize_aws_json_1_1(
                value["bgp_peers"]
            )
        )
    if "region" in value:
        out["region"] = value["region"]
    if "aws_device_v2" in value:
        out["awsDeviceV2"] = value["aws_device_v2"]
    if "aws_logical_device_id" in value:
        out["awsLogicalDeviceId"] = value["aws_logical_device_id"]
    if "tags" in value:
        import capo_direct_connect.types.tag_list

        out["tags"] = capo_direct_connect.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "site_link_enabled" in value:
        out["siteLinkEnabled"] = value["site_link_enabled"]
    if "prefix_pool_allocated_count_ipv4" in value:
        out["prefixPoolAllocatedCountIpv4"] = value["prefix_pool_allocated_count_ipv4"]
    if "prefix_pool_allocated_count_ipv6" in value:
        out["prefixPoolAllocatedCountIpv6"] = value["prefix_pool_allocated_count_ipv6"]
    if "rate_limit" in value:
        out["rateLimit"] = value["rate_limit"]
    return out


def deserialize_aws_json_1_1(data: dict) -> VirtualInterface:
    out: VirtualInterface = {}  # type: ignore[typeddict-item]
    if data.get("ownerAccount") is not None:
        out["owner_account"] = data["ownerAccount"]
    if data.get("virtualInterfaceId") is not None:
        out["virtual_interface_id"] = data["virtualInterfaceId"]
    if data.get("location") is not None:
        out["location"] = data["location"]
    if data.get("connectionId") is not None:
        out["connection_id"] = data["connectionId"]
    if data.get("virtualInterfaceType") is not None:
        out["virtual_interface_type"] = data["virtualInterfaceType"]
    if data.get("virtualInterfaceName") is not None:
        out["virtual_interface_name"] = data["virtualInterfaceName"]
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
    if data.get("amazonSideAsn") is not None:
        out["amazon_side_asn"] = data["amazonSideAsn"]
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
    if data.get("virtualInterfaceState") is not None:
        import capo_direct_connect.types.virtual_interface_state

        out["virtual_interface_state"] = (
            capo_direct_connect.types.virtual_interface_state.deserialize_aws_json_1_1(
                data["virtualInterfaceState"]
            )
        )
    if data.get("customerRouterConfig") is not None:
        out["customer_router_config"] = data["customerRouterConfig"]
    if data.get("mtu") is not None:
        out["mtu"] = data["mtu"]
    if data.get("jumboFrameCapable") is not None:
        out["jumbo_frame_capable"] = data["jumboFrameCapable"]
    if data.get("virtualGatewayId") is not None:
        out["virtual_gateway_id"] = data["virtualGatewayId"]
    if data.get("directConnectGatewayId") is not None:
        out["direct_connect_gateway_id"] = data["directConnectGatewayId"]
    if data.get("routeFilterPrefixes") is not None:
        import capo_direct_connect.types.route_filter_prefix_list

        out["route_filter_prefixes"] = (
            capo_direct_connect.types.route_filter_prefix_list.deserialize_aws_json_1_1(
                data["routeFilterPrefixes"]
            )
        )
    if data.get("bgpPeers") is not None:
        import capo_direct_connect.types.bgp_peer_list

        out["bgp_peers"] = (
            capo_direct_connect.types.bgp_peer_list.deserialize_aws_json_1_1(
                data["bgpPeers"]
            )
        )
    if data.get("region") is not None:
        out["region"] = data["region"]
    if data.get("awsDeviceV2") is not None:
        out["aws_device_v2"] = data["awsDeviceV2"]
    if data.get("awsLogicalDeviceId") is not None:
        out["aws_logical_device_id"] = data["awsLogicalDeviceId"]
    if data.get("tags") is not None:
        import capo_direct_connect.types.tag_list

        out["tags"] = capo_direct_connect.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    if data.get("siteLinkEnabled") is not None:
        out["site_link_enabled"] = data["siteLinkEnabled"]
    if data.get("prefixPoolAllocatedCountIpv4") is not None:
        out["prefix_pool_allocated_count_ipv4"] = data["prefixPoolAllocatedCountIpv4"]
    if data.get("prefixPoolAllocatedCountIpv6") is not None:
        out["prefix_pool_allocated_count_ipv6"] = data["prefixPoolAllocatedCountIpv6"]
    if data.get("rateLimit") is not None:
        out["rate_limit"] = data["rateLimit"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: VirtualInterface) -> dict:
    out: dict = {}
    if "owner_account" in value:
        out["ownerAccount"] = value["owner_account"]
    if "virtual_interface_id" in value:
        out["virtualInterfaceId"] = value["virtual_interface_id"]
    if "location" in value:
        out["location"] = value["location"]
    if "connection_id" in value:
        out["connectionId"] = value["connection_id"]
    if "virtual_interface_type" in value:
        out["virtualInterfaceType"] = value["virtual_interface_type"]
    if "virtual_interface_name" in value:
        out["virtualInterfaceName"] = value["virtual_interface_name"]
    out["vlan"] = value.get("vlan", 0)
    out["asn"] = value.get("asn", 0)
    if "asn_long" in value:
        out["asnLong"] = value["asn_long"]
    if "amazon_side_asn" in value:
        out["amazonSideAsn"] = value["amazon_side_asn"]
    if "auth_key" in value:
        out["authKey"] = value["auth_key"]
    if "amazon_address" in value:
        out["amazonAddress"] = value["amazon_address"]
    if "customer_address" in value:
        out["customerAddress"] = value["customer_address"]
    if "address_family" in value:
        import capo_direct_connect.types.address_family

        out["addressFamily"] = capo_direct_connect.types.address_family.serialize_cbor(
            value["address_family"]
        )
    if "virtual_interface_state" in value:
        import capo_direct_connect.types.virtual_interface_state

        out["virtualInterfaceState"] = (
            capo_direct_connect.types.virtual_interface_state.serialize_cbor(
                value["virtual_interface_state"]
            )
        )
    if "customer_router_config" in value:
        out["customerRouterConfig"] = value["customer_router_config"]
    if "mtu" in value:
        out["mtu"] = value["mtu"]
    if "jumbo_frame_capable" in value:
        out["jumboFrameCapable"] = value["jumbo_frame_capable"]
    if "virtual_gateway_id" in value:
        out["virtualGatewayId"] = value["virtual_gateway_id"]
    if "direct_connect_gateway_id" in value:
        out["directConnectGatewayId"] = value["direct_connect_gateway_id"]
    if "route_filter_prefixes" in value:
        import capo_direct_connect.types.route_filter_prefix_list

        out["routeFilterPrefixes"] = (
            capo_direct_connect.types.route_filter_prefix_list.serialize_cbor(
                value["route_filter_prefixes"]
            )
        )
    if "bgp_peers" in value:
        import capo_direct_connect.types.bgp_peer_list

        out["bgpPeers"] = capo_direct_connect.types.bgp_peer_list.serialize_cbor(
            value["bgp_peers"]
        )
    if "region" in value:
        out["region"] = value["region"]
    if "aws_device_v2" in value:
        out["awsDeviceV2"] = value["aws_device_v2"]
    if "aws_logical_device_id" in value:
        out["awsLogicalDeviceId"] = value["aws_logical_device_id"]
    if "tags" in value:
        import capo_direct_connect.types.tag_list

        out["tags"] = capo_direct_connect.types.tag_list.serialize_cbor(value["tags"])
    if "site_link_enabled" in value:
        out["siteLinkEnabled"] = value["site_link_enabled"]
    if "prefix_pool_allocated_count_ipv4" in value:
        out["prefixPoolAllocatedCountIpv4"] = value["prefix_pool_allocated_count_ipv4"]
    if "prefix_pool_allocated_count_ipv6" in value:
        out["prefixPoolAllocatedCountIpv6"] = value["prefix_pool_allocated_count_ipv6"]
    if "rate_limit" in value:
        out["rateLimit"] = value["rate_limit"]
    return out


def deserialize_cbor(data: dict) -> VirtualInterface:
    out: VirtualInterface = {}  # type: ignore[typeddict-item]
    if data.get("ownerAccount") is not None:
        out["owner_account"] = data["ownerAccount"]
    if data.get("virtualInterfaceId") is not None:
        out["virtual_interface_id"] = data["virtualInterfaceId"]
    if data.get("location") is not None:
        out["location"] = data["location"]
    if data.get("connectionId") is not None:
        out["connection_id"] = data["connectionId"]
    if data.get("virtualInterfaceType") is not None:
        out["virtual_interface_type"] = data["virtualInterfaceType"]
    if data.get("virtualInterfaceName") is not None:
        out["virtual_interface_name"] = data["virtualInterfaceName"]
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
    if data.get("amazonSideAsn") is not None:
        out["amazon_side_asn"] = data["amazonSideAsn"]
    if data.get("authKey") is not None:
        out["auth_key"] = data["authKey"]
    if data.get("amazonAddress") is not None:
        out["amazon_address"] = data["amazonAddress"]
    if data.get("customerAddress") is not None:
        out["customer_address"] = data["customerAddress"]
    if data.get("addressFamily") is not None:
        import capo_direct_connect.types.address_family

        out["address_family"] = (
            capo_direct_connect.types.address_family.deserialize_cbor(
                data["addressFamily"]
            )
        )
    if data.get("virtualInterfaceState") is not None:
        import capo_direct_connect.types.virtual_interface_state

        out["virtual_interface_state"] = (
            capo_direct_connect.types.virtual_interface_state.deserialize_cbor(
                data["virtualInterfaceState"]
            )
        )
    if data.get("customerRouterConfig") is not None:
        out["customer_router_config"] = data["customerRouterConfig"]
    if data.get("mtu") is not None:
        out["mtu"] = data["mtu"]
    if data.get("jumboFrameCapable") is not None:
        out["jumbo_frame_capable"] = data["jumboFrameCapable"]
    if data.get("virtualGatewayId") is not None:
        out["virtual_gateway_id"] = data["virtualGatewayId"]
    if data.get("directConnectGatewayId") is not None:
        out["direct_connect_gateway_id"] = data["directConnectGatewayId"]
    if data.get("routeFilterPrefixes") is not None:
        import capo_direct_connect.types.route_filter_prefix_list

        out["route_filter_prefixes"] = (
            capo_direct_connect.types.route_filter_prefix_list.deserialize_cbor(
                data["routeFilterPrefixes"]
            )
        )
    if data.get("bgpPeers") is not None:
        import capo_direct_connect.types.bgp_peer_list

        out["bgp_peers"] = capo_direct_connect.types.bgp_peer_list.deserialize_cbor(
            data["bgpPeers"]
        )
    if data.get("region") is not None:
        out["region"] = data["region"]
    if data.get("awsDeviceV2") is not None:
        out["aws_device_v2"] = data["awsDeviceV2"]
    if data.get("awsLogicalDeviceId") is not None:
        out["aws_logical_device_id"] = data["awsLogicalDeviceId"]
    if data.get("tags") is not None:
        import capo_direct_connect.types.tag_list

        out["tags"] = capo_direct_connect.types.tag_list.deserialize_cbor(data["tags"])
    if data.get("siteLinkEnabled") is not None:
        out["site_link_enabled"] = data["siteLinkEnabled"]
    if data.get("prefixPoolAllocatedCountIpv4") is not None:
        out["prefix_pool_allocated_count_ipv4"] = data["prefixPoolAllocatedCountIpv4"]
    if data.get("prefixPoolAllocatedCountIpv6") is not None:
        out["prefix_pool_allocated_count_ipv6"] = data["prefixPoolAllocatedCountIpv6"]
    if data.get("rateLimit") is not None:
        out["rate_limit"] = data["rateLimit"]
    return out
