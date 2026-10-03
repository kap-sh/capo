"""Generated from Smithy shape ``com.amazonaws.gamelift#StartGameSessionPlacementInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.desired_player_session_list
    import capo_gamelift.types.game_property_list
    import capo_gamelift.types.game_session_queue_name_or_arn
    import capo_gamelift.types.id_string_model
    import capo_gamelift.types.large_game_session_data
    import capo_gamelift.types.non_zero_and_max_string
    import capo_gamelift.types.player_latency_list
    import capo_gamelift.types.priority_configuration_override
    import capo_gamelift.types.whole_number


class StartGameSessionPlacementInput(TypedDict, closed=True):
    placement_id: NotRequired["capo_gamelift.types.id_string_model.IdStringModel"]
    """<p>A unique identifier to assign to the new game session placement. This value is developer-defined. The value must be unique across all Regions and cannot be reused.</p>"""
    game_session_queue_name: NotRequired[
        "capo_gamelift.types.game_session_queue_name_or_arn.GameSessionQueueNameOrArn"
    ]
    """<p>Name of the queue to use to place the new game session. You can use either the queue name or ARN value. </p>"""
    game_properties: NotRequired[
        "capo_gamelift.types.game_property_list.GamePropertyList"
    ]
    """<p>A set of key-value pairs that can store custom data in a game session. For example: <code>{"Key": "difficulty", "Value": "novice"}</code>.</p> <note> <ul> <li> <p>Avoid using periods (".") in property keys if you plan to search for game sessions by properties. Property keys containing periods cannot be searched and will be filtered out from search results due to search index limitations.</p> </li> <li> <p>If you use SearchGameSessions API, there is a limit of 500 game property keys across all game sessions and all fleets per region. If the limit is exceeded, there will potentially be game session entries missing from SearchGameSessions API results.</p> </li> </ul> </note>"""
    maximum_player_session_count: NotRequired[
        "capo_gamelift.types.whole_number.WholeNumber"
    ]
    """<p>The maximum number of players that can be connected simultaneously to the game session.</p>"""
    game_session_name: NotRequired[
        "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>A descriptive label that is associated with a game session. Session names do not need to be unique.</p>"""
    player_latencies: NotRequired[
        "capo_gamelift.types.player_latency_list.PlayerLatencyList"
    ]
    """<p>A set of values, expressed in milliseconds, that indicates the amount of latency that a player experiences when connected to a fleet location (Amazon Web Services Regions or custom locations for Amazon GameLift Servers Anywhere fleets). This information is used to try to place the new game session where it can offer the best possible gameplay experience for the players. </p>"""
    desired_player_sessions: NotRequired[
        "capo_gamelift.types.desired_player_session_list.DesiredPlayerSessionList"
    ]
    """<p>Set of information on each player to create a player session for.</p>"""
    game_session_data: NotRequired[
        "capo_gamelift.types.large_game_session_data.LargeGameSessionData"
    ]
    """<p>A set of custom game session properties, formatted as a single string value. This data is passed to a game server process with a request to start a new game session. For more information, see <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession">Start a game session</a>.</p>"""
    priority_configuration_override: NotRequired[
        "capo_gamelift.types.priority_configuration_override.PriorityConfigurationOverride"
    ]
    """<p>A prioritized list of locations to use for the game session placement and instructions on how to use it. This list overrides a queue's prioritized location list for this game session placement request only. You can include Amazon Web Services Regions, local zones, and custom locations (for Anywhere fleets). You can choose to limit placements to locations on the override list only, or you can prioritize locations on the override list first and then fall back to the queue's other locations if needed. Choose a fallback strategy to use in the event that Amazon GameLift Servers fails to place a game session in any of the locations on the priority override list. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartGameSessionPlacementInput) -> dict:
    out: dict = {}
    if "placement_id" in value:
        out["PlacementId"] = value["placement_id"]
    if "game_session_queue_name" in value:
        out["GameSessionQueueName"] = value["game_session_queue_name"]
    if "game_properties" in value:
        import capo_gamelift.types.game_property_list

        out["GameProperties"] = (
            capo_gamelift.types.game_property_list.serialize_aws_json_1_1(
                value["game_properties"]
            )
        )
    if "maximum_player_session_count" in value:
        out["MaximumPlayerSessionCount"] = value["maximum_player_session_count"]
    if "game_session_name" in value:
        out["GameSessionName"] = value["game_session_name"]
    if "player_latencies" in value:
        import capo_gamelift.types.player_latency_list

        out["PlayerLatencies"] = (
            capo_gamelift.types.player_latency_list.serialize_aws_json_1_1(
                value["player_latencies"]
            )
        )
    if "desired_player_sessions" in value:
        import capo_gamelift.types.desired_player_session_list

        out["DesiredPlayerSessions"] = (
            capo_gamelift.types.desired_player_session_list.serialize_aws_json_1_1(
                value["desired_player_sessions"]
            )
        )
    if "game_session_data" in value:
        out["GameSessionData"] = value["game_session_data"]
    if "priority_configuration_override" in value:
        import capo_gamelift.types.priority_configuration_override

        out["PriorityConfigurationOverride"] = (
            capo_gamelift.types.priority_configuration_override.serialize_aws_json_1_1(
                value["priority_configuration_override"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartGameSessionPlacementInput:
    out: StartGameSessionPlacementInput = {}  # type: ignore[typeddict-item]
    if data.get("PlacementId") is not None:
        out["placement_id"] = data["PlacementId"]
    if data.get("GameSessionQueueName") is not None:
        out["game_session_queue_name"] = data["GameSessionQueueName"]
    if data.get("GameProperties") is not None:
        import capo_gamelift.types.game_property_list

        out["game_properties"] = (
            capo_gamelift.types.game_property_list.deserialize_aws_json_1_1(
                data["GameProperties"]
            )
        )
    if data.get("MaximumPlayerSessionCount") is not None:
        out["maximum_player_session_count"] = data["MaximumPlayerSessionCount"]
    if data.get("GameSessionName") is not None:
        out["game_session_name"] = data["GameSessionName"]
    if data.get("PlayerLatencies") is not None:
        import capo_gamelift.types.player_latency_list

        out["player_latencies"] = (
            capo_gamelift.types.player_latency_list.deserialize_aws_json_1_1(
                data["PlayerLatencies"]
            )
        )
    if data.get("DesiredPlayerSessions") is not None:
        import capo_gamelift.types.desired_player_session_list

        out["desired_player_sessions"] = (
            capo_gamelift.types.desired_player_session_list.deserialize_aws_json_1_1(
                data["DesiredPlayerSessions"]
            )
        )
    if data.get("GameSessionData") is not None:
        out["game_session_data"] = data["GameSessionData"]
    if data.get("PriorityConfigurationOverride") is not None:
        import capo_gamelift.types.priority_configuration_override

        out["priority_configuration_override"] = (
            capo_gamelift.types.priority_configuration_override.deserialize_aws_json_1_1(
                data["PriorityConfigurationOverride"]
            )
        )
    return out
