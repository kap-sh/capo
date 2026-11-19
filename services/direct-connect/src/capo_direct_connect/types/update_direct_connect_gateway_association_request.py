"""Generated from Smithy shape ``com.amazonaws.directconnect#UpdateDirectConnectGatewayAssociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_direct_connect.types.direct_connect_gateway_association_id
    import capo_direct_connect.types.route_filter_prefix_list


class UpdateDirectConnectGatewayAssociationRequest(TypedDict, closed=True):
    association_id: NotRequired[
        "capo_direct_connect.types.direct_connect_gateway_association_id.DirectConnectGatewayAssociationId"
    ]
    """<p>The ID of the Direct Connect gateway association.</p>"""
    add_allowed_prefixes_to_direct_connect_gateway: NotRequired[
        "capo_direct_connect.types.route_filter_prefix_list.RouteFilterPrefixList"
    ]
    """<p>The Amazon VPC prefixes to advertise to the Direct Connect gateway.</p>"""
    remove_allowed_prefixes_to_direct_connect_gateway: NotRequired[
        "capo_direct_connect.types.route_filter_prefix_list.RouteFilterPrefixList"
    ]
    """<p>The Amazon VPC prefixes to no longer advertise to the Direct Connect gateway.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateDirectConnectGatewayAssociationRequest) -> dict:
    out: dict = {}
    if "association_id" in value:
        out["associationId"] = value["association_id"]
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
) -> UpdateDirectConnectGatewayAssociationRequest:
    out: UpdateDirectConnectGatewayAssociationRequest = {}  # type: ignore[typeddict-item]
    if data.get("associationId") is not None:
        out["association_id"] = data["associationId"]
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


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateDirectConnectGatewayAssociationRequest) -> dict:
    out: dict = {}
    if "association_id" in value:
        out["associationId"] = value["association_id"]
    if "add_allowed_prefixes_to_direct_connect_gateway" in value:
        import capo_direct_connect.types.route_filter_prefix_list

        out["addAllowedPrefixesToDirectConnectGateway"] = (
            capo_direct_connect.types.route_filter_prefix_list.serialize_cbor(
                value["add_allowed_prefixes_to_direct_connect_gateway"]
            )
        )
    if "remove_allowed_prefixes_to_direct_connect_gateway" in value:
        import capo_direct_connect.types.route_filter_prefix_list

        out["removeAllowedPrefixesToDirectConnectGateway"] = (
            capo_direct_connect.types.route_filter_prefix_list.serialize_cbor(
                value["remove_allowed_prefixes_to_direct_connect_gateway"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> UpdateDirectConnectGatewayAssociationRequest:
    out: UpdateDirectConnectGatewayAssociationRequest = {}  # type: ignore[typeddict-item]
    if data.get("associationId") is not None:
        out["association_id"] = data["associationId"]
    if data.get("addAllowedPrefixesToDirectConnectGateway") is not None:
        import capo_direct_connect.types.route_filter_prefix_list

        out["add_allowed_prefixes_to_direct_connect_gateway"] = (
            capo_direct_connect.types.route_filter_prefix_list.deserialize_cbor(
                data["addAllowedPrefixesToDirectConnectGateway"]
            )
        )
    if data.get("removeAllowedPrefixesToDirectConnectGateway") is not None:
        import capo_direct_connect.types.route_filter_prefix_list

        out["remove_allowed_prefixes_to_direct_connect_gateway"] = (
            capo_direct_connect.types.route_filter_prefix_list.deserialize_cbor(
                data["removeAllowedPrefixesToDirectConnectGateway"]
            )
        )
    return out
