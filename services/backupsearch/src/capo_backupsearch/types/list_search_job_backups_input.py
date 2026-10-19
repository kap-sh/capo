"""Generated from Smithy shape ``com.amazonaws.backupsearch#ListSearchJobBackupsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backupsearch.types.generic_id


class ListSearchJobBackupsInput(TypedDict, closed=True):
    search_job_identifier: "capo_backupsearch.types.generic_id.GenericId"
    """<p>The unique string that specifies the search job.</p>"""
    next_token: NotRequired["str"]
    """<p>The next item following a partial list of returned backups included in a search job.</p> <p>For example, if a request is made to return <code>MaxResults</code> number of backups, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of resource list items to be returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSearchJobBackupsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListSearchJobBackupsInput:
    out: ListSearchJobBackupsInput = {}  # type: ignore[typeddict-item]
    return out
