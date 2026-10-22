"""Generated from Smithy shape ``com.amazonaws.bedrockagent#RetrievalInstructionLastTransitionStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The outcome or in-progress state of the most recent create or update of a retrieval instruction. Delete is synchronous and has no representation here. Independent of RetrievalInstructionStatus.</p>"""
RetrievalInstructionLastTransitionStatus: TypeAlias = Literal[
    "CREATING",
    "UPDATING",
    "CREATE_SUCCESSFUL",
    "CREATE_FAILED",
    "UPDATE_SUCCESSFUL",
    "UPDATE_FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: RetrievalInstructionLastTransitionStatus) -> str:
    return value


def deserialize_json(data: str) -> RetrievalInstructionLastTransitionStatus:
    return cast(RetrievalInstructionLastTransitionStatus, data)
