"""Generated from Smithy shape ``com.amazonaws.gamelift#ValidateMatchmakingRuleSetInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.rule_set_body


class ValidateMatchmakingRuleSetInput(TypedDict, closed=True):
    rule_set_body: NotRequired["capo_gamelift.types.rule_set_body.RuleSetBody"]
    """<p>A collection of matchmaking rules to validate, formatted as a JSON string.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ValidateMatchmakingRuleSetInput) -> dict:
    out: dict = {}
    if "rule_set_body" in value:
        out["RuleSetBody"] = value["rule_set_body"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ValidateMatchmakingRuleSetInput:
    out: ValidateMatchmakingRuleSetInput = {}  # type: ignore[typeddict-item]
    if data.get("RuleSetBody") is not None:
        out["rule_set_body"] = data["RuleSetBody"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ValidateMatchmakingRuleSetInput) -> dict:
    out: dict = {}
    if "rule_set_body" in value:
        out["RuleSetBody"] = value["rule_set_body"]
    return out


def deserialize_cbor(data: dict) -> ValidateMatchmakingRuleSetInput:
    out: ValidateMatchmakingRuleSetInput = {}  # type: ignore[typeddict-item]
    if data.get("RuleSetBody") is not None:
        out["rule_set_body"] = data["RuleSetBody"]
    return out
