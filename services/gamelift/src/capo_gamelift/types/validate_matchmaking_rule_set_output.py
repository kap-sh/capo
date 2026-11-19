"""Generated from Smithy shape ``com.amazonaws.gamelift#ValidateMatchmakingRuleSetOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.boolean_model


class ValidateMatchmakingRuleSetOutput(TypedDict, closed=True):
    valid: NotRequired["capo_gamelift.types.boolean_model.BooleanModel"]
    """<p>A response indicating whether the rule set is valid.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ValidateMatchmakingRuleSetOutput) -> dict:
    out: dict = {}
    if "valid" in value:
        out["Valid"] = value["valid"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ValidateMatchmakingRuleSetOutput:
    out: ValidateMatchmakingRuleSetOutput = {}  # type: ignore[typeddict-item]
    if data.get("Valid") is not None:
        out["valid"] = data["Valid"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ValidateMatchmakingRuleSetOutput) -> dict:
    out: dict = {}
    if "valid" in value:
        out["Valid"] = value["valid"]
    return out


def deserialize_cbor(data: dict) -> ValidateMatchmakingRuleSetOutput:
    out: ValidateMatchmakingRuleSetOutput = {}  # type: ignore[typeddict-item]
    if data.get("Valid") is not None:
        out["valid"] = data["Valid"]
    return out
