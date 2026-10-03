"""Generated from Smithy shape ``com.amazonaws.directconnect#AcceptDirectConnectGatewayAssociationProposalRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_direct_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_direct_connect.types.direct_connect_gateway_association_proposal_id
    import capo_direct_connect.types.direct_connect_gateway_id
    import capo_direct_connect.types.owner_account
    import capo_direct_connect.types.route_filter_prefix_list


class AcceptDirectConnectGatewayAssociationProposalRequest(TypedDict, closed=True):
    direct_connect_gateway_id: (
        "capo_direct_connect.types.direct_connect_gateway_id.DirectConnectGatewayId"
    )
    """<p>The ID of the Direct Connect gateway.</p>"""
    proposal_id: "capo_direct_connect.types.direct_connect_gateway_association_proposal_id.DirectConnectGatewayAssociationProposalId"
    """<p>The ID of the request proposal.</p>"""
    associated_gateway_owner_account: (
        "capo_direct_connect.types.owner_account.OwnerAccount"
    )
    """<p>The ID of the Amazon Web Services account that owns the virtual private gateway or transit gateway.</p>"""
    override_allowed_prefixes_to_direct_connect_gateway: NotRequired[
        "capo_direct_connect.types.route_filter_prefix_list.RouteFilterPrefixList"
    ]
    """<p>Overrides the Amazon VPC prefixes advertised to the Direct Connect gateway.</p> <p>For information about how to set the prefixes, see <a href="https://docs.aws.amazon.com/directconnect/latest/UserGuide/multi-account-associate-vgw.html#allowed-prefixes">Allowed Prefixes</a> in the <i>Direct Connect User Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: AcceptDirectConnectGatewayAssociationProposalRequest,
) -> dict:
    out: dict = {}
    out["directConnectGatewayId"] = value["direct_connect_gateway_id"]
    out["proposalId"] = value["proposal_id"]
    out["associatedGatewayOwnerAccount"] = value["associated_gateway_owner_account"]
    if "override_allowed_prefixes_to_direct_connect_gateway" in value:
        import capo_direct_connect.types.route_filter_prefix_list

        out["overrideAllowedPrefixesToDirectConnectGateway"] = (
            capo_direct_connect.types.route_filter_prefix_list.serialize_aws_json_1_1(
                value["override_allowed_prefixes_to_direct_connect_gateway"]
            )
        )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> AcceptDirectConnectGatewayAssociationProposalRequest:
    out: AcceptDirectConnectGatewayAssociationProposalRequest = {}  # type: ignore[typeddict-item]
    if data.get("directConnectGatewayId") is not None:
        out["direct_connect_gateway_id"] = data["directConnectGatewayId"]
    else:
        raise DeserializationError(
            "AcceptDirectConnectGatewayAssociationProposalRequest.direct_connect_gateway_id required"
        )
    if data.get("proposalId") is not None:
        out["proposal_id"] = data["proposalId"]
    else:
        raise DeserializationError(
            "AcceptDirectConnectGatewayAssociationProposalRequest.proposal_id required"
        )
    if data.get("associatedGatewayOwnerAccount") is not None:
        out["associated_gateway_owner_account"] = data["associatedGatewayOwnerAccount"]
    else:
        raise DeserializationError(
            "AcceptDirectConnectGatewayAssociationProposalRequest.associated_gateway_owner_account required"
        )
    if data.get("overrideAllowedPrefixesToDirectConnectGateway") is not None:
        import capo_direct_connect.types.route_filter_prefix_list

        out["override_allowed_prefixes_to_direct_connect_gateway"] = (
            capo_direct_connect.types.route_filter_prefix_list.deserialize_aws_json_1_1(
                data["overrideAllowedPrefixesToDirectConnectGateway"]
            )
        )
    return out
