"""Generated from Smithy shape ``com.amazonaws.lightsail#LightsailDistributionSubdomainStateEnum``."""

from typing import Literal, TypeAlias, cast

LightsailDistributionSubdomainStateEnum: TypeAlias = Literal[
    "Creating",
    "Attaching",
    "Attached",
    "Error",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LightsailDistributionSubdomainStateEnum) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LightsailDistributionSubdomainStateEnum:
    return cast(LightsailDistributionSubdomainStateEnum, data)
