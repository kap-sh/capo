"""Generated from Smithy shape ``com.amazonaws.gamelift#DescribeMatchmakingRuleSetsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.matchmaking_rule_set_list
    import capo_gamelift.types.non_zero_and_max_string


class DescribeMatchmakingRuleSetsOutput(TypedDict, closed=True):
    rule_sets: NotRequired[
        "capo_gamelift.types.matchmaking_rule_set_list.MatchmakingRuleSetList"
    ]
    """<p>A collection of requested matchmaking rule set objects. </p>"""
    next_token: NotRequired[
        "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>A token that indicates where to resume retrieving results on the next call to this operation. If no token is returned, these results represent the end of the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeMatchmakingRuleSetsOutput) -> dict:
    out: dict = {}
    if "rule_sets" in value:
        import capo_gamelift.types.matchmaking_rule_set_list

        out["RuleSets"] = (
            capo_gamelift.types.matchmaking_rule_set_list.serialize_aws_json_1_1(
                value["rule_sets"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeMatchmakingRuleSetsOutput:
    out: DescribeMatchmakingRuleSetsOutput = {}  # type: ignore[typeddict-item]
    if data.get("RuleSets") is not None:
        import capo_gamelift.types.matchmaking_rule_set_list

        out["rule_sets"] = (
            capo_gamelift.types.matchmaking_rule_set_list.deserialize_aws_json_1_1(
                data["RuleSets"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeMatchmakingRuleSetsOutput) -> dict:
    out: dict = {}
    if "rule_sets" in value:
        import capo_gamelift.types.matchmaking_rule_set_list

        out["RuleSets"] = capo_gamelift.types.matchmaking_rule_set_list.serialize_cbor(
            value["rule_sets"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> DescribeMatchmakingRuleSetsOutput:
    out: DescribeMatchmakingRuleSetsOutput = {}  # type: ignore[typeddict-item]
    if data.get("RuleSets") is not None:
        import capo_gamelift.types.matchmaking_rule_set_list

        out["rule_sets"] = (
            capo_gamelift.types.matchmaking_rule_set_list.deserialize_cbor(
                data["RuleSets"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
