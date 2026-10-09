"""Generated from Smithy shape ``com.amazonaws.guardduty#UsageFeature``."""

from typing import Literal, TypeAlias, cast

UsageFeature: TypeAlias = Literal[
    "FLOW_LOGS",
    "CLOUD_TRAIL",
    "DNS_LOGS",
    "S3_DATA_EVENTS",
    "EKS_AUDIT_LOGS",
    "EBS_MALWARE_PROTECTION",
    "RDS_LOGIN_EVENTS",
    "LAMBDA_NETWORK_LOGS",
    "EKS_RUNTIME_MONITORING",
    "EC2_RUNTIME_MONITORING",
    "FARGATE_RUNTIME_MONITORING",
    "RDS_DBI_PROTECTION_PROVISIONED",
    "RDS_DBI_PROTECTION_SERVERLESS",
    "RDS_DBI_PROTECTION_LIMITLESS",
    "RDS_DATA_ACTIVITY_DBI_PROTECTION_PROVISIONED",
    "RDS_DATA_ACTIVITY_DBI_PROTECTION_SERVERLESS",
    "RDS_DATA_ACTIVITY_DBI_PROTECTION_LIMITLESS",
    "AI_PROTECTION",
]


# --- restJson1 ser/de ---
def serialize_json(value: UsageFeature) -> str:
    return value


def deserialize_json(data: str) -> UsageFeature:
    return cast(UsageFeature, data)
