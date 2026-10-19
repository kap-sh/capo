"""Generated from Smithy shape ``com.amazonaws.directconnect#DeleteBGPPeerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_direct_connect.types.asn
    import capo_direct_connect.types.bgp_peer_id
    import capo_direct_connect.types.customer_address
    import capo_direct_connect.types.long_asn
    import capo_direct_connect.types.virtual_interface_id


class DeleteBGPPeerRequest(TypedDict, closed=True):
    virtual_interface_id: NotRequired[
        "capo_direct_connect.types.virtual_interface_id.VirtualInterfaceId"
    ]
    """<p>The ID of the virtual interface.</p>"""
    asn: NotRequired["capo_direct_connect.types.asn.ASN"]
    """<p>The autonomous system number (ASN). The valid range is from 1 to 2147483646 for Border Gateway Protocol (BGP) configuration. If you provide a number greater than the maximum, an error is returned. Use <code>asnLong</code> instead.</p> <ul> <li> <p>You can use <code>asnLong</code> or <code>asn</code>, but not both. We recommend using <code>asnLong</code> as it supports a greater pool of numbers. </p> </li> <li> <p>If you provide a value in the same API call for both <code>asn</code> and <code>asnLong</code>, the API will only accept the value for <code>asnLong</code>. </p> </li> <li> <p>If you enter a 4-byte ASN for the <code>asn</code> parameter, the API returns an error. </p> </li> <li> <p>If you are using a 2-byte ASN, the API response will include the 2-byte value for both the <code>asn</code> and <code>asnLong</code> fields.</p> </li> </ul>"""
    asn_long: NotRequired["capo_direct_connect.types.long_asn.LongAsn"]
    """<p>The long ASN for the BGP peer to be deleted from a Direct Connect virtual interface. The valid range is from 1 to 4294967294 for BGP configuration. </p> <p>Note the following limitations when using <code>asnLong</code>:</p> <ul> <li> <p>You can use <code>asnLong</code> or <code>asn</code>, but not both. We recommend using <code>asnLong</code> as it supports a greater pool of numbers. </p> </li> <li> <p> <code>asnLong</code> accepts any valid ASN value, regardless if it's 2-byte or 4-byte. </p> </li> <li> <p>When using a 4-byte <code>asnLong</code>, the API response returns <code>0</code> for the legacy <code>asn</code> attribute since 4-byte ASN values exceed the maximum supported value of 2,147,483,647.</p> </li> <li> <p>If you are using a 2-byte ASN, the API response will include the 2-byte value for both the <code>asn</code> and <code>asnLong</code> fields.</p> </li> <li> <p>If you provide a value in the same API call for both <code>asn</code> and <code>asnLong</code>, the API will only accept the value for <code>asnLong</code>.</p> </li> </ul>"""
    customer_address: NotRequired[
        "capo_direct_connect.types.customer_address.CustomerAddress"
    ]
    """<p>The IP address assigned to the customer interface.</p>"""
    bgp_peer_id: NotRequired["capo_direct_connect.types.bgp_peer_id.BGPPeerId"]
    """<p>The ID of the BGP peer.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteBGPPeerRequest) -> dict:
    out: dict = {}
    if "virtual_interface_id" in value:
        out["virtualInterfaceId"] = value["virtual_interface_id"]
    if "asn" in value:
        out["asn"] = value["asn"]
    if "asn_long" in value:
        out["asnLong"] = value["asn_long"]
    if "customer_address" in value:
        out["customerAddress"] = value["customer_address"]
    if "bgp_peer_id" in value:
        out["bgpPeerId"] = value["bgp_peer_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteBGPPeerRequest:
    out: DeleteBGPPeerRequest = {}  # type: ignore[typeddict-item]
    if data.get("virtualInterfaceId") is not None:
        out["virtual_interface_id"] = data["virtualInterfaceId"]
    if data.get("asn") is not None:
        out["asn"] = data["asn"]
    if data.get("asnLong") is not None:
        out["asn_long"] = data["asnLong"]
    if data.get("customerAddress") is not None:
        out["customer_address"] = data["customerAddress"]
    if data.get("bgpPeerId") is not None:
        out["bgp_peer_id"] = data["bgpPeerId"]
    return out
