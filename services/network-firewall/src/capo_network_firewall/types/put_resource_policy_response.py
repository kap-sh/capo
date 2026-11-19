"""Generated from Smithy shape ``com.amazonaws.networkfirewall#PutResourcePolicyResponse``."""

from typing_extensions import TypedDict


class PutResourcePolicyResponse(TypedDict, closed=True):
    pass


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PutResourcePolicyResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> PutResourcePolicyResponse:
    out: PutResourcePolicyResponse = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PutResourcePolicyResponse) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> PutResourcePolicyResponse:
    out: PutResourcePolicyResponse = {}  # type: ignore[typeddict-item]
    return out
