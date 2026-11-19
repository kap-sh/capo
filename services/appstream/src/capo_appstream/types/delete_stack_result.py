"""Generated from Smithy shape ``com.amazonaws.appstream#DeleteStackResult``."""

from typing_extensions import TypedDict


class DeleteStackResult(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteStackResult) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteStackResult:
    out: DeleteStackResult = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteStackResult) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DeleteStackResult:
    out: DeleteStackResult = {}  # type: ignore[typeddict-item]
    return out
