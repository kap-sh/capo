"""Generated from Smithy shape ``com.amazonaws.guardduty#AnalysisType``."""

from typing import Literal, TypeAlias, cast

AnalysisType: TypeAlias = Literal[
    "REPUTATION",
    "THREAT_ASSESSMENT",
    "RDS_THREAT_ASSESSMENT",
    "KUBERNETES_POLICY_VIOLATION",
    "S3_EXPOSURE",
    "S3_ACTOR_CONTEXT",
    "S3_PEN_TEST",
    "PROCESS_LINEAGE",
    "TREND",
    "BASELINE",
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalysisType) -> str:
    return value


def deserialize_json(data: str) -> AnalysisType:
    return cast(AnalysisType, data)
