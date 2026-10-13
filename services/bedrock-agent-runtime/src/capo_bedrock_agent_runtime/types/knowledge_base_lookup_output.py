"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#KnowledgeBaseLookupOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.metadata
    import capo_bedrock_agent_runtime.types.retrieved_references


class KnowledgeBaseLookupOutput(TypedDict, closed=True):
    retrieved_references: NotRequired[
        "capo_bedrock_agent_runtime.types.retrieved_references.RetrievedReferences"
    ]
    """<p>Contains metadata about the sources cited for the generated response.</p>"""
    metadata: NotRequired["capo_bedrock_agent_runtime.types.metadata.Metadata"]
    """<p>Contains information about the knowledge base output.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KnowledgeBaseLookupOutput) -> dict:
    out: dict = {}
    if "retrieved_references" in value:
        import capo_bedrock_agent_runtime.types.retrieved_references

        out["retrievedReferences"] = (
            capo_bedrock_agent_runtime.types.retrieved_references.serialize_json(
                value["retrieved_references"]
            )
        )
    if "metadata" in value:
        import capo_bedrock_agent_runtime.types.metadata

        out["metadata"] = capo_bedrock_agent_runtime.types.metadata.serialize_json(
            value["metadata"]
        )
    return out


def deserialize_json(data: dict) -> KnowledgeBaseLookupOutput:
    out: KnowledgeBaseLookupOutput = {}  # type: ignore[typeddict-item]
    if data.get("retrievedReferences") is not None:
        import capo_bedrock_agent_runtime.types.retrieved_references

        out["retrieved_references"] = (
            capo_bedrock_agent_runtime.types.retrieved_references.deserialize_json(
                data["retrievedReferences"]
            )
        )
    if data.get("metadata") is not None:
        import capo_bedrock_agent_runtime.types.metadata

        out["metadata"] = capo_bedrock_agent_runtime.types.metadata.deserialize_json(
            data["metadata"]
        )
    return out


def redact_sensitive(value: KnowledgeBaseLookupOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "retrieved_references" in value:
        import capo_bedrock_agent_runtime.types.retrieved_references

        out["retrieved_references"] = (
            capo_bedrock_agent_runtime.types.retrieved_references.redact_sensitive(
                value["retrieved_references"]
            )
        )
    if "metadata" in value:
        out["metadata"] = "*** Sensitive Data Redacted ***"
    return out
