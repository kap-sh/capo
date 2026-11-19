"""Generated from Smithy shape ``com.amazonaws.appstream#DeleteAppBlockResult``."""

from typing_extensions import TypedDict


class DeleteAppBlockResult(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteAppBlockResult) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteAppBlockResult:
    out: DeleteAppBlockResult = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteAppBlockResult) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DeleteAppBlockResult:
    out: DeleteAppBlockResult = {}  # type: ignore[typeddict-item]
    return out
