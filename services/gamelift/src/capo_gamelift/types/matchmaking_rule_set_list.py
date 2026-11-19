"""Generated from Smithy shape ``com.amazonaws.gamelift#MatchmakingRuleSetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_gamelift.types.matchmaking_rule_set

MatchmakingRuleSetList: TypeAlias = list[
    "capo_gamelift.types.matchmaking_rule_set.MatchmakingRuleSet"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MatchmakingRuleSetList) -> list:
    import capo_gamelift.types.matchmaking_rule_set

    out: list = []
    for item in value:
        out.append(
            capo_gamelift.types.matchmaking_rule_set.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> MatchmakingRuleSetList:
    import capo_gamelift.types.matchmaking_rule_set

    out: MatchmakingRuleSetList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_gamelift.types.matchmaking_rule_set.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: MatchmakingRuleSetList) -> list:
    import capo_gamelift.types.matchmaking_rule_set

    out: list = []
    for item in value:
        out.append(capo_gamelift.types.matchmaking_rule_set.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> MatchmakingRuleSetList:
    import capo_gamelift.types.matchmaking_rule_set

    out: MatchmakingRuleSetList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_gamelift.types.matchmaking_rule_set.deserialize_cbor(item))
    return out
