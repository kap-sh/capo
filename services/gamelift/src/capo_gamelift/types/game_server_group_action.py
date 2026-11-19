"""Generated from Smithy shape ``com.amazonaws.gamelift#GameServerGroupAction``."""

from typing import Literal, TypeAlias, cast

GameServerGroupAction: TypeAlias = Literal["REPLACE_INSTANCE_TYPES",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GameServerGroupAction) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> GameServerGroupAction:
    return cast(GameServerGroupAction, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GameServerGroupAction) -> str:
    return value


def deserialize_cbor(data: str) -> GameServerGroupAction:
    return cast(GameServerGroupAction, data)
