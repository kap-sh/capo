"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateKnowledgeBaseRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.access_control_configuration
    import capo_quicksight.types.boolean
    import capo_quicksight.types.kb_aws_account_id
    import capo_quicksight.types.knowledge_base_configuration
    import capo_quicksight.types.knowledge_base_description
    import capo_quicksight.types.knowledge_base_id
    import capo_quicksight.types.knowledge_base_name
    import capo_quicksight.types.media_extraction_configuration


class UpdateKnowledgeBaseRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.kb_aws_account_id.KbAwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the knowledge base.</p>"""
    knowledge_base_id: "capo_quicksight.types.knowledge_base_id.KnowledgeBaseId"
    """<p>The unique identifier for the knowledge base.</p>"""
    name: NotRequired["capo_quicksight.types.knowledge_base_name.KnowledgeBaseName"]
    """<p>The name of the knowledge base. If you don't specify a name, the existing name is retained.</p>"""
    description: NotRequired[
        "capo_quicksight.types.knowledge_base_description.KnowledgeBaseDescription"
    ]
    """<p>A description for the knowledge base. If you don't specify a description, the existing description is retained.</p>"""
    knowledge_base_configuration: NotRequired[
        "capo_quicksight.types.knowledge_base_configuration.KnowledgeBaseConfiguration"
    ]
    media_extraction_configuration: NotRequired[
        "capo_quicksight.types.media_extraction_configuration.MediaExtractionConfiguration"
    ]
    is_email_notification_opted_for_ingestion_failures: NotRequired[
        "capo_quicksight.types.boolean.Boolean"
    ]
    """<p>Specifies whether email notifications are enabled for ingestion failures.</p>"""
    access_control_configuration: NotRequired[
        "capo_quicksight.types.access_control_configuration.AccessControlConfiguration"
    ]
    """<p>The access control configuration for the knowledge base. If you don't specify this parameter, the existing setting is retained.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateKnowledgeBaseRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "knowledge_base_configuration" in value:
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
    if "is_email_notification_opted_for_ingestion_failures" in value:
        out["IsEmailNotificationOptedForIngestionFailures"] = value[
            "is_email_notification_opted_for_ingestion_failures"
        ]
    if "access_control_configuration" in value:
        import capo_quicksight.types.access_control_configuration

        out["AccessControlConfiguration"] = (
            capo_quicksight.types.access_control_configuration.serialize_json(
                value["access_control_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateKnowledgeBaseRequest:
    out: UpdateKnowledgeBaseRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("KnowledgeBaseConfiguration") is not None:
        import capo_quicksight.types.knowledge_base_configuration

        out["knowledge_base_configuration"] = (
            capo_quicksight.types.knowledge_base_configuration.deserialize_json(
                data["KnowledgeBaseConfiguration"]
            )
        )
    if data.get("MediaExtractionConfiguration") is not None:
        import capo_quicksight.types.media_extraction_configuration

        out["media_extraction_configuration"] = (
            capo_quicksight.types.media_extraction_configuration.deserialize_json(
                data["MediaExtractionConfiguration"]
            )
        )
    if data.get("IsEmailNotificationOptedForIngestionFailures") is not None:
        out["is_email_notification_opted_for_ingestion_failures"] = data[
            "IsEmailNotificationOptedForIngestionFailures"
        ]
    if data.get("AccessControlConfiguration") is not None:
        import capo_quicksight.types.access_control_configuration

        out["access_control_configuration"] = (
            capo_quicksight.types.access_control_configuration.deserialize_json(
                data["AccessControlConfiguration"]
            )
        )
    return out


def redact_sensitive(value: UpdateKnowledgeBaseRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "knowledge_base_configuration" in value:
        out["knowledge_base_configuration"] = "*** Sensitive Data Redacted ***"
    return out
