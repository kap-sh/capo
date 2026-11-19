"""Generated from Smithy shape ``com.amazonaws.gamelift#GameServerInstanceIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_gamelift.types.game_server_instance_id

GameServerInstanceIds: TypeAlias = list[
    "capo_gamelift.types.game_server_instance_id.GameServerInstanceId"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GameServerInstanceIds) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> GameServerInstanceIds:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GameServerInstanceIds) -> list:
    return list(value)


def deserialize_cbor(data: list) -> GameServerInstanceIds:
    return [item for item in data if item is not None]
