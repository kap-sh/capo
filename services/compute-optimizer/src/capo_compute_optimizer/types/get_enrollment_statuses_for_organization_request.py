"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#GetEnrollmentStatusesForOrganizationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.enrollment_filters
    import capo_compute_optimizer.types.max_results
    import capo_compute_optimizer.types.next_token


class GetEnrollmentStatusesForOrganizationRequest(TypedDict, closed=True):
    filters: NotRequired[
        "capo_compute_optimizer.types.enrollment_filters.EnrollmentFilters"
    ]
    """<p>An array of objects to specify a filter that returns a more specific list of account enrollment statuses.</p>"""
    next_token: NotRequired["capo_compute_optimizer.types.next_token.NextToken"]
    """<p>The token to advance to the next page of account enrollment statuses.</p>"""
    max_results: NotRequired["capo_compute_optimizer.types.max_results.MaxResults"]
    """<p>The maximum number of account enrollment statuses to return with a single request. You can specify up to 100 statuses to return with each request.</p> <p>To retrieve the remaining results, make another request with the returned <code>nextToken</code> value.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetEnrollmentStatusesForOrganizationRequest) -> dict:
    out: dict = {}
    if "filters" in value:
        import capo_compute_optimizer.types.enrollment_filters

        out["filters"] = (
            capo_compute_optimizer.types.enrollment_filters.serialize_aws_json_1_0(
                value["filters"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetEnrollmentStatusesForOrganizationRequest:
    out: GetEnrollmentStatusesForOrganizationRequest = {}  # type: ignore[typeddict-item]
    if data.get("filters") is not None:
        import capo_compute_optimizer.types.enrollment_filters

        out["filters"] = (
            capo_compute_optimizer.types.enrollment_filters.deserialize_aws_json_1_0(
                data["filters"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetEnrollmentStatusesForOrganizationRequest) -> dict:
    out: dict = {}
    if "filters" in value:
        import capo_compute_optimizer.types.enrollment_filters

        out["filters"] = capo_compute_optimizer.types.enrollment_filters.serialize_cbor(
            value["filters"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_cbor(data: dict) -> GetEnrollmentStatusesForOrganizationRequest:
    out: GetEnrollmentStatusesForOrganizationRequest = {}  # type: ignore[typeddict-item]
    if data.get("filters") is not None:
        import capo_compute_optimizer.types.enrollment_filters

        out["filters"] = (
            capo_compute_optimizer.types.enrollment_filters.deserialize_cbor(
                data["filters"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    return out
