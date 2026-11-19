"""Generated from Smithy shape ``com.amazonaws.wafv2#AnalyticsMode``."""

from typing import Literal, TypeAlias, cast

AnalyticsMode: TypeAlias = Literal[
    "CROSS_REGION",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AnalyticsMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AnalyticsMode:
    return cast(AnalyticsMode, data)
