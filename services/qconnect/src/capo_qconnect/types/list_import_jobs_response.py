"""Generated from Smithy shape ``com.amazonaws.qconnect#ListImportJobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.import_job_list
    import capo_qconnect.types.non_empty_string


class ListImportJobsResponse(TypedDict, closed=True):
    import_job_summaries: "capo_qconnect.types.import_job_list.ImportJobList"
    """<p>Summary information about the import jobs.</p>"""
    next_token: NotRequired["capo_qconnect.types.non_empty_string.NonEmptyString"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListImportJobsResponse) -> dict:
    out: dict = {}
    import capo_qconnect.types.import_job_list

    out["importJobSummaries"] = capo_qconnect.types.import_job_list.serialize_json(
        value["import_job_summaries"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListImportJobsResponse:
    out: ListImportJobsResponse = {}  # type: ignore[typeddict-item]
    if data.get("importJobSummaries") is not None:
        import capo_qconnect.types.import_job_list

        out["import_job_summaries"] = (
            capo_qconnect.types.import_job_list.deserialize_json(
                data["importJobSummaries"]
            )
        )
    else:
        out["import_job_summaries"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
