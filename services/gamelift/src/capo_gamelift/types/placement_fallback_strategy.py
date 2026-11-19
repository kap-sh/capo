"""Generated from Smithy shape ``com.amazonaws.gamelift#PlacementFallbackStrategy``."""

from typing import Literal, TypeAlias, cast

PlacementFallbackStrategy: TypeAlias = Literal[
    "DEFAULT_AFTER_SINGLE_PASS",
    "NONE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PlacementFallbackStrategy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PlacementFallbackStrategy:
    return cast(PlacementFallbackStrategy, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PlacementFallbackStrategy) -> str:
    return value


def deserialize_cbor(data: str) -> PlacementFallbackStrategy:
    return cast(PlacementFallbackStrategy, data)
