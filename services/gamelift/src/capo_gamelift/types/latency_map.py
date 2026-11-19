"""Generated from Smithy shape ``com.amazonaws.gamelift#LatencyMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_gamelift.types.non_empty_string
    import capo_gamelift.types.positive_integer

LatencyMap: TypeAlias = dict[
    "capo_gamelift.types.non_empty_string.NonEmptyString",
    "capo_gamelift.types.positive_integer.PositiveInteger",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: LatencyMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> LatencyMap:
    out: LatencyMap = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(input_to_serialize: LatencyMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_cbor(data: dict) -> LatencyMap:
    out: LatencyMap = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out
