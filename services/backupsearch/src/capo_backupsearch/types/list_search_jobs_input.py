"""Generated from Smithy shape ``com.amazonaws.backupsearch#ListSearchJobsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backupsearch.types.search_job_state


class ListSearchJobsInput(TypedDict, closed=True):
    by_status: NotRequired["capo_backupsearch.types.search_job_state.SearchJobState"]
    """<p>Include this parameter to filter list by search job status.</p>"""
    next_token: NotRequired["str"]
    """<p>The next item following a partial list of returned search jobs.</p> <p>For example, if a request is made to return <code>MaxResults</code> number of backups, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of resource list items to be returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSearchJobsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListSearchJobsInput:
    out: ListSearchJobsInput = {}  # type: ignore[typeddict-item]
    return out
