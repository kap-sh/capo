"""Generated from Smithy shape ``com.amazonaws.appstream#DisableUserResult``."""

from typing_extensions import TypedDict


class DisableUserResult(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisableUserResult) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DisableUserResult:
    out: DisableUserResult = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DisableUserResult) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DisableUserResult:
    out: DisableUserResult = {}  # type: ignore[typeddict-item]
    return out
