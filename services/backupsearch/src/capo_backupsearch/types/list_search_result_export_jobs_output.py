"""Generated from Smithy shape ``com.amazonaws.backupsearch#ListSearchResultExportJobsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backupsearch.types.export_job_summaries


class ListSearchResultExportJobsOutput(TypedDict, closed=True):
    export_jobs: "capo_backupsearch.types.export_job_summaries.ExportJobSummaries"
    """<p>The operation returns the included export jobs.</p>"""
    next_token: NotRequired["str"]
    """<p>The next item following a partial list of returned backups included in a search job.</p> <p>For example, if a request is made to return <code>MaxResults</code> number of backups, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSearchResultExportJobsOutput) -> dict:
    out: dict = {}
    import capo_backupsearch.types.export_job_summaries

    out["ExportJobs"] = capo_backupsearch.types.export_job_summaries.serialize_json(
        value["export_jobs"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSearchResultExportJobsOutput:
    out: ListSearchResultExportJobsOutput = {}  # type: ignore[typeddict-item]
    if data.get("ExportJobs") is not None:
        import capo_backupsearch.types.export_job_summaries

        out["export_jobs"] = (
            capo_backupsearch.types.export_job_summaries.deserialize_json(
                data["ExportJobs"]
            )
        )
    else:
        out["export_jobs"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
