"""Generated from Smithy shape ``com.amazonaws.codecommit#UpdateCommentInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.comment_id
    import capo_codecommit.types.content


class UpdateCommentInput(TypedDict, closed=True):
    comment_id: "capo_codecommit.types.comment_id.CommentId"
    """<p>The system-generated ID of the comment you want to update. To get this ID, use <a>GetCommentsForComparedCommit</a> or <a>GetCommentsForPullRequest</a>.</p>"""
    content: "capo_codecommit.types.content.Content"
    """<p>The updated content to replace the existing content of the comment.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateCommentInput) -> dict:
    out: dict = {}
    out["commentId"] = value["comment_id"]
    out["content"] = value["content"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateCommentInput:
    out: UpdateCommentInput = {}  # type: ignore[typeddict-item]
    if data.get("commentId") is not None:
        out["comment_id"] = data["commentId"]
    else:
        out["comment_id"] = ""
    if data.get("content") is not None:
        out["content"] = data["content"]
    else:
        out["content"] = ""
    return out
