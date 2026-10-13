"""Generated from Smithy shape ``com.amazonaws.workdocs#DocumentVersionMetadata``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workdocs.types.document_content_type
    import capo_workdocs.types.document_source_url_map
    import capo_workdocs.types.document_status_type
    import capo_workdocs.types.document_thumbnail_url_map
    import capo_workdocs.types.document_version_id_type
    import capo_workdocs.types.hash_type
    import capo_workdocs.types.id_type
    import capo_workdocs.types.resource_name_type
    import capo_workdocs.types.size_type
    import capo_workdocs.types.timestamp_type


class DocumentVersionMetadata(TypedDict, closed=True):
    id: NotRequired[
        "capo_workdocs.types.document_version_id_type.DocumentVersionIdType"
    ]
    """<p>The ID of the version.</p>"""
    name: NotRequired["capo_workdocs.types.resource_name_type.ResourceNameType"]
    """<p>The name of the version.</p>"""
    content_type: NotRequired[
        "capo_workdocs.types.document_content_type.DocumentContentType"
    ]
    """<p>The content type of the document.</p>"""
    size: NotRequired["capo_workdocs.types.size_type.SizeType"]
    """<p>The size of the document, in bytes.</p>"""
    signature: NotRequired["capo_workdocs.types.hash_type.HashType"]
    """<p>The signature of the document.</p>"""
    status: NotRequired["capo_workdocs.types.document_status_type.DocumentStatusType"]
    """<p>The status of the document.</p>"""
    created_timestamp: NotRequired["capo_workdocs.types.timestamp_type.TimestampType"]
    """<p>The timestamp when the document was first uploaded.</p>"""
    modified_timestamp: NotRequired["capo_workdocs.types.timestamp_type.TimestampType"]
    """<p>The timestamp when the document was last uploaded.</p>"""
    content_created_timestamp: NotRequired[
        "capo_workdocs.types.timestamp_type.TimestampType"
    ]
    """<p>The timestamp when the content of the document was originally created.</p>"""
    content_modified_timestamp: NotRequired[
        "capo_workdocs.types.timestamp_type.TimestampType"
    ]
    """<p>The timestamp when the content of the document was modified.</p>"""
    creator_id: NotRequired["capo_workdocs.types.id_type.IdType"]
    """<p>The ID of the creator.</p>"""
    thumbnail: NotRequired[
        "capo_workdocs.types.document_thumbnail_url_map.DocumentThumbnailUrlMap"
    ]
    """<p>The thumbnail of the document.</p>"""
    source: NotRequired[
        "capo_workdocs.types.document_source_url_map.DocumentSourceUrlMap"
    ]
    """<p>The source of the document.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DocumentVersionMetadata) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "content_type" in value:
        out["ContentType"] = value["content_type"]
    if "size" in value:
        out["Size"] = value["size"]
    if "signature" in value:
        out["Signature"] = value["signature"]
    if "status" in value:
        import capo_workdocs.types.document_status_type

        out["Status"] = capo_workdocs.types.document_status_type.serialize_json(
            value["status"]
        )
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
    if "creator_id" in value:
        out["CreatorId"] = value["creator_id"]
    if "thumbnail" in value:
        import capo_workdocs.types.document_thumbnail_url_map

        out["Thumbnail"] = (
            capo_workdocs.types.document_thumbnail_url_map.serialize_json(
                value["thumbnail"]
            )
        )
    if "source" in value:
        import capo_workdocs.types.document_source_url_map

        out["Source"] = capo_workdocs.types.document_source_url_map.serialize_json(
            value["source"]
        )
    return out


def deserialize_json(data: dict) -> DocumentVersionMetadata:
    out: DocumentVersionMetadata = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("ContentType") is not None:
        out["content_type"] = data["ContentType"]
    if data.get("Size") is not None:
        out["size"] = data["Size"]
    if data.get("Signature") is not None:
        out["signature"] = data["Signature"]
    if data.get("Status") is not None:
        import capo_workdocs.types.document_status_type

        out["status"] = capo_workdocs.types.document_status_type.deserialize_json(
            data["Status"]
        )
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
    if data.get("CreatorId") is not None:
        out["creator_id"] = data["CreatorId"]
    if data.get("Thumbnail") is not None:
        import capo_workdocs.types.document_thumbnail_url_map

        out["thumbnail"] = (
            capo_workdocs.types.document_thumbnail_url_map.deserialize_json(
                data["Thumbnail"]
            )
        )
    if data.get("Source") is not None:
        import capo_workdocs.types.document_source_url_map

        out["source"] = capo_workdocs.types.document_source_url_map.deserialize_json(
            data["Source"]
        )
    return out


def redact_sensitive(value: DocumentVersionMetadata) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "thumbnail" in value:
        import capo_workdocs.types.document_thumbnail_url_map

        out["thumbnail"] = (
            capo_workdocs.types.document_thumbnail_url_map.redact_sensitive(
                value["thumbnail"]
            )
        )
    if "source" in value:
        import capo_workdocs.types.document_source_url_map

        out["source"] = capo_workdocs.types.document_source_url_map.redact_sensitive(
            value["source"]
        )
    return out
