"""Generated from Smithy shape ``com.amazonaws.devopsagent#CapabilityType``."""

from typing import Literal, TypeAlias, cast

"""<p>AWS DevOps Agent capability types representing the set of automated capabilities that can be enabled per association.</p>"""
CapabilityType: TypeAlias = Literal[
    "RELEASE_READINESS_REVIEW",
    "RELEASE_READINESS_REVIEW_AUTOMATED_TESTING",
    "CODE_CHANGE_RISK_ANALYSIS",
    "CODE_CHANGE_RISK_ANALYSIS_AUTOMATED_TESTING",
]


# --- restJson1 ser/de ---
def serialize_json(value: CapabilityType) -> str:
    return value


def deserialize_json(data: str) -> CapabilityType:
    return cast(CapabilityType, data)
