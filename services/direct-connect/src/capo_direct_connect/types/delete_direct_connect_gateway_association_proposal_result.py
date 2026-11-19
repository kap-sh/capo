"""Generated from Smithy shape ``com.amazonaws.directconnect#DeleteDirectConnectGatewayAssociationProposalResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_direct_connect.types.direct_connect_gateway_association_proposal


class DeleteDirectConnectGatewayAssociationProposalResult(TypedDict, closed=True):
    direct_connect_gateway_association_proposal: NotRequired[
        "capo_direct_connect.types.direct_connect_gateway_association_proposal.DirectConnectGatewayAssociationProposal"
    ]
    """<p>The ID of the associated gateway.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DeleteDirectConnectGatewayAssociationProposalResult,
) -> dict:
    out: dict = {}
    if "direct_connect_gateway_association_proposal" in value:
        import capo_direct_connect.types.direct_connect_gateway_association_proposal

        out["directConnectGatewayAssociationProposal"] = (
            capo_direct_connect.types.direct_connect_gateway_association_proposal.serialize_aws_json_1_1(
                value["direct_connect_gateway_association_proposal"]
            )
        )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DeleteDirectConnectGatewayAssociationProposalResult:
    out: DeleteDirectConnectGatewayAssociationProposalResult = {}  # type: ignore[typeddict-item]
    if data.get("directConnectGatewayAssociationProposal") is not None:
        import capo_direct_connect.types.direct_connect_gateway_association_proposal

        out["direct_connect_gateway_association_proposal"] = (
            capo_direct_connect.types.direct_connect_gateway_association_proposal.deserialize_aws_json_1_1(
                data["directConnectGatewayAssociationProposal"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteDirectConnectGatewayAssociationProposalResult) -> dict:
    out: dict = {}
    if "direct_connect_gateway_association_proposal" in value:
        import capo_direct_connect.types.direct_connect_gateway_association_proposal

        out["directConnectGatewayAssociationProposal"] = (
            capo_direct_connect.types.direct_connect_gateway_association_proposal.serialize_cbor(
                value["direct_connect_gateway_association_proposal"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> DeleteDirectConnectGatewayAssociationProposalResult:
    out: DeleteDirectConnectGatewayAssociationProposalResult = {}  # type: ignore[typeddict-item]
    if data.get("directConnectGatewayAssociationProposal") is not None:
        import capo_direct_connect.types.direct_connect_gateway_association_proposal

        out["direct_connect_gateway_association_proposal"] = (
            capo_direct_connect.types.direct_connect_gateway_association_proposal.deserialize_cbor(
                data["directConnectGatewayAssociationProposal"]
            )
        )
    return out
