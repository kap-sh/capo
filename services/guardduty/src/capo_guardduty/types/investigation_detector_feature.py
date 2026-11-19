"""Generated from Smithy shape ``com.amazonaws.guardduty#InvestigationDetectorFeature``."""

from typing import Literal, TypeAlias, cast

InvestigationDetectorFeature: TypeAlias = Literal[
    "CLOUD_TRAIL",
    "DNS_LOGS",
    "FLOW_LOGS",
    "S3_DATA_EVENTS",
    "EKS_AUDIT_LOGS",
    "EBS_MALWARE_PROTECTION",
    "RDS_LOGIN_EVENTS",
    "EKS_RUNTIME_MONITORING",
    "EKS_ADDON_MANAGEMENT",
    "LAMBDA_NETWORK_LOGS",
    "RUNTIME_MONITORING",
    "ECS_FARGATE_AGENT_MANAGEMENT",
    "EC2_AGENT_MANAGEMENT",
]


# --- restJson1 ser/de ---
def serialize_json(value: InvestigationDetectorFeature) -> str:
    return value


def deserialize_json(data: str) -> InvestigationDetectorFeature:
    return cast(InvestigationDetectorFeature, data)
