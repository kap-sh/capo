"""Generated from Smithy shape ``com.amazonaws.appstream#StartFleetResult``."""

from typing_extensions import TypedDict


class StartFleetResult(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartFleetResult) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> StartFleetResult:
    out: StartFleetResult = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StartFleetResult) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> StartFleetResult:
    out: StartFleetResult = {}  # type: ignore[typeddict-item]
    return out
