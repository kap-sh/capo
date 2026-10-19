"""Generated from Smithy shape ``com.amazonaws.directconnect#CreateDirectConnectGatewayRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_direct_connect.types.direct_connect_gateway_name
    import capo_direct_connect.types.long_asn
    import capo_direct_connect.types.tag_list


class CreateDirectConnectGatewayRequest(TypedDict, closed=True):
    direct_connect_gateway_name: (
        "capo_direct_connect.types.direct_connect_gateway_name.DirectConnectGatewayName"
    )
    """<p>The name of the Direct Connect gateway.</p>"""
    tags: NotRequired["capo_direct_connect.types.tag_list.TagList"]
    """<p>The key-value pair tags associated with the request.</p>"""
    amazon_side_asn: NotRequired["capo_direct_connect.types.long_asn.LongAsn"]
    """<p>The autonomous system number (ASN) for Border Gateway Protocol (BGP) to be configured on the Amazon side of the connection. The ASN must be in the private range of 64,512 to 65,534 or 4,200,000,000 to 4,294,967,294. The default is 64512.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDirectConnectGatewayRequest) -> dict:
    out: dict = {}
    out["directConnectGatewayName"] = value["direct_connect_gateway_name"]
    if "tags" in value:
        import capo_direct_connect.types.tag_list

        out["tags"] = capo_direct_connect.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "amazon_side_asn" in value:
        out["amazonSideAsn"] = value["amazon_side_asn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateDirectConnectGatewayRequest:
    out: CreateDirectConnectGatewayRequest = {}  # type: ignore[typeddict-item]
    if data.get("directConnectGatewayName") is not None:
        out["direct_connect_gateway_name"] = data["directConnectGatewayName"]
    else:
        out["direct_connect_gateway_name"] = ""
    if data.get("tags") is not None:
        import capo_direct_connect.types.tag_list

        out["tags"] = capo_direct_connect.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    if data.get("amazonSideAsn") is not None:
        out["amazon_side_asn"] = data["amazonSideAsn"]
    return out
