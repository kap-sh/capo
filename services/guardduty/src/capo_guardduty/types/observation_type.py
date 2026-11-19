"""Generated from Smithy shape ``com.amazonaws.guardduty#ObservationType``."""

from typing import Literal, TypeAlias, cast

ObservationType: TypeAlias = Literal[
    "FINDING_DETAIL",
    "RESOURCE",
    "NETWORK_ACTIVITY",
    "RDS_LOGIN_ACTIVITY",
    "S3_ACTIVITY",
    "KUBERNETES_ACTIVITY",
    "MALWARE_SCAN",
    "RELATED_FINDINGS",
    "DETECTION_COVERAGE",
    "ACCOUNT_OVERVIEW",
    "RECOMMENDATION",
    "RUNTIME_SIGNALS",
    "DISTRIBUTION",
    "REPRESENTATIVE_RESOURCE",
]


# --- restJson1 ser/de ---
def serialize_json(value: ObservationType) -> str:
    return value


def deserialize_json(data: str) -> ObservationType:
    return cast(ObservationType, data)
