"""Generated from Smithy shape ``com.amazonaws.bedrockagent#RetrievalInstructionVersionSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent.types.retrieval_instruction_version_summary

RetrievalInstructionVersionSummaries: TypeAlias = list[
    "capo_bedrock_agent.types.retrieval_instruction_version_summary.RetrievalInstructionVersionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: RetrievalInstructionVersionSummaries) -> list:
    import capo_bedrock_agent.types.retrieval_instruction_version_summary

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agent.types.retrieval_instruction_version_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> RetrievalInstructionVersionSummaries:
    import capo_bedrock_agent.types.retrieval_instruction_version_summary

    out: RetrievalInstructionVersionSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agent.types.retrieval_instruction_version_summary.deserialize_json(
                item
            )
        )
    return out
