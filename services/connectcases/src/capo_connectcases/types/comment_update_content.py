"""Generated from Smithy shape ``com.amazonaws.connectcases#CommentUpdateContent``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.comment_body
    import capo_connectcases.types.comment_body_text_type


class CommentUpdateContent(TypedDict, closed=True):
    body: "capo_connectcases.types.comment_body.CommentBody"
    """<p>Updated text in the body of a <code>Comment</code> on a case.</p>"""
    content_type: "capo_connectcases.types.comment_body_text_type.CommentBodyTextType"
    """<p>Type of the text in the box of a <code>Comment</code> on a case.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CommentUpdateContent) -> dict:
    out: dict = {}
    out["body"] = value["body"]
    out["contentType"] = value["content_type"]
    return out


def deserialize_json(data: dict) -> CommentUpdateContent:
    out: CommentUpdateContent = {}  # type: ignore[typeddict-item]
    if data.get("body") is not None:
        out["body"] = data["body"]
    else:
        out["body"] = ""
    if data.get("contentType") is not None:
        out["content_type"] = data["contentType"]
    else:
        out["content_type"] = ""
    return out
