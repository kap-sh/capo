"""Generated from Smithy shape ``com.amazonaws.networkfirewall#DeleteResourcePolicyResponse``."""

from typing_extensions import TypedDict


class DeleteResourcePolicyResponse(TypedDict, closed=True):
    pass


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteResourcePolicyResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteResourcePolicyResponse:
    out: DeleteResourcePolicyResponse = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteResourcePolicyResponse) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DeleteResourcePolicyResponse:
    out: DeleteResourcePolicyResponse = {}  # type: ignore[typeddict-item]
    return out
