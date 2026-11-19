"""Generated from Smithy shape ``com.amazonaws.gamelift#DeleteGameSessionQueueOutput``."""

from typing_extensions import TypedDict


class DeleteGameSessionQueueOutput(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteGameSessionQueueOutput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteGameSessionQueueOutput:
    out: DeleteGameSessionQueueOutput = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteGameSessionQueueOutput) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DeleteGameSessionQueueOutput:
    out: DeleteGameSessionQueueOutput = {}  # type: ignore[typeddict-item]
    return out
