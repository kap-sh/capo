"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#AgenticRetrieveStep``."""

from typing import Literal, TypeAlias, cast

"""<p>The step in the agentic retrieval process.</p>"""
AgenticRetrieveStep: TypeAlias = Literal[
    "Planning",
    "Retrieval",
    "SpeculativeRetrieval",
    "FullDocumentExpansion",
    "SessionHistoryLoad",
]


# --- restJson1 ser/de ---
def serialize_json(value: AgenticRetrieveStep) -> str:
    return value


def deserialize_json(data: str) -> AgenticRetrieveStep:
    return cast(AgenticRetrieveStep, data)
