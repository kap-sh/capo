"""Generated from Smithy shape ``com.amazonaws.gamelift#CreatePlayerSessionsInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.arn_string_model
    import capo_gamelift.types.player_data_map
    import capo_gamelift.types.player_id_list


class CreatePlayerSessionsInput(TypedDict, closed=True):
    game_session_id: NotRequired["capo_gamelift.types.arn_string_model.ArnStringModel"]
    """<p>An identifier for the game session that is unique across all regions to add players to. The value is always a full ARN in the following format: For Home Region game session - <code>arn:aws:gamelift:<home_region>::gamesession/<fleet ID>/<ID string></code>. For Remote Location game session - <code>arn:aws:gamelift:<home_region>::gamesession/<fleet ID>/<location>/<ID string></code>.</p>"""
    player_ids: NotRequired["capo_gamelift.types.player_id_list.PlayerIdList"]
    """<p>List of unique identifiers for the players to be added.</p>"""
    player_data_map: NotRequired["capo_gamelift.types.player_data_map.PlayerDataMap"]
    """<p>Map of string pairs, each specifying a player ID and a set of developer-defined information related to the player. Amazon GameLift Servers does not use this data, so it can be formatted as needed for use in the game. Any player data strings for player IDs that are not included in the <code>PlayerIds</code> parameter are ignored. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreatePlayerSessionsInput) -> dict:
    out: dict = {}
    if "game_session_id" in value:
        out["GameSessionId"] = value["game_session_id"]
    if "player_ids" in value:
        import capo_gamelift.types.player_id_list

        out["PlayerIds"] = capo_gamelift.types.player_id_list.serialize_aws_json_1_1(
            value["player_ids"]
        )
    if "player_data_map" in value:
        import capo_gamelift.types.player_data_map

        out["PlayerDataMap"] = (
            capo_gamelift.types.player_data_map.serialize_aws_json_1_1(
                value["player_data_map"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreatePlayerSessionsInput:
    out: CreatePlayerSessionsInput = {}  # type: ignore[typeddict-item]
    if data.get("GameSessionId") is not None:
        out["game_session_id"] = data["GameSessionId"]
    if data.get("PlayerIds") is not None:
        import capo_gamelift.types.player_id_list

        out["player_ids"] = capo_gamelift.types.player_id_list.deserialize_aws_json_1_1(
            data["PlayerIds"]
        )
    if data.get("PlayerDataMap") is not None:
        import capo_gamelift.types.player_data_map

        out["player_data_map"] = (
            capo_gamelift.types.player_data_map.deserialize_aws_json_1_1(
                data["PlayerDataMap"]
            )
        )
    return out


def redact_sensitive(value: CreatePlayerSessionsInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "player_ids" in value:
        out["player_ids"] = "*** Sensitive Data Redacted ***"
    if "player_data_map" in value:
        import capo_gamelift.types.player_data_map

        out["player_data_map"] = capo_gamelift.types.player_data_map.redact_sensitive(
            value["player_data_map"]
        )
    return out
