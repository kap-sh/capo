"""Generated from Smithy shape ``com.amazonaws.gamelift#TerminateGameSessionOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.game_session


class TerminateGameSessionOutput(TypedDict, closed=True):
    game_session: NotRequired["capo_gamelift.types.game_session.GameSession"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TerminateGameSessionOutput) -> dict:
    out: dict = {}
    if "game_session" in value:
        import capo_gamelift.types.game_session

        out["GameSession"] = capo_gamelift.types.game_session.serialize_aws_json_1_1(
            value["game_session"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TerminateGameSessionOutput:
    out: TerminateGameSessionOutput = {}  # type: ignore[typeddict-item]
    if data.get("GameSession") is not None:
        import capo_gamelift.types.game_session

        out["game_session"] = capo_gamelift.types.game_session.deserialize_aws_json_1_1(
            data["GameSession"]
        )
    return out


def redact_sensitive(value: TerminateGameSessionOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "game_session" in value:
        import capo_gamelift.types.game_session

        out["game_session"] = capo_gamelift.types.game_session.redact_sensitive(
            value["game_session"]
        )
    return out
