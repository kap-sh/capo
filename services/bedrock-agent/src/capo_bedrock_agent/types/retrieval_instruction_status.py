"""Generated from Smithy shape ``com.amazonaws.bedrockagent#RetrievalInstructionStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>Specifies whether you can use a retrieval instruction. You can resolve only an ACTIVE retrieval instruction at retrieval time. Monotone: INACTIVE to ACTIVE once, never back.</p>"""
RetrievalInstructionStatus: TypeAlias = Literal[
    "ACTIVE",
    "INACTIVE",
]


# --- restJson1 ser/de ---
def serialize_json(value: RetrievalInstructionStatus) -> str:
    return value


def deserialize_json(data: str) -> RetrievalInstructionStatus:
    return cast(RetrievalInstructionStatus, data)
