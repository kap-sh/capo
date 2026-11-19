"""Generated from Smithy shape ``com.amazonaws.fms#EC2CopyRouteTableAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_fms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_fms.types.action_target
    import capo_fms.types.length_bounded_string


class EC2CopyRouteTableAction(TypedDict, closed=True):
    description: NotRequired["capo_fms.types.length_bounded_string.LengthBoundedString"]
    """<p>A description of the copied EC2 route table that is associated with the remediation action.</p>"""
    vpc_id: "capo_fms.types.action_target.ActionTarget"
    """<p>The VPC ID of the copied EC2 route table that is associated with the remediation action.</p>"""
    route_table_id: "capo_fms.types.action_target.ActionTarget"
    """<p>The ID of the copied EC2 route table that is associated with the remediation action.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EC2CopyRouteTableAction) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    import capo_fms.types.action_target

    out["VpcId"] = capo_fms.types.action_target.serialize_aws_json_1_1(value["vpc_id"])
    import capo_fms.types.action_target

    out["RouteTableId"] = capo_fms.types.action_target.serialize_aws_json_1_1(
        value["route_table_id"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> EC2CopyRouteTableAction:
    out: EC2CopyRouteTableAction = {}  # type: ignore[typeddict-item]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("VpcId") is not None:
        import capo_fms.types.action_target

        out["vpc_id"] = capo_fms.types.action_target.deserialize_aws_json_1_1(
            data["VpcId"]
        )
    else:
        raise DeserializationError("EC2CopyRouteTableAction.vpc_id required")
    if data.get("RouteTableId") is not None:
        import capo_fms.types.action_target

        out["route_table_id"] = capo_fms.types.action_target.deserialize_aws_json_1_1(
            data["RouteTableId"]
        )
    else:
        raise DeserializationError("EC2CopyRouteTableAction.route_table_id required")
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EC2CopyRouteTableAction) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    import capo_fms.types.action_target

    out["VpcId"] = capo_fms.types.action_target.serialize_cbor(value["vpc_id"])
    import capo_fms.types.action_target

    out["RouteTableId"] = capo_fms.types.action_target.serialize_cbor(
        value["route_table_id"]
    )
    return out


def deserialize_cbor(data: dict) -> EC2CopyRouteTableAction:
    out: EC2CopyRouteTableAction = {}  # type: ignore[typeddict-item]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("VpcId") is not None:
        import capo_fms.types.action_target

        out["vpc_id"] = capo_fms.types.action_target.deserialize_cbor(data["VpcId"])
    else:
        raise DeserializationError("EC2CopyRouteTableAction.vpc_id required")
    if data.get("RouteTableId") is not None:
        import capo_fms.types.action_target

        out["route_table_id"] = capo_fms.types.action_target.deserialize_cbor(
            data["RouteTableId"]
        )
    else:
        raise DeserializationError("EC2CopyRouteTableAction.route_table_id required")
    return out
