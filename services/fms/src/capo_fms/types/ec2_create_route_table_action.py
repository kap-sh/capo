"""Generated from Smithy shape ``com.amazonaws.fms#EC2CreateRouteTableAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_fms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_fms.types.action_target
    import capo_fms.types.length_bounded_string


class EC2CreateRouteTableAction(TypedDict, closed=True):
    description: NotRequired["capo_fms.types.length_bounded_string.LengthBoundedString"]
    """<p>A description of the CreateRouteTable action.</p>"""
    vpc_id: "capo_fms.types.action_target.ActionTarget"
    """<p>Information about the ID of a VPC.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EC2CreateRouteTableAction) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    import capo_fms.types.action_target

    out["VpcId"] = capo_fms.types.action_target.serialize_aws_json_1_1(value["vpc_id"])
    return out


def deserialize_aws_json_1_1(data: dict) -> EC2CreateRouteTableAction:
    out: EC2CreateRouteTableAction = {}  # type: ignore[typeddict-item]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("VpcId") is not None:
        import capo_fms.types.action_target

        out["vpc_id"] = capo_fms.types.action_target.deserialize_aws_json_1_1(
            data["VpcId"]
        )
    else:
        raise DeserializationError("EC2CreateRouteTableAction.vpc_id required")
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EC2CreateRouteTableAction) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    import capo_fms.types.action_target

    out["VpcId"] = capo_fms.types.action_target.serialize_cbor(value["vpc_id"])
    return out


def deserialize_cbor(data: dict) -> EC2CreateRouteTableAction:
    out: EC2CreateRouteTableAction = {}  # type: ignore[typeddict-item]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("VpcId") is not None:
        import capo_fms.types.action_target

        out["vpc_id"] = capo_fms.types.action_target.deserialize_cbor(data["VpcId"])
    else:
        raise DeserializationError("EC2CreateRouteTableAction.vpc_id required")
    return out
