"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#AgenticRetrieveActionDetails``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.agentic_retrieve_message_content
    import capo_bedrock_agent_runtime.types.agentic_retrieve_source_retriever_list


class AgenticRetrieveActionDetails(TypedDict, closed=True):
    input_query: "capo_bedrock_agent_runtime.types.agentic_retrieve_message_content.AgenticRetrieveMessageContent"
    """<p>The input query used for retrieval.</p>"""
    source_retrievers: "capo_bedrock_agent_runtime.types.agentic_retrieve_source_retriever_list.AgenticRetrieveSourceRetrieverList"
    """<p>The list of source retrievers targeted by this action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgenticRetrieveActionDetails) -> dict:
    out: dict = {}
    import capo_bedrock_agent_runtime.types.agentic_retrieve_message_content

    out["inputQuery"] = (
        capo_bedrock_agent_runtime.types.agentic_retrieve_message_content.serialize_json(
            value["input_query"]
        )
    )
    import capo_bedrock_agent_runtime.types.agentic_retrieve_source_retriever_list

    out["sourceRetrievers"] = (
        capo_bedrock_agent_runtime.types.agentic_retrieve_source_retriever_list.serialize_json(
            value["source_retrievers"]
        )
    )
    return out


def deserialize_json(data: dict) -> AgenticRetrieveActionDetails:
    out: AgenticRetrieveActionDetails = {}  # type: ignore[typeddict-item]
    if data.get("inputQuery") is not None:
        import capo_bedrock_agent_runtime.types.agentic_retrieve_message_content

        out["input_query"] = (
            capo_bedrock_agent_runtime.types.agentic_retrieve_message_content.deserialize_json(
                data["inputQuery"]
            )
        )
    else:
        raise DeserializationError("AgenticRetrieveActionDetails.input_query required")
    if data.get("sourceRetrievers") is not None:
        import capo_bedrock_agent_runtime.types.agentic_retrieve_source_retriever_list

        out["source_retrievers"] = (
            capo_bedrock_agent_runtime.types.agentic_retrieve_source_retriever_list.deserialize_json(
                data["sourceRetrievers"]
            )
        )
    else:
        out["source_retrievers"] = []
    return out


def redact_sensitive(value: AgenticRetrieveActionDetails) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "input_query" in value:
        out["input_query"] = "*** Sensitive Data Redacted ***"
    return out
