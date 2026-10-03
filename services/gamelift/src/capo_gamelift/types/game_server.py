"""Generated from Smithy shape ``com.amazonaws.gamelift#GameServer``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.game_server_claim_status
    import capo_gamelift.types.game_server_connection_info
    import capo_gamelift.types.game_server_data
    import capo_gamelift.types.game_server_group_arn
    import capo_gamelift.types.game_server_group_name
    import capo_gamelift.types.game_server_id
    import capo_gamelift.types.game_server_instance_id
    import capo_gamelift.types.game_server_utilization_status
    import capo_gamelift.types.timestamp


class GameServer(TypedDict, closed=True):
    game_server_group_name: NotRequired[
        "capo_gamelift.types.game_server_group_name.GameServerGroupName"
    ]
    """<p>A unique identifier for the game server group where the game server is running.</p>"""
    game_server_group_arn: NotRequired[
        "capo_gamelift.types.game_server_group_arn.GameServerGroupArn"
    ]
    """<p>The ARN identifier for the game server group where the game server is located.</p>"""
    game_server_id: NotRequired["capo_gamelift.types.game_server_id.GameServerId"]
    """<p>A custom string that uniquely identifies the game server. Game server IDs are developer-defined and are unique across all game server groups in an Amazon Web Services account.</p>"""
    instance_id: NotRequired[
        "capo_gamelift.types.game_server_instance_id.GameServerInstanceId"
    ]
    """<p>The unique identifier for the instance where the game server is running. This ID is available in the instance metadata. EC2 instance IDs use a 17-character format, for example: <code>i-1234567890abcdef0</code>.</p>"""
    connection_info: NotRequired[
        "capo_gamelift.types.game_server_connection_info.GameServerConnectionInfo"
    ]
    """<p>The port and IP address that must be used to establish a client connection to the game server.</p>"""
    game_server_data: NotRequired["capo_gamelift.types.game_server_data.GameServerData"]
    """<p>A set of custom game server properties, formatted as a single string value. This data is passed to a game client or service when it requests information on game servers.</p>"""
    claim_status: NotRequired[
        "capo_gamelift.types.game_server_claim_status.GameServerClaimStatus"
    ]
    """<p>Indicates when an available game server has been reserved for gameplay but has not yet started hosting a game. Once it is claimed, the game server remains in <code>CLAIMED</code> status for a maximum of one minute. During this time, game clients connect to the game server to start the game and trigger the game server to update its utilization status. After one minute, the game server claim status reverts to null.</p>"""
    utilization_status: NotRequired[
        "capo_gamelift.types.game_server_utilization_status.GameServerUtilizationStatus"
    ]
    """<p>Indicates whether the game server is currently available for new games or is busy. Possible statuses include:</p> <ul> <li> <p> <code>AVAILABLE</code> - The game server is available to be claimed. A game server that has been claimed remains in this status until it reports game hosting activity. </p> </li> <li> <p> <code>UTILIZED</code> - The game server is currently hosting a game session with players. </p> </li> </ul>"""
    registration_time: NotRequired["capo_gamelift.types.timestamp.Timestamp"]
    """<p>Timestamp that indicates when the game server registered. The format is a number expressed in Unix time as milliseconds (for example <code>"1469498468.057"</code>).</p>"""
    last_claim_time: NotRequired["capo_gamelift.types.timestamp.Timestamp"]
    """<p>Timestamp that indicates the last time the game server was claimed. The format is a number expressed in Unix time as milliseconds (for example <code>"1469498468.057"</code>). This value is used to calculate when a claimed game server's status should revert to null.</p>"""
    last_health_check_time: NotRequired["capo_gamelift.types.timestamp.Timestamp"]
    """<p>Timestamp that indicates the last time the game server was updated with health status. The format is a number expressed in Unix time as milliseconds (for example <code>"1469498468.057"</code>). After game server registration, this property is only changed when a game server update specifies a health check value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GameServer) -> dict:
    out: dict = {}
    if "game_server_group_name" in value:
        out["GameServerGroupName"] = value["game_server_group_name"]
    if "game_server_group_arn" in value:
        out["GameServerGroupArn"] = value["game_server_group_arn"]
    if "game_server_id" in value:
        out["GameServerId"] = value["game_server_id"]
    if "instance_id" in value:
        out["InstanceId"] = value["instance_id"]
    if "connection_info" in value:
        out["ConnectionInfo"] = value["connection_info"]
    if "game_server_data" in value:
        out["GameServerData"] = value["game_server_data"]
    if "claim_status" in value:
        import capo_gamelift.types.game_server_claim_status

        out["ClaimStatus"] = (
            capo_gamelift.types.game_server_claim_status.serialize_aws_json_1_1(
                value["claim_status"]
            )
        )
    if "utilization_status" in value:
        import capo_gamelift.types.game_server_utilization_status

        out["UtilizationStatus"] = (
            capo_gamelift.types.game_server_utilization_status.serialize_aws_json_1_1(
                value["utilization_status"]
            )
        )
    if "registration_time" in value:
        import capo_gamelift.types.timestamp

        out["RegistrationTime"] = capo_gamelift.types.timestamp.serialize_aws_json_1_1(
            value["registration_time"]
        )
    if "last_claim_time" in value:
        import capo_gamelift.types.timestamp

        out["LastClaimTime"] = capo_gamelift.types.timestamp.serialize_aws_json_1_1(
            value["last_claim_time"]
        )
    if "last_health_check_time" in value:
        import capo_gamelift.types.timestamp

        out["LastHealthCheckTime"] = (
            capo_gamelift.types.timestamp.serialize_aws_json_1_1(
                value["last_health_check_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GameServer:
    out: GameServer = {}  # type: ignore[typeddict-item]
    if data.get("GameServerGroupName") is not None:
        out["game_server_group_name"] = data["GameServerGroupName"]
    if data.get("GameServerGroupArn") is not None:
        out["game_server_group_arn"] = data["GameServerGroupArn"]
    if data.get("GameServerId") is not None:
        out["game_server_id"] = data["GameServerId"]
    if data.get("InstanceId") is not None:
        out["instance_id"] = data["InstanceId"]
    if data.get("ConnectionInfo") is not None:
        out["connection_info"] = data["ConnectionInfo"]
    if data.get("GameServerData") is not None:
        out["game_server_data"] = data["GameServerData"]
    if data.get("ClaimStatus") is not None:
        import capo_gamelift.types.game_server_claim_status

        out["claim_status"] = (
            capo_gamelift.types.game_server_claim_status.deserialize_aws_json_1_1(
                data["ClaimStatus"]
            )
        )
    if data.get("UtilizationStatus") is not None:
        import capo_gamelift.types.game_server_utilization_status

        out["utilization_status"] = (
            capo_gamelift.types.game_server_utilization_status.deserialize_aws_json_1_1(
                data["UtilizationStatus"]
            )
        )
    if data.get("RegistrationTime") is not None:
        import capo_gamelift.types.timestamp

        out["registration_time"] = (
            capo_gamelift.types.timestamp.deserialize_aws_json_1_1(
                data["RegistrationTime"]
            )
        )
    if data.get("LastClaimTime") is not None:
        import capo_gamelift.types.timestamp

        out["last_claim_time"] = capo_gamelift.types.timestamp.deserialize_aws_json_1_1(
            data["LastClaimTime"]
        )
    if data.get("LastHealthCheckTime") is not None:
        import capo_gamelift.types.timestamp

        out["last_health_check_time"] = (
            capo_gamelift.types.timestamp.deserialize_aws_json_1_1(
                data["LastHealthCheckTime"]
            )
        )
    return out
