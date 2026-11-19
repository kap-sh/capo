"""Generated from Smithy shape ``com.amazonaws.directoryservice#ResetUserPasswordResult``."""

from typing_extensions import TypedDict


class ResetUserPasswordResult(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResetUserPasswordResult) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> ResetUserPasswordResult:
    out: ResetUserPasswordResult = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ResetUserPasswordResult) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> ResetUserPasswordResult:
    out: ResetUserPasswordResult = {}  # type: ignore[typeddict-item]
    return out
