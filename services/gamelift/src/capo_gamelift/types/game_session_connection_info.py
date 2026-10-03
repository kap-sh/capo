"""Generated from Smithy shape ``com.amazonaws.gamelift#GameSessionConnectionInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.arn_string_model
    import capo_gamelift.types.dns_name
    import capo_gamelift.types.ip_address
    import capo_gamelift.types.matched_player_session_list
    import capo_gamelift.types.player_gateway_status
    import capo_gamelift.types.positive_integer


class GameSessionConnectionInfo(TypedDict, closed=True):
    game_session_arn: NotRequired["capo_gamelift.types.arn_string_model.ArnStringModel"]
    """<p>An identifier for the game session that is unique across all regions. The value is always a full ARN in the following format: For Home Region game session - <code>arn:aws:gamelift:<home_region>::gamesession/<fleet ID>/<ID string></code>. For Remote Location game session - <code>arn:aws:gamelift:<home_region>::gamesession/<fleet ID>/<location>/<ID string></code>.</p>"""
    ip_address: NotRequired["capo_gamelift.types.ip_address.IpAddress"]
    """<p>The IP address of the game session. To connect to a Amazon GameLift Servers game server, an app needs both the IP address and port number.</p>"""
    dns_name: NotRequired["capo_gamelift.types.dns_name.DnsName"]
    """<p>The DNS identifier assigned to the instance that is running the game session. Values have the following format:</p> <ul> <li> <p>TLS-enabled fleets: <code><unique identifier>.<region identifier>.amazongamelift.com</code>.</p> </li> <li> <p>Non-TLS-enabled fleets: <code>ec2-<unique identifier>.compute.amazonaws.com</code>. (See <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-instance-addressing.html#concepts-public-addresses">Amazon EC2 Instance IP Addressing</a>.)</p> </li> </ul> <p>When connecting to a game session that is running on a TLS-enabled fleet, you must use the DNS name, not the IP address.</p>"""
    port: NotRequired["capo_gamelift.types.positive_integer.PositiveInteger"]
    """<p>The port number for the game session. To connect to a Amazon GameLift Servers game server, an app needs both the IP address and port number.</p>"""
    matched_player_sessions: NotRequired[
        "capo_gamelift.types.matched_player_session_list.MatchedPlayerSessionList"
    ]
    """<p>A collection of player session IDs, one for each player ID that was included in the original matchmaking request. </p>"""
    player_gateway_status: NotRequired[
        "capo_gamelift.types.player_gateway_status.PlayerGatewayStatus"
    ]
    """<p>The current status of player gateway for the game session. Note, even if a fleet has PlayerGatewayMode configured as <code>ENABLED</code>, player gateway might not be available in a specific location. For more information about locations where player gateway is supported, see <a href="https://docs.aws.amazon.com/gameliftservers/latest/developerguide/gamelift-regions.html">supported locations</a>.</p> <p>Possible values include:</p> <ul> <li> <p> <code>ENABLED</code> -- Player gateway is available for this game session.</p> </li> <li> <p> <code>DISABLED</code> -- Player gateway is not available for this game session.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GameSessionConnectionInfo) -> dict:
    out: dict = {}
    if "game_session_arn" in value:
        out["GameSessionArn"] = value["game_session_arn"]
    if "ip_address" in value:
        out["IpAddress"] = value["ip_address"]
    if "dns_name" in value:
        out["DnsName"] = value["dns_name"]
    if "port" in value:
        out["Port"] = value["port"]
    if "matched_player_sessions" in value:
        import capo_gamelift.types.matched_player_session_list

        out["MatchedPlayerSessions"] = (
            capo_gamelift.types.matched_player_session_list.serialize_aws_json_1_1(
                value["matched_player_sessions"]
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


def deserialize_aws_json_1_1(data: dict) -> GameSessionConnectionInfo:
    out: GameSessionConnectionInfo = {}  # type: ignore[typeddict-item]
    if data.get("GameSessionArn") is not None:
        out["game_session_arn"] = data["GameSessionArn"]
    if data.get("IpAddress") is not None:
        out["ip_address"] = data["IpAddress"]
    if data.get("DnsName") is not None:
        out["dns_name"] = data["DnsName"]
    if data.get("Port") is not None:
        out["port"] = data["Port"]
    if data.get("MatchedPlayerSessions") is not None:
        import capo_gamelift.types.matched_player_session_list

        out["matched_player_sessions"] = (
            capo_gamelift.types.matched_player_session_list.deserialize_aws_json_1_1(
                data["MatchedPlayerSessions"]
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
