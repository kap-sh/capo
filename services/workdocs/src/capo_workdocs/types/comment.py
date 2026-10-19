"""Generated from Smithy shape ``com.amazonaws.workdocs#Comment``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workdocs.types.comment_id_type
    import capo_workdocs.types.comment_status_type
    import capo_workdocs.types.comment_text_type
    import capo_workdocs.types.comment_visibility_type
    import capo_workdocs.types.id_type
    import capo_workdocs.types.timestamp_type
    import capo_workdocs.types.user


class Comment(TypedDict, closed=True):
    comment_id: "capo_workdocs.types.comment_id_type.CommentIdType"
    """<p>The ID of the comment.</p>"""
    parent_id: NotRequired["capo_workdocs.types.comment_id_type.CommentIdType"]
    """<p>The ID of the parent comment.</p>"""
    thread_id: NotRequired["capo_workdocs.types.comment_id_type.CommentIdType"]
    """<p>The ID of the root comment in the thread.</p>"""
    text: NotRequired["capo_workdocs.types.comment_text_type.CommentTextType"]
    """<p>The text of the comment.</p>"""
    contributor: NotRequired["capo_workdocs.types.user.User"]
    """<p>The details of the user who made the comment.</p>"""
    created_timestamp: NotRequired["capo_workdocs.types.timestamp_type.TimestampType"]
    """<p>The time that the comment was created.</p>"""
    status: NotRequired["capo_workdocs.types.comment_status_type.CommentStatusType"]
    """<p>The status of the comment.</p>"""
    visibility: NotRequired[
        "capo_workdocs.types.comment_visibility_type.CommentVisibilityType"
    ]
    """<p>The visibility of the comment. Options are either PRIVATE, where the comment is visible only to the comment author and document owner and co-owners, or PUBLIC, where the comment is visible to document owners, co-owners, and contributors.</p>"""
    recipient_id: NotRequired["capo_workdocs.types.id_type.IdType"]
    """<p>If the comment is a reply to another user's comment, this field contains the user ID of the user being replied to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Comment) -> dict:
    out: dict = {}
    out["CommentId"] = value["comment_id"]
    if "parent_id" in value:
        out["ParentId"] = value["parent_id"]
    if "thread_id" in value:
        out["ThreadId"] = value["thread_id"]
    if "text" in value:
        out["Text"] = value["text"]
    if "contributor" in value:
        import capo_workdocs.types.user

        out["Contributor"] = capo_workdocs.types.user.serialize_json(
            value["contributor"]
        )
    if "created_timestamp" in value:
        import capo_workdocs.types.timestamp_type

        out["CreatedTimestamp"] = capo_workdocs.types.timestamp_type.serialize_json(
            value["created_timestamp"]
        )
    if "status" in value:
        import capo_workdocs.types.comment_status_type

        out["Status"] = capo_workdocs.types.comment_status_type.serialize_json(
            value["status"]
        )
    if "visibility" in value:
        import capo_workdocs.types.comment_visibility_type

        out["Visibility"] = capo_workdocs.types.comment_visibility_type.serialize_json(
            value["visibility"]
        )
    if "recipient_id" in value:
        out["RecipientId"] = value["recipient_id"]
    return out


def deserialize_json(data: dict) -> Comment:
    out: Comment = {}  # type: ignore[typeddict-item]
    if data.get("CommentId") is not None:
        out["comment_id"] = data["CommentId"]
    else:
        out["comment_id"] = ""
    if data.get("ParentId") is not None:
        out["parent_id"] = data["ParentId"]
    if data.get("ThreadId") is not None:
        out["thread_id"] = data["ThreadId"]
    if data.get("Text") is not None:
        out["text"] = data["Text"]
    if data.get("Contributor") is not None:
        import capo_workdocs.types.user

        out["contributor"] = capo_workdocs.types.user.deserialize_json(
            data["Contributor"]
        )
    if data.get("CreatedTimestamp") is not None:
        import capo_workdocs.types.timestamp_type

        out["created_timestamp"] = capo_workdocs.types.timestamp_type.deserialize_json(
            data["CreatedTimestamp"]
        )
    if data.get("Status") is not None:
        import capo_workdocs.types.comment_status_type

        out["status"] = capo_workdocs.types.comment_status_type.deserialize_json(
            data["Status"]
        )
    if data.get("Visibility") is not None:
        import capo_workdocs.types.comment_visibility_type

        out["visibility"] = (
            capo_workdocs.types.comment_visibility_type.deserialize_json(
                data["Visibility"]
            )
        )
    if data.get("RecipientId") is not None:
        out["recipient_id"] = data["RecipientId"]
    return out


def redact_sensitive(value: Comment) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "text" in value:
        out["text"] = "*** Sensitive Data Redacted ***"
    if "contributor" in value:
        import capo_workdocs.types.user

        out["contributor"] = capo_workdocs.types.user.redact_sensitive(
            value["contributor"]
        )
    return out
