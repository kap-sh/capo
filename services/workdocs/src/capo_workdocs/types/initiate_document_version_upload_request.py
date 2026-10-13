"""Generated from Smithy shape ``com.amazonaws.workdocs#InitiateDocumentVersionUploadRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workdocs.types.authentication_header_type
    import capo_workdocs.types.document_content_type
    import capo_workdocs.types.resource_id_type
    import capo_workdocs.types.resource_name_type
    import capo_workdocs.types.size_type
    import capo_workdocs.types.timestamp_type


class InitiateDocumentVersionUploadRequest(TypedDict, closed=True):
    authentication_token: NotRequired[
        "capo_workdocs.types.authentication_header_type.AuthenticationHeaderType"
    ]
    """<p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>"""
    id: NotRequired["capo_workdocs.types.resource_id_type.ResourceIdType"]
    """<p>The ID of the document.</p>"""
    name: NotRequired["capo_workdocs.types.resource_name_type.ResourceNameType"]
    """<p>The name of the document.</p>"""
    content_created_timestamp: NotRequired[
        "capo_workdocs.types.timestamp_type.TimestampType"
    ]
    """<p>The timestamp when the content of the document was originally created.</p>"""
    content_modified_timestamp: NotRequired[
        "capo_workdocs.types.timestamp_type.TimestampType"
    ]
    """<p>The timestamp when the content of the document was modified.</p>"""
    content_type: NotRequired[
        "capo_workdocs.types.document_content_type.DocumentContentType"
    ]
    """<p>The content type of the document.</p>"""
    document_size_in_bytes: NotRequired["capo_workdocs.types.size_type.SizeType"]
    """<p>The size of the document, in bytes.</p>"""
    parent_folder_id: NotRequired["capo_workdocs.types.resource_id_type.ResourceIdType"]
    """<p>The ID of the parent folder.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InitiateDocumentVersionUploadRequest) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "content_created_timestamp" in value:
        import capo_workdocs.types.timestamp_type

        out["ContentCreatedTimestamp"] = (
            capo_workdocs.types.timestamp_type.serialize_json(
                value["content_created_timestamp"]
            )
        )
    if "content_modified_timestamp" in value:
        import capo_workdocs.types.timestamp_type

        out["ContentModifiedTimestamp"] = (
            capo_workdocs.types.timestamp_type.serialize_json(
                value["content_modified_timestamp"]
            )
        )
    if "content_type" in value:
        out["ContentType"] = value["content_type"]
    if "document_size_in_bytes" in value:
        out["DocumentSizeInBytes"] = value["document_size_in_bytes"]
    if "parent_folder_id" in value:
        out["ParentFolderId"] = value["parent_folder_id"]
    return out


def deserialize_json(data: dict) -> InitiateDocumentVersionUploadRequest:
    out: InitiateDocumentVersionUploadRequest = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("ContentCreatedTimestamp") is not None:
        import capo_workdocs.types.timestamp_type

        out["content_created_timestamp"] = (
            capo_workdocs.types.timestamp_type.deserialize_json(
                data["ContentCreatedTimestamp"]
            )
        )
    if data.get("ContentModifiedTimestamp") is not None:
        import capo_workdocs.types.timestamp_type

        out["content_modified_timestamp"] = (
            capo_workdocs.types.timestamp_type.deserialize_json(
                data["ContentModifiedTimestamp"]
            )
        )
    if data.get("ContentType") is not None:
        out["content_type"] = data["ContentType"]
    if data.get("DocumentSizeInBytes") is not None:
        out["document_size_in_bytes"] = data["DocumentSizeInBytes"]
    if data.get("ParentFolderId") is not None:
        out["parent_folder_id"] = data["ParentFolderId"]
    return out


def redact_sensitive(value: InitiateDocumentVersionUploadRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "authentication_token" in value:
        out["authentication_token"] = "*** Sensitive Data Redacted ***"
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    return out
