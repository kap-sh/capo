"""Generated from Smithy shape ``com.amazonaws.applicationinsights#UpdateProblemResponse``."""

from typing_extensions import TypedDict


class UpdateProblemResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateProblemResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateProblemResponse:
    out: UpdateProblemResponse = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateProblemResponse) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> UpdateProblemResponse:
    out: UpdateProblemResponse = {}  # type: ignore[typeddict-item]
    return out
