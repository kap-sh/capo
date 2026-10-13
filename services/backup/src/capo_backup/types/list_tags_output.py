"""Generated from Smithy shape ``com.amazonaws.backup#ListTagsOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.string
    import capo_backup.types.tags


class ListTagsOutput(TypedDict, closed=True):
    next_token: NotRequired["capo_backup.types.string.string"]
    """<p>The next item following a partial list of returned items. For example, if a request is made to return <code>MaxResults</code> number of items, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>"""
    tags: NotRequired["capo_backup.types.tags.Tags"]
    """<p>Information about the tags.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "tags" in value:
        import capo_backup.types.tags

        out["Tags"] = capo_backup.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> ListTagsOutput:
    out: ListTagsOutput = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Tags") is not None:
        import capo_backup.types.tags

        out["tags"] = capo_backup.types.tags.deserialize_json(data["Tags"])
    return out


def redact_sensitive(value: ListTagsOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        out["tags"] = "*** Sensitive Data Redacted ***"
    return out
