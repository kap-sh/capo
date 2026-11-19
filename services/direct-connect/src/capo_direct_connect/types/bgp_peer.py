"""Generated from Smithy shape ``com.amazonaws.directconnect#BGPPeer``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_direct_connect.types.address_family
    import capo_direct_connect.types.amazon_address
    import capo_direct_connect.types.asn
    import capo_direct_connect.types.aws_device_v2
    import capo_direct_connect.types.aws_logical_device_id
    import capo_direct_connect.types.bgp_auth_key
    import capo_direct_connect.types.bgp_peer_id
    import capo_direct_connect.types.bgp_peer_state
    import capo_direct_connect.types.bgp_status
    import capo_direct_connect.types.customer_address
    import capo_direct_connect.types.long_asn


class BGPPeer(TypedDict, closed=True):
    bgp_peer_id: NotRequired["capo_direct_connect.types.bgp_peer_id.BGPPeerId"]
    """<p>The ID of the BGP peer.</p>"""
    asn: "capo_direct_connect.types.asn.ASN"
    """<p>The autonomous system number (ASN). The valid range is from 1 to 2147483646 for Border Gateway Protocol (BGP) configuration. If you provide a number greater than the maximum, an error is returned. Use <code>asnLong</code> instead.</p> <ul> <li> <p>You can use <code>asnLong</code> or <code>asn</code>, but not both. We recommend using <code>asnLong</code> as it supports a greater pool of numbers. </p> </li> <li> <p>If you provide a value in the same API call for both <code>asn</code> and <code>asnLong</code>, the API will only accept the value for <code>asnLong</code>. </p> </li> <li> <p>If you enter a 4-byte ASN for the <code>asn</code> parameter, the API returns an error. </p> </li> <li> <p>If you are using a 2-byte ASN, the API response will include the 2-byte value for both the <code>asn</code> and <code>asnLong</code> fields.</p> </li> </ul>"""
    asn_long: NotRequired["capo_direct_connect.types.long_asn.LongAsn"]
    """<p>The long ASN for the BGP peer. The valid range is from 1 to 4294967294 for BGP configuration. </p> <p>Note the following limitations when using <code>asnLong</code>:</p> <ul> <li> <p>You can use <code>asnLong</code> or <code>asn</code>, but not both. We recommend using <code>asnLong</code> as it supports a greater pool of numbers. </p> </li> <li> <p> <code>asnLong</code> accepts any valid ASN value, regardless if it's 2-byte or 4-byte. </p> </li> <li> <p>When using a 4-byte <code>asnLong</code>, the API response returns <code>0</code> for the legacy <code>asn</code> attribute since 4-byte ASN values exceed the maximum supported value of 2,147,483,647.</p> </li> <li> <p>If you are using a 2-byte ASN, the API response will include the 2-byte value for both the <code>asn</code> and <code>asnLong</code> fields.</p> </li> <li> <p>If you provide a value in the same API call for both <code>asn</code> and <code>asnLong</code>, the API will only accept the value for <code>asnLong</code>.</p> </li> </ul>"""
    auth_key: NotRequired["capo_direct_connect.types.bgp_auth_key.BGPAuthKey"]
    """<p>The authentication key for BGP configuration. This string has a minimum length of 6 characters and and a maximun lenth of 80 characters.</p>"""
    address_family: NotRequired[
        "capo_direct_connect.types.address_family.AddressFamily"
    ]
    """<p>The address family for the BGP peer.</p>"""
    amazon_address: NotRequired[
        "capo_direct_connect.types.amazon_address.AmazonAddress"
    ]
    """<p>The IP address assigned to the Amazon interface.</p>"""
    customer_address: NotRequired[
        "capo_direct_connect.types.customer_address.CustomerAddress"
    ]
    """<p>The IP address assigned to the customer interface.</p>"""
    bgp_peer_state: NotRequired["capo_direct_connect.types.bgp_peer_state.BGPPeerState"]
    """<p>The state of the BGP peer. The following are the possible values:</p> <ul> <li> <p> <code>verifying</code>: The BGP peering addresses or ASN require validation before the BGP peer can be created. This state applies only to public virtual interfaces.</p> </li> <li> <p> <code>pending</code>: The BGP peer is created, and remains in this state until it is ready to be established.</p> </li> <li> <p> <code>available</code>: The BGP peer is ready to be established.</p> </li> <li> <p> <code>deleting</code>: The BGP peer is being deleted.</p> </li> <li> <p> <code>deleted</code>: The BGP peer is deleted and cannot be established.</p> </li> </ul>"""
    bgp_status: NotRequired["capo_direct_connect.types.bgp_status.BGPStatus"]
    """<p>The status of the BGP peer. The following are the possible values:</p> <ul> <li> <p> <code>up</code>: The BGP peer is established. This state does not indicate the state of the routing function. Ensure that you are receiving routes over the BGP session.</p> </li> <li> <p> <code>down</code>: The BGP peer is down.</p> </li> <li> <p> <code>unknown</code>: The BGP peer status is not available.</p> </li> </ul>"""
    aws_device_v2: NotRequired["capo_direct_connect.types.aws_device_v2.AwsDeviceV2"]
    """<p>The Direct Connect endpoint that terminates the BGP peer.</p>"""
    aws_logical_device_id: NotRequired[
        "capo_direct_connect.types.aws_logical_device_id.AwsLogicalDeviceId"
    ]
    """<p>The Direct Connect endpoint that terminates the logical connection. This device might be different than the device that terminates the physical connection.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BGPPeer) -> dict:
    out: dict = {}
    if "bgp_peer_id" in value:
        out["bgpPeerId"] = value["bgp_peer_id"]
    out["asn"] = value.get("asn", 0)
    if "asn_long" in value:
        out["asnLong"] = value["asn_long"]
    if "auth_key" in value:
        out["authKey"] = value["auth_key"]
    if "address_family" in value:
        import capo_direct_connect.types.address_family

        out["addressFamily"] = (
            capo_direct_connect.types.address_family.serialize_aws_json_1_1(
                value["address_family"]
            )
        )
    if "amazon_address" in value:
        out["amazonAddress"] = value["amazon_address"]
    if "customer_address" in value:
        out["customerAddress"] = value["customer_address"]
    if "bgp_peer_state" in value:
        import capo_direct_connect.types.bgp_peer_state

        out["bgpPeerState"] = (
            capo_direct_connect.types.bgp_peer_state.serialize_aws_json_1_1(
                value["bgp_peer_state"]
            )
        )
    if "bgp_status" in value:
        import capo_direct_connect.types.bgp_status

        out["bgpStatus"] = capo_direct_connect.types.bgp_status.serialize_aws_json_1_1(
            value["bgp_status"]
        )
    if "aws_device_v2" in value:
        out["awsDeviceV2"] = value["aws_device_v2"]
    if "aws_logical_device_id" in value:
        out["awsLogicalDeviceId"] = value["aws_logical_device_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> BGPPeer:
    out: BGPPeer = {}  # type: ignore[typeddict-item]
    if data.get("bgpPeerId") is not None:
        out["bgp_peer_id"] = data["bgpPeerId"]
    if data.get("asn") is not None:
        out["asn"] = data["asn"]
    else:
        out["asn"] = 0
    if data.get("asnLong") is not None:
        out["asn_long"] = data["asnLong"]
    if data.get("authKey") is not None:
        out["auth_key"] = data["authKey"]
    if data.get("addressFamily") is not None:
        import capo_direct_connect.types.address_family

        out["address_family"] = (
            capo_direct_connect.types.address_family.deserialize_aws_json_1_1(
                data["addressFamily"]
            )
        )
    if data.get("amazonAddress") is not None:
        out["amazon_address"] = data["amazonAddress"]
    if data.get("customerAddress") is not None:
        out["customer_address"] = data["customerAddress"]
    if data.get("bgpPeerState") is not None:
        import capo_direct_connect.types.bgp_peer_state

        out["bgp_peer_state"] = (
            capo_direct_connect.types.bgp_peer_state.deserialize_aws_json_1_1(
                data["bgpPeerState"]
            )
        )
    if data.get("bgpStatus") is not None:
        import capo_direct_connect.types.bgp_status

        out["bgp_status"] = (
            capo_direct_connect.types.bgp_status.deserialize_aws_json_1_1(
                data["bgpStatus"]
            )
        )
    if data.get("awsDeviceV2") is not None:
        out["aws_device_v2"] = data["awsDeviceV2"]
    if data.get("awsLogicalDeviceId") is not None:
        out["aws_logical_device_id"] = data["awsLogicalDeviceId"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: BGPPeer) -> dict:
    out: dict = {}
    if "bgp_peer_id" in value:
        out["bgpPeerId"] = value["bgp_peer_id"]
    out["asn"] = value.get("asn", 0)
    if "asn_long" in value:
        out["asnLong"] = value["asn_long"]
    if "auth_key" in value:
        out["authKey"] = value["auth_key"]
    if "address_family" in value:
        import capo_direct_connect.types.address_family

        out["addressFamily"] = capo_direct_connect.types.address_family.serialize_cbor(
            value["address_family"]
        )
    if "amazon_address" in value:
        out["amazonAddress"] = value["amazon_address"]
    if "customer_address" in value:
        out["customerAddress"] = value["customer_address"]
    if "bgp_peer_state" in value:
        import capo_direct_connect.types.bgp_peer_state

        out["bgpPeerState"] = capo_direct_connect.types.bgp_peer_state.serialize_cbor(
            value["bgp_peer_state"]
        )
    if "bgp_status" in value:
        import capo_direct_connect.types.bgp_status

        out["bgpStatus"] = capo_direct_connect.types.bgp_status.serialize_cbor(
            value["bgp_status"]
        )
    if "aws_device_v2" in value:
        out["awsDeviceV2"] = value["aws_device_v2"]
    if "aws_logical_device_id" in value:
        out["awsLogicalDeviceId"] = value["aws_logical_device_id"]
    return out


def deserialize_cbor(data: dict) -> BGPPeer:
    out: BGPPeer = {}  # type: ignore[typeddict-item]
    if data.get("bgpPeerId") is not None:
        out["bgp_peer_id"] = data["bgpPeerId"]
    if data.get("asn") is not None:
        out["asn"] = data["asn"]
    else:
        out["asn"] = 0
    if data.get("asnLong") is not None:
        out["asn_long"] = data["asnLong"]
    if data.get("authKey") is not None:
        out["auth_key"] = data["authKey"]
    if data.get("addressFamily") is not None:
        import capo_direct_connect.types.address_family

        out["address_family"] = (
            capo_direct_connect.types.address_family.deserialize_cbor(
                data["addressFamily"]
            )
        )
    if data.get("amazonAddress") is not None:
        out["amazon_address"] = data["amazonAddress"]
    if data.get("customerAddress") is not None:
        out["customer_address"] = data["customerAddress"]
    if data.get("bgpPeerState") is not None:
        import capo_direct_connect.types.bgp_peer_state

        out["bgp_peer_state"] = (
            capo_direct_connect.types.bgp_peer_state.deserialize_cbor(
                data["bgpPeerState"]
            )
        )
    if data.get("bgpStatus") is not None:
        import capo_direct_connect.types.bgp_status

        out["bgp_status"] = capo_direct_connect.types.bgp_status.deserialize_cbor(
            data["bgpStatus"]
        )
    if data.get("awsDeviceV2") is not None:
        out["aws_device_v2"] = data["awsDeviceV2"]
    if data.get("awsLogicalDeviceId") is not None:
        out["aws_logical_device_id"] = data["awsLogicalDeviceId"]
    return out
