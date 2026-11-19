"""Generated from Smithy shape ``com.amazonaws.directconnect#Connection``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_direct_connect.types.aws_device
    import capo_direct_connect.types.aws_device_v2
    import capo_direct_connect.types.aws_logical_device_id
    import capo_direct_connect.types.bandwidth
    import capo_direct_connect.types.billing_mode
    import capo_direct_connect.types.connection_id
    import capo_direct_connect.types.connection_name
    import capo_direct_connect.types.connection_state
    import capo_direct_connect.types.encryption_mode
    import capo_direct_connect.types.has_logical_redundancy
    import capo_direct_connect.types.jumbo_frame_capable
    import capo_direct_connect.types.lag_id
    import capo_direct_connect.types.loa_issue_time
    import capo_direct_connect.types.location_code
    import capo_direct_connect.types.mac_sec_capable
    import capo_direct_connect.types.mac_sec_key_list
    import capo_direct_connect.types.owner_account
    import capo_direct_connect.types.partner_interconnect_mac_sec_capable
    import capo_direct_connect.types.partner_name
    import capo_direct_connect.types.port_encryption_status
    import capo_direct_connect.types.prefix_pool_size
    import capo_direct_connect.types.prefix_pool_unallocated_count
    import capo_direct_connect.types.provider_name
    import capo_direct_connect.types.rate_limiter_status
    import capo_direct_connect.types.region
    import capo_direct_connect.types.tag_list
    import capo_direct_connect.types.vlan


class Connection(TypedDict, closed=True):
    owner_account: NotRequired["capo_direct_connect.types.owner_account.OwnerAccount"]
    """<p>The ID of the Amazon Web Services account that owns the connection.</p>"""
    connection_id: NotRequired["capo_direct_connect.types.connection_id.ConnectionId"]
    """<p>The ID of the connection.</p>"""
    connection_name: NotRequired[
        "capo_direct_connect.types.connection_name.ConnectionName"
    ]
    """<p>The name of the connection.</p>"""
    connection_state: NotRequired[
        "capo_direct_connect.types.connection_state.ConnectionState"
    ]
    """<p>The state of the connection. The following are the possible values:</p> <ul> <li> <p> <code>ordering</code>: The initial state of a hosted connection provisioned on an interconnect. The connection stays in the ordering state until the owner of the hosted connection confirms or declines the connection order.</p> </li> <li> <p> <code>requested</code>: The initial state of a standard connection. The connection stays in the requested state until the Letter of Authorization (LOA) is sent to the customer.</p> </li> <li> <p> <code>pending</code>: The connection has been approved and is being initialized.</p> </li> <li> <p> <code>available</code>: The network link is up and the connection is ready for use.</p> </li> <li> <p> <code>down</code>: The network link is down.</p> </li> <li> <p> <code>deleting</code>: The connection is being deleted.</p> </li> <li> <p> <code>deleted</code>: The connection has been deleted.</p> </li> <li> <p> <code>rejected</code>: A hosted connection in the <code>ordering</code> state enters the <code>rejected</code> state if it is deleted by the customer.</p> </li> <li> <p> <code>unknown</code>: The state of the connection is not available.</p> </li> </ul>"""
    region: NotRequired["capo_direct_connect.types.region.Region"]
    """<p>The Amazon Web Services Region where the connection is located.</p>"""
    location: NotRequired["capo_direct_connect.types.location_code.LocationCode"]
    """<p>The location of the connection.</p>"""
    bandwidth: NotRequired["capo_direct_connect.types.bandwidth.Bandwidth"]
    """<p>The bandwidth of the connection.</p>"""
    vlan: "capo_direct_connect.types.vlan.VLAN"
    """<p>The ID of the VLAN.</p>"""
    partner_name: NotRequired["capo_direct_connect.types.partner_name.PartnerName"]
    """<p>The name of the Direct Connect service provider associated with the connection.</p>"""
    loa_issue_time: NotRequired["capo_direct_connect.types.loa_issue_time.LoaIssueTime"]
    """<p>The time of the most recent call to <a>DescribeLoa</a> for this connection.</p>"""
    lag_id: NotRequired["capo_direct_connect.types.lag_id.LagId"]
    """<p>The ID of the LAG.</p>"""
    aws_device: NotRequired["capo_direct_connect.types.aws_device.AwsDevice"]
    """<p>The Direct Connect endpoint on which the physical connection terminates.</p>"""
    jumbo_frame_capable: NotRequired[
        "capo_direct_connect.types.jumbo_frame_capable.JumboFrameCapable"
    ]
    """<p>Indicates whether jumbo frames are supported.</p>"""
    aws_device_v2: NotRequired["capo_direct_connect.types.aws_device_v2.AwsDeviceV2"]
    """<p>The Direct Connect endpoint that terminates the physical connection.</p>"""
    aws_logical_device_id: NotRequired[
        "capo_direct_connect.types.aws_logical_device_id.AwsLogicalDeviceId"
    ]
    """<p>The Direct Connect endpoint that terminates the logical connection. This device might be different than the device that terminates the physical connection.</p>"""
    has_logical_redundancy: NotRequired[
        "capo_direct_connect.types.has_logical_redundancy.HasLogicalRedundancy"
    ]
    """<p>Indicates whether the connection supports a secondary BGP peer in the same address family (IPv4/IPv6).</p>"""
    tags: NotRequired["capo_direct_connect.types.tag_list.TagList"]
    """<p>The tags associated with the connection.</p>"""
    provider_name: NotRequired["capo_direct_connect.types.provider_name.ProviderName"]
    """<p>The name of the service provider associated with the connection.</p>"""
    mac_sec_capable: NotRequired[
        "capo_direct_connect.types.mac_sec_capable.MacSecCapable"
    ]
    """<p>Indicates whether the connection supports MAC Security (MACsec).</p>"""
    port_encryption_status: NotRequired[
        "capo_direct_connect.types.port_encryption_status.PortEncryptionStatus"
    ]
    """<p>The MAC Security (MACsec) port link status of the connection.</p> <p>The valid values are <code>Encryption Up</code>, which means that there is an active Connection Key Name, or <code>Encryption Down</code>.</p>"""
    encryption_mode: NotRequired[
        "capo_direct_connect.types.encryption_mode.EncryptionMode"
    ]
    """<p>The MAC Security (MACsec) connection encryption mode.</p> <p>The valid values are <code>no_encrypt</code>, <code>should_encrypt</code>, and <code>must_encrypt</code>.</p>"""
    mac_sec_keys: NotRequired[
        "capo_direct_connect.types.mac_sec_key_list.MacSecKeyList"
    ]
    """<p>The MAC Security (MACsec) security keys associated with the connection.</p>"""
    rate_limiter_status: NotRequired[
        "capo_direct_connect.types.rate_limiter_status.RateLimiterStatus"
    ]
    """<p>The rate limiter status for the connection, including how many rate limiters are in use and the maximum allowed.</p>"""
    partner_interconnect_mac_sec_capable: NotRequired[
        "capo_direct_connect.types.partner_interconnect_mac_sec_capable.PartnerInterconnectMacSecCapable"
    ]
    """<p>Indicates whether the interconnect hosting this connection supports MAC Security (MACsec).</p>"""
    prefix_pool_size_ipv4: NotRequired[
        "capo_direct_connect.types.prefix_pool_size.PrefixPoolSize"
    ]
    """<p>The total number of inbound IPv4 route prefixes you can allocate across the virtual interfaces on the connection. Not applicable to hosted connections or interconnects.</p>"""
    prefix_pool_size_ipv6: NotRequired[
        "capo_direct_connect.types.prefix_pool_size.PrefixPoolSize"
    ]
    """<p>The total number of inbound IPv6 route prefixes you can allocate across the virtual interfaces on the connection. Not applicable to hosted connections or interconnects.</p>"""
    prefix_pool_unallocated_count_ipv4: NotRequired[
        "capo_direct_connect.types.prefix_pool_unallocated_count.PrefixPoolUnallocatedCount"
    ]
    """<p>The number of inbound IPv4 route prefixes in the connection prefix pool not yet allocated to a virtual interface. Not applicable to hosted connections or interconnects.</p>"""
    prefix_pool_unallocated_count_ipv6: NotRequired[
        "capo_direct_connect.types.prefix_pool_unallocated_count.PrefixPoolUnallocatedCount"
    ]
    """<p>The number of inbound IPv6 route prefixes in the connection prefix pool not yet allocated to a virtual interface. Not applicable to hosted connections or interconnects.</p>"""
    billing_mode: NotRequired["capo_direct_connect.types.billing_mode.BillingMode"]
    """<p>The billing mode of the connection.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Connection) -> dict:
    out: dict = {}
    if "owner_account" in value:
        out["ownerAccount"] = value["owner_account"]
    if "connection_id" in value:
        out["connectionId"] = value["connection_id"]
    if "connection_name" in value:
        out["connectionName"] = value["connection_name"]
    if "connection_state" in value:
        import capo_direct_connect.types.connection_state

        out["connectionState"] = (
            capo_direct_connect.types.connection_state.serialize_aws_json_1_1(
                value["connection_state"]
            )
        )
    if "region" in value:
        out["region"] = value["region"]
    if "location" in value:
        out["location"] = value["location"]
    if "bandwidth" in value:
        out["bandwidth"] = value["bandwidth"]
    out["vlan"] = value.get("vlan", 0)
    if "partner_name" in value:
        out["partnerName"] = value["partner_name"]
    if "loa_issue_time" in value:
        import capo_direct_connect.types.loa_issue_time

        out["loaIssueTime"] = (
            capo_direct_connect.types.loa_issue_time.serialize_aws_json_1_1(
                value["loa_issue_time"]
            )
        )
    if "lag_id" in value:
        out["lagId"] = value["lag_id"]
    if "aws_device" in value:
        out["awsDevice"] = value["aws_device"]
    if "jumbo_frame_capable" in value:
        out["jumboFrameCapable"] = value["jumbo_frame_capable"]
    if "aws_device_v2" in value:
        out["awsDeviceV2"] = value["aws_device_v2"]
    if "aws_logical_device_id" in value:
        out["awsLogicalDeviceId"] = value["aws_logical_device_id"]
    if "has_logical_redundancy" in value:
        import capo_direct_connect.types.has_logical_redundancy

        out["hasLogicalRedundancy"] = (
            capo_direct_connect.types.has_logical_redundancy.serialize_aws_json_1_1(
                value["has_logical_redundancy"]
            )
        )
    if "tags" in value:
        import capo_direct_connect.types.tag_list

        out["tags"] = capo_direct_connect.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "provider_name" in value:
        out["providerName"] = value["provider_name"]
    if "mac_sec_capable" in value:
        out["macSecCapable"] = value["mac_sec_capable"]
    if "port_encryption_status" in value:
        out["portEncryptionStatus"] = value["port_encryption_status"]
    if "encryption_mode" in value:
        out["encryptionMode"] = value["encryption_mode"]
    if "mac_sec_keys" in value:
        import capo_direct_connect.types.mac_sec_key_list

        out["macSecKeys"] = (
            capo_direct_connect.types.mac_sec_key_list.serialize_aws_json_1_1(
                value["mac_sec_keys"]
            )
        )
    if "rate_limiter_status" in value:
        import capo_direct_connect.types.rate_limiter_status

        out["rateLimiterStatus"] = (
            capo_direct_connect.types.rate_limiter_status.serialize_aws_json_1_1(
                value["rate_limiter_status"]
            )
        )
    if "partner_interconnect_mac_sec_capable" in value:
        out["partnerInterconnectMacSecCapable"] = value[
            "partner_interconnect_mac_sec_capable"
        ]
    if "prefix_pool_size_ipv4" in value:
        out["prefixPoolSizeIpv4"] = value["prefix_pool_size_ipv4"]
    if "prefix_pool_size_ipv6" in value:
        out["prefixPoolSizeIpv6"] = value["prefix_pool_size_ipv6"]
    if "prefix_pool_unallocated_count_ipv4" in value:
        out["prefixPoolUnallocatedCountIpv4"] = value[
            "prefix_pool_unallocated_count_ipv4"
        ]
    if "prefix_pool_unallocated_count_ipv6" in value:
        out["prefixPoolUnallocatedCountIpv6"] = value[
            "prefix_pool_unallocated_count_ipv6"
        ]
    if "billing_mode" in value:
        import capo_direct_connect.types.billing_mode

        out["billingMode"] = (
            capo_direct_connect.types.billing_mode.serialize_aws_json_1_1(
                value["billing_mode"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Connection:
    out: Connection = {}  # type: ignore[typeddict-item]
    if data.get("ownerAccount") is not None:
        out["owner_account"] = data["ownerAccount"]
    if data.get("connectionId") is not None:
        out["connection_id"] = data["connectionId"]
    if data.get("connectionName") is not None:
        out["connection_name"] = data["connectionName"]
    if data.get("connectionState") is not None:
        import capo_direct_connect.types.connection_state

        out["connection_state"] = (
            capo_direct_connect.types.connection_state.deserialize_aws_json_1_1(
                data["connectionState"]
            )
        )
    if data.get("region") is not None:
        out["region"] = data["region"]
    if data.get("location") is not None:
        out["location"] = data["location"]
    if data.get("bandwidth") is not None:
        out["bandwidth"] = data["bandwidth"]
    if data.get("vlan") is not None:
        out["vlan"] = data["vlan"]
    else:
        out["vlan"] = 0
    if data.get("partnerName") is not None:
        out["partner_name"] = data["partnerName"]
    if data.get("loaIssueTime") is not None:
        import capo_direct_connect.types.loa_issue_time

        out["loa_issue_time"] = (
            capo_direct_connect.types.loa_issue_time.deserialize_aws_json_1_1(
                data["loaIssueTime"]
            )
        )
    if data.get("lagId") is not None:
        out["lag_id"] = data["lagId"]
    if data.get("awsDevice") is not None:
        out["aws_device"] = data["awsDevice"]
    if data.get("jumboFrameCapable") is not None:
        out["jumbo_frame_capable"] = data["jumboFrameCapable"]
    if data.get("awsDeviceV2") is not None:
        out["aws_device_v2"] = data["awsDeviceV2"]
    if data.get("awsLogicalDeviceId") is not None:
        out["aws_logical_device_id"] = data["awsLogicalDeviceId"]
    if data.get("hasLogicalRedundancy") is not None:
        import capo_direct_connect.types.has_logical_redundancy

        out["has_logical_redundancy"] = (
            capo_direct_connect.types.has_logical_redundancy.deserialize_aws_json_1_1(
                data["hasLogicalRedundancy"]
            )
        )
    if data.get("tags") is not None:
        import capo_direct_connect.types.tag_list

        out["tags"] = capo_direct_connect.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    if data.get("providerName") is not None:
        out["provider_name"] = data["providerName"]
    if data.get("macSecCapable") is not None:
        out["mac_sec_capable"] = data["macSecCapable"]
    if data.get("portEncryptionStatus") is not None:
        out["port_encryption_status"] = data["portEncryptionStatus"]
    if data.get("encryptionMode") is not None:
        out["encryption_mode"] = data["encryptionMode"]
    if data.get("macSecKeys") is not None:
        import capo_direct_connect.types.mac_sec_key_list

        out["mac_sec_keys"] = (
            capo_direct_connect.types.mac_sec_key_list.deserialize_aws_json_1_1(
                data["macSecKeys"]
            )
        )
    if data.get("rateLimiterStatus") is not None:
        import capo_direct_connect.types.rate_limiter_status

        out["rate_limiter_status"] = (
            capo_direct_connect.types.rate_limiter_status.deserialize_aws_json_1_1(
                data["rateLimiterStatus"]
            )
        )
    if data.get("partnerInterconnectMacSecCapable") is not None:
        out["partner_interconnect_mac_sec_capable"] = data[
            "partnerInterconnectMacSecCapable"
        ]
    if data.get("prefixPoolSizeIpv4") is not None:
        out["prefix_pool_size_ipv4"] = data["prefixPoolSizeIpv4"]
    if data.get("prefixPoolSizeIpv6") is not None:
        out["prefix_pool_size_ipv6"] = data["prefixPoolSizeIpv6"]
    if data.get("prefixPoolUnallocatedCountIpv4") is not None:
        out["prefix_pool_unallocated_count_ipv4"] = data[
            "prefixPoolUnallocatedCountIpv4"
        ]
    if data.get("prefixPoolUnallocatedCountIpv6") is not None:
        out["prefix_pool_unallocated_count_ipv6"] = data[
            "prefixPoolUnallocatedCountIpv6"
        ]
    if data.get("billingMode") is not None:
        import capo_direct_connect.types.billing_mode

        out["billing_mode"] = (
            capo_direct_connect.types.billing_mode.deserialize_aws_json_1_1(
                data["billingMode"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Connection) -> dict:
    out: dict = {}
    if "owner_account" in value:
        out["ownerAccount"] = value["owner_account"]
    if "connection_id" in value:
        out["connectionId"] = value["connection_id"]
    if "connection_name" in value:
        out["connectionName"] = value["connection_name"]
    if "connection_state" in value:
        import capo_direct_connect.types.connection_state

        out["connectionState"] = (
            capo_direct_connect.types.connection_state.serialize_cbor(
                value["connection_state"]
            )
        )
    if "region" in value:
        out["region"] = value["region"]
    if "location" in value:
        out["location"] = value["location"]
    if "bandwidth" in value:
        out["bandwidth"] = value["bandwidth"]
    out["vlan"] = value.get("vlan", 0)
    if "partner_name" in value:
        out["partnerName"] = value["partner_name"]
    if "loa_issue_time" in value:
        import capo_direct_connect.types.loa_issue_time

        out["loaIssueTime"] = capo_direct_connect.types.loa_issue_time.serialize_cbor(
            value["loa_issue_time"]
        )
    if "lag_id" in value:
        out["lagId"] = value["lag_id"]
    if "aws_device" in value:
        out["awsDevice"] = value["aws_device"]
    if "jumbo_frame_capable" in value:
        out["jumboFrameCapable"] = value["jumbo_frame_capable"]
    if "aws_device_v2" in value:
        out["awsDeviceV2"] = value["aws_device_v2"]
    if "aws_logical_device_id" in value:
        out["awsLogicalDeviceId"] = value["aws_logical_device_id"]
    if "has_logical_redundancy" in value:
        import capo_direct_connect.types.has_logical_redundancy

        out["hasLogicalRedundancy"] = (
            capo_direct_connect.types.has_logical_redundancy.serialize_cbor(
                value["has_logical_redundancy"]
            )
        )
    if "tags" in value:
        import capo_direct_connect.types.tag_list

        out["tags"] = capo_direct_connect.types.tag_list.serialize_cbor(value["tags"])
    if "provider_name" in value:
        out["providerName"] = value["provider_name"]
    if "mac_sec_capable" in value:
        out["macSecCapable"] = value["mac_sec_capable"]
    if "port_encryption_status" in value:
        out["portEncryptionStatus"] = value["port_encryption_status"]
    if "encryption_mode" in value:
        out["encryptionMode"] = value["encryption_mode"]
    if "mac_sec_keys" in value:
        import capo_direct_connect.types.mac_sec_key_list

        out["macSecKeys"] = capo_direct_connect.types.mac_sec_key_list.serialize_cbor(
            value["mac_sec_keys"]
        )
    if "rate_limiter_status" in value:
        import capo_direct_connect.types.rate_limiter_status

        out["rateLimiterStatus"] = (
            capo_direct_connect.types.rate_limiter_status.serialize_cbor(
                value["rate_limiter_status"]
            )
        )
    if "partner_interconnect_mac_sec_capable" in value:
        out["partnerInterconnectMacSecCapable"] = value[
            "partner_interconnect_mac_sec_capable"
        ]
    if "prefix_pool_size_ipv4" in value:
        out["prefixPoolSizeIpv4"] = value["prefix_pool_size_ipv4"]
    if "prefix_pool_size_ipv6" in value:
        out["prefixPoolSizeIpv6"] = value["prefix_pool_size_ipv6"]
    if "prefix_pool_unallocated_count_ipv4" in value:
        out["prefixPoolUnallocatedCountIpv4"] = value[
            "prefix_pool_unallocated_count_ipv4"
        ]
    if "prefix_pool_unallocated_count_ipv6" in value:
        out["prefixPoolUnallocatedCountIpv6"] = value[
            "prefix_pool_unallocated_count_ipv6"
        ]
    if "billing_mode" in value:
        import capo_direct_connect.types.billing_mode

        out["billingMode"] = capo_direct_connect.types.billing_mode.serialize_cbor(
            value["billing_mode"]
        )
    return out


def deserialize_cbor(data: dict) -> Connection:
    out: Connection = {}  # type: ignore[typeddict-item]
    if data.get("ownerAccount") is not None:
        out["owner_account"] = data["ownerAccount"]
    if data.get("connectionId") is not None:
        out["connection_id"] = data["connectionId"]
    if data.get("connectionName") is not None:
        out["connection_name"] = data["connectionName"]
    if data.get("connectionState") is not None:
        import capo_direct_connect.types.connection_state

        out["connection_state"] = (
            capo_direct_connect.types.connection_state.deserialize_cbor(
                data["connectionState"]
            )
        )
    if data.get("region") is not None:
        out["region"] = data["region"]
    if data.get("location") is not None:
        out["location"] = data["location"]
    if data.get("bandwidth") is not None:
        out["bandwidth"] = data["bandwidth"]
    if data.get("vlan") is not None:
        out["vlan"] = data["vlan"]
    else:
        out["vlan"] = 0
    if data.get("partnerName") is not None:
        out["partner_name"] = data["partnerName"]
    if data.get("loaIssueTime") is not None:
        import capo_direct_connect.types.loa_issue_time

        out["loa_issue_time"] = (
            capo_direct_connect.types.loa_issue_time.deserialize_cbor(
                data["loaIssueTime"]
            )
        )
    if data.get("lagId") is not None:
        out["lag_id"] = data["lagId"]
    if data.get("awsDevice") is not None:
        out["aws_device"] = data["awsDevice"]
    if data.get("jumboFrameCapable") is not None:
        out["jumbo_frame_capable"] = data["jumboFrameCapable"]
    if data.get("awsDeviceV2") is not None:
        out["aws_device_v2"] = data["awsDeviceV2"]
    if data.get("awsLogicalDeviceId") is not None:
        out["aws_logical_device_id"] = data["awsLogicalDeviceId"]
    if data.get("hasLogicalRedundancy") is not None:
        import capo_direct_connect.types.has_logical_redundancy

        out["has_logical_redundancy"] = (
            capo_direct_connect.types.has_logical_redundancy.deserialize_cbor(
                data["hasLogicalRedundancy"]
            )
        )
    if data.get("tags") is not None:
        import capo_direct_connect.types.tag_list

        out["tags"] = capo_direct_connect.types.tag_list.deserialize_cbor(data["tags"])
    if data.get("providerName") is not None:
        out["provider_name"] = data["providerName"]
    if data.get("macSecCapable") is not None:
        out["mac_sec_capable"] = data["macSecCapable"]
    if data.get("portEncryptionStatus") is not None:
        out["port_encryption_status"] = data["portEncryptionStatus"]
    if data.get("encryptionMode") is not None:
        out["encryption_mode"] = data["encryptionMode"]
    if data.get("macSecKeys") is not None:
        import capo_direct_connect.types.mac_sec_key_list

        out["mac_sec_keys"] = (
            capo_direct_connect.types.mac_sec_key_list.deserialize_cbor(
                data["macSecKeys"]
            )
        )
    if data.get("rateLimiterStatus") is not None:
        import capo_direct_connect.types.rate_limiter_status

        out["rate_limiter_status"] = (
            capo_direct_connect.types.rate_limiter_status.deserialize_cbor(
                data["rateLimiterStatus"]
            )
        )
    if data.get("partnerInterconnectMacSecCapable") is not None:
        out["partner_interconnect_mac_sec_capable"] = data[
            "partnerInterconnectMacSecCapable"
        ]
    if data.get("prefixPoolSizeIpv4") is not None:
        out["prefix_pool_size_ipv4"] = data["prefixPoolSizeIpv4"]
    if data.get("prefixPoolSizeIpv6") is not None:
        out["prefix_pool_size_ipv6"] = data["prefixPoolSizeIpv6"]
    if data.get("prefixPoolUnallocatedCountIpv4") is not None:
        out["prefix_pool_unallocated_count_ipv4"] = data[
            "prefixPoolUnallocatedCountIpv4"
        ]
    if data.get("prefixPoolUnallocatedCountIpv6") is not None:
        out["prefix_pool_unallocated_count_ipv6"] = data[
            "prefixPoolUnallocatedCountIpv6"
        ]
    if data.get("billingMode") is not None:
        import capo_direct_connect.types.billing_mode

        out["billing_mode"] = capo_direct_connect.types.billing_mode.deserialize_cbor(
            data["billingMode"]
        )
    return out
