"""Generated from Smithy shape ``com.amazonaws.codeconnections#DeleteRepositoryLinkOutput``."""

from typing_extensions import TypedDict


class DeleteRepositoryLinkOutput(TypedDict, closed=True):
    pass


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteRepositoryLinkOutput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteRepositoryLinkOutput:
    out: DeleteRepositoryLinkOutput = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteRepositoryLinkOutput) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DeleteRepositoryLinkOutput:
    out: DeleteRepositoryLinkOutput = {}  # type: ignore[typeddict-item]
    return out
