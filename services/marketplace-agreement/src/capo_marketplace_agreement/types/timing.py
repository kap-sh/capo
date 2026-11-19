"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#Timing``."""

from typing import Literal, TypeAlias, cast

Timing: TypeAlias = Literal[
    "ON_ACCEPTANCE",
    "SCHEDULED",
    "BILLING_PERIOD",
    "NOT_APPLICABLE",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Timing) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> Timing:
    return cast(Timing, data)
