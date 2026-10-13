"""Generated from Smithy shape ``com.amazonaws.gamelift#CreatePlayerSessionOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.player_session


class CreatePlayerSessionOutput(TypedDict, closed=True):
    player_session: NotRequired["capo_gamelift.types.player_session.PlayerSession"]
    """<p>Object that describes the newly created player session record.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreatePlayerSessionOutput) -> dict:
    out: dict = {}
    if "player_session" in value:
        import capo_gamelift.types.player_session

        out["PlayerSession"] = (
            capo_gamelift.types.player_session.serialize_aws_json_1_1(
                value["player_session"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreatePlayerSessionOutput:
    out: CreatePlayerSessionOutput = {}  # type: ignore[typeddict-item]
    if data.get("PlayerSession") is not None:
        import capo_gamelift.types.player_session

        out["player_session"] = (
            capo_gamelift.types.player_session.deserialize_aws_json_1_1(
                data["PlayerSession"]
            )
        )
    return out


def redact_sensitive(value: CreatePlayerSessionOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "player_session" in value:
        import capo_gamelift.types.player_session

        out["player_session"] = capo_gamelift.types.player_session.redact_sensitive(
            value["player_session"]
        )
    return out
