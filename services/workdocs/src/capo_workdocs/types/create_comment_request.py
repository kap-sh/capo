"""Generated from Smithy shape ``com.amazonaws.workdocs#CreateCommentRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_workdocs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_workdocs.types.authentication_header_type
    import capo_workdocs.types.boolean_type
    import capo_workdocs.types.comment_id_type
    import capo_workdocs.types.comment_text_type
    import capo_workdocs.types.comment_visibility_type
    import capo_workdocs.types.document_version_id_type
    import capo_workdocs.types.resource_id_type


class CreateCommentRequest(TypedDict, closed=True):
    authentication_token: NotRequired[
        "capo_workdocs.types.authentication_header_type.AuthenticationHeaderType"
    ]
    """<p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>"""
    document_id: "capo_workdocs.types.resource_id_type.ResourceIdType"
    """<p>The ID of the document.</p>"""
    version_id: "capo_workdocs.types.document_version_id_type.DocumentVersionIdType"
    """<p>The ID of the document version.</p>"""
    parent_id: NotRequired["capo_workdocs.types.comment_id_type.CommentIdType"]
    """<p>The ID of the parent comment.</p>"""
    thread_id: NotRequired["capo_workdocs.types.comment_id_type.CommentIdType"]
    """<p>The ID of the root comment in the thread.</p>"""
    text: "capo_workdocs.types.comment_text_type.CommentTextType"
    """<p>The text of the comment.</p>"""
    visibility: NotRequired[
        "capo_workdocs.types.comment_visibility_type.CommentVisibilityType"
    ]
    """<p>The visibility of the comment. Options are either PRIVATE, where the comment is visible only to the comment author and document owner and co-owners, or PUBLIC, where the comment is visible to document owners, co-owners, and contributors.</p>"""
    notify_collaborators: "capo_workdocs.types.boolean_type.BooleanType"
    """<p>Set this parameter to TRUE to send an email out to the document collaborators after the comment is created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCommentRequest) -> dict:
    out: dict = {}
    if "parent_id" in value:
        out["ParentId"] = value["parent_id"]
    if "thread_id" in value:
        out["ThreadId"] = value["thread_id"]
    out["Text"] = value["text"]
    if "visibility" in value:
        import capo_workdocs.types.comment_visibility_type

        out["Visibility"] = capo_workdocs.types.comment_visibility_type.serialize_json(
            value["visibility"]
        )
    out["NotifyCollaborators"] = value.get("notify_collaborators", False)
    return out


def deserialize_json(data: dict) -> CreateCommentRequest:
    out: CreateCommentRequest = {}  # type: ignore[typeddict-item]
    if data.get("ParentId") is not None:
        out["parent_id"] = data["ParentId"]
    if data.get("ThreadId") is not None:
        out["thread_id"] = data["ThreadId"]
    if data.get("Text") is not None:
        out["text"] = data["Text"]
    else:
        raise DeserializationError("CreateCommentRequest.text required")
    if data.get("Visibility") is not None:
        import capo_workdocs.types.comment_visibility_type

        out["visibility"] = (
            capo_workdocs.types.comment_visibility_type.deserialize_json(
                data["Visibility"]
            )
        )
    if data.get("NotifyCollaborators") is not None:
        out["notify_collaborators"] = data["NotifyCollaborators"]
    else:
        out["notify_collaborators"] = False
    return out


def redact_sensitive(value: CreateCommentRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "authentication_token" in value:
        out["authentication_token"] = "*** Sensitive Data Redacted ***"
    if "text" in value:
        out["text"] = "*** Sensitive Data Redacted ***"
    return out
