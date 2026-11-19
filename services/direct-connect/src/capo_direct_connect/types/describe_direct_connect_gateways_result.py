"""Generated from Smithy shape ``com.amazonaws.directconnect#DescribeDirectConnectGatewaysResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_direct_connect.types.direct_connect_gateway_list
    import capo_direct_connect.types.pagination_token


class DescribeDirectConnectGatewaysResult(TypedDict, closed=True):
    direct_connect_gateways: NotRequired[
        "capo_direct_connect.types.direct_connect_gateway_list.DirectConnectGatewayList"
    ]
    """<p>The Direct Connect gateways.</p>"""
    next_token: NotRequired[
        "capo_direct_connect.types.pagination_token.PaginationToken"
    ]
    """<p>The token to retrieve the next page.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDirectConnectGatewaysResult) -> dict:
    out: dict = {}
    if "direct_connect_gateways" in value:
        import capo_direct_connect.types.direct_connect_gateway_list

        out["directConnectGateways"] = (
            capo_direct_connect.types.direct_connect_gateway_list.serialize_aws_json_1_1(
                value["direct_connect_gateways"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDirectConnectGatewaysResult:
    out: DescribeDirectConnectGatewaysResult = {}  # type: ignore[typeddict-item]
    if data.get("directConnectGateways") is not None:
        import capo_direct_connect.types.direct_connect_gateway_list

        out["direct_connect_gateways"] = (
            capo_direct_connect.types.direct_connect_gateway_list.deserialize_aws_json_1_1(
                data["directConnectGateways"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeDirectConnectGatewaysResult) -> dict:
    out: dict = {}
    if "direct_connect_gateways" in value:
        import capo_direct_connect.types.direct_connect_gateway_list

        out["directConnectGateways"] = (
            capo_direct_connect.types.direct_connect_gateway_list.serialize_cbor(
                value["direct_connect_gateways"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> DescribeDirectConnectGatewaysResult:
    out: DescribeDirectConnectGatewaysResult = {}  # type: ignore[typeddict-item]
    if data.get("directConnectGateways") is not None:
        import capo_direct_connect.types.direct_connect_gateway_list

        out["direct_connect_gateways"] = (
            capo_direct_connect.types.direct_connect_gateway_list.deserialize_cbor(
                data["directConnectGateways"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
