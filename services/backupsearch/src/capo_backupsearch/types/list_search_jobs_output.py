"""Generated from Smithy shape ``com.amazonaws.backupsearch#ListSearchJobsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backupsearch.types.search_jobs


class ListSearchJobsOutput(TypedDict, closed=True):
    search_jobs: "capo_backupsearch.types.search_jobs.SearchJobs"
    """<p>The search jobs among the list, with details of the returned search jobs.</p>"""
    next_token: NotRequired["str"]
    """<p>The next item following a partial list of returned backups included in a search job.</p> <p>For example, if a request is made to return <code>MaxResults</code> number of backups, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSearchJobsOutput) -> dict:
    out: dict = {}
    import capo_backupsearch.types.search_jobs

    out["SearchJobs"] = capo_backupsearch.types.search_jobs.serialize_json(
        value["search_jobs"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSearchJobsOutput:
    out: ListSearchJobsOutput = {}  # type: ignore[typeddict-item]
    if data.get("SearchJobs") is not None:
        import capo_backupsearch.types.search_jobs

        out["search_jobs"] = capo_backupsearch.types.search_jobs.deserialize_json(
            data["SearchJobs"]
        )
    else:
        out["search_jobs"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
