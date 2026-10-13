"""Generated from Smithy shape ``com.amazonaws.gamelift#GetPlayerConnectionDetailsOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.arn_string_model
    import capo_gamelift.types.player_connection_detail_list


class GetPlayerConnectionDetailsOutput(TypedDict, closed=True):
    game_session_id: NotRequired["capo_gamelift.types.arn_string_model.ArnStringModel"]
    """<p>An identifier for the game session that is unique across all regions for which the player connection details were retrieved. The value is always a full ARN in the following format: For Home Region game session - <code>arn:aws:gamelift:<home_region>::gamesession/<fleet ID>/<ID string></code>. For Remote Location game session - <code>arn:aws:gamelift:<home_region>::gamesession/<fleet ID>/<location>/<ID string></code>.</p>"""
    player_connection_details: NotRequired[
        "capo_gamelift.types.player_connection_detail_list.PlayerConnectionDetailList"
    ]
    """<p>A collection of player connection detail objects, one for each requested player.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetPlayerConnectionDetailsOutput) -> dict:
    out: dict = {}
    if "game_session_id" in value:
        out["GameSessionId"] = value["game_session_id"]
    if "player_connection_details" in value:
        import capo_gamelift.types.player_connection_detail_list

        out["PlayerConnectionDetails"] = (
            capo_gamelift.types.player_connection_detail_list.serialize_aws_json_1_1(
                value["player_connection_details"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetPlayerConnectionDetailsOutput:
    out: GetPlayerConnectionDetailsOutput = {}  # type: ignore[typeddict-item]
    if data.get("GameSessionId") is not None:
        out["game_session_id"] = data["GameSessionId"]
    if data.get("PlayerConnectionDetails") is not None:
        import capo_gamelift.types.player_connection_detail_list

        out["player_connection_details"] = (
            capo_gamelift.types.player_connection_detail_list.deserialize_aws_json_1_1(
                data["PlayerConnectionDetails"]
            )
        )
    return out


def redact_sensitive(value: GetPlayerConnectionDetailsOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "player_connection_details" in value:
        import capo_gamelift.types.player_connection_detail_list

        out["player_connection_details"] = (
            capo_gamelift.types.player_connection_detail_list.redact_sensitive(
                value["player_connection_details"]
            )
        )
    return out
