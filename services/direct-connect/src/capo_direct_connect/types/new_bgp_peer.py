"""Generated from Smithy shape ``com.amazonaws.directconnect#NewBGPPeer``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_direct_connect.types.address_family
    import capo_direct_connect.types.amazon_address
    import capo_direct_connect.types.asn
    import capo_direct_connect.types.bgp_auth_key
    import capo_direct_connect.types.customer_address
    import capo_direct_connect.types.long_asn


class NewBGPPeer(TypedDict, closed=True):
    asn: "capo_direct_connect.types.asn.ASN"
    """<p>The autonomous system number (ASN). The valid range is from 1 to 2147483646 for Border Gateway Protocol (BGP) configuration. If you provide a number greater than the maximum, an error is returned. Use <code>asnLong</code> instead.</p>"""
    asn_long: NotRequired["capo_direct_connect.types.long_asn.LongAsn"]
    """<p>The long ASN for a new BGP peer. The valid range is from 1 to 4294967294.</p>"""
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


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NewBGPPeer) -> dict:
    out: dict = {}
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
    return out


def deserialize_aws_json_1_1(data: dict) -> NewBGPPeer:
    out: NewBGPPeer = {}  # type: ignore[typeddict-item]
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
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: NewBGPPeer) -> dict:
    out: dict = {}
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
    return out


def deserialize_cbor(data: dict) -> NewBGPPeer:
    out: NewBGPPeer = {}  # type: ignore[typeddict-item]
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
    return out
