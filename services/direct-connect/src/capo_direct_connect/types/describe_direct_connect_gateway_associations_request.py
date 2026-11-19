"""Generated from Smithy shape ``com.amazonaws.directconnect#DescribeDirectConnectGatewayAssociationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_direct_connect.types.associated_gateway_id
    import capo_direct_connect.types.direct_connect_gateway_association_id
    import capo_direct_connect.types.direct_connect_gateway_id
    import capo_direct_connect.types.max_result_set_size
    import capo_direct_connect.types.pagination_token
    import capo_direct_connect.types.virtual_gateway_id


class DescribeDirectConnectGatewayAssociationsRequest(TypedDict, closed=True):
    association_id: NotRequired[
        "capo_direct_connect.types.direct_connect_gateway_association_id.DirectConnectGatewayAssociationId"
    ]
    """<p>The ID of the Direct Connect gateway association.</p>"""
    associated_gateway_id: NotRequired[
        "capo_direct_connect.types.associated_gateway_id.AssociatedGatewayId"
    ]
    """<p>The ID of the associated gateway.</p>"""
    direct_connect_gateway_id: NotRequired[
        "capo_direct_connect.types.direct_connect_gateway_id.DirectConnectGatewayId"
    ]
    """<p>The ID of the Direct Connect gateway.</p>"""
    max_results: NotRequired[
        "capo_direct_connect.types.max_result_set_size.MaxResultSetSize"
    ]
    """<p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p> <p>If <code>MaxResults</code> is given a value larger than 100, only 100 results are returned.</p>"""
    next_token: NotRequired[
        "capo_direct_connect.types.pagination_token.PaginationToken"
    ]
    """<p>The token provided in the previous call to retrieve the next page.</p>"""
    virtual_gateway_id: NotRequired[
        "capo_direct_connect.types.virtual_gateway_id.VirtualGatewayId"
    ]
    """<p>The ID of the virtual private gateway or transit gateway.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DescribeDirectConnectGatewayAssociationsRequest,
) -> dict:
    out: dict = {}
    if "association_id" in value:
        out["associationId"] = value["association_id"]
    if "associated_gateway_id" in value:
        out["associatedGatewayId"] = value["associated_gateway_id"]
    if "direct_connect_gateway_id" in value:
        out["directConnectGatewayId"] = value["direct_connect_gateway_id"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "virtual_gateway_id" in value:
        out["virtualGatewayId"] = value["virtual_gateway_id"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DescribeDirectConnectGatewayAssociationsRequest:
    out: DescribeDirectConnectGatewayAssociationsRequest = {}  # type: ignore[typeddict-item]
    if data.get("associationId") is not None:
        out["association_id"] = data["associationId"]
    if data.get("associatedGatewayId") is not None:
        out["associated_gateway_id"] = data["associatedGatewayId"]
    if data.get("directConnectGatewayId") is not None:
        out["direct_connect_gateway_id"] = data["directConnectGatewayId"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("virtualGatewayId") is not None:
        out["virtual_gateway_id"] = data["virtualGatewayId"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeDirectConnectGatewayAssociationsRequest) -> dict:
    out: dict = {}
    if "association_id" in value:
        out["associationId"] = value["association_id"]
    if "associated_gateway_id" in value:
        out["associatedGatewayId"] = value["associated_gateway_id"]
    if "direct_connect_gateway_id" in value:
        out["directConnectGatewayId"] = value["direct_connect_gateway_id"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "virtual_gateway_id" in value:
        out["virtualGatewayId"] = value["virtual_gateway_id"]
    return out


def deserialize_cbor(data: dict) -> DescribeDirectConnectGatewayAssociationsRequest:
    out: DescribeDirectConnectGatewayAssociationsRequest = {}  # type: ignore[typeddict-item]
    if data.get("associationId") is not None:
        out["association_id"] = data["associationId"]
    if data.get("associatedGatewayId") is not None:
        out["associated_gateway_id"] = data["associatedGatewayId"]
    if data.get("directConnectGatewayId") is not None:
        out["direct_connect_gateway_id"] = data["directConnectGatewayId"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("virtualGatewayId") is not None:
        out["virtual_gateway_id"] = data["virtualGatewayId"]
    return out
