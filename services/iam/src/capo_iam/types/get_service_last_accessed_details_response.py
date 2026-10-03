"""Generated from Smithy shape ``com.amazonaws.iam#GetServiceLastAccessedDetailsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element
from capo_iam.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iam.types.access_advisor_usage_granularity_type
    import capo_iam.types.boolean_type
    import capo_iam.types.date_type
    import capo_iam.types.error_details
    import capo_iam.types.job_status_type
    import capo_iam.types.response_marker_type
    import capo_iam.types.services_last_accessed


class GetServiceLastAccessedDetailsResponse(TypedDict, closed=True):
    job_status: "capo_iam.types.job_status_type.jobStatusType"
    """<p>The status of the job.</p>"""
    job_type: NotRequired[
        "capo_iam.types.access_advisor_usage_granularity_type.AccessAdvisorUsageGranularityType"
    ]
    """<p>The type of job. Service jobs return information about when each service was last accessed. Action jobs also include information about when tracked actions within the service were last accessed.</p>"""
    job_creation_date: "capo_iam.types.date_type.dateType"
    """<p>The date and time, in <a href="http://www.iso.org/iso/iso8601">ISO 8601 date-time format</a>, when the report job was created.</p>"""
    services_last_accessed: "capo_iam.types.services_last_accessed.ServicesLastAccessed"
    """<p> A <code>ServiceLastAccessed</code> object that contains details about the most recent attempt to access the service.</p>"""
    job_completion_date: "capo_iam.types.date_type.dateType"
    """<p>The date and time, in <a href="http://www.iso.org/iso/iso8601">ISO 8601 date-time format</a>, when the generated report job was completed or failed.</p> <p>This field is null if the job is still in progress, as indicated by a job status value of <code>IN_PROGRESS</code>.</p>"""
    is_truncated: "capo_iam.types.boolean_type.booleanType"
    """<p>A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent pagination request using the <code>Marker</code> request parameter to retrieve more items. Note that IAM might return fewer than the <code>MaxItems</code> number of results even when there are more results available. We recommend that you check <code>IsTruncated</code> after every call to ensure that you receive all your results.</p>"""
    marker: NotRequired["capo_iam.types.response_marker_type.responseMarkerType"]
    """<p>When <code>IsTruncated</code> is <code>true</code>, this element is present and contains the value to use for the <code>Marker</code> parameter in a subsequent pagination request.</p>"""
    error: NotRequired["capo_iam.types.error_details.ErrorDetails"]
    """<p>An object that contains details about the reason the operation failed.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetServiceLastAccessedDetailsResponse,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    import capo_iam.types.job_status_type

    capo_iam.types.job_status_type.serialize_query(
        value["job_status"], pairs, f"{key_prefix}JobStatus"
    )
    if "job_type" in value:
        import capo_iam.types.access_advisor_usage_granularity_type

        capo_iam.types.access_advisor_usage_granularity_type.serialize_query(
            value["job_type"], pairs, f"{key_prefix}JobType"
        )
    import capo_iam.types.date_type

    capo_iam.types.date_type.serialize_query(
        value["job_creation_date"], pairs, f"{key_prefix}JobCreationDate"
    )
    import capo_iam.types.services_last_accessed

    capo_iam.types.services_last_accessed.serialize_query(
        value["services_last_accessed"], pairs, f"{key_prefix}ServicesLastAccessed"
    )
    import capo_iam.types.date_type

    capo_iam.types.date_type.serialize_query(
        value["job_completion_date"], pairs, f"{key_prefix}JobCompletionDate"
    )
    pairs.append(
        (
            f"{key_prefix}IsTruncated",
            "true" if value.get("is_truncated", False) else "false",
        )
    )
    if "marker" in value:
        pairs.append((f"{key_prefix}Marker", str(value["marker"])))
    if "error" in value:
        import capo_iam.types.error_details

        capo_iam.types.error_details.serialize_query(
            value["error"], pairs, f"{key_prefix}Error"
        )


def deserialize_query(el: Element) -> GetServiceLastAccessedDetailsResponse:
    out: GetServiceLastAccessedDetailsResponse = {}  # type: ignore[typeddict-item]
    child_job_status = el.find("JobStatus")
    if child_job_status is not None:
        import capo_iam.types.job_status_type

        out["job_status"] = capo_iam.types.job_status_type.deserialize_query(
            child_job_status
        )
    else:
        raise DeserializationError(
            "GetServiceLastAccessedDetailsResponse.job_status required"
        )
    child_job_type = el.find("JobType")
    if child_job_type is not None:
        import capo_iam.types.access_advisor_usage_granularity_type

        out["job_type"] = (
            capo_iam.types.access_advisor_usage_granularity_type.deserialize_query(
                child_job_type
            )
        )
    child_job_creation_date = el.find("JobCreationDate")
    if child_job_creation_date is not None:
        import capo_iam.types.date_type

        out["job_creation_date"] = capo_iam.types.date_type.deserialize_query(
            child_job_creation_date
        )
    else:
        raise DeserializationError(
            "GetServiceLastAccessedDetailsResponse.job_creation_date required"
        )
    child_services_last_accessed = el.find("ServicesLastAccessed")
    if child_services_last_accessed is not None:
        import capo_iam.types.services_last_accessed

        out["services_last_accessed"] = (
            capo_iam.types.services_last_accessed.deserialize_query(
                child_services_last_accessed
            )
        )
    else:
        raise DeserializationError(
            "GetServiceLastAccessedDetailsResponse.services_last_accessed required"
        )
    child_job_completion_date = el.find("JobCompletionDate")
    if child_job_completion_date is not None:
        import capo_iam.types.date_type

        out["job_completion_date"] = capo_iam.types.date_type.deserialize_query(
            child_job_completion_date
        )
    else:
        raise DeserializationError(
            "GetServiceLastAccessedDetailsResponse.job_completion_date required"
        )
    child_is_truncated = el.find("IsTruncated")
    if child_is_truncated is not None:
        out["is_truncated"] = (child_is_truncated.text or "").lower() == "true"
    else:
        out["is_truncated"] = False
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_error = el.find("Error")
    if child_error is not None:
        import capo_iam.types.error_details

        out["error"] = capo_iam.types.error_details.deserialize_query(child_error)
    return out
