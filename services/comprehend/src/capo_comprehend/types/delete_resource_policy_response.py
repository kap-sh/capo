"""Generated from Smithy shape ``com.amazonaws.comprehend#DeleteResourcePolicyResponse``."""

from typing_extensions import TypedDict


class DeleteResourcePolicyResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteResourcePolicyResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteResourcePolicyResponse:
    out: DeleteResourcePolicyResponse = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteResourcePolicyResponse) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DeleteResourcePolicyResponse:
    out: DeleteResourcePolicyResponse = {}  # type: ignore[typeddict-item]
    return out
