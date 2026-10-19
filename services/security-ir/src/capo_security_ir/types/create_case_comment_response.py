"""Generated from Smithy shape ``com.amazonaws.securityir#CreateCaseCommentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_security_ir.types.comment_id


class CreateCaseCommentResponse(TypedDict, closed=True):
    comment_id: "capo_security_ir.types.comment_id.CommentId"
    """<p>Response element indicating the new comment ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCaseCommentResponse) -> dict:
    out: dict = {}
    out["commentId"] = value["comment_id"]
    return out


def deserialize_json(data: dict) -> CreateCaseCommentResponse:
    out: CreateCaseCommentResponse = {}  # type: ignore[typeddict-item]
    if data.get("commentId") is not None:
        out["comment_id"] = data["commentId"]
    else:
        out["comment_id"] = ""
    return out
