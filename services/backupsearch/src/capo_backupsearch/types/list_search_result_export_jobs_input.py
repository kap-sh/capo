"""Generated from Smithy shape ``com.amazonaws.backupsearch#ListSearchResultExportJobsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backupsearch.types.export_job_status
    import capo_backupsearch.types.generic_id


class ListSearchResultExportJobsInput(TypedDict, closed=True):
    status: NotRequired["capo_backupsearch.types.export_job_status.ExportJobStatus"]
    """<p>The search jobs to be included in the export job can be filtered by including this parameter.</p>"""
    search_job_identifier: NotRequired["capo_backupsearch.types.generic_id.GenericId"]
    """<p>The unique string that specifies the search job.</p>"""
    next_token: NotRequired["str"]
    """<p>The next item following a partial list of returned backups included in a search job.</p> <p>For example, if a request is made to return <code>MaxResults</code> number of backups, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of resource list items to be returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSearchResultExportJobsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListSearchResultExportJobsInput:
    out: ListSearchResultExportJobsInput = {}  # type: ignore[typeddict-item]
    return out
