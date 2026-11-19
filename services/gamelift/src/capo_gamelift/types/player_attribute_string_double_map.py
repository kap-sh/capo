"""Generated from Smithy shape ``com.amazonaws.gamelift#PlayerAttributeStringDoubleMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_gamelift.types.double_object
    import capo_gamelift.types.player_attribute_string

PlayerAttributeStringDoubleMap: TypeAlias = dict[
    "capo_gamelift.types.player_attribute_string.PlayerAttributeString",
    "capo_gamelift.types.double_object.DoubleObject",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: PlayerAttributeStringDoubleMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = (
            "NaN"
            if value != value
            else "Infinity"
            if value == float("inf")
            else "-Infinity"
            if value == float("-inf")
            else value
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PlayerAttributeStringDoubleMap:
    out: PlayerAttributeStringDoubleMap = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = float(value)
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(input_to_serialize: PlayerAttributeStringDoubleMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_cbor(data: dict) -> PlayerAttributeStringDoubleMap:
    out: PlayerAttributeStringDoubleMap = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = float(value)
    return out
