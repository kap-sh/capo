"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ListDatasetExportJobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.export_job_summary_list
    import capo_iotsitewise.types.list_export_jobs_next_token


class ListDatasetExportJobsResponse(TypedDict, closed=True):
    jobs: "capo_iotsitewise.types.export_job_summary_list.ExportJobSummaryList"
    """<p>A list of dataset export job summaries.</p>"""
    next_token: NotRequired[
        "capo_iotsitewise.types.list_export_jobs_next_token.ListExportJobsNextToken"
    ]
    """<p>The token for the next set of results, or null if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDatasetExportJobsResponse) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.export_job_summary_list

    out["jobs"] = capo_iotsitewise.types.export_job_summary_list.serialize_json(
        value["jobs"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDatasetExportJobsResponse:
    out: ListDatasetExportJobsResponse = {}  # type: ignore[typeddict-item]
    if data.get("jobs") is not None:
        import capo_iotsitewise.types.export_job_summary_list

        out["jobs"] = capo_iotsitewise.types.export_job_summary_list.deserialize_json(
            data["jobs"]
        )
    else:
        out["jobs"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
