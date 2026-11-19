"""Generated from Smithy shape ``com.amazonaws.gamelift#DeregisterComputeOutput``."""

from typing_extensions import TypedDict


class DeregisterComputeOutput(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeregisterComputeOutput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeregisterComputeOutput:
    out: DeregisterComputeOutput = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeregisterComputeOutput) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DeregisterComputeOutput:
    out: DeregisterComputeOutput = {}  # type: ignore[typeddict-item]
    return out
