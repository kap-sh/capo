"""Generated from Smithy shape ``com.amazonaws.gamelift#CreatePlayerSessionsOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.player_session_list


class CreatePlayerSessionsOutput(TypedDict, closed=True):
    player_sessions: NotRequired[
        "capo_gamelift.types.player_session_list.PlayerSessionList"
    ]
    """<p>A collection of player session objects created for the added players.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreatePlayerSessionsOutput) -> dict:
    out: dict = {}
    if "player_sessions" in value:
        import capo_gamelift.types.player_session_list

        out["PlayerSessions"] = (
            capo_gamelift.types.player_session_list.serialize_aws_json_1_1(
                value["player_sessions"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreatePlayerSessionsOutput:
    out: CreatePlayerSessionsOutput = {}  # type: ignore[typeddict-item]
    if data.get("PlayerSessions") is not None:
        import capo_gamelift.types.player_session_list

        out["player_sessions"] = (
            capo_gamelift.types.player_session_list.deserialize_aws_json_1_1(
                data["PlayerSessions"]
            )
        )
    return out


def redact_sensitive(value: CreatePlayerSessionsOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "player_sessions" in value:
        import capo_gamelift.types.player_session_list

        out["player_sessions"] = (
            capo_gamelift.types.player_session_list.redact_sensitive(
                value["player_sessions"]
            )
        )
    return out
