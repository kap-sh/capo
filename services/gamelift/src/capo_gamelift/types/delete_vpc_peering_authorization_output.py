"""Generated from Smithy shape ``com.amazonaws.gamelift#DeleteVpcPeeringAuthorizationOutput``."""

from typing_extensions import TypedDict


class DeleteVpcPeeringAuthorizationOutput(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteVpcPeeringAuthorizationOutput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteVpcPeeringAuthorizationOutput:
    out: DeleteVpcPeeringAuthorizationOutput = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteVpcPeeringAuthorizationOutput) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DeleteVpcPeeringAuthorizationOutput:
    out: DeleteVpcPeeringAuthorizationOutput = {}  # type: ignore[typeddict-item]
    return out
