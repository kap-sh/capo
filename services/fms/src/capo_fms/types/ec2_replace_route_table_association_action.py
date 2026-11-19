"""Generated from Smithy shape ``com.amazonaws.fms#EC2ReplaceRouteTableAssociationAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_fms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_fms.types.action_target
    import capo_fms.types.length_bounded_string


class EC2ReplaceRouteTableAssociationAction(TypedDict, closed=True):
    description: NotRequired["capo_fms.types.length_bounded_string.LengthBoundedString"]
    """<p>A description of the ReplaceRouteTableAssociation action in Amazon EC2.</p>"""
    association_id: "capo_fms.types.action_target.ActionTarget"
    """<p>Information about the association ID.</p>"""
    route_table_id: "capo_fms.types.action_target.ActionTarget"
    """<p>Information about the ID of the new route table to associate with the subnet.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EC2ReplaceRouteTableAssociationAction) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    import capo_fms.types.action_target

    out["AssociationId"] = capo_fms.types.action_target.serialize_aws_json_1_1(
        value["association_id"]
    )
    import capo_fms.types.action_target

    out["RouteTableId"] = capo_fms.types.action_target.serialize_aws_json_1_1(
        value["route_table_id"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> EC2ReplaceRouteTableAssociationAction:
    out: EC2ReplaceRouteTableAssociationAction = {}  # type: ignore[typeddict-item]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("AssociationId") is not None:
        import capo_fms.types.action_target

        out["association_id"] = capo_fms.types.action_target.deserialize_aws_json_1_1(
            data["AssociationId"]
        )
    else:
        raise DeserializationError(
            "EC2ReplaceRouteTableAssociationAction.association_id required"
        )
    if data.get("RouteTableId") is not None:
        import capo_fms.types.action_target

        out["route_table_id"] = capo_fms.types.action_target.deserialize_aws_json_1_1(
            data["RouteTableId"]
        )
    else:
        raise DeserializationError(
            "EC2ReplaceRouteTableAssociationAction.route_table_id required"
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EC2ReplaceRouteTableAssociationAction) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    import capo_fms.types.action_target

    out["AssociationId"] = capo_fms.types.action_target.serialize_cbor(
        value["association_id"]
    )
    import capo_fms.types.action_target

    out["RouteTableId"] = capo_fms.types.action_target.serialize_cbor(
        value["route_table_id"]
    )
    return out


def deserialize_cbor(data: dict) -> EC2ReplaceRouteTableAssociationAction:
    out: EC2ReplaceRouteTableAssociationAction = {}  # type: ignore[typeddict-item]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("AssociationId") is not None:
        import capo_fms.types.action_target

        out["association_id"] = capo_fms.types.action_target.deserialize_cbor(
            data["AssociationId"]
        )
    else:
        raise DeserializationError(
            "EC2ReplaceRouteTableAssociationAction.association_id required"
        )
    if data.get("RouteTableId") is not None:
        import capo_fms.types.action_target

        out["route_table_id"] = capo_fms.types.action_target.deserialize_cbor(
            data["RouteTableId"]
        )
    else:
        raise DeserializationError(
            "EC2ReplaceRouteTableAssociationAction.route_table_id required"
        )
    return out
