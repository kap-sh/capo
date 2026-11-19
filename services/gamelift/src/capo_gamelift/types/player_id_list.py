"""Generated from Smithy shape ``com.amazonaws.gamelift#PlayerIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_gamelift.types.player_id

PlayerIdList: TypeAlias = list["capo_gamelift.types.player_id.PlayerId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PlayerIdList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> PlayerIdList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PlayerIdList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> PlayerIdList:
    return [item for item in data if item is not None]
