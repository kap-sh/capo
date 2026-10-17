"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#DevOpsAgentConfidence``."""

from typing import Literal, TypeAlias, cast

DevOpsAgentConfidence: TypeAlias = Literal[
    "HIGH",
    "MEDIUM",
    "LOW",
]


# --- restJson1 ser/de ---
def serialize_json(value: DevOpsAgentConfidence) -> str:
    return value


def deserialize_json(data: str) -> DevOpsAgentConfidence:
    return cast(DevOpsAgentConfidence, data)
