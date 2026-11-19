"""Generated from Smithy shape ``com.amazonaws.sagemaker#RoutingStrategy``."""

from typing import Literal, TypeAlias, cast

RoutingStrategy: TypeAlias = Literal[
    "LEAST_OUTSTANDING_REQUESTS",
    "RANDOM",
    "PREFIX_AWARE",
    "KV_AWARE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RoutingStrategy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RoutingStrategy:
    return cast(RoutingStrategy, data)
