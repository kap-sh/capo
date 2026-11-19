"""Generated from Smithy shape ``com.amazonaws.codebuild#DeleteProjectOutput``."""

from typing_extensions import TypedDict


class DeleteProjectOutput(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteProjectOutput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteProjectOutput:
    out: DeleteProjectOutput = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteProjectOutput) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DeleteProjectOutput:
    out: DeleteProjectOutput = {}  # type: ignore[typeddict-item]
    return out
