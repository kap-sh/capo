"""Generated from Smithy shape ``com.amazonaws.gamelift#UpdateGameSessionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.arn_string_model
    import capo_gamelift.types.game_property_list
    import capo_gamelift.types.non_zero_and_max_string
    import capo_gamelift.types.player_session_creation_policy
    import capo_gamelift.types.protection_policy
    import capo_gamelift.types.whole_number


class UpdateGameSessionInput(TypedDict, closed=True):
    game_session_id: NotRequired["capo_gamelift.types.arn_string_model.ArnStringModel"]
    """<p>An identifier for the game session that is unique across all regions to update. The value is always a full ARN in the following format: For Home Region game session - <code>arn:aws:gamelift:<home_region>::gamesession/<fleet ID>/<ID string></code>. For Remote Location game session - <code>arn:aws:gamelift:<home_region>::gamesession/<fleet ID>/<location>/<ID string></code>.</p>"""
    maximum_player_session_count: NotRequired[
        "capo_gamelift.types.whole_number.WholeNumber"
    ]
    """<p>The maximum number of players that can be connected simultaneously to the game session.</p>"""
    name: NotRequired["capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"]
    """<p>A descriptive label that is associated with a game session. Session names do not need to be unique.</p>"""
    player_session_creation_policy: NotRequired[
        "capo_gamelift.types.player_session_creation_policy.PlayerSessionCreationPolicy"
    ]
    """<p>A policy that determines whether the game session is accepting new players.</p>"""
    protection_policy: NotRequired[
        "capo_gamelift.types.protection_policy.ProtectionPolicy"
    ]
    """<p>Game session protection policy to apply to this game session only.</p> <ul> <li> <p> <code>NoProtection</code> -- The game session can be terminated during a scale-down event.</p> </li> <li> <p> <code>FullProtection</code> -- If the game session is in an <code>ACTIVE</code> status, it cannot be terminated during a scale-down event.</p> </li> </ul>"""
    game_properties: NotRequired[
        "capo_gamelift.types.game_property_list.GamePropertyList"
    ]
    """<p>A set of key-value pairs that can store custom data in a game session. For example: <code>{"Key": "difficulty", "Value": "novice"}</code>. You can use this parameter to modify game properties in an active game session. This action adds new properties and modifies existing properties. There is no way to delete properties. For an example, see <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#game-properties-update">Update the value of a game property</a>. </p> <note> <ul> <li> <p>Avoid using periods (".") in property keys if you plan to search for game sessions by properties. Property keys containing periods cannot be searched and will be filtered out from search results due to search index limitations.</p> </li> <li> <p>If you use SearchGameSessions API, there is a limit of 500 game property keys across all game sessions and all fleets per region. If the limit is exceeded, there will potentially be game session entries missing from SearchGameSessions API results.</p> </li> </ul> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateGameSessionInput) -> dict:
    out: dict = {}
    if "game_session_id" in value:
        out["GameSessionId"] = value["game_session_id"]
    if "maximum_player_session_count" in value:
        out["MaximumPlayerSessionCount"] = value["maximum_player_session_count"]
    if "name" in value:
        out["Name"] = value["name"]
    if "player_session_creation_policy" in value:
        import capo_gamelift.types.player_session_creation_policy

        out["PlayerSessionCreationPolicy"] = (
            capo_gamelift.types.player_session_creation_policy.serialize_aws_json_1_1(
                value["player_session_creation_policy"]
            )
        )
    if "protection_policy" in value:
        import capo_gamelift.types.protection_policy

        out["ProtectionPolicy"] = (
            capo_gamelift.types.protection_policy.serialize_aws_json_1_1(
                value["protection_policy"]
            )
        )
    if "game_properties" in value:
        import capo_gamelift.types.game_property_list

        out["GameProperties"] = (
            capo_gamelift.types.game_property_list.serialize_aws_json_1_1(
                value["game_properties"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateGameSessionInput:
    out: UpdateGameSessionInput = {}  # type: ignore[typeddict-item]
    if data.get("GameSessionId") is not None:
        out["game_session_id"] = data["GameSessionId"]
    if data.get("MaximumPlayerSessionCount") is not None:
        out["maximum_player_session_count"] = data["MaximumPlayerSessionCount"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("PlayerSessionCreationPolicy") is not None:
        import capo_gamelift.types.player_session_creation_policy

        out["player_session_creation_policy"] = (
            capo_gamelift.types.player_session_creation_policy.deserialize_aws_json_1_1(
                data["PlayerSessionCreationPolicy"]
            )
        )
    if data.get("ProtectionPolicy") is not None:
        import capo_gamelift.types.protection_policy

        out["protection_policy"] = (
            capo_gamelift.types.protection_policy.deserialize_aws_json_1_1(
                data["ProtectionPolicy"]
            )
        )
    if data.get("GameProperties") is not None:
        import capo_gamelift.types.game_property_list

        out["game_properties"] = (
            capo_gamelift.types.game_property_list.deserialize_aws_json_1_1(
                data["GameProperties"]
            )
        )
    return out
