"""Generated from Smithy shape ``com.amazonaws.gamelift#DeleteMatchmakingRuleSetInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.matchmaking_rule_set_name


class DeleteMatchmakingRuleSetInput(TypedDict, closed=True):
    name: NotRequired[
        "capo_gamelift.types.matchmaking_rule_set_name.MatchmakingRuleSetName"
    ]
    """<p>A unique identifier for the matchmaking rule set to be deleted. (Note: The rule set name is different from the optional "name" field in the rule set body.) You can use either the rule set name or ARN value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteMatchmakingRuleSetInput) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteMatchmakingRuleSetInput:
    out: DeleteMatchmakingRuleSetInput = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    return out
