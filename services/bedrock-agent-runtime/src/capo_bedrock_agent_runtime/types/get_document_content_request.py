"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#GetDocumentContentRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.data_source_id
    import capo_bedrock_agent_runtime.types.document_id
    import capo_bedrock_agent_runtime.types.document_output_format
    import capo_bedrock_agent_runtime.types.knowledge_base_identifier
    import capo_bedrock_agent_runtime.types.user_context


class GetDocumentContentRequest(TypedDict, closed=True):
    knowledge_base_id: "capo_bedrock_agent_runtime.types.knowledge_base_identifier.KnowledgeBaseIdentifier"
    """<p>The unique identifier of the knowledge base that contains the document.</p>"""
    data_source_id: "capo_bedrock_agent_runtime.types.data_source_id.DataSourceId"
    """<p>The unique identifier of the data source that contains the document.</p>"""
    document_id: "capo_bedrock_agent_runtime.types.document_id.DocumentId"
    """<p>The unique identifier of the document to retrieve content for.</p>"""
    output_format: NotRequired[
        "capo_bedrock_agent_runtime.types.document_output_format.DocumentOutputFormat"
    ]
    """<p>The output format for the document content. <code>RAW</code> returns the original file. <code>EXTRACTED</code> returns parsed text as JSON. Defaults to <code>RAW</code>.</p>"""
    user_context: NotRequired[
        "capo_bedrock_agent_runtime.types.user_context.UserContext"
    ]
    """<p>Contains information about the user making the request. This is used for access control filtering to ensure that results only include documents the user is authorized to access.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDocumentContentRequest) -> dict:
    out: dict = {}
    if "output_format" in value:
        import capo_bedrock_agent_runtime.types.document_output_format

        out["outputFormat"] = (
            capo_bedrock_agent_runtime.types.document_output_format.serialize_json(
                value["output_format"]
            )
        )
    if "user_context" in value:
        import capo_bedrock_agent_runtime.types.user_context

        out["userContext"] = (
            capo_bedrock_agent_runtime.types.user_context.serialize_json(
                value["user_context"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetDocumentContentRequest:
    out: GetDocumentContentRequest = {}  # type: ignore[typeddict-item]
    if data.get("outputFormat") is not None:
        import capo_bedrock_agent_runtime.types.document_output_format

        out["output_format"] = (
            capo_bedrock_agent_runtime.types.document_output_format.deserialize_json(
                data["outputFormat"]
            )
        )
    if data.get("userContext") is not None:
        import capo_bedrock_agent_runtime.types.user_context

        out["user_context"] = (
            capo_bedrock_agent_runtime.types.user_context.deserialize_json(
                data["userContext"]
            )
        )
    return out


def redact_sensitive(value: GetDocumentContentRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "user_context" in value:
        out["user_context"] = "*** Sensitive Data Redacted ***"
    return out
