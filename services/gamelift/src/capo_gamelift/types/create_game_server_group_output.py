"""Generated from Smithy shape ``com.amazonaws.gamelift#CreateGameServerGroupOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.game_server_group


class CreateGameServerGroupOutput(TypedDict, closed=True):
    game_server_group: NotRequired[
        "capo_gamelift.types.game_server_group.GameServerGroup"
    ]
    """<p>The newly created game server group object, including the new ARN value for the Amazon GameLift Servers FleetIQ game server group and the object's status. The Amazon EC2 Auto Scaling group ARN is initially null, since the group has not yet been created. This value is added once the game server group status reaches <code>ACTIVE</code>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateGameServerGroupOutput) -> dict:
    out: dict = {}
    if "game_server_group" in value:
        import capo_gamelift.types.game_server_group

        out["GameServerGroup"] = (
            capo_gamelift.types.game_server_group.serialize_aws_json_1_1(
                value["game_server_group"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateGameServerGroupOutput:
    out: CreateGameServerGroupOutput = {}  # type: ignore[typeddict-item]
    if data.get("GameServerGroup") is not None:
        import capo_gamelift.types.game_server_group

        out["game_server_group"] = (
            capo_gamelift.types.game_server_group.deserialize_aws_json_1_1(
                data["GameServerGroup"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateGameServerGroupOutput) -> dict:
    out: dict = {}
    if "game_server_group" in value:
        import capo_gamelift.types.game_server_group

        out["GameServerGroup"] = capo_gamelift.types.game_server_group.serialize_cbor(
            value["game_server_group"]
        )
    return out


def deserialize_cbor(data: dict) -> CreateGameServerGroupOutput:
    out: CreateGameServerGroupOutput = {}  # type: ignore[typeddict-item]
    if data.get("GameServerGroup") is not None:
        import capo_gamelift.types.game_server_group

        out["game_server_group"] = (
            capo_gamelift.types.game_server_group.deserialize_cbor(
                data["GameServerGroup"]
            )
        )
    return out
