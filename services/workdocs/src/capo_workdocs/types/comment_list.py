"""Generated from Smithy shape ``com.amazonaws.workdocs#CommentList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_workdocs.types.comment

CommentList: TypeAlias = list["capo_workdocs.types.comment.Comment"]


# --- restJson1 ser/de ---
def serialize_json(value: CommentList) -> list:
    import capo_workdocs.types.comment

    out: list = []
    for item in value:
        out.append(capo_workdocs.types.comment.serialize_json(item))
    return out


def deserialize_json(data: list) -> CommentList:
    import capo_workdocs.types.comment

    out: CommentList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_workdocs.types.comment.deserialize_json(item))
    return out


def redact_sensitive(value: CommentList) -> list[Any]:
    import capo_workdocs.types.comment

    return [capo_workdocs.types.comment.redact_sensitive(item) for item in value]
