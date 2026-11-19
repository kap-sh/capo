"""Generated from Smithy shape ``com.amazonaws.gamelift#DeleteMatchmakingRuleSetOutput``."""

from typing_extensions import TypedDict


class DeleteMatchmakingRuleSetOutput(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteMatchmakingRuleSetOutput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteMatchmakingRuleSetOutput:
    out: DeleteMatchmakingRuleSetOutput = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteMatchmakingRuleSetOutput) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DeleteMatchmakingRuleSetOutput:
    out: DeleteMatchmakingRuleSetOutput = {}  # type: ignore[typeddict-item]
    return out
