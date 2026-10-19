"""Generated from Smithy shape ``com.amazonaws.qconnect#ContentData``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_qconnect.types.arn
    import capo_qconnect.types.content_metadata
    import capo_qconnect.types.content_status
    import capo_qconnect.types.content_title
    import capo_qconnect.types.content_type
    import capo_qconnect.types.name
    import capo_qconnect.types.non_empty_string
    import capo_qconnect.types.tags
    import capo_qconnect.types.uri
    import capo_qconnect.types.url
    import capo_qconnect.types.uuid


class ContentData(TypedDict, closed=True):
    content_arn: "capo_qconnect.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the content.</p>"""
    content_id: "capo_qconnect.types.uuid.Uuid"
    """<p>The identifier of the content.</p>"""
    knowledge_base_arn: "capo_qconnect.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the knowledge base.</p>"""
    knowledge_base_id: "capo_qconnect.types.uuid.Uuid"
    """<p>The identifier of the knowledge base.</p>"""
    name: "capo_qconnect.types.name.Name"
    """<p>The name of the content.</p>"""
    revision_id: "capo_qconnect.types.non_empty_string.NonEmptyString"
    """<p>The identifier of the content revision.</p>"""
    title: "capo_qconnect.types.content_title.ContentTitle"
    """<p>The title of the content.</p>"""
    content_type: "capo_qconnect.types.content_type.ContentType"
    """<p>The media type of the content.</p>"""
    status: "capo_qconnect.types.content_status.ContentStatus"
    """<p>The status of the content.</p>"""
    metadata: "capo_qconnect.types.content_metadata.ContentMetadata"
    """<p>A key/value map to store attributes without affecting tagging or recommendations. For example, when synchronizing data between an external system and Amazon Q in Connect, you can store an external version identifier as metadata to utilize for determining drift.</p>"""
    tags: NotRequired["capo_qconnect.types.tags.Tags"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""
    link_out_uri: NotRequired["capo_qconnect.types.uri.Uri"]
    """<p>The URI of the content.</p>"""
    url: "capo_qconnect.types.url.Url"
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
    import capo_qconnect.types.content_metadata

    out["metadata"] = capo_qconnect.types.content_metadata.serialize_json(
        value["metadata"]
    )
    if "tags" in value:
        import capo_qconnect.types.tags

        out["tags"] = capo_qconnect.types.tags.serialize_json(value["tags"])
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
        out["content_arn"] = ""
    if data.get("contentId") is not None:
        out["content_id"] = data["contentId"]
    else:
        out["content_id"] = ""
    if data.get("knowledgeBaseArn") is not None:
        out["knowledge_base_arn"] = data["knowledgeBaseArn"]
    else:
        out["knowledge_base_arn"] = ""
    if data.get("knowledgeBaseId") is not None:
        out["knowledge_base_id"] = data["knowledgeBaseId"]
    else:
        out["knowledge_base_id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("revisionId") is not None:
        out["revision_id"] = data["revisionId"]
    else:
        out["revision_id"] = ""
    if data.get("title") is not None:
        out["title"] = data["title"]
    else:
        out["title"] = ""
    if data.get("contentType") is not None:
        out["content_type"] = data["contentType"]
    else:
        out["content_type"] = ""
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        out["status"] = ""
    if data.get("metadata") is not None:
        import capo_qconnect.types.content_metadata

        out["metadata"] = capo_qconnect.types.content_metadata.deserialize_json(
            data["metadata"]
        )
    else:
        out["metadata"] = {}
    if data.get("tags") is not None:
        import capo_qconnect.types.tags

        out["tags"] = capo_qconnect.types.tags.deserialize_json(data["tags"])
    if data.get("linkOutUri") is not None:
        out["link_out_uri"] = data["linkOutUri"]
    if data.get("url") is not None:
        out["url"] = data["url"]
    else:
        out["url"] = ""
    if data.get("urlExpiry") is not None:
        import datetime

        out["url_expiry"] = datetime.datetime.fromtimestamp(
            float(data["urlExpiry"]), tz=datetime.timezone.utc
        )
    else:
        import datetime

        out["url_expiry"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out


def redact_sensitive(value: ContentData) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "url" in value:
        out["url"] = "*** Sensitive Data Redacted ***"
    return out
