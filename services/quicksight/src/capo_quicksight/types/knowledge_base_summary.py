"""Generated from Smithy shape ``com.amazonaws.quicksight#KnowledgeBaseSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_quicksight.types.data_set_status
    import capo_quicksight.types.data_source_arn
    import capo_quicksight.types.knowledge_base_arn
    import capo_quicksight.types.knowledge_base_id
    import capo_quicksight.types.knowledge_base_name
    import capo_quicksight.types.long
    import capo_quicksight.types.sensitive_string


class KnowledgeBaseSummary(TypedDict, closed=True):
    knowledge_base_arn: "capo_quicksight.types.knowledge_base_arn.KnowledgeBaseArn"
    """<p>The Amazon Resource Name (ARN) of the knowledge base.</p>"""
    knowledge_base_id: "capo_quicksight.types.knowledge_base_id.KnowledgeBaseId"
    """<p>The unique identifier for the knowledge base.</p>"""
    name: "capo_quicksight.types.knowledge_base_name.KnowledgeBaseName"
    """<p>The name of the knowledge base.</p>"""
    status: "capo_quicksight.types.data_set_status.DataSetStatus"
    """<p>The status of the knowledge base.</p>"""
    data_source_arn: "capo_quicksight.types.data_source_arn.DataSourceArn"
    """<p>The ARN of the data source associated with the knowledge base.</p>"""
    type: NotRequired["str"]
    """<p>The type of the knowledge base.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The date and time that the knowledge base was created.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The date and time that the knowledge base was last updated.</p>"""
    knowledge_base_size_bytes: NotRequired["capo_quicksight.types.long.Long"]
    """<p>The size of the knowledge base in bytes.</p>"""
    document_count: NotRequired["capo_quicksight.types.long.Long"]
    """<p>The number of documents in the knowledge base.</p>"""
    primary_owner_arn: NotRequired["str"]
    """<p>The ARN of the primary owner of the knowledge base.</p>"""
    primary_owner_username: NotRequired[
        "capo_quicksight.types.sensitive_string.SensitiveString"
    ]
    """<p>The username of the primary owner of the knowledge base.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KnowledgeBaseSummary) -> dict:
    out: dict = {}
    out["KnowledgeBaseArn"] = value["knowledge_base_arn"]
    out["KnowledgeBaseId"] = value["knowledge_base_id"]
    out["Name"] = value["name"]
    import capo_quicksight.types.data_set_status

    out["Status"] = capo_quicksight.types.data_set_status.serialize_json(
        value["status"]
    )
    out["DataSourceArn"] = value["data_source_arn"]
    if "type" in value:
        out["Type"] = value["type"]
    if "created_at" in value:
        import capo_quicksight.types._prelude.timestamp

        out["CreatedAt"] = capo_quicksight.types._prelude.timestamp.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_quicksight.types._prelude.timestamp

        out["UpdatedAt"] = capo_quicksight.types._prelude.timestamp.serialize_json(
            value["updated_at"]
        )
    if "knowledge_base_size_bytes" in value:
        out["KnowledgeBaseSizeBytes"] = value["knowledge_base_size_bytes"]
    if "document_count" in value:
        out["DocumentCount"] = value["document_count"]
    if "primary_owner_arn" in value:
        out["PrimaryOwnerArn"] = value["primary_owner_arn"]
    if "primary_owner_username" in value:
        out["PrimaryOwnerUsername"] = value["primary_owner_username"]
    return out


def deserialize_json(data: dict) -> KnowledgeBaseSummary:
    out: KnowledgeBaseSummary = {}  # type: ignore[typeddict-item]
    if data.get("KnowledgeBaseArn") is not None:
        out["knowledge_base_arn"] = data["KnowledgeBaseArn"]
    else:
        raise DeserializationError("KnowledgeBaseSummary.knowledge_base_arn required")
    if data.get("KnowledgeBaseId") is not None:
        out["knowledge_base_id"] = data["KnowledgeBaseId"]
    else:
        raise DeserializationError("KnowledgeBaseSummary.knowledge_base_id required")
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("KnowledgeBaseSummary.name required")
    if data.get("Status") is not None:
        import capo_quicksight.types.data_set_status

        out["status"] = capo_quicksight.types.data_set_status.deserialize_json(
            data["Status"]
        )
    else:
        raise DeserializationError("KnowledgeBaseSummary.status required")
    if data.get("DataSourceArn") is not None:
        out["data_source_arn"] = data["DataSourceArn"]
    else:
        raise DeserializationError("KnowledgeBaseSummary.data_source_arn required")
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    if data.get("CreatedAt") is not None:
        import capo_quicksight.types._prelude.timestamp

        out["created_at"] = capo_quicksight.types._prelude.timestamp.deserialize_json(
            data["CreatedAt"]
        )
    if data.get("UpdatedAt") is not None:
        import capo_quicksight.types._prelude.timestamp

        out["updated_at"] = capo_quicksight.types._prelude.timestamp.deserialize_json(
            data["UpdatedAt"]
        )
    if data.get("KnowledgeBaseSizeBytes") is not None:
        out["knowledge_base_size_bytes"] = data["KnowledgeBaseSizeBytes"]
    if data.get("DocumentCount") is not None:
        out["document_count"] = data["DocumentCount"]
    if data.get("PrimaryOwnerArn") is not None:
        out["primary_owner_arn"] = data["PrimaryOwnerArn"]
    if data.get("PrimaryOwnerUsername") is not None:
        out["primary_owner_username"] = data["PrimaryOwnerUsername"]
    return out


def redact_sensitive(value: KnowledgeBaseSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "primary_owner_username" in value:
        out["primary_owner_username"] = "*** Sensitive Data Redacted ***"
    return out
