"""Generated from Smithy shape ``com.amazonaws.kendra#ListDataSourceSyncJobsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.data_source_id
    import capo_kendra.types.data_source_sync_job_status
    import capo_kendra.types.index_id
    import capo_kendra.types.max_results_integer_for_list_data_source_sync_jobs_request
    import capo_kendra.types.next_token
    import capo_kendra.types.time_range


class ListDataSourceSyncJobsRequest(TypedDict, closed=True):
    id: "capo_kendra.types.data_source_id.DataSourceId"
    """<p>The identifier of the data source connector.</p>"""
    index_id: "capo_kendra.types.index_id.IndexId"
    """<p>The identifier of the index used with the data source connector.</p>"""
    next_token: NotRequired["capo_kendra.types.next_token.NextToken"]
    """<p>If the previous response was incomplete (because there is more data to retrieve), Amazon Kendra returns a pagination token in the response. You can use this pagination token to retrieve the next set of jobs.</p>"""
    max_results: NotRequired[
        "capo_kendra.types.max_results_integer_for_list_data_source_sync_jobs_request.MaxResultsIntegerForListDataSourceSyncJobsRequest"
    ]
    """<p>The maximum number of synchronization jobs to return in the response. If there are fewer results in the list, this response contains only the actual results.</p>"""
    start_time_filter: NotRequired["capo_kendra.types.time_range.TimeRange"]
    """<p>When specified, the synchronization jobs returned in the list are limited to jobs between the specified dates.</p>"""
    status_filter: NotRequired[
        "capo_kendra.types.data_source_sync_job_status.DataSourceSyncJobStatus"
    ]
    """<p>Only returns synchronization jobs with the <code>Status</code> field equal to the specified status.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDataSourceSyncJobsRequest) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    out["IndexId"] = value["index_id"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "start_time_filter" in value:
        import capo_kendra.types.time_range

        out["StartTimeFilter"] = capo_kendra.types.time_range.serialize_aws_json_1_1(
            value["start_time_filter"]
        )
    if "status_filter" in value:
        import capo_kendra.types.data_source_sync_job_status

        out["StatusFilter"] = (
            capo_kendra.types.data_source_sync_job_status.serialize_aws_json_1_1(
                value["status_filter"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDataSourceSyncJobsRequest:
    out: ListDataSourceSyncJobsRequest = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = ""
    if data.get("IndexId") is not None:
        out["index_id"] = data["IndexId"]
    else:
        out["index_id"] = ""
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("StartTimeFilter") is not None:
        import capo_kendra.types.time_range

        out["start_time_filter"] = (
            capo_kendra.types.time_range.deserialize_aws_json_1_1(
                data["StartTimeFilter"]
            )
        )
    if data.get("StatusFilter") is not None:
        import capo_kendra.types.data_source_sync_job_status

        out["status_filter"] = (
            capo_kendra.types.data_source_sync_job_status.deserialize_aws_json_1_1(
                data["StatusFilter"]
            )
        )
    return out
