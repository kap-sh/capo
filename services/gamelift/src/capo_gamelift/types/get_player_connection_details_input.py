"""Generated from Smithy shape ``com.amazonaws.gamelift#GetPlayerConnectionDetailsInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.arn_string_model
    import capo_gamelift.types.player_id_list


class GetPlayerConnectionDetailsInput(TypedDict, closed=True):
    game_session_id: NotRequired["capo_gamelift.types.arn_string_model.ArnStringModel"]
    """<p>An identifier for the game session that is unique across all regions for which to retrieve player connection details. The value is always a full ARN in the following format: For Home Region game session - <code>arn:aws:gamelift:<home_region>::gamesession/<fleet ID>/<ID string></code>. For Remote Location game session - <code>arn:aws:gamelift:<home_region>::gamesession/<fleet ID>/<location>/<ID string></code>.</p>"""
    player_ids: NotRequired["capo_gamelift.types.player_id_list.PlayerIdList"]
    """<p>List of unique identifiers for players. Connection details are returned for each player in this list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetPlayerConnectionDetailsInput) -> dict:
    out: dict = {}
    if "game_session_id" in value:
        out["GameSessionId"] = value["game_session_id"]
    if "player_ids" in value:
        import capo_gamelift.types.player_id_list

        out["PlayerIds"] = capo_gamelift.types.player_id_list.serialize_aws_json_1_1(
            value["player_ids"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetPlayerConnectionDetailsInput:
    out: GetPlayerConnectionDetailsInput = {}  # type: ignore[typeddict-item]
    if data.get("GameSessionId") is not None:
        out["game_session_id"] = data["GameSessionId"]
    if data.get("PlayerIds") is not None:
        import capo_gamelift.types.player_id_list

        out["player_ids"] = capo_gamelift.types.player_id_list.deserialize_aws_json_1_1(
            data["PlayerIds"]
        )
    return out


def redact_sensitive(value: GetPlayerConnectionDetailsInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "player_ids" in value:
        out["player_ids"] = "*** Sensitive Data Redacted ***"
    return out
