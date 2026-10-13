"""Generated from Smithy shape ``com.amazonaws.quicksight#CreateKnowledgeBaseRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.access_control_configuration
    import capo_quicksight.types.data_source_arn
    import capo_quicksight.types.kb_aws_account_id
    import capo_quicksight.types.knowledge_base_configuration
    import capo_quicksight.types.knowledge_base_description
    import capo_quicksight.types.knowledge_base_id
    import capo_quicksight.types.knowledge_base_name
    import capo_quicksight.types.media_extraction_configuration
    import capo_quicksight.types.resource_permission_list
    import capo_quicksight.types.string
    import capo_quicksight.types.tag_list


class CreateKnowledgeBaseRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.kb_aws_account_id.KbAwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the knowledge base.</p>"""
    knowledge_base_id: "capo_quicksight.types.knowledge_base_id.KnowledgeBaseId"
    """<p>The unique identifier for the knowledge base.</p>"""
    name: "capo_quicksight.types.knowledge_base_name.KnowledgeBaseName"
    """<p>The name of the knowledge base.</p>"""
    data_source_arn: "capo_quicksight.types.data_source_arn.DataSourceArn"
    """<p>The Amazon Resource Name (ARN) of the data source for the knowledge base.</p>"""
    knowledge_base_configuration: (
        "capo_quicksight.types.knowledge_base_configuration.KnowledgeBaseConfiguration"
    )
    description: NotRequired[
        "capo_quicksight.types.knowledge_base_description.KnowledgeBaseDescription"
    ]
    """<p>A description for the knowledge base. If you don't specify a description, the knowledge base is created without one.</p>"""
    permissions: NotRequired[
        "capo_quicksight.types.resource_permission_list.ResourcePermissionList"
    ]
    """<p>A list of resource permissions on the knowledge base. Each entry grants a specified Amazon QuickSight principal either owner or viewer access. If you don't specify permissions, only the primary owner (if provided) receives owner access.</p>"""
    media_extraction_configuration: NotRequired[
        "capo_quicksight.types.media_extraction_configuration.MediaExtractionConfiguration"
    ]
    access_control_configuration: NotRequired[
        "capo_quicksight.types.access_control_configuration.AccessControlConfiguration"
    ]
    """<p>The access control configuration for the knowledge base. If you don't specify this parameter, document-level ACLs are disabled.</p>"""
    primary_owner_arn: NotRequired["capo_quicksight.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the Amazon QuickSight user or group to set as the primary owner of the knowledge base. The specified principal is always granted owner access, regardless of what is specified in the <code>Permissions</code> field.</p> <p>This must be an Amazon QuickSight principal ARN, not an IAM user or role ARN. The API caller is never assigned as the owner automatically. If you don't specify a primary owner and don't grant owner access in <code>Permissions</code>, the knowledge base is created without an owner, even when you call the operation as an Amazon QuickSight user.</p> <p>When you call <code>CreateKnowledgeBase</code> as an IAM user or an assumed IAM role, specify <code>PrimaryOwnerArn</code> (as an Amazon QuickSight principal ARN) or an owner entry in <code>Permissions</code> so that the knowledge base has an owner. Although optional, specifying a primary owner is recommended.</p>"""
    tags: NotRequired["capo_quicksight.types.tag_list.TagList"]
    """<p>The tags to assign to the knowledge base. If you don't specify tags, the knowledge base is created without tags.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateKnowledgeBaseRequest) -> dict:
    out: dict = {}
    out["KnowledgeBaseId"] = value["knowledge_base_id"]
    out["Name"] = value["name"]
    out["DataSourceArn"] = value["data_source_arn"]
    import capo_quicksight.types.knowledge_base_configuration

    out["KnowledgeBaseConfiguration"] = (
        capo_quicksight.types.knowledge_base_configuration.serialize_json(
            value["knowledge_base_configuration"]
        )
    )
    if "description" in value:
        out["Description"] = value["description"]
    if "permissions" in value:
        import capo_quicksight.types.resource_permission_list

        out["Permissions"] = (
            capo_quicksight.types.resource_permission_list.serialize_json(
                value["permissions"]
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
    if "primary_owner_arn" in value:
        out["PrimaryOwnerArn"] = value["primary_owner_arn"]
    if "tags" in value:
        import capo_quicksight.types.tag_list

        out["Tags"] = capo_quicksight.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateKnowledgeBaseRequest:
    out: CreateKnowledgeBaseRequest = {}  # type: ignore[typeddict-item]
    if data.get("KnowledgeBaseId") is not None:
        out["knowledge_base_id"] = data["KnowledgeBaseId"]
    else:
        raise DeserializationError(
            "CreateKnowledgeBaseRequest.knowledge_base_id required"
        )
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateKnowledgeBaseRequest.name required")
    if data.get("DataSourceArn") is not None:
        out["data_source_arn"] = data["DataSourceArn"]
    else:
        raise DeserializationError(
            "CreateKnowledgeBaseRequest.data_source_arn required"
        )
    if data.get("KnowledgeBaseConfiguration") is not None:
        import capo_quicksight.types.knowledge_base_configuration

        out["knowledge_base_configuration"] = (
            capo_quicksight.types.knowledge_base_configuration.deserialize_json(
                data["KnowledgeBaseConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "CreateKnowledgeBaseRequest.knowledge_base_configuration required"
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Permissions") is not None:
        import capo_quicksight.types.resource_permission_list

        out["permissions"] = (
            capo_quicksight.types.resource_permission_list.deserialize_json(
                data["Permissions"]
            )
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
    if data.get("PrimaryOwnerArn") is not None:
        out["primary_owner_arn"] = data["PrimaryOwnerArn"]
    if data.get("Tags") is not None:
        import capo_quicksight.types.tag_list

        out["tags"] = capo_quicksight.types.tag_list.deserialize_json(data["Tags"])
    return out


def redact_sensitive(value: CreateKnowledgeBaseRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "knowledge_base_configuration" in value:
        out["knowledge_base_configuration"] = "*** Sensitive Data Redacted ***"
    return out
