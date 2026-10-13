"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#AgenticRetrieveAction``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.agentic_retrieve_action_details
    import capo_bedrock_agent_runtime.types.agentic_retrieve_full_doc_expansion_details
    import capo_bedrock_agent_runtime.types.agentic_retrieve_memory_retrieve_details


class AgenticRetrieveAction(TypedDict, closed=True):
    retrieve: NotRequired[
        "capo_bedrock_agent_runtime.types.agentic_retrieve_action_details.AgenticRetrieveActionDetails"
    ]
    """<p>Details of the retrieve action.</p>"""
    full_document_expansion: NotRequired[
        "capo_bedrock_agent_runtime.types.agentic_retrieve_full_doc_expansion_details.AgenticRetrieveFullDocExpansionDetails"
    ]
    """<p>Details of a full document expansion action.</p>"""
    memory_retrieve: NotRequired[
        "capo_bedrock_agent_runtime.types.agentic_retrieve_memory_retrieve_details.AgenticRetrieveMemoryRetrieveDetails"
    ]
    """<p>The details of a long-term memory retrieval that the agent chose to perform.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgenticRetrieveAction) -> dict:
    out: dict = {}
    if "retrieve" in value:
        import capo_bedrock_agent_runtime.types.agentic_retrieve_action_details

        out["retrieve"] = (
            capo_bedrock_agent_runtime.types.agentic_retrieve_action_details.serialize_json(
                value["retrieve"]
            )
        )
    if "full_document_expansion" in value:
        import capo_bedrock_agent_runtime.types.agentic_retrieve_full_doc_expansion_details

        out["fullDocumentExpansion"] = (
            capo_bedrock_agent_runtime.types.agentic_retrieve_full_doc_expansion_details.serialize_json(
                value["full_document_expansion"]
            )
        )
    if "memory_retrieve" in value:
        import capo_bedrock_agent_runtime.types.agentic_retrieve_memory_retrieve_details

        out["memoryRetrieve"] = (
            capo_bedrock_agent_runtime.types.agentic_retrieve_memory_retrieve_details.serialize_json(
                value["memory_retrieve"]
            )
        )
    return out


def deserialize_json(data: dict) -> AgenticRetrieveAction:
    out: AgenticRetrieveAction = {}  # type: ignore[typeddict-item]
    if data.get("retrieve") is not None:
        import capo_bedrock_agent_runtime.types.agentic_retrieve_action_details

        out["retrieve"] = (
            capo_bedrock_agent_runtime.types.agentic_retrieve_action_details.deserialize_json(
                data["retrieve"]
            )
        )
    if data.get("fullDocumentExpansion") is not None:
        import capo_bedrock_agent_runtime.types.agentic_retrieve_full_doc_expansion_details

        out["full_document_expansion"] = (
            capo_bedrock_agent_runtime.types.agentic_retrieve_full_doc_expansion_details.deserialize_json(
                data["fullDocumentExpansion"]
            )
        )
    if data.get("memoryRetrieve") is not None:
        import capo_bedrock_agent_runtime.types.agentic_retrieve_memory_retrieve_details

        out["memory_retrieve"] = (
            capo_bedrock_agent_runtime.types.agentic_retrieve_memory_retrieve_details.deserialize_json(
                data["memoryRetrieve"]
            )
        )
    return out


def redact_sensitive(value: AgenticRetrieveAction) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "retrieve" in value:
        import capo_bedrock_agent_runtime.types.agentic_retrieve_action_details

        out["retrieve"] = (
            capo_bedrock_agent_runtime.types.agentic_retrieve_action_details.redact_sensitive(
                value["retrieve"]
            )
        )
    if "memory_retrieve" in value:
        import capo_bedrock_agent_runtime.types.agentic_retrieve_memory_retrieve_details

        out["memory_retrieve"] = (
            capo_bedrock_agent_runtime.types.agentic_retrieve_memory_retrieve_details.redact_sensitive(
                value["memory_retrieve"]
            )
        )
    return out
