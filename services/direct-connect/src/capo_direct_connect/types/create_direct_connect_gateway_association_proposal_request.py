"""Generated from Smithy shape ``com.amazonaws.directconnect#CreateDirectConnectGatewayAssociationProposalRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_direct_connect.types.direct_connect_gateway_id
    import capo_direct_connect.types.gateway_id_to_associate
    import capo_direct_connect.types.owner_account
    import capo_direct_connect.types.route_filter_prefix_list


class CreateDirectConnectGatewayAssociationProposalRequest(TypedDict, closed=True):
    direct_connect_gateway_id: (
        "capo_direct_connect.types.direct_connect_gateway_id.DirectConnectGatewayId"
    )
    """<p>The ID of the Direct Connect gateway.</p>"""
    direct_connect_gateway_owner_account: (
        "capo_direct_connect.types.owner_account.OwnerAccount"
    )
    """<p>The ID of the Amazon Web Services account that owns the Direct Connect gateway.</p>"""
    gateway_id: "capo_direct_connect.types.gateway_id_to_associate.GatewayIdToAssociate"
    """<p>The ID of the virtual private gateway or transit gateway.</p>"""
    add_allowed_prefixes_to_direct_connect_gateway: NotRequired[
        "capo_direct_connect.types.route_filter_prefix_list.RouteFilterPrefixList"
    ]
    """<p>The Amazon VPC prefixes to advertise to the Direct Connect gateway.</p>"""
    remove_allowed_prefixes_to_direct_connect_gateway: NotRequired[
        "capo_direct_connect.types.route_filter_prefix_list.RouteFilterPrefixList"
    ]
    """<p>The Amazon VPC prefixes to no longer advertise to the Direct Connect gateway.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: CreateDirectConnectGatewayAssociationProposalRequest,
) -> dict:
    out: dict = {}
    out["directConnectGatewayId"] = value["direct_connect_gateway_id"]
    out["directConnectGatewayOwnerAccount"] = value[
        "direct_connect_gateway_owner_account"
    ]
    out["gatewayId"] = value["gateway_id"]
    if "add_allowed_prefixes_to_direct_connect_gateway" in value:
        import capo_direct_connect.types.route_filter_prefix_list

        out["addAllowedPrefixesToDirectConnectGateway"] = (
            capo_direct_connect.types.route_filter_prefix_list.serialize_aws_json_1_1(
                value["add_allowed_prefixes_to_direct_connect_gateway"]
            )
        )
    if "remove_allowed_prefixes_to_direct_connect_gateway" in value:
        import capo_direct_connect.types.route_filter_prefix_list

        out["removeAllowedPrefixesToDirectConnectGateway"] = (
            capo_direct_connect.types.route_filter_prefix_list.serialize_aws_json_1_1(
                value["remove_allowed_prefixes_to_direct_connect_gateway"]
            )
        )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> CreateDirectConnectGatewayAssociationProposalRequest:
    out: CreateDirectConnectGatewayAssociationProposalRequest = {}  # type: ignore[typeddict-item]
    if data.get("directConnectGatewayId") is not None:
        out["direct_connect_gateway_id"] = data["directConnectGatewayId"]
    else:
        out["direct_connect_gateway_id"] = ""
    if data.get("directConnectGatewayOwnerAccount") is not None:
        out["direct_connect_gateway_owner_account"] = data[
            "directConnectGatewayOwnerAccount"
        ]
    else:
        out["direct_connect_gateway_owner_account"] = ""
    if data.get("gatewayId") is not None:
        out["gateway_id"] = data["gatewayId"]
    else:
        out["gateway_id"] = ""
    if data.get("addAllowedPrefixesToDirectConnectGateway") is not None:
        import capo_direct_connect.types.route_filter_prefix_list

        out["add_allowed_prefixes_to_direct_connect_gateway"] = (
            capo_direct_connect.types.route_filter_prefix_list.deserialize_aws_json_1_1(
                data["addAllowedPrefixesToDirectConnectGateway"]
            )
        )
    if data.get("removeAllowedPrefixesToDirectConnectGateway") is not None:
        import capo_direct_connect.types.route_filter_prefix_list

        out["remove_allowed_prefixes_to_direct_connect_gateway"] = (
            capo_direct_connect.types.route_filter_prefix_list.deserialize_aws_json_1_1(
                data["removeAllowedPrefixesToDirectConnectGateway"]
            )
        )
    return out
