"""Generated from Smithy shape ``com.amazonaws.iam#GetOrganizationsAccessReportResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element
from capo_iam.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iam.types.access_details
    import capo_iam.types.boolean_type
    import capo_iam.types.date_type
    import capo_iam.types.error_details
    import capo_iam.types.integer_type
    import capo_iam.types.job_status_type
    import capo_iam.types.marker_type


class GetOrganizationsAccessReportResponse(TypedDict, closed=True):
    job_status: "capo_iam.types.job_status_type.jobStatusType"
    """<p>The status of the job.</p>"""
    job_creation_date: "capo_iam.types.date_type.dateType"
    """<p>The date and time, in <a href="http://www.iso.org/iso/iso8601">ISO 8601 date-time format</a>, when the report job was created.</p>"""
    job_completion_date: NotRequired["capo_iam.types.date_type.dateType"]
    """<p>The date and time, in <a href="http://www.iso.org/iso/iso8601">ISO 8601 date-time format</a>, when the generated report job was completed or failed.</p> <p>This field is null if the job is still in progress, as indicated by a job status value of <code>IN_PROGRESS</code>.</p>"""
    number_of_services_accessible: NotRequired[
        "capo_iam.types.integer_type.integerType"
    ]
    """<p>The number of services that the applicable SCPs allow account principals to access.</p>"""
    number_of_services_not_accessed: NotRequired[
        "capo_iam.types.integer_type.integerType"
    ]
    """<p>The number of services that account principals are allowed but did not attempt to access.</p>"""
    access_details: NotRequired["capo_iam.types.access_details.AccessDetails"]
    """<p>An object that contains details about the most recent attempt to access the service.</p>"""
    is_truncated: "capo_iam.types.boolean_type.booleanType"
    """<p>A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent pagination request using the <code>Marker</code> request parameter to retrieve more items. Note that IAM might return fewer than the <code>MaxItems</code> number of results even when there are more results available. We recommend that you check <code>IsTruncated</code> after every call to ensure that you receive all your results.</p>"""
    marker: NotRequired["capo_iam.types.marker_type.markerType"]
    """<p>When <code>IsTruncated</code> is <code>true</code>, this element is present and contains the value to use for the <code>Marker</code> parameter in a subsequent pagination request.</p>"""
    error_details: NotRequired["capo_iam.types.error_details.ErrorDetails"]


# --- awsQuery ser/de ---
def serialize_query(
    value: GetOrganizationsAccessReportResponse,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    import capo_iam.types.job_status_type

    capo_iam.types.job_status_type.serialize_query(
        value["job_status"], pairs, f"{key_prefix}JobStatus"
    )
    import capo_iam.types.date_type

    capo_iam.types.date_type.serialize_query(
        value["job_creation_date"], pairs, f"{key_prefix}JobCreationDate"
    )
    if "job_completion_date" in value:
        import capo_iam.types.date_type

        capo_iam.types.date_type.serialize_query(
            value["job_completion_date"], pairs, f"{key_prefix}JobCompletionDate"
        )
    if "number_of_services_accessible" in value:
        pairs.append(
            (
                f"{key_prefix}NumberOfServicesAccessible",
                str(value["number_of_services_accessible"]),
            )
        )
    if "number_of_services_not_accessed" in value:
        pairs.append(
            (
                f"{key_prefix}NumberOfServicesNotAccessed",
                str(value["number_of_services_not_accessed"]),
            )
        )
    if "access_details" in value:
        import capo_iam.types.access_details

        capo_iam.types.access_details.serialize_query(
            value["access_details"], pairs, f"{key_prefix}AccessDetails"
        )
    pairs.append(
        (
            f"{key_prefix}IsTruncated",
            "true" if value.get("is_truncated", False) else "false",
        )
    )
    if "marker" in value:
        pairs.append((f"{key_prefix}Marker", str(value["marker"])))
    if "error_details" in value:
        import capo_iam.types.error_details

        capo_iam.types.error_details.serialize_query(
            value["error_details"], pairs, f"{key_prefix}ErrorDetails"
        )


def deserialize_query(el: Element) -> GetOrganizationsAccessReportResponse:
    out: GetOrganizationsAccessReportResponse = {}  # type: ignore[typeddict-item]
    child_job_status = el.find("JobStatus")
    if child_job_status is not None:
        import capo_iam.types.job_status_type

        out["job_status"] = capo_iam.types.job_status_type.deserialize_query(
            child_job_status
        )
    else:
        raise DeserializationError(
            "GetOrganizationsAccessReportResponse.job_status required"
        )
    child_job_creation_date = el.find("JobCreationDate")
    if child_job_creation_date is not None:
        import capo_iam.types.date_type

        out["job_creation_date"] = capo_iam.types.date_type.deserialize_query(
            child_job_creation_date
        )
    else:
        raise DeserializationError(
            "GetOrganizationsAccessReportResponse.job_creation_date required"
        )
    child_job_completion_date = el.find("JobCompletionDate")
    if child_job_completion_date is not None:
        import capo_iam.types.date_type

        out["job_completion_date"] = capo_iam.types.date_type.deserialize_query(
            child_job_completion_date
        )
    child_number_of_services_accessible = el.find("NumberOfServicesAccessible")
    if child_number_of_services_accessible is not None:
        out["number_of_services_accessible"] = int(
            child_number_of_services_accessible.text or ""
        )
    child_number_of_services_not_accessed = el.find("NumberOfServicesNotAccessed")
    if child_number_of_services_not_accessed is not None:
        out["number_of_services_not_accessed"] = int(
            child_number_of_services_not_accessed.text or ""
        )
    child_access_details = el.find("AccessDetails")
    if child_access_details is not None:
        import capo_iam.types.access_details

        out["access_details"] = capo_iam.types.access_details.deserialize_query(
            child_access_details
        )
    child_is_truncated = el.find("IsTruncated")
    if child_is_truncated is not None:
        out["is_truncated"] = (child_is_truncated.text or "").lower() == "true"
    else:
        out["is_truncated"] = False
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_error_details = el.find("ErrorDetails")
    if child_error_details is not None:
        import capo_iam.types.error_details

        out["error_details"] = capo_iam.types.error_details.deserialize_query(
            child_error_details
        )
    return out
