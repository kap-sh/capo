"""Generated from Smithy shape ``com.amazonaws.wisdom#UpdateContentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wisdom.types.content_metadata
    import capo_wisdom.types.content_title
    import capo_wisdom.types.non_empty_string
    import capo_wisdom.types.upload_id
    import capo_wisdom.types.uri
    import capo_wisdom.types.uuid_or_arn


class UpdateContentRequest(TypedDict, closed=True):
    knowledge_base_id: "capo_wisdom.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the knowledge base. This should not be a QUICK_RESPONSES type knowledge base if you're storing Wisdom Content resource to it. Can be either the ID or the ARN</p>"""
    content_id: "capo_wisdom.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the content. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""
    revision_id: NotRequired["capo_wisdom.types.non_empty_string.NonEmptyString"]
    """<p>The <code>revisionId</code> of the content resource to update, taken from an earlier call to <code>GetContent</code>, <code>GetContentSummary</code>, <code>SearchContent</code>, or <code>ListContents</code>. If included, this argument acts as an optimistic lock to ensure content was not modified since it was last read. If it has been modified, this API throws a <code>PreconditionFailedException</code>.</p>"""
    title: NotRequired["capo_wisdom.types.content_title.ContentTitle"]
    """<p>The title of the content.</p>"""
    override_link_out_uri: NotRequired["capo_wisdom.types.uri.Uri"]
    """<p>The URI for the article. If the knowledge base has a templateUri, setting this argument overrides it for this piece of content. To remove an existing <code>overrideLinkOurUri</code>, exclude this argument and set <code>removeOverrideLinkOutUri</code> to true.</p>"""
    remove_override_link_out_uri: NotRequired["bool"]
    """<p>Unset the existing <code>overrideLinkOutUri</code> if it exists.</p>"""
    metadata: NotRequired["capo_wisdom.types.content_metadata.ContentMetadata"]
    """<p>A key/value map to store attributes without affecting tagging or recommendations. For example, when synchronizing data between an external system and Wisdom, you can store an external version identifier as metadata to utilize for determining drift.</p>"""
    upload_id: NotRequired["capo_wisdom.types.upload_id.UploadId"]
    """<p>A pointer to the uploaded asset. This value is returned by <a href="https://docs.aws.amazon.com/wisdom/latest/APIReference/API_StartContentUpload.html">StartContentUpload</a>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateContentRequest) -> dict:
    out: dict = {}
    if "revision_id" in value:
        out["revisionId"] = value["revision_id"]
    if "title" in value:
        out["title"] = value["title"]
    if "override_link_out_uri" in value:
        out["overrideLinkOutUri"] = value["override_link_out_uri"]
    if "remove_override_link_out_uri" in value:
        out["removeOverrideLinkOutUri"] = value["remove_override_link_out_uri"]
    if "metadata" in value:
        import capo_wisdom.types.content_metadata

        out["metadata"] = capo_wisdom.types.content_metadata.serialize_json(
            value["metadata"]
        )
    if "upload_id" in value:
        out["uploadId"] = value["upload_id"]
    return out


def deserialize_json(data: dict) -> UpdateContentRequest:
    out: UpdateContentRequest = {}  # type: ignore[typeddict-item]
    if data.get("revisionId") is not None:
        out["revision_id"] = data["revisionId"]
    if data.get("title") is not None:
        out["title"] = data["title"]
    if data.get("overrideLinkOutUri") is not None:
        out["override_link_out_uri"] = data["overrideLinkOutUri"]
    if data.get("removeOverrideLinkOutUri") is not None:
        out["remove_override_link_out_uri"] = data["removeOverrideLinkOutUri"]
    if data.get("metadata") is not None:
        import capo_wisdom.types.content_metadata

        out["metadata"] = capo_wisdom.types.content_metadata.deserialize_json(
            data["metadata"]
        )
    if data.get("uploadId") is not None:
        out["upload_id"] = data["uploadId"]
    return out
