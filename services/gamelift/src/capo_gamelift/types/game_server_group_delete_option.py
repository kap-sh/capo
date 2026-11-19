"""Generated from Smithy shape ``com.amazonaws.gamelift#GameServerGroupDeleteOption``."""

from typing import Literal, TypeAlias, cast

GameServerGroupDeleteOption: TypeAlias = Literal[
    "SAFE_DELETE",
    "FORCE_DELETE",
    "RETAIN",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GameServerGroupDeleteOption) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> GameServerGroupDeleteOption:
    return cast(GameServerGroupDeleteOption, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GameServerGroupDeleteOption) -> str:
    return value


def deserialize_cbor(data: str) -> GameServerGroupDeleteOption:
    return cast(GameServerGroupDeleteOption, data)
