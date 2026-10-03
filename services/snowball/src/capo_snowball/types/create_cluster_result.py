"""Generated from Smithy shape ``com.amazonaws.snowball#CreateClusterResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_snowball.types.cluster_id
    import capo_snowball.types.job_list_entry_list


class CreateClusterResult(TypedDict, closed=True):
    cluster_id: NotRequired["capo_snowball.types.cluster_id.ClusterId"]
    """<p>The automatically generated ID for a cluster.</p>"""
    job_list_entries: NotRequired[
        "capo_snowball.types.job_list_entry_list.JobListEntryList"
    ]
    """<p>List of jobs created for this cluster. For syntax, see <a href="http://amazonaws.com/snowball/latest/api-reference/API_ListJobs.html#API_ListJobs_ResponseSyntax">ListJobsResult$JobListEntries</a> in this guide.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateClusterResult) -> dict:
    out: dict = {}
    if "cluster_id" in value:
        out["ClusterId"] = value["cluster_id"]
    if "job_list_entries" in value:
        import capo_snowball.types.job_list_entry_list

        out["JobListEntries"] = (
            capo_snowball.types.job_list_entry_list.serialize_aws_json_1_1(
                value["job_list_entries"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateClusterResult:
    out: CreateClusterResult = {}  # type: ignore[typeddict-item]
    if data.get("ClusterId") is not None:
        out["cluster_id"] = data["ClusterId"]
    if data.get("JobListEntries") is not None:
        import capo_snowball.types.job_list_entry_list

        out["job_list_entries"] = (
            capo_snowball.types.job_list_entry_list.deserialize_aws_json_1_1(
                data["JobListEntries"]
            )
        )
    return out
