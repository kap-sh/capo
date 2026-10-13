"""Generated from Smithy shape ``com.amazonaws.securityir#UpdateCaseCommentResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_security_ir.errors import DeserializationError

if TYPE_CHECKING:
    import capo_security_ir.types.comment_body
    import capo_security_ir.types.comment_id


class UpdateCaseCommentResponse(TypedDict, closed=True):
    comment_id: "capo_security_ir.types.comment_id.CommentId"
    """<p>Response element for UpdateCaseComment providing the updated comment ID.</p>"""
    body: NotRequired["capo_security_ir.types.comment_body.CommentBody"]
    """<p>Response element for UpdateCaseComment providing the updated comment content.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCaseCommentResponse) -> dict:
    out: dict = {}
    out["commentId"] = value["comment_id"]
    if "body" in value:
        out["body"] = value["body"]
    return out


def deserialize_json(data: dict) -> UpdateCaseCommentResponse:
    out: UpdateCaseCommentResponse = {}  # type: ignore[typeddict-item]
    if data.get("commentId") is not None:
        out["comment_id"] = data["commentId"]
    else:
        raise DeserializationError("UpdateCaseCommentResponse.comment_id required")
    if data.get("body") is not None:
        out["body"] = data["body"]
    return out


def redact_sensitive(value: UpdateCaseCommentResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "body" in value:
        out["body"] = "*** Sensitive Data Redacted ***"
    return out
