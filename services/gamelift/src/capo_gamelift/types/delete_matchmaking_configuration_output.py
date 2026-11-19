"""Generated from Smithy shape ``com.amazonaws.gamelift#DeleteMatchmakingConfigurationOutput``."""

from typing_extensions import TypedDict


class DeleteMatchmakingConfigurationOutput(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteMatchmakingConfigurationOutput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteMatchmakingConfigurationOutput:
    out: DeleteMatchmakingConfigurationOutput = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteMatchmakingConfigurationOutput) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DeleteMatchmakingConfigurationOutput:
    out: DeleteMatchmakingConfigurationOutput = {}  # type: ignore[typeddict-item]
    return out
