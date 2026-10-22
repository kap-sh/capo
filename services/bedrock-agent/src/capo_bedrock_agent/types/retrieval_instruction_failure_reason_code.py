"""Generated from Smithy shape ``com.amazonaws.bedrockagent#RetrievalInstructionFailureReasonCode``."""

from typing import Literal, TypeAlias, cast

"""<p>A machine-readable failure classification. See RetrievalInstructionFailureReason.code for the value semantics.</p>"""
RetrievalInstructionFailureReasonCode: TypeAlias = Literal[
    "CONTENT_REJECTED",
    "CLIENT_ERROR",
    "INTERNAL_ERROR",
]


# --- restJson1 ser/de ---
def serialize_json(value: RetrievalInstructionFailureReasonCode) -> str:
    return value


def deserialize_json(data: str) -> RetrievalInstructionFailureReasonCode:
    return cast(RetrievalInstructionFailureReasonCode, data)
