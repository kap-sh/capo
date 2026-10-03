"""Generated from Smithy shape ``com.amazonaws.directconnect#CreateDirectConnectGatewayAssociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_direct_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_direct_connect.types.direct_connect_gateway_id
    import capo_direct_connect.types.gateway_id_to_associate
    import capo_direct_connect.types.route_filter_prefix_list
    import capo_direct_connect.types.virtual_gateway_id


class CreateDirectConnectGatewayAssociationRequest(TypedDict, closed=True):
    direct_connect_gateway_id: (
        "capo_direct_connect.types.direct_connect_gateway_id.DirectConnectGatewayId"
    )
    """<p>The ID of the Direct Connect gateway.</p>"""
    gateway_id: NotRequired[
        "capo_direct_connect.types.gateway_id_to_associate.GatewayIdToAssociate"
    ]
    """<p>The ID of the virtual private gateway or transit gateway.</p>"""
    add_allowed_prefixes_to_direct_connect_gateway: NotRequired[
        "capo_direct_connect.types.route_filter_prefix_list.RouteFilterPrefixList"
    ]
    """<p>The Amazon VPC prefixes to advertise to the Direct Connect gateway</p> <p>This parameter is required when you create an association to a transit gateway.</p> <p>For information about how to set the prefixes, see <a href="https://docs.aws.amazon.com/directconnect/latest/UserGuide/multi-account-associate-vgw.html#allowed-prefixes">Allowed Prefixes</a> in the <i>Direct Connect User Guide</i>.</p>"""
    virtual_gateway_id: NotRequired[
        "capo_direct_connect.types.virtual_gateway_id.VirtualGatewayId"
    ]
    """<p>The ID of the virtual private gateway.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDirectConnectGatewayAssociationRequest) -> dict:
    out: dict = {}
    out["directConnectGatewayId"] = value["direct_connect_gateway_id"]
    if "gateway_id" in value:
        out["gatewayId"] = value["gateway_id"]
    if "add_allowed_prefixes_to_direct_connect_gateway" in value:
        import capo_direct_connect.types.route_filter_prefix_list

        out["addAllowedPrefixesToDirectConnectGateway"] = (
            capo_direct_connect.types.route_filter_prefix_list.serialize_aws_json_1_1(
                value["add_allowed_prefixes_to_direct_connect_gateway"]
            )
        )
    if "virtual_gateway_id" in value:
        out["virtualGatewayId"] = value["virtual_gateway_id"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> CreateDirectConnectGatewayAssociationRequest:
    out: CreateDirectConnectGatewayAssociationRequest = {}  # type: ignore[typeddict-item]
    if data.get("directConnectGatewayId") is not None:
        out["direct_connect_gateway_id"] = data["directConnectGatewayId"]
    else:
        raise DeserializationError(
            "CreateDirectConnectGatewayAssociationRequest.direct_connect_gateway_id required"
        )
    if data.get("gatewayId") is not None:
        out["gateway_id"] = data["gatewayId"]
    if data.get("addAllowedPrefixesToDirectConnectGateway") is not None:
        import capo_direct_connect.types.route_filter_prefix_list

        out["add_allowed_prefixes_to_direct_connect_gateway"] = (
            capo_direct_connect.types.route_filter_prefix_list.deserialize_aws_json_1_1(
                data["addAllowedPrefixesToDirectConnectGateway"]
            )
        )
    if data.get("virtualGatewayId") is not None:
        out["virtual_gateway_id"] = data["virtualGatewayId"]
    return out
