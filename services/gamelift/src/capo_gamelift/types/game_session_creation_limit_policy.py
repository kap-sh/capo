"""Generated from Smithy shape ``com.amazonaws.gamelift#GameSessionCreationLimitPolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.whole_number


class GameSessionCreationLimitPolicy(TypedDict, closed=True):
    new_game_sessions_per_creator: NotRequired[
        "capo_gamelift.types.whole_number.WholeNumber"
    ]
    """<p>A policy that puts limits on the number of game sessions that a player can create within a specified span of time. With this policy, you can control players' ability to consume available resources.</p> <p>The policy evaluates when a player tries to create a new game session. On receiving a <code>CreateGameSession</code> request, Amazon GameLift Servers checks that the player (identified by <code>CreatorId</code>) has created fewer than the game session limit in the specified time period.</p>"""
    policy_period_in_minutes: NotRequired[
        "capo_gamelift.types.whole_number.WholeNumber"
    ]
    """<p>The time span used in evaluating the resource creation limit policy. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GameSessionCreationLimitPolicy) -> dict:
    out: dict = {}
    if "new_game_sessions_per_creator" in value:
        out["NewGameSessionsPerCreator"] = value["new_game_sessions_per_creator"]
    if "policy_period_in_minutes" in value:
        out["PolicyPeriodInMinutes"] = value["policy_period_in_minutes"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GameSessionCreationLimitPolicy:
    out: GameSessionCreationLimitPolicy = {}  # type: ignore[typeddict-item]
    if data.get("NewGameSessionsPerCreator") is not None:
        out["new_game_sessions_per_creator"] = data["NewGameSessionsPerCreator"]
    if data.get("PolicyPeriodInMinutes") is not None:
        out["policy_period_in_minutes"] = data["PolicyPeriodInMinutes"]
    return out
