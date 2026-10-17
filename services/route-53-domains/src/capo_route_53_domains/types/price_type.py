"""Generated from Smithy shape ``com.amazonaws.route53domains#PriceType``."""

from typing import Literal, TypeAlias, cast

PriceType: TypeAlias = Literal[
    "STANDARD",
    "REGISTRY_PREMIUM",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PriceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PriceType:
    return cast(PriceType, data)
