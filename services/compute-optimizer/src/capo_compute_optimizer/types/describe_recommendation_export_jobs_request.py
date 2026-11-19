"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#DescribeRecommendationExportJobsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.job_filters
    import capo_compute_optimizer.types.job_ids
    import capo_compute_optimizer.types.max_results
    import capo_compute_optimizer.types.next_token


class DescribeRecommendationExportJobsRequest(TypedDict, closed=True):
    job_ids: NotRequired["capo_compute_optimizer.types.job_ids.JobIds"]
    """<p>The identification numbers of the export jobs to return.</p> <p>An export job ID is returned when you create an export using the <a>ExportAutoScalingGroupRecommendations</a> or <a>ExportEC2InstanceRecommendations</a> actions.</p> <p>All export jobs created in the last seven days are returned if this parameter is omitted.</p>"""
    filters: NotRequired["capo_compute_optimizer.types.job_filters.JobFilters"]
    """<p>An array of objects to specify a filter that returns a more specific list of export jobs.</p>"""
    next_token: NotRequired["capo_compute_optimizer.types.next_token.NextToken"]
    """<p>The token to advance to the next page of export jobs.</p>"""
    max_results: NotRequired["capo_compute_optimizer.types.max_results.MaxResults"]
    """<p>The maximum number of export jobs to return with a single request.</p> <p>To retrieve the remaining results, make another request with the returned <code>nextToken</code> value.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeRecommendationExportJobsRequest) -> dict:
    out: dict = {}
    if "job_ids" in value:
        import capo_compute_optimizer.types.job_ids

        out["jobIds"] = capo_compute_optimizer.types.job_ids.serialize_aws_json_1_0(
            value["job_ids"]
        )
    if "filters" in value:
        import capo_compute_optimizer.types.job_filters

        out["filters"] = (
            capo_compute_optimizer.types.job_filters.serialize_aws_json_1_0(
                value["filters"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeRecommendationExportJobsRequest:
    out: DescribeRecommendationExportJobsRequest = {}  # type: ignore[typeddict-item]
    if data.get("jobIds") is not None:
        import capo_compute_optimizer.types.job_ids

        out["job_ids"] = capo_compute_optimizer.types.job_ids.deserialize_aws_json_1_0(
            data["jobIds"]
        )
    if data.get("filters") is not None:
        import capo_compute_optimizer.types.job_filters

        out["filters"] = (
            capo_compute_optimizer.types.job_filters.deserialize_aws_json_1_0(
                data["filters"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeRecommendationExportJobsRequest) -> dict:
    out: dict = {}
    if "job_ids" in value:
        import capo_compute_optimizer.types.job_ids

        out["jobIds"] = capo_compute_optimizer.types.job_ids.serialize_cbor(
            value["job_ids"]
        )
    if "filters" in value:
        import capo_compute_optimizer.types.job_filters

        out["filters"] = capo_compute_optimizer.types.job_filters.serialize_cbor(
            value["filters"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_cbor(data: dict) -> DescribeRecommendationExportJobsRequest:
    out: DescribeRecommendationExportJobsRequest = {}  # type: ignore[typeddict-item]
    if data.get("jobIds") is not None:
        import capo_compute_optimizer.types.job_ids

        out["job_ids"] = capo_compute_optimizer.types.job_ids.deserialize_cbor(
            data["jobIds"]
        )
    if data.get("filters") is not None:
        import capo_compute_optimizer.types.job_filters

        out["filters"] = capo_compute_optimizer.types.job_filters.deserialize_cbor(
            data["filters"]
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    return out
