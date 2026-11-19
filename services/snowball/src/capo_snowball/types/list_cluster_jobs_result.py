"""Generated from Smithy shape ``com.amazonaws.snowball#ListClusterJobsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_snowball.types.job_list_entry_list
    import capo_snowball.types.string


class ListClusterJobsResult(TypedDict, closed=True):
    job_list_entries: NotRequired[
        "capo_snowball.types.job_list_entry_list.JobListEntryList"
    ]
    """<p>Each <code>JobListEntry</code> object contains a job's state, a job's ID, and a value that indicates whether the job is a job part, in the case of export jobs. </p>"""
    next_token: NotRequired["capo_snowball.types.string.String"]
    """<p>HTTP requests are stateless. If you use the automatically generated <code>NextToken</code> value in your next <code>ListClusterJobsResult</code> call, your list of returned jobs will start from this point in the array.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListClusterJobsResult) -> dict:
    out: dict = {}
    if "job_list_entries" in value:
        import capo_snowball.types.job_list_entry_list

        out["JobListEntries"] = (
            capo_snowball.types.job_list_entry_list.serialize_aws_json_1_1(
                value["job_list_entries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListClusterJobsResult:
    out: ListClusterJobsResult = {}  # type: ignore[typeddict-item]
    if data.get("JobListEntries") is not None:
        import capo_snowball.types.job_list_entry_list

        out["job_list_entries"] = (
            capo_snowball.types.job_list_entry_list.deserialize_aws_json_1_1(
                data["JobListEntries"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListClusterJobsResult) -> dict:
    out: dict = {}
    if "job_list_entries" in value:
        import capo_snowball.types.job_list_entry_list

        out["JobListEntries"] = capo_snowball.types.job_list_entry_list.serialize_cbor(
            value["job_list_entries"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListClusterJobsResult:
    out: ListClusterJobsResult = {}  # type: ignore[typeddict-item]
    if data.get("JobListEntries") is not None:
        import capo_snowball.types.job_list_entry_list

        out["job_list_entries"] = (
            capo_snowball.types.job_list_entry_list.deserialize_cbor(
                data["JobListEntries"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
