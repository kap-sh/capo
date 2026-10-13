"""Generated from Smithy shape ``com.amazonaws.gamelift#CreateGameSessionQueueOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.game_session_queue


class CreateGameSessionQueueOutput(TypedDict, closed=True):
    game_session_queue: NotRequired[
        "capo_gamelift.types.game_session_queue.GameSessionQueue"
    ]
    """<p>An object that describes the newly created game session queue.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateGameSessionQueueOutput) -> dict:
    out: dict = {}
    if "game_session_queue" in value:
        import capo_gamelift.types.game_session_queue

        out["GameSessionQueue"] = (
            capo_gamelift.types.game_session_queue.serialize_aws_json_1_1(
                value["game_session_queue"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateGameSessionQueueOutput:
    out: CreateGameSessionQueueOutput = {}  # type: ignore[typeddict-item]
    if data.get("GameSessionQueue") is not None:
        import capo_gamelift.types.game_session_queue

        out["game_session_queue"] = (
            capo_gamelift.types.game_session_queue.deserialize_aws_json_1_1(
                data["GameSessionQueue"]
            )
        )
    return out


def redact_sensitive(value: CreateGameSessionQueueOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "game_session_queue" in value:
        import capo_gamelift.types.game_session_queue

        out["game_session_queue"] = (
            capo_gamelift.types.game_session_queue.redact_sensitive(
                value["game_session_queue"]
            )
        )
    return out
