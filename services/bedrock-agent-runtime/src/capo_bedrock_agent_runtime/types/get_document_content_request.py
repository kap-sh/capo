"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#GetDocumentContentRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.data_source_id
    import capo_bedrock_agent_runtime.types.document_id
    import capo_bedrock_agent_runtime.types.document_output_format
    import capo_bedrock_agent_runtime.types.knowledge_base_identifier
    import capo_bedrock_agent_runtime.types.media_id
    import capo_bedrock_agent_runtime.types.user_context


class GetDocumentContentRequest(TypedDict, closed=True):
    knowledge_base_id: "capo_bedrock_agent_runtime.types.knowledge_base_identifier.KnowledgeBaseIdentifier"
    """<p>The unique identifier of the knowledge base that contains the document.</p>"""
    data_source_id: "capo_bedrock_agent_runtime.types.data_source_id.DataSourceId"
    """<p>The unique identifier of the data source that contains the document.</p>"""
    document_id: "capo_bedrock_agent_runtime.types.document_id.DocumentId"
    """<p>The unique identifier of the document to retrieve content for.</p>"""
    media_id: NotRequired["capo_bedrock_agent_runtime.types.media_id.MediaId"]
    """<p>The unique identifier (in UUID format) of an image embedded in the specified document. Set this parameter to the <code>_media_id</code> value in the metadata of the corresponding <code>Retrieve</code> result. If you specify this parameter, the response contains a pre-signed URL for the image instead of the document, and you must omit <code>outputFormat</code> or set it to <code>RAW</code>.</p>"""
    output_format: NotRequired[
        "capo_bedrock_agent_runtime.types.document_output_format.DocumentOutputFormat"
    ]
    """<p>The output format for the content. You can specify one of the following values:</p> <dl> <dt>RAW</dt> <dd> <p>Returns the original document, or the selected image if you specify <code>mediaId</code>.</p> </dd> <dt>EXTRACTED</dt> <dd> <p>Returns parsed document text as JSON.</p> </dd> </dl> <p>If you omit this parameter, the default is <code>RAW</code>. You can't use <code>EXTRACTED</code> with <code>mediaId</code>.</p>"""
    user_context: NotRequired[
        "capo_bedrock_agent_runtime.types.user_context.UserContext"
    ]
    """<p>Contains information about the user making the request. This is used for access control filtering to ensure that results only include documents the user is authorized to access.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDocumentContentRequest) -> dict:
    out: dict = {}
    if "media_id" in value:
        out["mediaId"] = value["media_id"]
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
    if data.get("mediaId") is not None:
        out["media_id"] = data["mediaId"]
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
