"""Generated from Smithy shape ``com.amazonaws.lambda#CapacityProviderPredefinedMetricType``."""

from typing import Literal, TypeAlias, cast

CapacityProviderPredefinedMetricType: TypeAlias = Literal[
    "LambdaCapacityProviderAverageCPUUtilization",
    "LambdaCapacityProviderAverageGPUUtilization",
]


# --- restJson1 ser/de ---
def serialize_json(value: CapacityProviderPredefinedMetricType) -> str:
    return value


def deserialize_json(data: str) -> CapacityProviderPredefinedMetricType:
    return cast(CapacityProviderPredefinedMetricType, data)
