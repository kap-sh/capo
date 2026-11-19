"""Generated from Smithy shape ``com.amazonaws.directconnect#DescribeDirectConnectGatewayAssociationsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_direct_connect.types.direct_connect_gateway_association_list
    import capo_direct_connect.types.pagination_token


class DescribeDirectConnectGatewayAssociationsResult(TypedDict, closed=True):
    direct_connect_gateway_associations: NotRequired[
        "capo_direct_connect.types.direct_connect_gateway_association_list.DirectConnectGatewayAssociationList"
    ]
    """<p>Information about the associations.</p>"""
    next_token: NotRequired[
        "capo_direct_connect.types.pagination_token.PaginationToken"
    ]
    """<p>The token to retrieve the next page.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DescribeDirectConnectGatewayAssociationsResult,
) -> dict:
    out: dict = {}
    if "direct_connect_gateway_associations" in value:
        import capo_direct_connect.types.direct_connect_gateway_association_list

        out["directConnectGatewayAssociations"] = (
            capo_direct_connect.types.direct_connect_gateway_association_list.serialize_aws_json_1_1(
                value["direct_connect_gateway_associations"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DescribeDirectConnectGatewayAssociationsResult:
    out: DescribeDirectConnectGatewayAssociationsResult = {}  # type: ignore[typeddict-item]
    if data.get("directConnectGatewayAssociations") is not None:
        import capo_direct_connect.types.direct_connect_gateway_association_list

        out["direct_connect_gateway_associations"] = (
            capo_direct_connect.types.direct_connect_gateway_association_list.deserialize_aws_json_1_1(
                data["directConnectGatewayAssociations"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeDirectConnectGatewayAssociationsResult) -> dict:
    out: dict = {}
    if "direct_connect_gateway_associations" in value:
        import capo_direct_connect.types.direct_connect_gateway_association_list

        out["directConnectGatewayAssociations"] = (
            capo_direct_connect.types.direct_connect_gateway_association_list.serialize_cbor(
                value["direct_connect_gateway_associations"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> DescribeDirectConnectGatewayAssociationsResult:
    out: DescribeDirectConnectGatewayAssociationsResult = {}  # type: ignore[typeddict-item]
    if data.get("directConnectGatewayAssociations") is not None:
        import capo_direct_connect.types.direct_connect_gateway_association_list

        out["direct_connect_gateway_associations"] = (
            capo_direct_connect.types.direct_connect_gateway_association_list.deserialize_cbor(
                data["directConnectGatewayAssociations"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
