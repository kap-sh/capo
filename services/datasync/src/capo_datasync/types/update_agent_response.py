"""Generated from Smithy shape ``com.amazonaws.datasync#UpdateAgentResponse``."""

from typing_extensions import TypedDict


class UpdateAgentResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateAgentResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateAgentResponse:
    out: UpdateAgentResponse = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateAgentResponse) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> UpdateAgentResponse:
    out: UpdateAgentResponse = {}  # type: ignore[typeddict-item]
    return out
