"""Generated from Smithy shape ``com.amazonaws.bedrockagent#KnowledgeBaseDocumentDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.date_timestamp
    import capo_bedrock_agent.types.document_identifier
    import capo_bedrock_agent.types.document_status
    import capo_bedrock_agent.types.id


class KnowledgeBaseDocumentDetail(TypedDict, closed=True):
    knowledge_base_id: "capo_bedrock_agent.types.id.Id"
    """<p>The identifier of the knowledge base that the document was ingested into or deleted from.</p>"""
    data_source_id: "capo_bedrock_agent.types.id.Id"
    """<p>The identifier of the data source connected to the knowledge base that the document was ingested into or deleted from.</p>"""
    status: "capo_bedrock_agent.types.document_status.DocumentStatus"
    """<p>The ingestion status of the document. The following statuses are possible:</p> <ul> <li> <p>STARTING – You submitted the ingestion job containing the document.</p> </li> <li> <p>PENDING – The document is waiting to be ingested.</p> </li> <li> <p>IN_PROGRESS – The document is being ingested.</p> </li> <li> <p>INDEXED – The document was successfully indexed.</p> </li> <li> <p>PARTIALLY_INDEXED – The document was partially indexed.</p> </li> <li> <p>METADATA_PARTIALLY_INDEXED – You submitted metadata for an existing document and it was partially indexed.</p> </li> <li> <p>METADATA_UPDATE_FAILED – You submitted a metadata update for an existing document but it failed.</p> </li> <li> <p>FAILED – The document failed to be ingested.</p> </li> <li> <p>NOT_FOUND – The document wasn't found.</p> </li> <li> <p>IGNORED – The document was ignored during ingestion.</p> </li> <li> <p>DELETING – You submitted the delete job containing the document.</p> </li> <li> <p>DELETE_IN_PROGRESS – The document is being deleted.</p> </li> </ul>"""
    identifier: "capo_bedrock_agent.types.document_identifier.DocumentIdentifier"
    """<p>Contains information that identifies the document.</p>"""
    status_reason: NotRequired["str"]
    """<p>The reason for the status. Appears alongside the status <code>IGNORED</code>.</p>"""
    updated_at: NotRequired["capo_bedrock_agent.types.date_timestamp.DateTimestamp"]
    """<p>The date and time at which the document was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KnowledgeBaseDocumentDetail) -> dict:
    out: dict = {}
    out["knowledgeBaseId"] = value["knowledge_base_id"]
    out["dataSourceId"] = value["data_source_id"]
    import capo_bedrock_agent.types.document_status

    out["status"] = capo_bedrock_agent.types.document_status.serialize_json(
        value["status"]
    )
    import capo_bedrock_agent.types.document_identifier

    out["identifier"] = capo_bedrock_agent.types.document_identifier.serialize_json(
        value["identifier"]
    )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    if "updated_at" in value:
        import capo_bedrock_agent.types.date_timestamp

        out["updatedAt"] = capo_bedrock_agent.types.date_timestamp.serialize_json(
            value["updated_at"]
        )
    return out


def deserialize_json(data: dict) -> KnowledgeBaseDocumentDetail:
    out: KnowledgeBaseDocumentDetail = {}  # type: ignore[typeddict-item]
    if data.get("knowledgeBaseId") is not None:
        out["knowledge_base_id"] = data["knowledgeBaseId"]
    else:
        out["knowledge_base_id"] = ""
    if data.get("dataSourceId") is not None:
        out["data_source_id"] = data["dataSourceId"]
    else:
        out["data_source_id"] = ""
    if data.get("status") is not None:
        import capo_bedrock_agent.types.document_status

        out["status"] = capo_bedrock_agent.types.document_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_bedrock_agent.types.document_status.DocumentStatus", ""
        )
    if data.get("identifier") is not None:
        import capo_bedrock_agent.types.document_identifier

        out["identifier"] = (
            capo_bedrock_agent.types.document_identifier.deserialize_json(
                data["identifier"]
            )
        )
    else:
        raise DeserializationError("KnowledgeBaseDocumentDetail.identifier required")
    if data.get("statusReason") is not None:
        out["status_reason"] = data["statusReason"]
    if data.get("updatedAt") is not None:
        import capo_bedrock_agent.types.date_timestamp

        out["updated_at"] = capo_bedrock_agent.types.date_timestamp.deserialize_json(
            data["updatedAt"]
        )
    return out
