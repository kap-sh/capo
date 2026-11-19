"""Generated from Smithy shape ``com.amazonaws.appstream#DeleteUserResult``."""

from typing_extensions import TypedDict


class DeleteUserResult(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteUserResult) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteUserResult:
    out: DeleteUserResult = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteUserResult) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DeleteUserResult:
    out: DeleteUserResult = {}  # type: ignore[typeddict-item]
    return out
