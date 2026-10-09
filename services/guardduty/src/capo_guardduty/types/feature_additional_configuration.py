"""Generated from Smithy shape ``com.amazonaws.guardduty#FeatureAdditionalConfiguration``."""

from typing import Literal, TypeAlias, cast

FeatureAdditionalConfiguration: TypeAlias = Literal[
    "EKS_ADDON_MANAGEMENT",
    "ECS_FARGATE_AGENT_MANAGEMENT",
    "EC2_AGENT_MANAGEMENT",
    "RDS_DATA_RISK",
]


# --- restJson1 ser/de ---
def serialize_json(value: FeatureAdditionalConfiguration) -> str:
    return value


def deserialize_json(data: str) -> FeatureAdditionalConfiguration:
    return cast(FeatureAdditionalConfiguration, data)
