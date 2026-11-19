"""Generated from Smithy shape ``com.amazonaws.gamelift#MatchmakingRuleSetNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_gamelift.types.matchmaking_rule_set_name

MatchmakingRuleSetNameList: TypeAlias = list[
    "capo_gamelift.types.matchmaking_rule_set_name.MatchmakingRuleSetName"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MatchmakingRuleSetNameList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> MatchmakingRuleSetNameList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: MatchmakingRuleSetNameList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> MatchmakingRuleSetNameList:
    return [item for item in data if item is not None]
