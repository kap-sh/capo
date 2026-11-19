"""Generated from Smithy shape ``com.amazonaws.directconnect#DescribeDirectConnectGatewayAssociationProposalsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_direct_connect.types.direct_connect_gateway_association_proposal_list
    import capo_direct_connect.types.pagination_token


class DescribeDirectConnectGatewayAssociationProposalsResult(TypedDict, closed=True):
    direct_connect_gateway_association_proposals: NotRequired[
        "capo_direct_connect.types.direct_connect_gateway_association_proposal_list.DirectConnectGatewayAssociationProposalList"
    ]
    """<p>Describes the Direct Connect gateway association proposals.</p>"""
    next_token: NotRequired[
        "capo_direct_connect.types.pagination_token.PaginationToken"
    ]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DescribeDirectConnectGatewayAssociationProposalsResult,
) -> dict:
    out: dict = {}
    if "direct_connect_gateway_association_proposals" in value:
        import capo_direct_connect.types.direct_connect_gateway_association_proposal_list

        out["directConnectGatewayAssociationProposals"] = (
            capo_direct_connect.types.direct_connect_gateway_association_proposal_list.serialize_aws_json_1_1(
                value["direct_connect_gateway_association_proposals"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DescribeDirectConnectGatewayAssociationProposalsResult:
    out: DescribeDirectConnectGatewayAssociationProposalsResult = {}  # type: ignore[typeddict-item]
    if data.get("directConnectGatewayAssociationProposals") is not None:
        import capo_direct_connect.types.direct_connect_gateway_association_proposal_list

        out["direct_connect_gateway_association_proposals"] = (
            capo_direct_connect.types.direct_connect_gateway_association_proposal_list.deserialize_aws_json_1_1(
                data["directConnectGatewayAssociationProposals"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(
    value: DescribeDirectConnectGatewayAssociationProposalsResult,
) -> dict:
    out: dict = {}
    if "direct_connect_gateway_association_proposals" in value:
        import capo_direct_connect.types.direct_connect_gateway_association_proposal_list

        out["directConnectGatewayAssociationProposals"] = (
            capo_direct_connect.types.direct_connect_gateway_association_proposal_list.serialize_cbor(
                value["direct_connect_gateway_association_proposals"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_cbor(
    data: dict,
) -> DescribeDirectConnectGatewayAssociationProposalsResult:
    out: DescribeDirectConnectGatewayAssociationProposalsResult = {}  # type: ignore[typeddict-item]
    if data.get("directConnectGatewayAssociationProposals") is not None:
        import capo_direct_connect.types.direct_connect_gateway_association_proposal_list

        out["direct_connect_gateway_association_proposals"] = (
            capo_direct_connect.types.direct_connect_gateway_association_proposal_list.deserialize_cbor(
                data["directConnectGatewayAssociationProposals"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
