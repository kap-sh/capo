"""Generated from Smithy shape ``com.amazonaws.gamelift#DeleteGameServerGroupOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.game_server_group


class DeleteGameServerGroupOutput(TypedDict, closed=True):
    game_server_group: NotRequired[
        "capo_gamelift.types.game_server_group.GameServerGroup"
    ]
    """<p>An object that describes the deleted game server group resource, with status updated to <code>DELETE_SCHEDULED</code>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteGameServerGroupOutput) -> dict:
    out: dict = {}
    if "game_server_group" in value:
        import capo_gamelift.types.game_server_group

        out["GameServerGroup"] = (
            capo_gamelift.types.game_server_group.serialize_aws_json_1_1(
                value["game_server_group"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteGameServerGroupOutput:
    out: DeleteGameServerGroupOutput = {}  # type: ignore[typeddict-item]
    if data.get("GameServerGroup") is not None:
        import capo_gamelift.types.game_server_group

        out["game_server_group"] = (
            capo_gamelift.types.game_server_group.deserialize_aws_json_1_1(
                data["GameServerGroup"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteGameServerGroupOutput) -> dict:
    out: dict = {}
    if "game_server_group" in value:
        import capo_gamelift.types.game_server_group

        out["GameServerGroup"] = capo_gamelift.types.game_server_group.serialize_cbor(
            value["game_server_group"]
        )
    return out


def deserialize_cbor(data: dict) -> DeleteGameServerGroupOutput:
    out: DeleteGameServerGroupOutput = {}  # type: ignore[typeddict-item]
    if data.get("GameServerGroup") is not None:
        import capo_gamelift.types.game_server_group

        out["game_server_group"] = (
            capo_gamelift.types.game_server_group.deserialize_cbor(
                data["GameServerGroup"]
            )
        )
    return out
