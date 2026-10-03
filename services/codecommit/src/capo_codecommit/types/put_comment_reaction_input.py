"""Generated from Smithy shape ``com.amazonaws.codecommit#PutCommentReactionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_codecommit.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codecommit.types.comment_id
    import capo_codecommit.types.reaction_value


class PutCommentReactionInput(TypedDict, closed=True):
    comment_id: "capo_codecommit.types.comment_id.CommentId"
    """<p>The ID of the comment to which you want to add or update a reaction.</p>"""
    reaction_value: "capo_codecommit.types.reaction_value.ReactionValue"
    """<p>The emoji reaction you want to add or update. To remove a reaction, provide a value of blank or null. You can also provide the value of none. For information about emoji reaction values supported in CodeCommit, see the <a href="https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-commit-comment.html#emoji-reaction-table">CodeCommit User Guide</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutCommentReactionInput) -> dict:
    out: dict = {}
    out["commentId"] = value["comment_id"]
    out["reactionValue"] = value["reaction_value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutCommentReactionInput:
    out: PutCommentReactionInput = {}  # type: ignore[typeddict-item]
    if data.get("commentId") is not None:
        out["comment_id"] = data["commentId"]
    else:
        raise DeserializationError("PutCommentReactionInput.comment_id required")
    if data.get("reactionValue") is not None:
        out["reaction_value"] = data["reactionValue"]
    else:
        raise DeserializationError("PutCommentReactionInput.reaction_value required")
    return out
