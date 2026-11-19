"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#CancelPlanExecutionResponse``."""

from typing_extensions import TypedDict


class CancelPlanExecutionResponse(TypedDict, closed=True):
    pass


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CancelPlanExecutionResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> CancelPlanExecutionResponse:
    out: CancelPlanExecutionResponse = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CancelPlanExecutionResponse) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> CancelPlanExecutionResponse:
    out: CancelPlanExecutionResponse = {}  # type: ignore[typeddict-item]
    return out
