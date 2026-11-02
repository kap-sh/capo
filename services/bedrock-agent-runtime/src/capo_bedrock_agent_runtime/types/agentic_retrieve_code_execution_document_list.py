"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#AgenticRetrieveCodeExecutionDocumentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.agentic_retrieve_code_execution_document

AgenticRetrieveCodeExecutionDocumentList: TypeAlias = list[
    "capo_bedrock_agent_runtime.types.agentic_retrieve_code_execution_document.AgenticRetrieveCodeExecutionDocument"
]


# --- restJson1 ser/de ---
def serialize_json(value: AgenticRetrieveCodeExecutionDocumentList) -> list:
    import capo_bedrock_agent_runtime.types.agentic_retrieve_code_execution_document

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agent_runtime.types.agentic_retrieve_code_execution_document.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AgenticRetrieveCodeExecutionDocumentList:
    import capo_bedrock_agent_runtime.types.agentic_retrieve_code_execution_document

    out: AgenticRetrieveCodeExecutionDocumentList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agent_runtime.types.agentic_retrieve_code_execution_document.deserialize_json(
                item
            )
        )
    return out
