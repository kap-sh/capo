"""Generated from Smithy shape ``com.amazonaws.datasync#DeleteAgentResponse``."""

from typing_extensions import TypedDict


class DeleteAgentResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteAgentResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteAgentResponse:
    out: DeleteAgentResponse = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteAgentResponse) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DeleteAgentResponse:
    out: DeleteAgentResponse = {}  # type: ignore[typeddict-item]
    return out
