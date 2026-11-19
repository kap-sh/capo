"""Generated from Smithy shape ``com.amazonaws.guardduty#InvestigationFilterCriterionKey``."""

from typing import Literal, TypeAlias, cast

InvestigationFilterCriterionKey: TypeAlias = Literal[
    "STATUS",
    "RISK_LEVEL",
    "CONFIDENCE",
    "FINDING_ID",
    "INVESTIGATION_TYPE",
]


# --- restJson1 ser/de ---
def serialize_json(value: InvestigationFilterCriterionKey) -> str:
    return value


def deserialize_json(data: str) -> InvestigationFilterCriterionKey:
    return cast(InvestigationFilterCriterionKey, data)
