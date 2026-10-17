"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#DevOpsAgentInvestigationStatus``."""

from typing import Literal, TypeAlias, cast

DevOpsAgentInvestigationStatus: TypeAlias = Literal[
    "PENDING",
    "IN_PROGRESS",
    "COMPLETED",
    "FAILED",
    "TIMED_OUT",
    "CANCELED",
]


# --- restJson1 ser/de ---
def serialize_json(value: DevOpsAgentInvestigationStatus) -> str:
    return value


def deserialize_json(data: str) -> DevOpsAgentInvestigationStatus:
    return cast(DevOpsAgentInvestigationStatus, data)
