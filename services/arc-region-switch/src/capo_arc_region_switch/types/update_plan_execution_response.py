"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#UpdatePlanExecutionResponse``."""

from typing_extensions import TypedDict


class UpdatePlanExecutionResponse(TypedDict, closed=True):
    pass


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdatePlanExecutionResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdatePlanExecutionResponse:
    out: UpdatePlanExecutionResponse = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdatePlanExecutionResponse) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> UpdatePlanExecutionResponse:
    out: UpdatePlanExecutionResponse = {}  # type: ignore[typeddict-item]
    return out
