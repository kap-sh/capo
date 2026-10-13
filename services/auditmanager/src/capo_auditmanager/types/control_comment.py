"""Generated from Smithy shape ``com.amazonaws.auditmanager#ControlComment``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.control_comment_body
    import capo_auditmanager.types.timestamp
    import capo_auditmanager.types.username


class ControlComment(TypedDict, closed=True):
    author_name: NotRequired["capo_auditmanager.types.username.Username"]
    """<p> The name of the user who authored the comment. </p>"""
    comment_body: NotRequired[
        "capo_auditmanager.types.control_comment_body.ControlCommentBody"
    ]
    """<p> The body text of a control comment. </p>"""
    posted_date: NotRequired["capo_auditmanager.types.timestamp.Timestamp"]
    """<p> The time when the comment was posted. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ControlComment) -> dict:
    out: dict = {}
    if "author_name" in value:
        out["authorName"] = value["author_name"]
    if "comment_body" in value:
        out["commentBody"] = value["comment_body"]
    if "posted_date" in value:
        import capo_auditmanager.types.timestamp

        out["postedDate"] = capo_auditmanager.types.timestamp.serialize_json(
            value["posted_date"]
        )
    return out


def deserialize_json(data: dict) -> ControlComment:
    out: ControlComment = {}  # type: ignore[typeddict-item]
    if data.get("authorName") is not None:
        out["author_name"] = data["authorName"]
    if data.get("commentBody") is not None:
        out["comment_body"] = data["commentBody"]
    if data.get("postedDate") is not None:
        import capo_auditmanager.types.timestamp

        out["posted_date"] = capo_auditmanager.types.timestamp.deserialize_json(
            data["postedDate"]
        )
    return out


def redact_sensitive(value: ControlComment) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "author_name" in value:
        out["author_name"] = "*** Sensitive Data Redacted ***"
    if "comment_body" in value:
        out["comment_body"] = "*** Sensitive Data Redacted ***"
    return out
