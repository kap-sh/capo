"""Generated from Smithy shape ``com.amazonaws.wisdom#CreateContentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_wisdom.errors import DeserializationError

if TYPE_CHECKING:
    import capo_wisdom.types.content_metadata
    import capo_wisdom.types.content_title
    import capo_wisdom.types.name
    import capo_wisdom.types.non_empty_string
    import capo_wisdom.types.tags
    import capo_wisdom.types.upload_id
    import capo_wisdom.types.uri
    import capo_wisdom.types.uuid_or_arn


class CreateContentRequest(TypedDict, closed=True):
    knowledge_base_id: "capo_wisdom.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the knowledge base. This should not be a QUICK_RESPONSES type knowledge base if you're storing Wisdom Content resource to it. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""
    name: "capo_wisdom.types.name.Name"
    """<p>The name of the content. Each piece of content in a knowledge base must have a unique name. You can retrieve a piece of content using only its knowledge base and its name with the <a href="https://docs.aws.amazon.com/wisdom/latest/APIReference/API_SearchContent.html">SearchContent</a> API.</p>"""
    title: NotRequired["capo_wisdom.types.content_title.ContentTitle"]
    """<p>The title of the content. If not set, the title is equal to the name.</p>"""
    override_link_out_uri: NotRequired["capo_wisdom.types.uri.Uri"]
    """<p>The URI you want to use for the article. If the knowledge base has a templateUri, setting this argument overrides it for this piece of content.</p>"""
    metadata: NotRequired["capo_wisdom.types.content_metadata.ContentMetadata"]
    """<p>A key/value map to store attributes without affecting tagging or recommendations. For example, when synchronizing data between an external system and Wisdom, you can store an external version identifier as metadata to utilize for determining drift.</p>"""
    upload_id: "capo_wisdom.types.upload_id.UploadId"
    """<p>A pointer to the uploaded asset. This value is returned by <a href="https://docs.aws.amazon.com/wisdom/latest/APIReference/API_StartContentUpload.html">StartContentUpload</a>.</p>"""
    client_token: NotRequired["capo_wisdom.types.non_empty_string.NonEmptyString"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>"""
    tags: NotRequired["capo_wisdom.types.tags.Tags"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateContentRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "title" in value:
        out["title"] = value["title"]
    if "override_link_out_uri" in value:
        out["overrideLinkOutUri"] = value["override_link_out_uri"]
    if "metadata" in value:
        import capo_wisdom.types.content_metadata

        out["metadata"] = capo_wisdom.types.content_metadata.serialize_json(
            value["metadata"]
        )
    out["uploadId"] = value["upload_id"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "tags" in value:
        import capo_wisdom.types.tags

        out["tags"] = capo_wisdom.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateContentRequest:
    out: CreateContentRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateContentRequest.name required")
    if data.get("title") is not None:
        out["title"] = data["title"]
    if data.get("overrideLinkOutUri") is not None:
        out["override_link_out_uri"] = data["overrideLinkOutUri"]
    if data.get("metadata") is not None:
        import capo_wisdom.types.content_metadata

        out["metadata"] = capo_wisdom.types.content_metadata.deserialize_json(
            data["metadata"]
        )
    if data.get("uploadId") is not None:
        out["upload_id"] = data["uploadId"]
    else:
        raise DeserializationError("CreateContentRequest.upload_id required")
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("tags") is not None:
        import capo_wisdom.types.tags

        out["tags"] = capo_wisdom.types.tags.deserialize_json(data["tags"])
    return out
