"""Generated from Smithy shape ``com.amazonaws.gamelift#PlayerAttributeStringList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_gamelift.types.player_attribute_string

PlayerAttributeStringList: TypeAlias = list[
    "capo_gamelift.types.player_attribute_string.PlayerAttributeString"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PlayerAttributeStringList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> PlayerAttributeStringList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PlayerAttributeStringList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> PlayerAttributeStringList:
    return [item for item in data if item is not None]
