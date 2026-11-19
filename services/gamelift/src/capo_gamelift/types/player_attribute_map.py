"""Generated from Smithy shape ``com.amazonaws.gamelift#PlayerAttributeMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_gamelift.types.attribute_value
    import capo_gamelift.types.non_zero_and_max_string

PlayerAttributeMap: TypeAlias = dict[
    "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString",
    "capo_gamelift.types.attribute_value.AttributeValue",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: PlayerAttributeMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_gamelift.types.attribute_value

        out[key] = capo_gamelift.types.attribute_value.serialize_aws_json_1_1(value)
    return out


def deserialize_aws_json_1_1(data: dict) -> PlayerAttributeMap:
    out: PlayerAttributeMap = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_gamelift.types.attribute_value

        out[key] = capo_gamelift.types.attribute_value.deserialize_aws_json_1_1(value)
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(input_to_serialize: PlayerAttributeMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_gamelift.types.attribute_value

        out[key] = capo_gamelift.types.attribute_value.serialize_cbor(value)
    return out


def deserialize_cbor(data: dict) -> PlayerAttributeMap:
    out: PlayerAttributeMap = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_gamelift.types.attribute_value

        out[key] = capo_gamelift.types.attribute_value.deserialize_cbor(value)
    return out
