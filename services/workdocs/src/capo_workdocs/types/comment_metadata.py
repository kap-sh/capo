"""Generated from Smithy shape ``com.amazonaws.workdocs#CommentMetadata``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workdocs.types.comment_id_type
    import capo_workdocs.types.comment_status_type
    import capo_workdocs.types.id_type
    import capo_workdocs.types.timestamp_type
    import capo_workdocs.types.user


class CommentMetadata(TypedDict, closed=True):
    comment_id: NotRequired["capo_workdocs.types.comment_id_type.CommentIdType"]
    """<p>The ID of the comment.</p>"""
    contributor: NotRequired["capo_workdocs.types.user.User"]
    """<p>The user who made the comment.</p>"""
    created_timestamp: NotRequired["capo_workdocs.types.timestamp_type.TimestampType"]
    """<p>The timestamp that the comment was created.</p>"""
    comment_status: NotRequired[
        "capo_workdocs.types.comment_status_type.CommentStatusType"
    ]
    """<p>The status of the comment.</p>"""
    recipient_id: NotRequired["capo_workdocs.types.id_type.IdType"]
    """<p>The ID of the user being replied to.</p>"""
    contributor_id: NotRequired["capo_workdocs.types.id_type.IdType"]
    """<p>The ID of the user who made the comment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CommentMetadata) -> dict:
    out: dict = {}
    if "comment_id" in value:
        out["CommentId"] = value["comment_id"]
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
    if "comment_status" in value:
        import capo_workdocs.types.comment_status_type

        out["CommentStatus"] = capo_workdocs.types.comment_status_type.serialize_json(
            value["comment_status"]
        )
    if "recipient_id" in value:
        out["RecipientId"] = value["recipient_id"]
    if "contributor_id" in value:
        out["ContributorId"] = value["contributor_id"]
    return out


def deserialize_json(data: dict) -> CommentMetadata:
    out: CommentMetadata = {}  # type: ignore[typeddict-item]
    if data.get("CommentId") is not None:
        out["comment_id"] = data["CommentId"]
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
    if data.get("CommentStatus") is not None:
        import capo_workdocs.types.comment_status_type

        out["comment_status"] = (
            capo_workdocs.types.comment_status_type.deserialize_json(
                data["CommentStatus"]
            )
        )
    if data.get("RecipientId") is not None:
        out["recipient_id"] = data["RecipientId"]
    if data.get("ContributorId") is not None:
        out["contributor_id"] = data["ContributorId"]
    return out


def redact_sensitive(value: CommentMetadata) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "contributor" in value:
        import capo_workdocs.types.user

        out["contributor"] = capo_workdocs.types.user.redact_sensitive(
            value["contributor"]
        )
    return out
