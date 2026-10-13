"""Generated from Smithy shape ``com.amazonaws.workdocs#CreateCommentResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workdocs.types.comment


class CreateCommentResponse(TypedDict, closed=True):
    comment: NotRequired["capo_workdocs.types.comment.Comment"]
    """<p>The comment that has been created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCommentResponse) -> dict:
    out: dict = {}
    if "comment" in value:
        import capo_workdocs.types.comment

        out["Comment"] = capo_workdocs.types.comment.serialize_json(value["comment"])
    return out


def deserialize_json(data: dict) -> CreateCommentResponse:
    out: CreateCommentResponse = {}  # type: ignore[typeddict-item]
    if data.get("Comment") is not None:
        import capo_workdocs.types.comment

        out["comment"] = capo_workdocs.types.comment.deserialize_json(data["Comment"])
    return out


def redact_sensitive(value: CreateCommentResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "comment" in value:
        import capo_workdocs.types.comment

        out["comment"] = capo_workdocs.types.comment.redact_sensitive(value["comment"])
    return out
