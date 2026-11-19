"""Generated from Smithy shape ``com.amazonaws.codeconnections#DeleteSyncConfigurationOutput``."""

from typing_extensions import TypedDict


class DeleteSyncConfigurationOutput(TypedDict, closed=True):
    pass


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteSyncConfigurationOutput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteSyncConfigurationOutput:
    out: DeleteSyncConfigurationOutput = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteSyncConfigurationOutput) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DeleteSyncConfigurationOutput:
    out: DeleteSyncConfigurationOutput = {}  # type: ignore[typeddict-item]
    return out
