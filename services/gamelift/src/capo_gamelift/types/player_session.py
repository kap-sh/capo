"""Generated from Smithy shape ``com.amazonaws.gamelift#PlayerSession``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.dns_name
    import capo_gamelift.types.fleet_arn
    import capo_gamelift.types.fleet_id
    import capo_gamelift.types.ip_address
    import capo_gamelift.types.non_zero_and_max_string
    import capo_gamelift.types.player_data
    import capo_gamelift.types.player_id
    import capo_gamelift.types.player_session_id
    import capo_gamelift.types.player_session_status
    import capo_gamelift.types.port_number
    import capo_gamelift.types.timestamp


class PlayerSession(TypedDict, closed=True):
    player_session_id: NotRequired[
        "capo_gamelift.types.player_session_id.PlayerSessionId"
    ]
    """<p>A unique identifier for a player session.</p>"""
    player_id: NotRequired["capo_gamelift.types.player_id.PlayerId"]
    """<p>A unique identifier for a player that is associated with this player session.</p>"""
    game_session_id: NotRequired[
        "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>An identifier for the game session that is unique across all regions that the player session is connected to. The value is always a full ARN in the following format: For Home Region game session - <code>arn:aws:gamelift:<home_region>::gamesession/<fleet ID>/<ID string></code>. For Remote Location game session - <code>arn:aws:gamelift:<home_region>::gamesession/<fleet ID>/<location>/<ID string></code>.</p>"""
    fleet_id: NotRequired["capo_gamelift.types.fleet_id.FleetId"]
    """<p>A unique identifier for the fleet that the player's game session is running on.</p>"""
    fleet_arn: NotRequired["capo_gamelift.types.fleet_arn.FleetArn"]
    """<p> The Amazon Resource Name (<a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html">ARN</a>) associated with the GameLift fleet that the player's game session is running on. </p>"""
    creation_time: NotRequired["capo_gamelift.types.timestamp.Timestamp"]
    """<p>A time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example <code>"1469498468.057"</code>).</p>"""
    termination_time: NotRequired["capo_gamelift.types.timestamp.Timestamp"]
    """<p>A time stamp indicating when this data object was terminated. Format is a number expressed in Unix time as milliseconds (for example <code>"1469498468.057"</code>).</p>"""
    status: NotRequired["capo_gamelift.types.player_session_status.PlayerSessionStatus"]
    """<p>Current status of the player session.</p> <p>Possible player session statuses include the following:</p> <ul> <li> <p> <b>RESERVED</b> -- The player session request has been received, but the player has not yet connected to the server process and/or been validated. </p> </li> <li> <p> <b>ACTIVE</b> -- The player has been validated by the server process and is currently connected.</p> </li> <li> <p> <b>COMPLETED</b> -- The player connection has been dropped.</p> </li> <li> <p> <b>TIMEDOUT</b> -- A player session request was received, but the player did not connect and/or was not validated within the timeout limit (60 seconds).</p> </li> </ul>"""
    ip_address: NotRequired["capo_gamelift.types.ip_address.IpAddress"]
    """<p>The IP address of the game session. To connect to a Amazon GameLift Servers game server, an app needs both the IP address and port number.</p>"""
    dns_name: NotRequired["capo_gamelift.types.dns_name.DnsName"]
    """<p>The DNS identifier assigned to the instance that is running the game session. Values have the following format:</p> <ul> <li> <p>TLS-enabled fleets: <code><unique identifier>.<region identifier>.amazongamelift.com</code>.</p> </li> <li> <p>Non-TLS-enabled fleets: <code>ec2-<unique identifier>.compute.amazonaws.com</code>. (See <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-instance-addressing.html#concepts-public-addresses">Amazon EC2 Instance IP Addressing</a>.)</p> </li> </ul> <p>When connecting to a game session that is running on a TLS-enabled fleet, you must use the DNS name, not the IP address.</p>"""
    port: NotRequired["capo_gamelift.types.port_number.PortNumber"]
    """<p>Port number for the game session. To connect to a Amazon GameLift Servers server process, an app needs both the IP address and port number.</p>"""
    player_data: NotRequired["capo_gamelift.types.player_data.PlayerData"]
    """<p>Developer-defined information related to a player. Amazon GameLift Servers does not use this data, so it can be formatted as needed for use in the game. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PlayerSession) -> dict:
    out: dict = {}
    if "player_session_id" in value:
        out["PlayerSessionId"] = value["player_session_id"]
    if "player_id" in value:
        out["PlayerId"] = value["player_id"]
    if "game_session_id" in value:
        out["GameSessionId"] = value["game_session_id"]
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
    if "status" in value:
        import capo_gamelift.types.player_session_status

        out["Status"] = (
            capo_gamelift.types.player_session_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "ip_address" in value:
        out["IpAddress"] = value["ip_address"]
    if "dns_name" in value:
        out["DnsName"] = value["dns_name"]
    if "port" in value:
        out["Port"] = value["port"]
    if "player_data" in value:
        out["PlayerData"] = value["player_data"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PlayerSession:
    out: PlayerSession = {}  # type: ignore[typeddict-item]
    if data.get("PlayerSessionId") is not None:
        out["player_session_id"] = data["PlayerSessionId"]
    if data.get("PlayerId") is not None:
        out["player_id"] = data["PlayerId"]
    if data.get("GameSessionId") is not None:
        out["game_session_id"] = data["GameSessionId"]
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
    if data.get("Status") is not None:
        import capo_gamelift.types.player_session_status

        out["status"] = (
            capo_gamelift.types.player_session_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if data.get("IpAddress") is not None:
        out["ip_address"] = data["IpAddress"]
    if data.get("DnsName") is not None:
        out["dns_name"] = data["DnsName"]
    if data.get("Port") is not None:
        out["port"] = data["Port"]
    if data.get("PlayerData") is not None:
        out["player_data"] = data["PlayerData"]
    return out
