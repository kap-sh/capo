"""Generated from Smithy shape ``com.amazonaws.workdocs#DocumentMetadata``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workdocs.types.document_version_metadata
    import capo_workdocs.types.id_type
    import capo_workdocs.types.resource_id_type
    import capo_workdocs.types.resource_state_type
    import capo_workdocs.types.shared_labels
    import capo_workdocs.types.timestamp_type


class DocumentMetadata(TypedDict, closed=True):
    id: NotRequired["capo_workdocs.types.resource_id_type.ResourceIdType"]
    """<p>The ID of the document.</p>"""
    creator_id: NotRequired["capo_workdocs.types.id_type.IdType"]
    """<p>The ID of the creator.</p>"""
    parent_folder_id: NotRequired["capo_workdocs.types.resource_id_type.ResourceIdType"]
    """<p>The ID of the parent folder.</p>"""
    created_timestamp: NotRequired["capo_workdocs.types.timestamp_type.TimestampType"]
    """<p>The time when the document was created.</p>"""
    modified_timestamp: NotRequired["capo_workdocs.types.timestamp_type.TimestampType"]
    """<p>The time when the document was updated.</p>"""
    latest_version_metadata: NotRequired[
        "capo_workdocs.types.document_version_metadata.DocumentVersionMetadata"
    ]
    """<p>The latest version of the document.</p>"""
    resource_state: NotRequired[
        "capo_workdocs.types.resource_state_type.ResourceStateType"
    ]
    """<p>The resource state.</p>"""
    labels: NotRequired["capo_workdocs.types.shared_labels.SharedLabels"]
    """<p>List of labels on the document.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DocumentMetadata) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "creator_id" in value:
        out["CreatorId"] = value["creator_id"]
    if "parent_folder_id" in value:
        out["ParentFolderId"] = value["parent_folder_id"]
    if "created_timestamp" in value:
        import capo_workdocs.types.timestamp_type

        out["CreatedTimestamp"] = capo_workdocs.types.timestamp_type.serialize_json(
            value["created_timestamp"]
        )
    if "modified_timestamp" in value:
        import capo_workdocs.types.timestamp_type

        out["ModifiedTimestamp"] = capo_workdocs.types.timestamp_type.serialize_json(
            value["modified_timestamp"]
        )
    if "latest_version_metadata" in value:
        import capo_workdocs.types.document_version_metadata

        out["LatestVersionMetadata"] = (
            capo_workdocs.types.document_version_metadata.serialize_json(
                value["latest_version_metadata"]
            )
        )
    if "resource_state" in value:
        import capo_workdocs.types.resource_state_type

        out["ResourceState"] = capo_workdocs.types.resource_state_type.serialize_json(
            value["resource_state"]
        )
    if "labels" in value:
        import capo_workdocs.types.shared_labels

        out["Labels"] = capo_workdocs.types.shared_labels.serialize_json(
            value["labels"]
        )
    return out


def deserialize_json(data: dict) -> DocumentMetadata:
    out: DocumentMetadata = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("CreatorId") is not None:
        out["creator_id"] = data["CreatorId"]
    if data.get("ParentFolderId") is not None:
        out["parent_folder_id"] = data["ParentFolderId"]
    if data.get("CreatedTimestamp") is not None:
        import capo_workdocs.types.timestamp_type

        out["created_timestamp"] = capo_workdocs.types.timestamp_type.deserialize_json(
            data["CreatedTimestamp"]
        )
    if data.get("ModifiedTimestamp") is not None:
        import capo_workdocs.types.timestamp_type

        out["modified_timestamp"] = capo_workdocs.types.timestamp_type.deserialize_json(
            data["ModifiedTimestamp"]
        )
    if data.get("LatestVersionMetadata") is not None:
        import capo_workdocs.types.document_version_metadata

        out["latest_version_metadata"] = (
            capo_workdocs.types.document_version_metadata.deserialize_json(
                data["LatestVersionMetadata"]
            )
        )
    if data.get("ResourceState") is not None:
        import capo_workdocs.types.resource_state_type

        out["resource_state"] = (
            capo_workdocs.types.resource_state_type.deserialize_json(
                data["ResourceState"]
            )
        )
    if data.get("Labels") is not None:
        import capo_workdocs.types.shared_labels

        out["labels"] = capo_workdocs.types.shared_labels.deserialize_json(
            data["Labels"]
        )
    return out


def redact_sensitive(value: DocumentMetadata) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "latest_version_metadata" in value:
        import capo_workdocs.types.document_version_metadata

        out["latest_version_metadata"] = (
            capo_workdocs.types.document_version_metadata.redact_sensitive(
                value["latest_version_metadata"]
            )
        )
    return out
