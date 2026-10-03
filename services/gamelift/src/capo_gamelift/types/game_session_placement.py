"""Generated from Smithy shape ``com.amazonaws.gamelift#GameSessionPlacement``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.dns_name
    import capo_gamelift.types.game_property_list
    import capo_gamelift.types.game_session_placement_state
    import capo_gamelift.types.game_session_queue_name
    import capo_gamelift.types.id_string_model
    import capo_gamelift.types.ip_address
    import capo_gamelift.types.large_game_session_data
    import capo_gamelift.types.matchmaker_data
    import capo_gamelift.types.non_zero_and_max_string
    import capo_gamelift.types.placed_player_session_list
    import capo_gamelift.types.player_gateway_status
    import capo_gamelift.types.player_latency_list
    import capo_gamelift.types.port_number
    import capo_gamelift.types.priority_configuration_override
    import capo_gamelift.types.timestamp
    import capo_gamelift.types.whole_number


class GameSessionPlacement(TypedDict, closed=True):
    placement_id: NotRequired["capo_gamelift.types.id_string_model.IdStringModel"]
    """<p>A unique identifier for a game session placement.</p>"""
    game_session_queue_name: NotRequired[
        "capo_gamelift.types.game_session_queue_name.GameSessionQueueName"
    ]
    """<p>A descriptive label that is associated with game session queue. Queue names must be unique within each Region.</p>"""
    status: NotRequired[
        "capo_gamelift.types.game_session_placement_state.GameSessionPlacementState"
    ]
    """<p>Current status of the game session placement request.</p> <ul> <li> <p> <b>PENDING</b> -- The placement request is in the queue waiting to be processed. Game session properties are not yet final. </p> </li> <li> <p> <b>FULFILLED</b> -- A new game session has been successfully placed. Game session properties are now final.</p> </li> <li> <p> <b>CANCELLED</b> -- The placement request was canceled.</p> </li> <li> <p> <b>TIMED_OUT</b> -- A new game session was not successfully created before the time limit expired. You can resubmit the placement request as needed.</p> </li> <li> <p> <b>FAILED</b> -- Amazon GameLift Servers is not able to complete the process of placing the game session. Common reasons are the game session terminated before the placement process was completed, or an unexpected internal error.</p> </li> </ul>"""
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
    game_session_id: NotRequired[
        "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>An identifier for the game session that is unique across all regions. The value is always a full ARN in the following format: For Home Region game session - <code>arn:aws:gamelift:<home_region>::gamesession/<fleet ID>/<ID string></code>. For Remote Location game session - <code>arn:aws:gamelift:<home_region>::gamesession/<fleet ID>/<location>/<ID string></code>. This value is the same as <code>GameSessionArn</code>. This value isn't final until placement status is <code>FULFILLED</code>.</p>"""
    game_session_arn: NotRequired[
        "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>An identifier for the game session that is unique across all regions. The value is always a full ARN in the following format: For Home Region game session - <code>arn:aws:gamelift:<home_region>::gamesession/<fleet ID>/<ID string></code>. For Remote Location game session - <code>arn:aws:gamelift:<home_region>::gamesession/<fleet ID>/<location>/<ID string></code>. This value is the same as <code>GameSessionId</code>. This value isn't final until placement status is <code>FULFILLED</code>.</p>"""
    game_session_region: NotRequired[
        "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>Name of the Region where the game session created by this placement request is running. This value isn't final until placement status is <code>FULFILLED</code>.</p>"""
    player_latencies: NotRequired[
        "capo_gamelift.types.player_latency_list.PlayerLatencyList"
    ]
    """<p>A set of values, expressed in milliseconds, that indicates the amount of latency that a player experiences when connected to a fleet location (Amazon Web Services Regions or custom locations for Amazon GameLift Servers Anywhere fleets).</p>"""
    start_time: NotRequired["capo_gamelift.types.timestamp.Timestamp"]
    """<p>Time stamp indicating when this request was placed in the queue. Format is a number expressed in Unix time as milliseconds (for example <code>"1469498468.057"</code>).</p>"""
    end_time: NotRequired["capo_gamelift.types.timestamp.Timestamp"]
    """<p>Time stamp indicating when this request was completed, canceled, or timed out.</p>"""
    ip_address: NotRequired["capo_gamelift.types.ip_address.IpAddress"]
    """<p>The IP address of the game session. To connect to a Amazon GameLift Servers game server, an app needs both the IP address and port number. This value isn't final until placement status is <code>FULFILLED</code>. </p>"""
    dns_name: NotRequired["capo_gamelift.types.dns_name.DnsName"]
    """<p>The DNS identifier assigned to the instance that is running the game session. Values have the following format:</p> <ul> <li> <p>TLS-enabled fleets: <code><unique identifier>.<region identifier>.amazongamelift.com</code>.</p> </li> <li> <p>Non-TLS-enabled fleets: <code>ec2-<unique identifier>.compute.amazonaws.com</code>. (See <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-instance-addressing.html#concepts-public-addresses">Amazon EC2 Instance IP Addressing</a>.)</p> </li> </ul> <p>When connecting to a game session that is running on a TLS-enabled fleet, you must use the DNS name, not the IP address.</p>"""
    port: NotRequired["capo_gamelift.types.port_number.PortNumber"]
    """<p>The port number for the game session. To connect to a Amazon GameLift Servers game server, an app needs both the IP address and port number. This value isn't final until placement status is <code>FULFILLED</code>.</p>"""
    placed_player_sessions: NotRequired[
        "capo_gamelift.types.placed_player_session_list.PlacedPlayerSessionList"
    ]
    """<p>A collection of information on player sessions created in response to the game session placement request. These player sessions are created only after a new game session is successfully placed (placement status is <code>FULFILLED</code>). This information includes the player ID, provided in the placement request, and a corresponding player session ID.</p>"""
    game_session_data: NotRequired[
        "capo_gamelift.types.large_game_session_data.LargeGameSessionData"
    ]
    """<p>A set of custom game session properties, formatted as a single string value. This data is passed to a game server process with a request to start a new game session. For more information, see <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession">Start a game session</a>.</p>"""
    matchmaker_data: NotRequired["capo_gamelift.types.matchmaker_data.MatchmakerData"]
    """<p>Information on the matchmaking process for this game. Data is in JSON syntax, formatted as a string. It identifies the matchmaking configuration used to create the match, and contains data on all players assigned to the match, including player attributes and team assignments. For more details on matchmaker data, see <a href="https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-server.html#match-server-data">Match Data</a>.</p>"""
    priority_configuration_override: NotRequired[
        "capo_gamelift.types.priority_configuration_override.PriorityConfigurationOverride"
    ]
    """<p>An alternative priority list of locations that's included with a game session placement request. When provided, the list overrides a queue's location order list for this game session placement request only. The list might include Amazon Web Services Regions, local zones, and custom locations (for Anywhere fleets). The fallback strategy tells Amazon GameLift Servers what action to take (if any) in the event that it failed to place a new game session. </p>"""
    player_gateway_status: NotRequired[
        "capo_gamelift.types.player_gateway_status.PlayerGatewayStatus"
    ]
    """<p>The current status of player gateway for the game session placement. Note, even if a fleet has PlayerGatewayMode configured as <code>ENABLED</code>, player gateway might not be available in a specific location. For more information about locations where player gateway is supported, see <a href="https://docs.aws.amazon.com/gameliftservers/latest/developerguide/gamelift-regions.html">Amazon GameLift Servers service locations</a>.</p> <p>Possible values include:</p> <ul> <li> <p> <code>ENABLED</code> -- Player gateway is available for this game session placement.</p> </li> <li> <p> <code>DISABLED</code> -- Player gateway is not available for this game session placement.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GameSessionPlacement) -> dict:
    out: dict = {}
    if "placement_id" in value:
        out["PlacementId"] = value["placement_id"]
    if "game_session_queue_name" in value:
        out["GameSessionQueueName"] = value["game_session_queue_name"]
    if "status" in value:
        import capo_gamelift.types.game_session_placement_state

        out["Status"] = (
            capo_gamelift.types.game_session_placement_state.serialize_aws_json_1_1(
                value["status"]
            )
        )
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
    if "game_session_id" in value:
        out["GameSessionId"] = value["game_session_id"]
    if "game_session_arn" in value:
        out["GameSessionArn"] = value["game_session_arn"]
    if "game_session_region" in value:
        out["GameSessionRegion"] = value["game_session_region"]
    if "player_latencies" in value:
        import capo_gamelift.types.player_latency_list

        out["PlayerLatencies"] = (
            capo_gamelift.types.player_latency_list.serialize_aws_json_1_1(
                value["player_latencies"]
            )
        )
    if "start_time" in value:
        import capo_gamelift.types.timestamp

        out["StartTime"] = capo_gamelift.types.timestamp.serialize_aws_json_1_1(
            value["start_time"]
        )
    if "end_time" in value:
        import capo_gamelift.types.timestamp

        out["EndTime"] = capo_gamelift.types.timestamp.serialize_aws_json_1_1(
            value["end_time"]
        )
    if "ip_address" in value:
        out["IpAddress"] = value["ip_address"]
    if "dns_name" in value:
        out["DnsName"] = value["dns_name"]
    if "port" in value:
        out["Port"] = value["port"]
    if "placed_player_sessions" in value:
        import capo_gamelift.types.placed_player_session_list

        out["PlacedPlayerSessions"] = (
            capo_gamelift.types.placed_player_session_list.serialize_aws_json_1_1(
                value["placed_player_sessions"]
            )
        )
    if "game_session_data" in value:
        out["GameSessionData"] = value["game_session_data"]
    if "matchmaker_data" in value:
        out["MatchmakerData"] = value["matchmaker_data"]
    if "priority_configuration_override" in value:
        import capo_gamelift.types.priority_configuration_override

        out["PriorityConfigurationOverride"] = (
            capo_gamelift.types.priority_configuration_override.serialize_aws_json_1_1(
                value["priority_configuration_override"]
            )
        )
    if "player_gateway_status" in value:
        import capo_gamelift.types.player_gateway_status

        out["PlayerGatewayStatus"] = (
            capo_gamelift.types.player_gateway_status.serialize_aws_json_1_1(
                value["player_gateway_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GameSessionPlacement:
    out: GameSessionPlacement = {}  # type: ignore[typeddict-item]
    if data.get("PlacementId") is not None:
        out["placement_id"] = data["PlacementId"]
    if data.get("GameSessionQueueName") is not None:
        out["game_session_queue_name"] = data["GameSessionQueueName"]
    if data.get("Status") is not None:
        import capo_gamelift.types.game_session_placement_state

        out["status"] = (
            capo_gamelift.types.game_session_placement_state.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
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
    if data.get("GameSessionId") is not None:
        out["game_session_id"] = data["GameSessionId"]
    if data.get("GameSessionArn") is not None:
        out["game_session_arn"] = data["GameSessionArn"]
    if data.get("GameSessionRegion") is not None:
        out["game_session_region"] = data["GameSessionRegion"]
    if data.get("PlayerLatencies") is not None:
        import capo_gamelift.types.player_latency_list

        out["player_latencies"] = (
            capo_gamelift.types.player_latency_list.deserialize_aws_json_1_1(
                data["PlayerLatencies"]
            )
        )
    if data.get("StartTime") is not None:
        import capo_gamelift.types.timestamp

        out["start_time"] = capo_gamelift.types.timestamp.deserialize_aws_json_1_1(
            data["StartTime"]
        )
    if data.get("EndTime") is not None:
        import capo_gamelift.types.timestamp

        out["end_time"] = capo_gamelift.types.timestamp.deserialize_aws_json_1_1(
            data["EndTime"]
        )
    if data.get("IpAddress") is not None:
        out["ip_address"] = data["IpAddress"]
    if data.get("DnsName") is not None:
        out["dns_name"] = data["DnsName"]
    if data.get("Port") is not None:
        out["port"] = data["Port"]
    if data.get("PlacedPlayerSessions") is not None:
        import capo_gamelift.types.placed_player_session_list

        out["placed_player_sessions"] = (
            capo_gamelift.types.placed_player_session_list.deserialize_aws_json_1_1(
                data["PlacedPlayerSessions"]
            )
        )
    if data.get("GameSessionData") is not None:
        out["game_session_data"] = data["GameSessionData"]
    if data.get("MatchmakerData") is not None:
        out["matchmaker_data"] = data["MatchmakerData"]
    if data.get("PriorityConfigurationOverride") is not None:
        import capo_gamelift.types.priority_configuration_override

        out["priority_configuration_override"] = (
            capo_gamelift.types.priority_configuration_override.deserialize_aws_json_1_1(
                data["PriorityConfigurationOverride"]
            )
        )
    if data.get("PlayerGatewayStatus") is not None:
        import capo_gamelift.types.player_gateway_status

        out["player_gateway_status"] = (
            capo_gamelift.types.player_gateway_status.deserialize_aws_json_1_1(
                data["PlayerGatewayStatus"]
            )
        )
    return out
