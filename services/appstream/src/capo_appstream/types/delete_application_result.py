"""Generated from Smithy shape ``com.amazonaws.appstream#DeleteApplicationResult``."""

from typing_extensions import TypedDict


class DeleteApplicationResult(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteApplicationResult) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteApplicationResult:
    out: DeleteApplicationResult = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteApplicationResult) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DeleteApplicationResult:
    out: DeleteApplicationResult = {}  # type: ignore[typeddict-item]
    return out
