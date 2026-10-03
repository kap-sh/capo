"""Generated from Smithy shape ``com.amazonaws.gamelift#GameSession``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.compute_name
    import capo_gamelift.types.dns_name
    import capo_gamelift.types.fleet_arn
    import capo_gamelift.types.fleet_id
    import capo_gamelift.types.game_property_list
    import capo_gamelift.types.game_session_status
    import capo_gamelift.types.game_session_status_reason
    import capo_gamelift.types.ip_address
    import capo_gamelift.types.large_game_session_data
    import capo_gamelift.types.location_string_model
    import capo_gamelift.types.matchmaker_data
    import capo_gamelift.types.non_zero_and_max_string
    import capo_gamelift.types.player_gateway_status
    import capo_gamelift.types.player_session_creation_policy
    import capo_gamelift.types.port_number
    import capo_gamelift.types.timestamp
    import capo_gamelift.types.whole_number


class GameSession(TypedDict, closed=True):
    game_session_id: NotRequired[
        "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>An identifier for the game session that is unique across all regions. The value is always a full ARN in the following format: For Home Region game session - <code>arn:aws:gamelift:<home_region>::gamesession/<fleet ID>/<ID string></code>. For Remote Location game session - <code>arn:aws:gamelift:<home_region>::gamesession/<fleet ID>/<location>/<ID string></code>.</p>"""
    name: NotRequired["capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"]
    """<p>A descriptive label that is associated with a game session. Session names do not need to be unique.</p>"""
    fleet_id: NotRequired["capo_gamelift.types.fleet_id.FleetId"]
    """<p>A unique identifier for the fleet that the game session is running on.</p>"""
    fleet_arn: NotRequired["capo_gamelift.types.fleet_arn.FleetArn"]
    """<p>The Amazon Resource Name (<a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html">ARN</a>) associated with the GameLift fleet that this game session is running on. </p>"""
    creation_time: NotRequired["capo_gamelift.types.timestamp.Timestamp"]
    """<p>A time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example <code>"1469498468.057"</code>).</p>"""
    termination_time: NotRequired["capo_gamelift.types.timestamp.Timestamp"]
    """<p>A time stamp indicating when this data object was terminated. Format is a number expressed in Unix time as milliseconds (for example <code>"1469498468.057"</code>).</p>"""
    current_player_session_count: NotRequired[
        "capo_gamelift.types.whole_number.WholeNumber"
    ]
    """<p>Number of players currently in the game session.</p>"""
    maximum_player_session_count: NotRequired[
        "capo_gamelift.types.whole_number.WholeNumber"
    ]
    """<p>The maximum number of players that can be connected simultaneously to the game session.</p>"""
    status: NotRequired["capo_gamelift.types.game_session_status.GameSessionStatus"]
    """<p>Current status of the game session. A game session must have an <code>ACTIVE</code> status to have player sessions.</p>"""
    status_reason: NotRequired[
        "capo_gamelift.types.game_session_status_reason.GameSessionStatusReason"
    ]
    """<p>Provides additional information about game session status. </p> <ul> <li> <p> <code>INTERRUPTED</code> -- The game session was hosted on an EC2 Spot instance that was reclaimed, causing the active game session to be stopped.</p> </li> <li> <p> <code>TRIGGERED_ON_PROCESS_TERMINATE</code> – The game session was stopped by calling <code>TerminateGameSession</code> with the termination mode <code>TRIGGER_ON_PROCESS_TERMINATE</code>. </p> </li> <li> <p> <code>FORCE_TERMINATED</code> – The game session was stopped by calling <code>TerminateGameSession</code> with the termination mode <code>FORCE_TERMINATE</code>. </p> </li> </ul> <p></p>"""
    game_properties: NotRequired[
        "capo_gamelift.types.game_property_list.GamePropertyList"
    ]
    """<p>A set of key-value pairs that can store custom data in a game session. For example: <code>{"Key": "difficulty", "Value": "novice"}</code>.</p> <note> <ul> <li> <p>Avoid using periods (".") in property keys if you plan to search for game sessions by properties. Property keys containing periods cannot be searched and will be filtered out from search results due to search index limitations.</p> </li> <li> <p>If you use SearchGameSessions API, there is a limit of 500 game property keys across all game sessions and all fleets per region. If the limit is exceeded, there will potentially be game session entries missing from SearchGameSessions API results.</p> </li> </ul> </note>"""
    ip_address: NotRequired["capo_gamelift.types.ip_address.IpAddress"]
    """<p>The IP address of the game session. To connect to a Amazon GameLift Servers game server, an app needs both the IP address and port number.</p>"""
    dns_name: NotRequired["capo_gamelift.types.dns_name.DnsName"]
    """<p>The DNS identifier assigned to the instance that is running the game session. Values have the following format:</p> <ul> <li> <p>TLS-enabled fleets: <code><unique identifier>.<region identifier>.amazongamelift.com</code>.</p> </li> <li> <p>Non-TLS-enabled fleets: <code>ec2-<unique identifier>.compute.amazonaws.com</code>. (See <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-instance-addressing.html#concepts-public-addresses">Amazon EC2 Instance IP Addressing</a>.)</p> </li> </ul> <p>When connecting to a game session that is running on a TLS-enabled fleet, you must use the DNS name, not the IP address.</p>"""
    port: NotRequired["capo_gamelift.types.port_number.PortNumber"]
    """<p>The port number for the game session. To connect to a Amazon GameLift Servers game server, an app needs both the IP address and port number.</p>"""
    player_session_creation_policy: NotRequired[
        "capo_gamelift.types.player_session_creation_policy.PlayerSessionCreationPolicy"
    ]
    """<p>Indicates whether the game session is accepting new players.</p>"""
    creator_id: NotRequired[
        "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>A unique identifier for a player. This ID is used to enforce a resource protection policy (if one exists), that limits the number of game sessions a player can create.</p>"""
    game_session_data: NotRequired[
        "capo_gamelift.types.large_game_session_data.LargeGameSessionData"
    ]
    """<p>A set of custom game session properties, formatted as a single string value. This data is passed to a game server process with a request to start a new game session. For more information, see <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession">Start a game session</a>.</p>"""
    matchmaker_data: NotRequired["capo_gamelift.types.matchmaker_data.MatchmakerData"]
    """<p>Information about the matchmaking process that resulted in the game session, if matchmaking was used. Data is in JSON syntax, formatted as a string. Information includes the matchmaker ID as well as player attributes and team assignments. For more details on matchmaker data, see <a href="https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-server.html#match-server-data">Match Data</a>. Matchmaker data is updated whenever new players are added during a successful backfill (see <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_StartMatchBackfill.html">StartMatchBackfill</a>). </p>"""
    location: NotRequired[
        "capo_gamelift.types.location_string_model.LocationStringModel"
    ]
    """<p>The fleet location where the game session is running. This value might specify the fleet's home Region or a remote location. Location is expressed as an Amazon Web Services Region code such as <code>us-west-2</code>. </p>"""
    compute_name: NotRequired["capo_gamelift.types.compute_name.ComputeName"]
    """<p>A descriptive label for the compute resource. The compute resource that is hosting the game session. For EC2 fleets, this is the EC2 instance ID. For Container fleets, each game server container group on a fleet instance is assigned a compute name. For Anywhere fleets, this is the custom compute name.</p>"""
    player_gateway_status: NotRequired[
        "capo_gamelift.types.player_gateway_status.PlayerGatewayStatus"
    ]
    """<p>Indicates whether player gateway is available for use for this game session. Note, even if a fleet has PlayerGatewayMode configured as <code>ENABLED</code>, player gateway might not be available in a specific location. For more information about locations where player gateway is supported, see <a href="https://docs.aws.amazon.com/gameliftservers/latest/developerguide/gamelift-regions.html">Amazon GameLift Servers service locations</a>.</p> <p>Possible values include:</p> <ul> <li> <p> <code>ENABLED</code> -- Player gateway is available for routing player connections for this game session.</p> </li> <li> <p> <code>DISABLED</code> -- Player gateway is not available for this game session.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GameSession) -> dict:
    out: dict = {}
    if "game_session_id" in value:
        out["GameSessionId"] = value["game_session_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "fleet_id" in value:
        out["FleetId"] = value["fleet_id"]
    if "fleet_arn" in value:
        out["FleetArn"] = value["fleet_arn"]
    if "creation_time" in value:
        import capo_gamelift.types.timestamp

        out["CreationTime"] = capo_gamelift.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "termination_time" in value:
        import capo_gamelift.types.timestamp

        out["TerminationTime"] = capo_gamelift.types.timestamp.serialize_aws_json_1_1(
            value["termination_time"]
        )
    if "current_player_session_count" in value:
        out["CurrentPlayerSessionCount"] = value["current_player_session_count"]
    if "maximum_player_session_count" in value:
        out["MaximumPlayerSessionCount"] = value["maximum_player_session_count"]
    if "status" in value:
        import capo_gamelift.types.game_session_status

        out["Status"] = capo_gamelift.types.game_session_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "status_reason" in value:
        import capo_gamelift.types.game_session_status_reason

        out["StatusReason"] = (
            capo_gamelift.types.game_session_status_reason.serialize_aws_json_1_1(
                value["status_reason"]
            )
        )
    if "game_properties" in value:
        import capo_gamelift.types.game_property_list

        out["GameProperties"] = (
            capo_gamelift.types.game_property_list.serialize_aws_json_1_1(
                value["game_properties"]
            )
        )
    if "ip_address" in value:
        out["IpAddress"] = value["ip_address"]
    if "dns_name" in value:
        out["DnsName"] = value["dns_name"]
    if "port" in value:
        out["Port"] = value["port"]
    if "player_session_creation_policy" in value:
        import capo_gamelift.types.player_session_creation_policy

        out["PlayerSessionCreationPolicy"] = (
            capo_gamelift.types.player_session_creation_policy.serialize_aws_json_1_1(
                value["player_session_creation_policy"]
            )
        )
    if "creator_id" in value:
        out["CreatorId"] = value["creator_id"]
    if "game_session_data" in value:
        out["GameSessionData"] = value["game_session_data"]
    if "matchmaker_data" in value:
        out["MatchmakerData"] = value["matchmaker_data"]
    if "location" in value:
        out["Location"] = value["location"]
    if "compute_name" in value:
        out["ComputeName"] = value["compute_name"]
    if "player_gateway_status" in value:
        import capo_gamelift.types.player_gateway_status

        out["PlayerGatewayStatus"] = (
            capo_gamelift.types.player_gateway_status.serialize_aws_json_1_1(
                value["player_gateway_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GameSession:
    out: GameSession = {}  # type: ignore[typeddict-item]
    if data.get("GameSessionId") is not None:
        out["game_session_id"] = data["GameSessionId"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("FleetId") is not None:
        out["fleet_id"] = data["FleetId"]
    if data.get("FleetArn") is not None:
        out["fleet_arn"] = data["FleetArn"]
    if data.get("CreationTime") is not None:
        import capo_gamelift.types.timestamp

        out["creation_time"] = capo_gamelift.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if data.get("TerminationTime") is not None:
        import capo_gamelift.types.timestamp

        out["termination_time"] = (
            capo_gamelift.types.timestamp.deserialize_aws_json_1_1(
                data["TerminationTime"]
            )
        )
    if data.get("CurrentPlayerSessionCount") is not None:
        out["current_player_session_count"] = data["CurrentPlayerSessionCount"]
    if data.get("MaximumPlayerSessionCount") is not None:
        out["maximum_player_session_count"] = data["MaximumPlayerSessionCount"]
    if data.get("Status") is not None:
        import capo_gamelift.types.game_session_status

        out["status"] = (
            capo_gamelift.types.game_session_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if data.get("StatusReason") is not None:
        import capo_gamelift.types.game_session_status_reason

        out["status_reason"] = (
            capo_gamelift.types.game_session_status_reason.deserialize_aws_json_1_1(
                data["StatusReason"]
            )
        )
    if data.get("GameProperties") is not None:
        import capo_gamelift.types.game_property_list

        out["game_properties"] = (
            capo_gamelift.types.game_property_list.deserialize_aws_json_1_1(
                data["GameProperties"]
            )
        )
    if data.get("IpAddress") is not None:
        out["ip_address"] = data["IpAddress"]
    if data.get("DnsName") is not None:
        out["dns_name"] = data["DnsName"]
    if data.get("Port") is not None:
        out["port"] = data["Port"]
    if data.get("PlayerSessionCreationPolicy") is not None:
        import capo_gamelift.types.player_session_creation_policy

        out["player_session_creation_policy"] = (
            capo_gamelift.types.player_session_creation_policy.deserialize_aws_json_1_1(
                data["PlayerSessionCreationPolicy"]
            )
        )
    if data.get("CreatorId") is not None:
        out["creator_id"] = data["CreatorId"]
    if data.get("GameSessionData") is not None:
        out["game_session_data"] = data["GameSessionData"]
    if data.get("MatchmakerData") is not None:
        out["matchmaker_data"] = data["MatchmakerData"]
    if data.get("Location") is not None:
        out["location"] = data["Location"]
    if data.get("ComputeName") is not None:
        out["compute_name"] = data["ComputeName"]
    if data.get("PlayerGatewayStatus") is not None:
        import capo_gamelift.types.player_gateway_status

        out["player_gateway_status"] = (
            capo_gamelift.types.player_gateway_status.deserialize_aws_json_1_1(
                data["PlayerGatewayStatus"]
            )
        )
    return out
