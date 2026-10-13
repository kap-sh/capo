"""Generated from Smithy shape ``com.amazonaws.workdocs#DeleteCommentRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workdocs.types.authentication_header_type
    import capo_workdocs.types.comment_id_type
    import capo_workdocs.types.document_version_id_type
    import capo_workdocs.types.resource_id_type


class DeleteCommentRequest(TypedDict, closed=True):
    authentication_token: NotRequired[
        "capo_workdocs.types.authentication_header_type.AuthenticationHeaderType"
    ]
    """<p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>"""
    document_id: "capo_workdocs.types.resource_id_type.ResourceIdType"
    """<p>The ID of the document.</p>"""
    version_id: "capo_workdocs.types.document_version_id_type.DocumentVersionIdType"
    """<p>The ID of the document version.</p>"""
    comment_id: "capo_workdocs.types.comment_id_type.CommentIdType"
    """<p>The ID of the comment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteCommentRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteCommentRequest:
    out: DeleteCommentRequest = {}  # type: ignore[typeddict-item]
    return out


def redact_sensitive(value: DeleteCommentRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "authentication_token" in value:
        out["authentication_token"] = "*** Sensitive Data Redacted ***"
    return out
