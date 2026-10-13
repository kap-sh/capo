"""Generated from Smithy shape ``com.amazonaws.gamelift#StopGameSessionPlacementOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.game_session_placement


class StopGameSessionPlacementOutput(TypedDict, closed=True):
    game_session_placement: NotRequired[
        "capo_gamelift.types.game_session_placement.GameSessionPlacement"
    ]
    """<p>Object that describes the canceled game session placement, with <code>CANCELLED</code> status and an end time stamp. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopGameSessionPlacementOutput) -> dict:
    out: dict = {}
    if "game_session_placement" in value:
        import capo_gamelift.types.game_session_placement

        out["GameSessionPlacement"] = (
            capo_gamelift.types.game_session_placement.serialize_aws_json_1_1(
                value["game_session_placement"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StopGameSessionPlacementOutput:
    out: StopGameSessionPlacementOutput = {}  # type: ignore[typeddict-item]
    if data.get("GameSessionPlacement") is not None:
        import capo_gamelift.types.game_session_placement

        out["game_session_placement"] = (
            capo_gamelift.types.game_session_placement.deserialize_aws_json_1_1(
                data["GameSessionPlacement"]
            )
        )
    return out


def redact_sensitive(value: StopGameSessionPlacementOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "game_session_placement" in value:
        import capo_gamelift.types.game_session_placement

        out["game_session_placement"] = (
            capo_gamelift.types.game_session_placement.redact_sensitive(
                value["game_session_placement"]
            )
        )
    return out
