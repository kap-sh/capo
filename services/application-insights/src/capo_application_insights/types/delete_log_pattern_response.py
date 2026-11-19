"""Generated from Smithy shape ``com.amazonaws.applicationinsights#DeleteLogPatternResponse``."""

from typing_extensions import TypedDict


class DeleteLogPatternResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteLogPatternResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteLogPatternResponse:
    out: DeleteLogPatternResponse = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteLogPatternResponse) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DeleteLogPatternResponse:
    out: DeleteLogPatternResponse = {}  # type: ignore[typeddict-item]
    return out
