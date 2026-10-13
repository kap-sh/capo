"""Generated from Smithy shape ``com.amazonaws.quicksight#GetSessionEmbedUrlResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.embedding_url
    import capo_quicksight.types.status_code
    import capo_quicksight.types.string


class GetSessionEmbedUrlResponse(TypedDict, closed=True):
    embed_url: NotRequired["capo_quicksight.types.embedding_url.EmbeddingUrl"]
    """<p>A single-use URL that you can put into your server-side web page to embed your Quick session. This URL is valid for 5 minutes. The API operation provides the URL with an <code>auth_code</code> value that enables one (and only one) sign-on to a user session that is valid for 10 hours. </p>"""
    status: "capo_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""
    request_id: NotRequired["capo_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSessionEmbedUrlResponse) -> dict:
    out: dict = {}
    if "embed_url" in value:
        out["EmbedUrl"] = value["embed_url"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> GetSessionEmbedUrlResponse:
    out: GetSessionEmbedUrlResponse = {}  # type: ignore[typeddict-item]
    if data.get("EmbedUrl") is not None:
        out["embed_url"] = data["EmbedUrl"]
    if data.get("RequestId") is not None:
        out["request_id"] = data["RequestId"]
    return out


def redact_sensitive(value: GetSessionEmbedUrlResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "embed_url" in value:
        out["embed_url"] = "*** Sensitive Data Redacted ***"
    return out
