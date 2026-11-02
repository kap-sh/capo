"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#AgenticRetrieveCodeExecutionDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.agentic_retrieve_code_execution_document_list


class AgenticRetrieveCodeExecutionDetails(TypedDict, closed=True):
    documents: NotRequired[
        "capo_bedrock_agent_runtime.types.agentic_retrieve_code_execution_document_list.AgenticRetrieveCodeExecutionDocumentList"
    ]
    """<p>The documents that the code reads. This field is present when the code reads documents.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgenticRetrieveCodeExecutionDetails) -> dict:
    out: dict = {}
    if "documents" in value:
        import capo_bedrock_agent_runtime.types.agentic_retrieve_code_execution_document_list

        out["documents"] = (
            capo_bedrock_agent_runtime.types.agentic_retrieve_code_execution_document_list.serialize_json(
                value["documents"]
            )
        )
    return out


def deserialize_json(data: dict) -> AgenticRetrieveCodeExecutionDetails:
    out: AgenticRetrieveCodeExecutionDetails = {}  # type: ignore[typeddict-item]
    if data.get("documents") is not None:
        import capo_bedrock_agent_runtime.types.agentic_retrieve_code_execution_document_list

        out["documents"] = (
            capo_bedrock_agent_runtime.types.agentic_retrieve_code_execution_document_list.deserialize_json(
                data["documents"]
            )
        )
    return out
