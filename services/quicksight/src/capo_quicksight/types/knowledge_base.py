"""Generated from Smithy shape ``com.amazonaws.quicksight#KnowledgeBase``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_quicksight.types.access_control_configuration
    import capo_quicksight.types.boolean
    import capo_quicksight.types.data_set_status
    import capo_quicksight.types.data_source_arn
    import capo_quicksight.types.knowledge_base_arn
    import capo_quicksight.types.knowledge_base_configuration
    import capo_quicksight.types.knowledge_base_description
    import capo_quicksight.types.knowledge_base_id
    import capo_quicksight.types.knowledge_base_ingestion_summary
    import capo_quicksight.types.knowledge_base_name
    import capo_quicksight.types.long
    import capo_quicksight.types.media_extraction_configuration
    import capo_quicksight.types.sensitive_string
    import capo_quicksight.types.string


class KnowledgeBase(TypedDict, closed=True):
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
    knowledge_base_configuration: (
        "capo_quicksight.types.knowledge_base_configuration.KnowledgeBaseConfiguration"
    )
    """<p>The configuration settings for the knowledge base.</p>"""
    media_extraction_configuration: NotRequired[
        "capo_quicksight.types.media_extraction_configuration.MediaExtractionConfiguration"
    ]
    """<p>The media extraction configuration for the knowledge base.</p>"""
    access_control_configuration: NotRequired[
        "capo_quicksight.types.access_control_configuration.AccessControlConfiguration"
    ]
    """<p>The access control configuration for the knowledge base.</p>"""
    type: NotRequired["str"]
    """<p>The type of the knowledge base.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The date and time that the knowledge base was created.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The date and time that the knowledge base was last updated.</p>"""
    description: NotRequired[
        "capo_quicksight.types.knowledge_base_description.KnowledgeBaseDescription"
    ]
    """<p>The description of the knowledge base.</p>"""
    is_email_notification_opted_for_ingestion_failures: NotRequired[
        "capo_quicksight.types.boolean.Boolean"
    ]
    """<p>Specifies whether email notifications are enabled for ingestion failures.</p>"""
    first_completed_ingestion_summary: NotRequired[
        "capo_quicksight.types.knowledge_base_ingestion_summary.KnowledgeBaseIngestionSummary"
    ]
    """<p>A summary of the first completed ingestion for the knowledge base.</p>"""
    first_incomplete_ingestion_summary: NotRequired[
        "capo_quicksight.types.knowledge_base_ingestion_summary.KnowledgeBaseIngestionSummary"
    ]
    """<p>A summary of the first incomplete ingestion for the knowledge base.</p>"""
    latest_ingestion_summary: NotRequired[
        "capo_quicksight.types.knowledge_base_ingestion_summary.KnowledgeBaseIngestionSummary"
    ]
    """<p>A summary of the most recent ingestion for the knowledge base.</p>"""
    knowledge_base_size_bytes: NotRequired["capo_quicksight.types.long.Long"]
    """<p>The size of the knowledge base in bytes.</p>"""
    document_count: NotRequired["capo_quicksight.types.long.Long"]
    """<p>The number of documents in the knowledge base.</p>"""
    primary_owner_arn: NotRequired["capo_quicksight.types.string.String"]
    """<p>The ARN of the primary owner of the knowledge base.</p>"""
    primary_owner_username: NotRequired[
        "capo_quicksight.types.sensitive_string.SensitiveString"
    ]
    """<p>The username of the primary owner of the knowledge base.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KnowledgeBase) -> dict:
    out: dict = {}
    out["KnowledgeBaseArn"] = value["knowledge_base_arn"]
    out["KnowledgeBaseId"] = value["knowledge_base_id"]
    out["Name"] = value["name"]
    import capo_quicksight.types.data_set_status

    out["Status"] = capo_quicksight.types.data_set_status.serialize_json(
        value["status"]
    )
    out["DataSourceArn"] = value["data_source_arn"]
    import capo_quicksight.types.knowledge_base_configuration

    out["KnowledgeBaseConfiguration"] = (
        capo_quicksight.types.knowledge_base_configuration.serialize_json(
            value["knowledge_base_configuration"]
        )
    )
    if "media_extraction_configuration" in value:
        import capo_quicksight.types.media_extraction_configuration

        out["MediaExtractionConfiguration"] = (
            capo_quicksight.types.media_extraction_configuration.serialize_json(
                value["media_extraction_configuration"]
            )
        )
    if "access_control_configuration" in value:
        import capo_quicksight.types.access_control_configuration

        out["AccessControlConfiguration"] = (
            capo_quicksight.types.access_control_configuration.serialize_json(
                value["access_control_configuration"]
            )
        )
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
    if "description" in value:
        out["Description"] = value["description"]
    if "is_email_notification_opted_for_ingestion_failures" in value:
        out["IsEmailNotificationOptedForIngestionFailures"] = value[
            "is_email_notification_opted_for_ingestion_failures"
        ]
    if "first_completed_ingestion_summary" in value:
        import capo_quicksight.types.knowledge_base_ingestion_summary

        out["FirstCompletedIngestionSummary"] = (
            capo_quicksight.types.knowledge_base_ingestion_summary.serialize_json(
                value["first_completed_ingestion_summary"]
            )
        )
    if "first_incomplete_ingestion_summary" in value:
        import capo_quicksight.types.knowledge_base_ingestion_summary

        out["FirstIncompleteIngestionSummary"] = (
            capo_quicksight.types.knowledge_base_ingestion_summary.serialize_json(
                value["first_incomplete_ingestion_summary"]
            )
        )
    if "latest_ingestion_summary" in value:
        import capo_quicksight.types.knowledge_base_ingestion_summary

        out["LatestIngestionSummary"] = (
            capo_quicksight.types.knowledge_base_ingestion_summary.serialize_json(
                value["latest_ingestion_summary"]
            )
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


def deserialize_json(data: dict) -> KnowledgeBase:
    out: KnowledgeBase = {}  # type: ignore[typeddict-item]
    if data.get("KnowledgeBaseArn") is not None:
        out["knowledge_base_arn"] = data["KnowledgeBaseArn"]
    else:
        raise DeserializationError("KnowledgeBase.knowledge_base_arn required")
    if data.get("KnowledgeBaseId") is not None:
        out["knowledge_base_id"] = data["KnowledgeBaseId"]
    else:
        raise DeserializationError("KnowledgeBase.knowledge_base_id required")
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("KnowledgeBase.name required")
    if data.get("Status") is not None:
        import capo_quicksight.types.data_set_status

        out["status"] = capo_quicksight.types.data_set_status.deserialize_json(
            data["Status"]
        )
    else:
        raise DeserializationError("KnowledgeBase.status required")
    if data.get("DataSourceArn") is not None:
        out["data_source_arn"] = data["DataSourceArn"]
    else:
        raise DeserializationError("KnowledgeBase.data_source_arn required")
    if data.get("KnowledgeBaseConfiguration") is not None:
        import capo_quicksight.types.knowledge_base_configuration

        out["knowledge_base_configuration"] = (
            capo_quicksight.types.knowledge_base_configuration.deserialize_json(
                data["KnowledgeBaseConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "KnowledgeBase.knowledge_base_configuration required"
        )
    if data.get("MediaExtractionConfiguration") is not None:
        import capo_quicksight.types.media_extraction_configuration

        out["media_extraction_configuration"] = (
            capo_quicksight.types.media_extraction_configuration.deserialize_json(
                data["MediaExtractionConfiguration"]
            )
        )
    if data.get("AccessControlConfiguration") is not None:
        import capo_quicksight.types.access_control_configuration

        out["access_control_configuration"] = (
            capo_quicksight.types.access_control_configuration.deserialize_json(
                data["AccessControlConfiguration"]
            )
        )
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
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("IsEmailNotificationOptedForIngestionFailures") is not None:
        out["is_email_notification_opted_for_ingestion_failures"] = data[
            "IsEmailNotificationOptedForIngestionFailures"
        ]
    if data.get("FirstCompletedIngestionSummary") is not None:
        import capo_quicksight.types.knowledge_base_ingestion_summary

        out["first_completed_ingestion_summary"] = (
            capo_quicksight.types.knowledge_base_ingestion_summary.deserialize_json(
                data["FirstCompletedIngestionSummary"]
            )
        )
    if data.get("FirstIncompleteIngestionSummary") is not None:
        import capo_quicksight.types.knowledge_base_ingestion_summary

        out["first_incomplete_ingestion_summary"] = (
            capo_quicksight.types.knowledge_base_ingestion_summary.deserialize_json(
                data["FirstIncompleteIngestionSummary"]
            )
        )
    if data.get("LatestIngestionSummary") is not None:
        import capo_quicksight.types.knowledge_base_ingestion_summary

        out["latest_ingestion_summary"] = (
            capo_quicksight.types.knowledge_base_ingestion_summary.deserialize_json(
                data["LatestIngestionSummary"]
            )
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


def redact_sensitive(value: KnowledgeBase) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "knowledge_base_configuration" in value:
        out["knowledge_base_configuration"] = "*** Sensitive Data Redacted ***"
    if "primary_owner_username" in value:
        out["primary_owner_username"] = "*** Sensitive Data Redacted ***"
    return out
