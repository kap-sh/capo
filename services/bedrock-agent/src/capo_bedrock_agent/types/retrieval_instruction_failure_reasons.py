"""Generated from Smithy shape ``com.amazonaws.bedrockagent#RetrievalInstructionFailureReasons``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent.types.retrieval_instruction_failure_reason

RetrievalInstructionFailureReasons: TypeAlias = list[
    "capo_bedrock_agent.types.retrieval_instruction_failure_reason.RetrievalInstructionFailureReason"
]


# --- restJson1 ser/de ---
def serialize_json(value: RetrievalInstructionFailureReasons) -> list:
    import capo_bedrock_agent.types.retrieval_instruction_failure_reason

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agent.types.retrieval_instruction_failure_reason.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> RetrievalInstructionFailureReasons:
    import capo_bedrock_agent.types.retrieval_instruction_failure_reason

    out: RetrievalInstructionFailureReasons = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agent.types.retrieval_instruction_failure_reason.deserialize_json(
                item
            )
        )
    return out
