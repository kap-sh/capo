"""Generated from Smithy shape ``com.amazonaws.healthlake#AgentErrorType``."""

from typing import Literal, TypeAlias, cast

AgentErrorType: TypeAlias = Literal[
    "InternalServerException",
    "ResourceNotFoundException",
    "ValidationException",
    "AccessDeniedException",
    "ThrottlingException",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AgentErrorType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AgentErrorType:
    return cast(AgentErrorType, data)
