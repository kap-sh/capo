"""Generated from Smithy shape ``com.amazonaws.gamelift#GameSessionDetail``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.game_session
    import capo_gamelift.types.protection_policy


class GameSessionDetail(TypedDict, closed=True):
    game_session: NotRequired["capo_gamelift.types.game_session.GameSession"]
    """<p>Object that describes a game session.</p>"""
    protection_policy: NotRequired[
        "capo_gamelift.types.protection_policy.ProtectionPolicy"
    ]
    """<p>Current status of protection for the game session.</p> <ul> <li> <p> <b>NoProtection</b> -- The game session can be terminated during a scale-down event.</p> </li> <li> <p> <b>FullProtection</b> -- If the game session is in an <code>ACTIVE</code> status, it cannot be terminated during a scale-down event.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GameSessionDetail) -> dict:
    out: dict = {}
    if "game_session" in value:
        import capo_gamelift.types.game_session

        out["GameSession"] = capo_gamelift.types.game_session.serialize_aws_json_1_1(
            value["game_session"]
        )
    if "protection_policy" in value:
        import capo_gamelift.types.protection_policy

        out["ProtectionPolicy"] = (
            capo_gamelift.types.protection_policy.serialize_aws_json_1_1(
                value["protection_policy"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GameSessionDetail:
    out: GameSessionDetail = {}  # type: ignore[typeddict-item]
    if data.get("GameSession") is not None:
        import capo_gamelift.types.game_session

        out["game_session"] = capo_gamelift.types.game_session.deserialize_aws_json_1_1(
            data["GameSession"]
        )
    if data.get("ProtectionPolicy") is not None:
        import capo_gamelift.types.protection_policy

        out["protection_policy"] = (
            capo_gamelift.types.protection_policy.deserialize_aws_json_1_1(
                data["ProtectionPolicy"]
            )
        )
    return out


def redact_sensitive(value: GameSessionDetail) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "game_session" in value:
        import capo_gamelift.types.game_session

        out["game_session"] = capo_gamelift.types.game_session.redact_sensitive(
            value["game_session"]
        )
    return out
