"""Generated from Smithy shape ``com.amazonaws.codebuild#DeleteFleetOutput``."""

from typing_extensions import TypedDict


class DeleteFleetOutput(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteFleetOutput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteFleetOutput:
    out: DeleteFleetOutput = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteFleetOutput) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DeleteFleetOutput:
    out: DeleteFleetOutput = {}  # type: ignore[typeddict-item]
    return out
