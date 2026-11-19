"""Generated from Smithy shape ``com.amazonaws.directoryservice#DisableRadiusResult``."""

from typing_extensions import TypedDict


class DisableRadiusResult(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisableRadiusResult) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DisableRadiusResult:
    out: DisableRadiusResult = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DisableRadiusResult) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DisableRadiusResult:
    out: DisableRadiusResult = {}  # type: ignore[typeddict-item]
    return out
