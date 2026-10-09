"""Generated from Smithy shape ``com.amazonaws.gamelift#CreateGameSessionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.alias_id_or_arn
    import capo_gamelift.types.fleet_id_or_arn
    import capo_gamelift.types.game_property_list
    import capo_gamelift.types.id_string_model
    import capo_gamelift.types.large_game_session_data
    import capo_gamelift.types.location_string_model
    import capo_gamelift.types.non_zero_and_max_string
    import capo_gamelift.types.whole_number


class CreateGameSessionInput(TypedDict, closed=True):
    fleet_id: NotRequired["capo_gamelift.types.fleet_id_or_arn.FleetIdOrArn"]
    """<p>A unique identifier for the fleet to create a game session in. You can use either the fleet ID or ARN value. Each request must reference either a fleet ID or alias ID, but not both.</p>"""
    alias_id: NotRequired["capo_gamelift.types.alias_id_or_arn.AliasIdOrArn"]
    """<p>A unique identifier for the alias associated with the fleet to create a game session in. You can use either the alias ID or ARN value. Each request must reference either a fleet ID or alias ID, but not both.</p>"""
    maximum_player_session_count: NotRequired[
        "capo_gamelift.types.whole_number.WholeNumber"
    ]
    """<p>The maximum number of players that can be connected simultaneously to the game session.</p>"""
    name: NotRequired["capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"]
    """<p>A descriptive label that is associated with a game session. Session names do not need to be unique.</p>"""
    game_properties: NotRequired[
        "capo_gamelift.types.game_property_list.GamePropertyList"
    ]
    """<p>A set of key-value pairs that can store custom data in a game session. For example: <code>{"Key": "difficulty", "Value": "novice"}</code>. For an example, see <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#game-properties-create">Create a game session with custom properties</a>. </p> <note> <ul> <li> <p>Avoid using periods (".") in property keys if you plan to search for game sessions by properties. Property keys containing periods cannot be searched and will be filtered out from search results due to search index limitations.</p> </li> <li> <p>If you use SearchGameSessions API, there is a limit of 500 game property keys across all game sessions and all fleets per region. If the limit is exceeded, there will potentially be game session entries missing from SearchGameSessions API results.</p> </li> </ul> </note>"""
    creator_id: NotRequired[
        "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>A unique identifier for a player or entity creating the game session. </p> <p>If you add a resource creation limit policy to a fleet, the <code>CreateGameSession</code> operation requires a <code>CreatorId</code>. Amazon GameLift Servers limits the number of game session creation requests with the same <code>CreatorId</code> in a specified time period.</p> <p>If your fleet doesn't have a resource creation limit policy and you provide a <code>CreatorId</code> in your <code>CreateGameSession</code> requests, Amazon GameLift Servers limits requests to one request per <code>CreatorId</code> per second.</p> <p>To not limit <code>CreateGameSession</code> requests with the same <code>CreatorId</code>, don't provide a <code>CreatorId</code> in your <code>CreateGameSession</code> request.</p>"""
    game_session_id: NotRequired["capo_gamelift.types.id_string_model.IdStringModel"]
    """<p> <i>This parameter is deprecated. Use <code>IdempotencyToken</code> instead.</i> </p> <p>Custom string that uniquely identifies a request for a new game session. Maximum token length is 48 characters. If provided, this string is included in the new game session's ID.</p>"""
    idempotency_token: NotRequired["capo_gamelift.types.id_string_model.IdStringModel"]
    """<p>Custom string that uniquely identifies the new game session request. This is useful for ensuring that game session requests with the same idempotency token are processed only once. Subsequent requests with the same string return the original <code>GameSession</code> object, with an updated status. Maximum token length is 48 characters. If provided, this string is included in the new game session's ID. The value is always a full ARN in the following format: For Home Region game session - <code>arn:aws:gamelift:<home_region>::gamesession/<fleet ID>/<ID string></code>. For Remote Location game session - <code>arn:aws:gamelift:<home_region>::gamesession/<fleet ID>/<location>/<ID string></code>. Idempotency tokens remain in use for 30 days after a game session has ended; game session objects are retained for this time period and then deleted.</p>"""
    game_session_data: NotRequired[
        "capo_gamelift.types.large_game_session_data.LargeGameSessionData"
    ]
    """<p>A set of custom game session properties, formatted as a single string value. This data is passed to a game server process with a request to start a new game session. For more information, see <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession">Start a game session</a>.</p>"""
    location: NotRequired[
        "capo_gamelift.types.location_string_model.LocationStringModel"
    ]
    """<p>A fleet's remote location to place the new game session in. If this parameter is not set, the new game session is placed in the fleet's home Region. Specify a remote location with an Amazon Web Services Region code such as <code>us-west-2</code>. When using an Anywhere fleet, this parameter is required and must be set to the Anywhere fleet's custom location.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateGameSessionInput) -> dict:
    out: dict = {}
    if "fleet_id" in value:
        out["FleetId"] = value["fleet_id"]
    if "alias_id" in value:
        out["AliasId"] = value["alias_id"]
    if "maximum_player_session_count" in value:
        out["MaximumPlayerSessionCount"] = value["maximum_player_session_count"]
    if "name" in value:
        out["Name"] = value["name"]
    if "game_properties" in value:
        import capo_gamelift.types.game_property_list

        out["GameProperties"] = (
            capo_gamelift.types.game_property_list.serialize_aws_json_1_1(
                value["game_properties"]
            )
        )
    if "creator_id" in value:
        out["CreatorId"] = value["creator_id"]
    if "game_session_id" in value:
        out["GameSessionId"] = value["game_session_id"]
    if "idempotency_token" in value:
        out["IdempotencyToken"] = value["idempotency_token"]
    if "game_session_data" in value:
        out["GameSessionData"] = value["game_session_data"]
    if "location" in value:
        out["Location"] = value["location"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateGameSessionInput:
    out: CreateGameSessionInput = {}  # type: ignore[typeddict-item]
    if data.get("FleetId") is not None:
        out["fleet_id"] = data["FleetId"]
    if data.get("AliasId") is not None:
        out["alias_id"] = data["AliasId"]
    if data.get("MaximumPlayerSessionCount") is not None:
        out["maximum_player_session_count"] = data["MaximumPlayerSessionCount"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("GameProperties") is not None:
        import capo_gamelift.types.game_property_list

        out["game_properties"] = (
            capo_gamelift.types.game_property_list.deserialize_aws_json_1_1(
                data["GameProperties"]
            )
        )
    if data.get("CreatorId") is not None:
        out["creator_id"] = data["CreatorId"]
    if data.get("GameSessionId") is not None:
        out["game_session_id"] = data["GameSessionId"]
    if data.get("IdempotencyToken") is not None:
        out["idempotency_token"] = data["IdempotencyToken"]
    if data.get("GameSessionData") is not None:
        out["game_session_data"] = data["GameSessionData"]
    if data.get("Location") is not None:
        out["location"] = data["Location"]
    return out
