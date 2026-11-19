"""Generated from Smithy shape ``com.amazonaws.appstream#DeleteAppBlockBuilderResult``."""

from typing_extensions import TypedDict


class DeleteAppBlockBuilderResult(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteAppBlockBuilderResult) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteAppBlockBuilderResult:
    out: DeleteAppBlockBuilderResult = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteAppBlockBuilderResult) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DeleteAppBlockBuilderResult:
    out: DeleteAppBlockBuilderResult = {}  # type: ignore[typeddict-item]
    return out
