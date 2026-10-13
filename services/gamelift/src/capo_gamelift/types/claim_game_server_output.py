"""Generated from Smithy shape ``com.amazonaws.gamelift#ClaimGameServerOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.game_server


class ClaimGameServerOutput(TypedDict, closed=True):
    game_server: NotRequired["capo_gamelift.types.game_server.GameServer"]
    """<p>Object that describes the newly claimed game server.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClaimGameServerOutput) -> dict:
    out: dict = {}
    if "game_server" in value:
        import capo_gamelift.types.game_server

        out["GameServer"] = capo_gamelift.types.game_server.serialize_aws_json_1_1(
            value["game_server"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ClaimGameServerOutput:
    out: ClaimGameServerOutput = {}  # type: ignore[typeddict-item]
    if data.get("GameServer") is not None:
        import capo_gamelift.types.game_server

        out["game_server"] = capo_gamelift.types.game_server.deserialize_aws_json_1_1(
            data["GameServer"]
        )
    return out


def redact_sensitive(value: ClaimGameServerOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "game_server" in value:
        import capo_gamelift.types.game_server

        out["game_server"] = capo_gamelift.types.game_server.redact_sensitive(
            value["game_server"]
        )
    return out
