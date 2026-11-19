"""Generated from Smithy shape ``com.amazonaws.mailmanager#UpdateTrafficPolicyResponse``."""

from typing_extensions import TypedDict


class UpdateTrafficPolicyResponse(TypedDict, closed=True):
    pass


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateTrafficPolicyResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateTrafficPolicyResponse:
    out: UpdateTrafficPolicyResponse = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateTrafficPolicyResponse) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> UpdateTrafficPolicyResponse:
    out: UpdateTrafficPolicyResponse = {}  # type: ignore[typeddict-item]
    return out
