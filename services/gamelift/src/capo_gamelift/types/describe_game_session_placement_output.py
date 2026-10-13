"""Generated from Smithy shape ``com.amazonaws.gamelift#DescribeGameSessionPlacementOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.game_session_placement


class DescribeGameSessionPlacementOutput(TypedDict, closed=True):
    game_session_placement: NotRequired[
        "capo_gamelift.types.game_session_placement.GameSessionPlacement"
    ]
    """<p>Object that describes the requested game session placement.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeGameSessionPlacementOutput) -> dict:
    out: dict = {}
    if "game_session_placement" in value:
        import capo_gamelift.types.game_session_placement

        out["GameSessionPlacement"] = (
            capo_gamelift.types.game_session_placement.serialize_aws_json_1_1(
                value["game_session_placement"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeGameSessionPlacementOutput:
    out: DescribeGameSessionPlacementOutput = {}  # type: ignore[typeddict-item]
    if data.get("GameSessionPlacement") is not None:
        import capo_gamelift.types.game_session_placement

        out["game_session_placement"] = (
            capo_gamelift.types.game_session_placement.deserialize_aws_json_1_1(
                data["GameSessionPlacement"]
            )
        )
    return out


def redact_sensitive(value: DescribeGameSessionPlacementOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "game_session_placement" in value:
        import capo_gamelift.types.game_session_placement

        out["game_session_placement"] = (
            capo_gamelift.types.game_session_placement.redact_sensitive(
                value["game_session_placement"]
            )
        )
    return out
