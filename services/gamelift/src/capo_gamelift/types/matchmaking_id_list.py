"""Generated from Smithy shape ``com.amazonaws.gamelift#MatchmakingIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_gamelift.types.matchmaking_id_string_model

MatchmakingIdList: TypeAlias = list[
    "capo_gamelift.types.matchmaking_id_string_model.MatchmakingIdStringModel"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MatchmakingIdList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> MatchmakingIdList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: MatchmakingIdList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> MatchmakingIdList:
    return [item for item in data if item is not None]
