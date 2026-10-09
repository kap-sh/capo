"""Generated from Smithy shape ``com.amazonaws.guardduty#OrgFeatureAdditionalConfiguration``."""

from typing import Literal, TypeAlias, cast

OrgFeatureAdditionalConfiguration: TypeAlias = Literal[
    "EKS_ADDON_MANAGEMENT",
    "ECS_FARGATE_AGENT_MANAGEMENT",
    "EC2_AGENT_MANAGEMENT",
    "RDS_DATA_RISK",
]


# --- restJson1 ser/de ---
def serialize_json(value: OrgFeatureAdditionalConfiguration) -> str:
    return value


def deserialize_json(data: str) -> OrgFeatureAdditionalConfiguration:
    return cast(OrgFeatureAdditionalConfiguration, data)
