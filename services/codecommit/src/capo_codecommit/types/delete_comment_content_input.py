"""Generated from Smithy shape ``com.amazonaws.codecommit#DeleteCommentContentInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.comment_id


class DeleteCommentContentInput(TypedDict, closed=True):
    comment_id: "capo_codecommit.types.comment_id.CommentId"
    """<p>The unique, system-generated ID of the comment. To get this ID, use <a>GetCommentsForComparedCommit</a> or <a>GetCommentsForPullRequest</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteCommentContentInput) -> dict:
    out: dict = {}
    out["commentId"] = value["comment_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteCommentContentInput:
    out: DeleteCommentContentInput = {}  # type: ignore[typeddict-item]
    if data.get("commentId") is not None:
        out["comment_id"] = data["commentId"]
    else:
        out["comment_id"] = ""
    return out
