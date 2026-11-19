"""Generated from Smithy shape ``com.amazonaws.appstream#CreateUserResult``."""

from typing_extensions import TypedDict


class CreateUserResult(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateUserResult) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateUserResult:
    out: CreateUserResult = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateUserResult) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> CreateUserResult:
    out: CreateUserResult = {}  # type: ignore[typeddict-item]
    return out
