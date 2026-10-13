"""Generated from Smithy shape ``com.amazonaws.workdocs#DescribeCommentsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workdocs.types.comment_list
    import capo_workdocs.types.marker_type


class DescribeCommentsResponse(TypedDict, closed=True):
    comments: NotRequired["capo_workdocs.types.comment_list.CommentList"]
    """<p>The list of comments for the specified document version.</p>"""
    marker: NotRequired["capo_workdocs.types.marker_type.MarkerType"]
    """<p>The marker for the next set of results. This marker was received from a previous call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeCommentsResponse) -> dict:
    out: dict = {}
    if "comments" in value:
        import capo_workdocs.types.comment_list

        out["Comments"] = capo_workdocs.types.comment_list.serialize_json(
            value["comments"]
        )
    if "marker" in value:
        out["Marker"] = value["marker"]
    return out


def deserialize_json(data: dict) -> DescribeCommentsResponse:
    out: DescribeCommentsResponse = {}  # type: ignore[typeddict-item]
    if data.get("Comments") is not None:
        import capo_workdocs.types.comment_list

        out["comments"] = capo_workdocs.types.comment_list.deserialize_json(
            data["Comments"]
        )
    if data.get("Marker") is not None:
        out["marker"] = data["Marker"]
    return out


def redact_sensitive(value: DescribeCommentsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "comments" in value:
        import capo_workdocs.types.comment_list

        out["comments"] = capo_workdocs.types.comment_list.redact_sensitive(
            value["comments"]
        )
    return out
