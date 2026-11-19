"""Generated from Smithy shape ``com.amazonaws.gamelift#SuspendGameServerGroupInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.game_server_group_actions
    import capo_gamelift.types.game_server_group_name_or_arn


class SuspendGameServerGroupInput(TypedDict, closed=True):
    game_server_group_name: NotRequired[
        "capo_gamelift.types.game_server_group_name_or_arn.GameServerGroupNameOrArn"
    ]
    """<p>A unique identifier for the game server group. Use either the name or ARN value.</p>"""
    suspend_actions: NotRequired[
        "capo_gamelift.types.game_server_group_actions.GameServerGroupActions"
    ]
    """<p>The activity to suspend for this game server group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SuspendGameServerGroupInput) -> dict:
    out: dict = {}
    if "game_server_group_name" in value:
        out["GameServerGroupName"] = value["game_server_group_name"]
    if "suspend_actions" in value:
        import capo_gamelift.types.game_server_group_actions

        out["SuspendActions"] = (
            capo_gamelift.types.game_server_group_actions.serialize_aws_json_1_1(
                value["suspend_actions"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SuspendGameServerGroupInput:
    out: SuspendGameServerGroupInput = {}  # type: ignore[typeddict-item]
    if data.get("GameServerGroupName") is not None:
        out["game_server_group_name"] = data["GameServerGroupName"]
    if data.get("SuspendActions") is not None:
        import capo_gamelift.types.game_server_group_actions

        out["suspend_actions"] = (
            capo_gamelift.types.game_server_group_actions.deserialize_aws_json_1_1(
                data["SuspendActions"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SuspendGameServerGroupInput) -> dict:
    out: dict = {}
    if "game_server_group_name" in value:
        out["GameServerGroupName"] = value["game_server_group_name"]
    if "suspend_actions" in value:
        import capo_gamelift.types.game_server_group_actions

        out["SuspendActions"] = (
            capo_gamelift.types.game_server_group_actions.serialize_cbor(
                value["suspend_actions"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> SuspendGameServerGroupInput:
    out: SuspendGameServerGroupInput = {}  # type: ignore[typeddict-item]
    if data.get("GameServerGroupName") is not None:
        out["game_server_group_name"] = data["GameServerGroupName"]
    if data.get("SuspendActions") is not None:
        import capo_gamelift.types.game_server_group_actions

        out["suspend_actions"] = (
            capo_gamelift.types.game_server_group_actions.deserialize_cbor(
                data["SuspendActions"]
            )
        )
    return out
