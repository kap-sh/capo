"""Generated from Smithy shape ``com.amazonaws.guardduty#InvestigationResourceType``."""

from typing import Literal, TypeAlias, cast

InvestigationResourceType: TypeAlias = Literal[
    "EC2_INSTANCE",
    "EBS_VOLUME",
    "S3_BUCKET",
    "IAM_ROLE",
    "IAM_USER",
    "IAM_ACCESS_KEY",
    "LAMBDA_FUNCTION",
    "EKS_CLUSTER",
    "ECS_CLUSTER",
    "KUBERNETES_WORKLOAD",
    "RDS_INSTANCE",
    "RDS_DB_USER",
    "EC2_SECURITY_GROUP",
]


# --- restJson1 ser/de ---
def serialize_json(value: InvestigationResourceType) -> str:
    return value


def deserialize_json(data: str) -> InvestigationResourceType:
    return cast(InvestigationResourceType, data)
