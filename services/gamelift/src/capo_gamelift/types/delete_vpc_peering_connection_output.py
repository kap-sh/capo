"""Generated from Smithy shape ``com.amazonaws.gamelift#DeleteVpcPeeringConnectionOutput``."""

from typing_extensions import TypedDict


class DeleteVpcPeeringConnectionOutput(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteVpcPeeringConnectionOutput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteVpcPeeringConnectionOutput:
    out: DeleteVpcPeeringConnectionOutput = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteVpcPeeringConnectionOutput) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DeleteVpcPeeringConnectionOutput:
    out: DeleteVpcPeeringConnectionOutput = {}  # type: ignore[typeddict-item]
    return out
