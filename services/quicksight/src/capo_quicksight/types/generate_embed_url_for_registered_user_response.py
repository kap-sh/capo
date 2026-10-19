"""Generated from Smithy shape ``com.amazonaws.quicksight#GenerateEmbedUrlForRegisteredUserResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.embedding_url
    import capo_quicksight.types.status_code
    import capo_quicksight.types.string


class GenerateEmbedUrlForRegisteredUserResponse(TypedDict, closed=True):
    embed_url: "capo_quicksight.types.embedding_url.EmbeddingUrl"
    """<p>The embed URL for the Amazon Quick Sight dashboard, visual, Q search bar, Generative Q&A experience, or console.</p>"""
    status: "capo_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""
    request_id: "capo_quicksight.types.string.String"
    """<p>The Amazon Web Services request ID for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GenerateEmbedUrlForRegisteredUserResponse) -> dict:
    out: dict = {}
    out["EmbedUrl"] = value["embed_url"]
    out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> GenerateEmbedUrlForRegisteredUserResponse:
    out: GenerateEmbedUrlForRegisteredUserResponse = {}  # type: ignore[typeddict-item]
    if data.get("EmbedUrl") is not None:
        out["embed_url"] = data["EmbedUrl"]
    else:
        out["embed_url"] = ""
    if data.get("RequestId") is not None:
        out["request_id"] = data["RequestId"]
    else:
        out["request_id"] = ""
    return out


def redact_sensitive(
    value: GenerateEmbedUrlForRegisteredUserResponse,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "embed_url" in value:
        out["embed_url"] = "*** Sensitive Data Redacted ***"
    return out
