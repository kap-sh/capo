"""Generated from Smithy shape ``com.amazonaws.gamelift#CreateMatchmakingRuleSetOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.matchmaking_rule_set


class CreateMatchmakingRuleSetOutput(TypedDict, closed=True):
    rule_set: NotRequired["capo_gamelift.types.matchmaking_rule_set.MatchmakingRuleSet"]
    """<p>The newly created matchmaking rule set.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateMatchmakingRuleSetOutput) -> dict:
    out: dict = {}
    if "rule_set" in value:
        import capo_gamelift.types.matchmaking_rule_set

        out["RuleSet"] = (
            capo_gamelift.types.matchmaking_rule_set.serialize_aws_json_1_1(
                value["rule_set"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateMatchmakingRuleSetOutput:
    out: CreateMatchmakingRuleSetOutput = {}  # type: ignore[typeddict-item]
    if data.get("RuleSet") is not None:
        import capo_gamelift.types.matchmaking_rule_set

        out["rule_set"] = (
            capo_gamelift.types.matchmaking_rule_set.deserialize_aws_json_1_1(
                data["RuleSet"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateMatchmakingRuleSetOutput) -> dict:
    out: dict = {}
    if "rule_set" in value:
        import capo_gamelift.types.matchmaking_rule_set

        out["RuleSet"] = capo_gamelift.types.matchmaking_rule_set.serialize_cbor(
            value["rule_set"]
        )
    return out


def deserialize_cbor(data: dict) -> CreateMatchmakingRuleSetOutput:
    out: CreateMatchmakingRuleSetOutput = {}  # type: ignore[typeddict-item]
    if data.get("RuleSet") is not None:
        import capo_gamelift.types.matchmaking_rule_set

        out["rule_set"] = capo_gamelift.types.matchmaking_rule_set.deserialize_cbor(
            data["RuleSet"]
        )
    return out
