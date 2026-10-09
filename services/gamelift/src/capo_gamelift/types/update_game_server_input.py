"""Generated from Smithy shape ``com.amazonaws.gamelift#UpdateGameServerInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.game_server_data
    import capo_gamelift.types.game_server_group_name_or_arn
    import capo_gamelift.types.game_server_health_check
    import capo_gamelift.types.game_server_id
    import capo_gamelift.types.game_server_utilization_status


class UpdateGameServerInput(TypedDict, closed=True):
    game_server_group_name: NotRequired[
        "capo_gamelift.types.game_server_group_name_or_arn.GameServerGroupNameOrArn"
    ]
    """<p>A unique identifier for the game server group where the game server is running.</p>"""
    game_server_id: NotRequired["capo_gamelift.types.game_server_id.GameServerId"]
    """<p>A custom string that uniquely identifies the game server to update.</p>"""
    game_server_data: NotRequired["capo_gamelift.types.game_server_data.GameServerData"]
    """<p>A set of custom game server properties, formatted as a single string value. This data is passed to a game client or service when it requests information on game servers. </p>"""
    utilization_status: NotRequired[
        "capo_gamelift.types.game_server_utilization_status.GameServerUtilizationStatus"
    ]
    """<p>Indicates if the game server is available or is currently hosting gameplay. You can update a game server status from <code>AVAILABLE</code> to <code>UTILIZED</code>, but you can't change the status from <code>UTILIZED</code> to <code>AVAILABLE</code>.</p>"""
    health_check: NotRequired[
        "capo_gamelift.types.game_server_health_check.GameServerHealthCheck"
    ]
    """<p>Indicates health status of the game server. A request that includes this parameter updates the game server's <i>LastHealthCheckTime</i> timestamp. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateGameServerInput) -> dict:
    out: dict = {}
    if "game_server_group_name" in value:
        out["GameServerGroupName"] = value["game_server_group_name"]
    if "game_server_id" in value:
        out["GameServerId"] = value["game_server_id"]
    if "game_server_data" in value:
        out["GameServerData"] = value["game_server_data"]
    if "utilization_status" in value:
        import capo_gamelift.types.game_server_utilization_status

        out["UtilizationStatus"] = (
            capo_gamelift.types.game_server_utilization_status.serialize_aws_json_1_1(
                value["utilization_status"]
            )
        )
    if "health_check" in value:
        import capo_gamelift.types.game_server_health_check

        out["HealthCheck"] = (
            capo_gamelift.types.game_server_health_check.serialize_aws_json_1_1(
                value["health_check"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateGameServerInput:
    out: UpdateGameServerInput = {}  # type: ignore[typeddict-item]
    if data.get("GameServerGroupName") is not None:
        out["game_server_group_name"] = data["GameServerGroupName"]
    if data.get("GameServerId") is not None:
        out["game_server_id"] = data["GameServerId"]
    if data.get("GameServerData") is not None:
        out["game_server_data"] = data["GameServerData"]
    if data.get("UtilizationStatus") is not None:
        import capo_gamelift.types.game_server_utilization_status

        out["utilization_status"] = (
            capo_gamelift.types.game_server_utilization_status.deserialize_aws_json_1_1(
                data["UtilizationStatus"]
            )
        )
    if data.get("HealthCheck") is not None:
        import capo_gamelift.types.game_server_health_check

        out["health_check"] = (
            capo_gamelift.types.game_server_health_check.deserialize_aws_json_1_1(
                data["HealthCheck"]
            )
        )
    return out
