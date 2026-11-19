"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#DeletePlanResponse``."""

from typing_extensions import TypedDict


class DeletePlanResponse(TypedDict, closed=True):
    pass


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeletePlanResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> DeletePlanResponse:
    out: DeletePlanResponse = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeletePlanResponse) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DeletePlanResponse:
    out: DeletePlanResponse = {}  # type: ignore[typeddict-item]
    return out
