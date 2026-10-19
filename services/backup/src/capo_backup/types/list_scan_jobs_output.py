"""Generated from Smithy shape ``com.amazonaws.backup#ListScanJobsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.scan_jobs


class ListScanJobsOutput(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p>The next item following a partial list of returned items. For example, if a request is made to return <code>MaxResults</code> number of items, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>"""
    scan_jobs: "capo_backup.types.scan_jobs.ScanJobs"
    """<p>An array of structures containing metadata about your scan jobs returned in JSON format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListScanJobsOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    import capo_backup.types.scan_jobs

    out["ScanJobs"] = capo_backup.types.scan_jobs.serialize_json(value["scan_jobs"])
    return out


def deserialize_json(data: dict) -> ListScanJobsOutput:
    out: ListScanJobsOutput = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("ScanJobs") is not None:
        import capo_backup.types.scan_jobs

        out["scan_jobs"] = capo_backup.types.scan_jobs.deserialize_json(
            data["ScanJobs"]
        )
    else:
        out["scan_jobs"] = []
    return out
