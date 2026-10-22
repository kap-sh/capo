"""Generated from Smithy shape ``com.amazonaws.bedrockagent#RetrievalInstructionSummaries``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent.types.retrieval_instruction_summary

RetrievalInstructionSummaries: TypeAlias = list[
    "capo_bedrock_agent.types.retrieval_instruction_summary.RetrievalInstructionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: RetrievalInstructionSummaries) -> list:
    import capo_bedrock_agent.types.retrieval_instruction_summary

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agent.types.retrieval_instruction_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RetrievalInstructionSummaries:
    import capo_bedrock_agent.types.retrieval_instruction_summary

    out: RetrievalInstructionSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agent.types.retrieval_instruction_summary.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: RetrievalInstructionSummaries) -> list[Any]:
    import capo_bedrock_agent.types.retrieval_instruction_summary

    return [
        capo_bedrock_agent.types.retrieval_instruction_summary.redact_sensitive(item)
        for item in value
    ]
