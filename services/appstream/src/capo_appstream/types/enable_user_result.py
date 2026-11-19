"""Generated from Smithy shape ``com.amazonaws.appstream#EnableUserResult``."""

from typing_extensions import TypedDict


class EnableUserResult(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EnableUserResult) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> EnableUserResult:
    out: EnableUserResult = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EnableUserResult) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> EnableUserResult:
    out: EnableUserResult = {}  # type: ignore[typeddict-item]
    return out
