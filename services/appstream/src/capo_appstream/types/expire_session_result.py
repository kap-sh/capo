"""Generated from Smithy shape ``com.amazonaws.appstream#ExpireSessionResult``."""

from typing_extensions import TypedDict


class ExpireSessionResult(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExpireSessionResult) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> ExpireSessionResult:
    out: ExpireSessionResult = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ExpireSessionResult) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> ExpireSessionResult:
    out: ExpireSessionResult = {}  # type: ignore[typeddict-item]
    return out
