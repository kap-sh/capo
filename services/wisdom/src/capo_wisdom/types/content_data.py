"""Generated from Smithy shape ``com.amazonaws.wisdom#ContentData``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_wisdom.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_wisdom.types.arn
    import capo_wisdom.types.content_metadata
    import capo_wisdom.types.content_status
    import capo_wisdom.types.content_title
    import capo_wisdom.types.content_type
    import capo_wisdom.types.name
    import capo_wisdom.types.non_empty_string
    import capo_wisdom.types.tags
    import capo_wisdom.types.uri
    import capo_wisdom.types.url
    import capo_wisdom.types.uuid


class ContentData(TypedDict, closed=True):
    content_arn: "capo_wisdom.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the content.</p>"""
    content_id: "capo_wisdom.types.uuid.Uuid"
    """<p>The identifier of the content.</p>"""
    knowledge_base_arn: "capo_wisdom.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the knowledge base.</p>"""
    knowledge_base_id: "capo_wisdom.types.uuid.Uuid"
    """<p>The identifier of the knowledge base. This should not be a QUICK_RESPONSES type knowledge base if you're storing Wisdom Content resource to it.</p>"""
    name: "capo_wisdom.types.name.Name"
    """<p>The name of the content.</p>"""
    revision_id: "capo_wisdom.types.non_empty_string.NonEmptyString"
    """<p>The identifier of the content revision.</p>"""
    title: "capo_wisdom.types.content_title.ContentTitle"
    """<p>The title of the content.</p>"""
    content_type: "capo_wisdom.types.content_type.ContentType"
    """<p>The media type of the content.</p>"""
    status: "capo_wisdom.types.content_status.ContentStatus"
    """<p>The status of the content.</p>"""
    metadata: "capo_wisdom.types.content_metadata.ContentMetadata"
    """<p>A key/value map to store attributes without affecting tagging or recommendations. For example, when synchronizing data between an external system and Wisdom, you can store an external version identifier as metadata to utilize for determining drift.</p>"""
    tags: NotRequired["capo_wisdom.types.tags.Tags"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""
    link_out_uri: NotRequired["capo_wisdom.types.uri.Uri"]
    """<p>The URI of the content.</p>"""
    url: "capo_wisdom.types.url.Url"
    """<p>The URL of the content.</p>"""
    url_expiry: "datetime.datetime"
    """<p>The expiration time of the URL as an epoch timestamp.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContentData) -> dict:
    out: dict = {}
    out["contentArn"] = value["content_arn"]
    out["contentId"] = value["content_id"]
    out["knowledgeBaseArn"] = value["knowledge_base_arn"]
    out["knowledgeBaseId"] = value["knowledge_base_id"]
    out["name"] = value["name"]
    out["revisionId"] = value["revision_id"]
    out["title"] = value["title"]
    out["contentType"] = value["content_type"]
    out["status"] = value["status"]
    import capo_wisdom.types.content_metadata

    out["metadata"] = capo_wisdom.types.content_metadata.serialize_json(
        value["metadata"]
    )
    if "tags" in value:
        import capo_wisdom.types.tags

        out["tags"] = capo_wisdom.types.tags.serialize_json(value["tags"])
    if "link_out_uri" in value:
        out["linkOutUri"] = value["link_out_uri"]
    out["url"] = value["url"]
    out["urlExpiry"] = value["url_expiry"].timestamp()
    return out


def deserialize_json(data: dict) -> ContentData:
    out: ContentData = {}  # type: ignore[typeddict-item]
    if data.get("contentArn") is not None:
        out["content_arn"] = data["contentArn"]
    else:
        raise DeserializationError("ContentData.content_arn required")
    if data.get("contentId") is not None:
        out["content_id"] = data["contentId"]
    else:
        raise DeserializationError("ContentData.content_id required")
    if data.get("knowledgeBaseArn") is not None:
        out["knowledge_base_arn"] = data["knowledgeBaseArn"]
    else:
        raise DeserializationError("ContentData.knowledge_base_arn required")
    if data.get("knowledgeBaseId") is not None:
        out["knowledge_base_id"] = data["knowledgeBaseId"]
    else:
        raise DeserializationError("ContentData.knowledge_base_id required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ContentData.name required")
    if data.get("revisionId") is not None:
        out["revision_id"] = data["revisionId"]
    else:
        raise DeserializationError("ContentData.revision_id required")
    if data.get("title") is not None:
        out["title"] = data["title"]
    else:
        raise DeserializationError("ContentData.title required")
    if data.get("contentType") is not None:
        out["content_type"] = data["contentType"]
    else:
        raise DeserializationError("ContentData.content_type required")
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        raise DeserializationError("ContentData.status required")
    if data.get("metadata") is not None:
        import capo_wisdom.types.content_metadata

        out["metadata"] = capo_wisdom.types.content_metadata.deserialize_json(
            data["metadata"]
        )
    else:
        raise DeserializationError("ContentData.metadata required")
    if data.get("tags") is not None:
        import capo_wisdom.types.tags

        out["tags"] = capo_wisdom.types.tags.deserialize_json(data["tags"])
    if data.get("linkOutUri") is not None:
        out["link_out_uri"] = data["linkOutUri"]
    if data.get("url") is not None:
        out["url"] = data["url"]
    else:
        raise DeserializationError("ContentData.url required")
    if data.get("urlExpiry") is not None:
        import datetime

        out["url_expiry"] = datetime.datetime.fromtimestamp(
            float(data["urlExpiry"]), tz=datetime.timezone.utc
        )
    else:
        raise DeserializationError("ContentData.url_expiry required")
    return out


def redact_sensitive(value: ContentData) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "url" in value:
        out["url"] = "*** Sensitive Data Redacted ***"
    return out
