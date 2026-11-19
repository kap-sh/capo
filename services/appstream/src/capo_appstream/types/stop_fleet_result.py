"""Generated from Smithy shape ``com.amazonaws.appstream#StopFleetResult``."""

from typing_extensions import TypedDict


class StopFleetResult(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopFleetResult) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> StopFleetResult:
    out: StopFleetResult = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StopFleetResult) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> StopFleetResult:
    out: StopFleetResult = {}  # type: ignore[typeddict-item]
    return out
