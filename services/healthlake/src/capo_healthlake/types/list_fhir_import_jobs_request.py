"""Generated from Smithy shape ``com.amazonaws.healthlake#ListFHIRImportJobsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_healthlake.types.datastore_id
    import capo_healthlake.types.health_lake_timestamp
    import capo_healthlake.types.job_name
    import capo_healthlake.types.job_status
    import capo_healthlake.types.max_results_integer
    import capo_healthlake.types.next_token


class ListFHIRImportJobsRequest(TypedDict, closed=True):
    datastore_id: "capo_healthlake.types.datastore_id.DatastoreId"
    """<p>Limits the response to the import job with the specified data store ID. </p>"""
    next_token: NotRequired["capo_healthlake.types.next_token.NextToken"]
    """<p>The pagination token used to identify the next page of results to return.</p>"""
    max_results: NotRequired[
        "capo_healthlake.types.max_results_integer.MaxResultsInteger"
    ]
    """<p>Limits the number of results returned for <code>ListFHIRImportJobs</code> to a maximum quantity specified by the user.</p>"""
    job_name: NotRequired["capo_healthlake.types.job_name.JobName"]
    """<p>Limits the response to the import job with the specified job name. </p>"""
    job_status: NotRequired["capo_healthlake.types.job_status.JobStatus"]
    """<p>Limits the response to the import job with the specified job status. </p>"""
    submitted_before: NotRequired[
        "capo_healthlake.types.health_lake_timestamp.HealthLakeTimestamp"
    ]
    """<p>Limits the response to FHIR import jobs submitted before a user- specified date. </p>"""
    submitted_after: NotRequired[
        "capo_healthlake.types.health_lake_timestamp.HealthLakeTimestamp"
    ]
    """<p>Limits the response to FHIR import jobs submitted after a user-specified date.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListFHIRImportJobsRequest) -> dict:
    out: dict = {}
    out["DatastoreId"] = value["datastore_id"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "job_name" in value:
        out["JobName"] = value["job_name"]
    if "job_status" in value:
        import capo_healthlake.types.job_status

        out["JobStatus"] = capo_healthlake.types.job_status.serialize_aws_json_1_0(
            value["job_status"]
        )
    if "submitted_before" in value:
        import capo_healthlake.types.health_lake_timestamp

        out["SubmittedBefore"] = (
            capo_healthlake.types.health_lake_timestamp.serialize_aws_json_1_0(
                value["submitted_before"]
            )
        )
    if "submitted_after" in value:
        import capo_healthlake.types.health_lake_timestamp

        out["SubmittedAfter"] = (
            capo_healthlake.types.health_lake_timestamp.serialize_aws_json_1_0(
                value["submitted_after"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListFHIRImportJobsRequest:
    out: ListFHIRImportJobsRequest = {}  # type: ignore[typeddict-item]
    if data.get("DatastoreId") is not None:
        out["datastore_id"] = data["DatastoreId"]
    else:
        out["datastore_id"] = ""
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("JobName") is not None:
        out["job_name"] = data["JobName"]
    if data.get("JobStatus") is not None:
        import capo_healthlake.types.job_status

        out["job_status"] = capo_healthlake.types.job_status.deserialize_aws_json_1_0(
            data["JobStatus"]
        )
    if data.get("SubmittedBefore") is not None:
        import capo_healthlake.types.health_lake_timestamp

        out["submitted_before"] = (
            capo_healthlake.types.health_lake_timestamp.deserialize_aws_json_1_0(
                data["SubmittedBefore"]
            )
        )
    if data.get("SubmittedAfter") is not None:
        import capo_healthlake.types.health_lake_timestamp

        out["submitted_after"] = (
            capo_healthlake.types.health_lake_timestamp.deserialize_aws_json_1_0(
                data["SubmittedAfter"]
            )
        )
    return out
