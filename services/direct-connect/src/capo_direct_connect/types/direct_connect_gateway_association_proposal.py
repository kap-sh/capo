"""Generated from Smithy shape ``com.amazonaws.directconnect#DirectConnectGatewayAssociationProposal``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_direct_connect.types.associated_gateway
    import capo_direct_connect.types.direct_connect_gateway_association_proposal_id
    import capo_direct_connect.types.direct_connect_gateway_association_proposal_state
    import capo_direct_connect.types.direct_connect_gateway_id
    import capo_direct_connect.types.owner_account
    import capo_direct_connect.types.route_filter_prefix_list


class DirectConnectGatewayAssociationProposal(TypedDict, closed=True):
    proposal_id: NotRequired[
        "capo_direct_connect.types.direct_connect_gateway_association_proposal_id.DirectConnectGatewayAssociationProposalId"
    ]
    """<p>The ID of the association proposal.</p>"""
    direct_connect_gateway_id: NotRequired[
        "capo_direct_connect.types.direct_connect_gateway_id.DirectConnectGatewayId"
    ]
    """<p>The ID of the Direct Connect gateway.</p>"""
    direct_connect_gateway_owner_account: NotRequired[
        "capo_direct_connect.types.owner_account.OwnerAccount"
    ]
    """<p>The ID of the Amazon Web Services account that owns the Direct Connect gateway.</p>"""
    proposal_state: NotRequired[
        "capo_direct_connect.types.direct_connect_gateway_association_proposal_state.DirectConnectGatewayAssociationProposalState"
    ]
    """<p>The state of the proposal. The following are possible values:</p> <ul> <li> <p> <code>accepted</code>: The proposal has been accepted. The Direct Connect gateway association is available to use in this state.</p> </li> <li> <p> <code>deleted</code>: The proposal has been deleted by the owner that made the proposal. The Direct Connect gateway association cannot be used in this state.</p> </li> <li> <p> <code>requested</code>: The proposal has been requested. The Direct Connect gateway association cannot be used in this state.</p> </li> </ul>"""
    associated_gateway: NotRequired[
        "capo_direct_connect.types.associated_gateway.AssociatedGateway"
    ]
    """<p>Information about the associated gateway.</p>"""
    existing_allowed_prefixes_to_direct_connect_gateway: NotRequired[
        "capo_direct_connect.types.route_filter_prefix_list.RouteFilterPrefixList"
    ]
    """<p>The existing Amazon VPC prefixes advertised to the Direct Connect gateway.</p>"""
    requested_allowed_prefixes_to_direct_connect_gateway: NotRequired[
        "capo_direct_connect.types.route_filter_prefix_list.RouteFilterPrefixList"
    ]
    """<p>The Amazon VPC prefixes to advertise to the Direct Connect gateway.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DirectConnectGatewayAssociationProposal) -> dict:
    out: dict = {}
    if "proposal_id" in value:
        out["proposalId"] = value["proposal_id"]
    if "direct_connect_gateway_id" in value:
        out["directConnectGatewayId"] = value["direct_connect_gateway_id"]
    if "direct_connect_gateway_owner_account" in value:
        out["directConnectGatewayOwnerAccount"] = value[
            "direct_connect_gateway_owner_account"
        ]
    if "proposal_state" in value:
        import capo_direct_connect.types.direct_connect_gateway_association_proposal_state

        out["proposalState"] = (
            capo_direct_connect.types.direct_connect_gateway_association_proposal_state.serialize_aws_json_1_1(
                value["proposal_state"]
            )
        )
    if "associated_gateway" in value:
        import capo_direct_connect.types.associated_gateway

        out["associatedGateway"] = (
            capo_direct_connect.types.associated_gateway.serialize_aws_json_1_1(
                value["associated_gateway"]
            )
        )
    if "existing_allowed_prefixes_to_direct_connect_gateway" in value:
        import capo_direct_connect.types.route_filter_prefix_list

        out["existingAllowedPrefixesToDirectConnectGateway"] = (
            capo_direct_connect.types.route_filter_prefix_list.serialize_aws_json_1_1(
                value["existing_allowed_prefixes_to_direct_connect_gateway"]
            )
        )
    if "requested_allowed_prefixes_to_direct_connect_gateway" in value:
        import capo_direct_connect.types.route_filter_prefix_list

        out["requestedAllowedPrefixesToDirectConnectGateway"] = (
            capo_direct_connect.types.route_filter_prefix_list.serialize_aws_json_1_1(
                value["requested_allowed_prefixes_to_direct_connect_gateway"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DirectConnectGatewayAssociationProposal:
    out: DirectConnectGatewayAssociationProposal = {}  # type: ignore[typeddict-item]
    if data.get("proposalId") is not None:
        out["proposal_id"] = data["proposalId"]
    if data.get("directConnectGatewayId") is not None:
        out["direct_connect_gateway_id"] = data["directConnectGatewayId"]
    if data.get("directConnectGatewayOwnerAccount") is not None:
        out["direct_connect_gateway_owner_account"] = data[
            "directConnectGatewayOwnerAccount"
        ]
    if data.get("proposalState") is not None:
        import capo_direct_connect.types.direct_connect_gateway_association_proposal_state

        out["proposal_state"] = (
            capo_direct_connect.types.direct_connect_gateway_association_proposal_state.deserialize_aws_json_1_1(
                data["proposalState"]
            )
        )
    if data.get("associatedGateway") is not None:
        import capo_direct_connect.types.associated_gateway

        out["associated_gateway"] = (
            capo_direct_connect.types.associated_gateway.deserialize_aws_json_1_1(
                data["associatedGateway"]
            )
        )
    if data.get("existingAllowedPrefixesToDirectConnectGateway") is not None:
        import capo_direct_connect.types.route_filter_prefix_list

        out["existing_allowed_prefixes_to_direct_connect_gateway"] = (
            capo_direct_connect.types.route_filter_prefix_list.deserialize_aws_json_1_1(
                data["existingAllowedPrefixesToDirectConnectGateway"]
            )
        )
    if data.get("requestedAllowedPrefixesToDirectConnectGateway") is not None:
        import capo_direct_connect.types.route_filter_prefix_list

        out["requested_allowed_prefixes_to_direct_connect_gateway"] = (
            capo_direct_connect.types.route_filter_prefix_list.deserialize_aws_json_1_1(
                data["requestedAllowedPrefixesToDirectConnectGateway"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DirectConnectGatewayAssociationProposal) -> dict:
    out: dict = {}
    if "proposal_id" in value:
        out["proposalId"] = value["proposal_id"]
    if "direct_connect_gateway_id" in value:
        out["directConnectGatewayId"] = value["direct_connect_gateway_id"]
    if "direct_connect_gateway_owner_account" in value:
        out["directConnectGatewayOwnerAccount"] = value[
            "direct_connect_gateway_owner_account"
        ]
    if "proposal_state" in value:
        import capo_direct_connect.types.direct_connect_gateway_association_proposal_state

        out["proposalState"] = (
            capo_direct_connect.types.direct_connect_gateway_association_proposal_state.serialize_cbor(
                value["proposal_state"]
            )
        )
    if "associated_gateway" in value:
        import capo_direct_connect.types.associated_gateway

        out["associatedGateway"] = (
            capo_direct_connect.types.associated_gateway.serialize_cbor(
                value["associated_gateway"]
            )
        )
    if "existing_allowed_prefixes_to_direct_connect_gateway" in value:
        import capo_direct_connect.types.route_filter_prefix_list

        out["existingAllowedPrefixesToDirectConnectGateway"] = (
            capo_direct_connect.types.route_filter_prefix_list.serialize_cbor(
                value["existing_allowed_prefixes_to_direct_connect_gateway"]
            )
        )
    if "requested_allowed_prefixes_to_direct_connect_gateway" in value:
        import capo_direct_connect.types.route_filter_prefix_list

        out["requestedAllowedPrefixesToDirectConnectGateway"] = (
            capo_direct_connect.types.route_filter_prefix_list.serialize_cbor(
                value["requested_allowed_prefixes_to_direct_connect_gateway"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> DirectConnectGatewayAssociationProposal:
    out: DirectConnectGatewayAssociationProposal = {}  # type: ignore[typeddict-item]
    if data.get("proposalId") is not None:
        out["proposal_id"] = data["proposalId"]
    if data.get("directConnectGatewayId") is not None:
        out["direct_connect_gateway_id"] = data["directConnectGatewayId"]
    if data.get("directConnectGatewayOwnerAccount") is not None:
        out["direct_connect_gateway_owner_account"] = data[
            "directConnectGatewayOwnerAccount"
        ]
    if data.get("proposalState") is not None:
        import capo_direct_connect.types.direct_connect_gateway_association_proposal_state

        out["proposal_state"] = (
            capo_direct_connect.types.direct_connect_gateway_association_proposal_state.deserialize_cbor(
                data["proposalState"]
            )
        )
    if data.get("associatedGateway") is not None:
        import capo_direct_connect.types.associated_gateway

        out["associated_gateway"] = (
            capo_direct_connect.types.associated_gateway.deserialize_cbor(
                data["associatedGateway"]
            )
        )
    if data.get("existingAllowedPrefixesToDirectConnectGateway") is not None:
        import capo_direct_connect.types.route_filter_prefix_list

        out["existing_allowed_prefixes_to_direct_connect_gateway"] = (
            capo_direct_connect.types.route_filter_prefix_list.deserialize_cbor(
                data["existingAllowedPrefixesToDirectConnectGateway"]
            )
        )
    if data.get("requestedAllowedPrefixesToDirectConnectGateway") is not None:
        import capo_direct_connect.types.route_filter_prefix_list

        out["requested_allowed_prefixes_to_direct_connect_gateway"] = (
            capo_direct_connect.types.route_filter_prefix_list.deserialize_cbor(
                data["requestedAllowedPrefixesToDirectConnectGateway"]
            )
        )
    return out
