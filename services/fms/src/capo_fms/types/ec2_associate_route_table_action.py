"""Generated from Smithy shape ``com.amazonaws.fms#EC2AssociateRouteTableAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_fms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_fms.types.action_target
    import capo_fms.types.length_bounded_string


class EC2AssociateRouteTableAction(TypedDict, closed=True):
    description: NotRequired["capo_fms.types.length_bounded_string.LengthBoundedString"]
    """<p>A description of the EC2 route table that is associated with the remediation action.</p>"""
    route_table_id: "capo_fms.types.action_target.ActionTarget"
    """<p>The ID of the EC2 route table that is associated with the remediation action.</p>"""
    subnet_id: NotRequired["capo_fms.types.action_target.ActionTarget"]
    """<p>The ID of the subnet for the EC2 route table that is associated with the remediation action.</p>"""
    gateway_id: NotRequired["capo_fms.types.action_target.ActionTarget"]
    """<p>The ID of the gateway to be used with the EC2 route table that is associated with the remediation action.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EC2AssociateRouteTableAction) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    import capo_fms.types.action_target

    out["RouteTableId"] = capo_fms.types.action_target.serialize_aws_json_1_1(
        value["route_table_id"]
    )
    if "subnet_id" in value:
        import capo_fms.types.action_target

        out["SubnetId"] = capo_fms.types.action_target.serialize_aws_json_1_1(
            value["subnet_id"]
        )
    if "gateway_id" in value:
        import capo_fms.types.action_target

        out["GatewayId"] = capo_fms.types.action_target.serialize_aws_json_1_1(
            value["gateway_id"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EC2AssociateRouteTableAction:
    out: EC2AssociateRouteTableAction = {}  # type: ignore[typeddict-item]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("RouteTableId") is not None:
        import capo_fms.types.action_target

        out["route_table_id"] = capo_fms.types.action_target.deserialize_aws_json_1_1(
            data["RouteTableId"]
        )
    else:
        raise DeserializationError(
            "EC2AssociateRouteTableAction.route_table_id required"
        )
    if data.get("SubnetId") is not None:
        import capo_fms.types.action_target

        out["subnet_id"] = capo_fms.types.action_target.deserialize_aws_json_1_1(
            data["SubnetId"]
        )
    if data.get("GatewayId") is not None:
        import capo_fms.types.action_target

        out["gateway_id"] = capo_fms.types.action_target.deserialize_aws_json_1_1(
            data["GatewayId"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EC2AssociateRouteTableAction) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    import capo_fms.types.action_target

    out["RouteTableId"] = capo_fms.types.action_target.serialize_cbor(
        value["route_table_id"]
    )
    if "subnet_id" in value:
        import capo_fms.types.action_target

        out["SubnetId"] = capo_fms.types.action_target.serialize_cbor(
            value["subnet_id"]
        )
    if "gateway_id" in value:
        import capo_fms.types.action_target

        out["GatewayId"] = capo_fms.types.action_target.serialize_cbor(
            value["gateway_id"]
        )
    return out


def deserialize_cbor(data: dict) -> EC2AssociateRouteTableAction:
    out: EC2AssociateRouteTableAction = {}  # type: ignore[typeddict-item]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("RouteTableId") is not None:
        import capo_fms.types.action_target

        out["route_table_id"] = capo_fms.types.action_target.deserialize_cbor(
            data["RouteTableId"]
        )
    else:
        raise DeserializationError(
            "EC2AssociateRouteTableAction.route_table_id required"
        )
    if data.get("SubnetId") is not None:
        import capo_fms.types.action_target

        out["subnet_id"] = capo_fms.types.action_target.deserialize_cbor(
            data["SubnetId"]
        )
    if data.get("GatewayId") is not None:
        import capo_fms.types.action_target

        out["gateway_id"] = capo_fms.types.action_target.deserialize_cbor(
            data["GatewayId"]
        )
    return out
