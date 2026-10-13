"""Generated from Smithy shape ``com.amazonaws.customerprofiles#GetUploadJobResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.expiration_days_integer
    import capo_customer_profiles.types.field_map
    import capo_customer_profiles.types.results_summary
    import capo_customer_profiles.types.status_reason
    import capo_customer_profiles.types.string1_to255
    import capo_customer_profiles.types.text
    import capo_customer_profiles.types.timestamp
    import capo_customer_profiles.types.upload_job_status
    import capo_customer_profiles.types.uuid


class GetUploadJobResponse(TypedDict, closed=True):
    job_id: NotRequired["capo_customer_profiles.types.uuid.uuid"]
    """<p>The unique identifier of the upload job. </p>"""
    display_name: NotRequired["capo_customer_profiles.types.string1_to255.string1To255"]
    """<p>The unique name of the upload job. Could be a file name to identify the upload job. </p>"""
    status: NotRequired[
        "capo_customer_profiles.types.upload_job_status.UploadJobStatus"
    ]
    """<p>The status describing the status for the upload job. The following are Valid Values: </p> <ul> <li> <p> <b>CREATED</b>: The upload job has been created, but has not started processing yet. </p> </li> <li> <p> <b>IN_PROGRESS</b>: The upload job is currently in progress, ingesting and processing the profile data. </p> </li> <li> <p> <b>PARTIALLY_SUCCEEDED</b>: The upload job has successfully completed the ingestion and processing of all profile data. </p> </li> <li> <p> <b>SUCCEEDED</b>: The upload job has successfully completed the ingestion and processing of all profile data. </p> </li> <li> <p> <b>FAILED</b>: The upload job has failed to complete. </p> </li> <li> <p> <b>STOPPED</b>: The upload job has been manually stopped or terminated before completion. </p> </li> </ul>"""
    status_reason: NotRequired[
        "capo_customer_profiles.types.status_reason.StatusReason"
    ]
    """<p>The reason for the current status of the upload job. Possible reasons: </p> <ul> <li> <p> <b>VALIDATION_FAILURE</b>: The upload job has encountered an error or issue and was unable to complete the profile data ingestion. </p> </li> <li> <p> <b>INTERNAL_FAILURE</b>: Failure caused from service side </p> </li> </ul>"""
    created_at: NotRequired["capo_customer_profiles.types.timestamp.timestamp"]
    """<p>The timestamp when the upload job was created. </p>"""
    completed_at: NotRequired["capo_customer_profiles.types.timestamp.timestamp"]
    """<p>The timestamp when the upload job was completed. </p>"""
    fields: NotRequired["capo_customer_profiles.types.field_map.FieldMap"]
    """<p>The mapping between CSV Columns and Profile Object attributes for the upload job. </p>"""
    unique_key: NotRequired["capo_customer_profiles.types.text.text"]
    """<p>The unique key columns used for de-duping the keys in the upload job. </p>"""
    results_summary: NotRequired[
        "capo_customer_profiles.types.results_summary.ResultsSummary"
    ]
    """<p>The summary of results for the upload job, including the number of updated, created, and failed records. </p>"""
    data_expiry: NotRequired[
        "capo_customer_profiles.types.expiration_days_integer.expirationDaysInteger"
    ]
    """<p>The expiry duration for the profiles ingested with the upload job. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetUploadJobResponse) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["JobId"] = value["job_id"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "status" in value:
        import capo_customer_profiles.types.upload_job_status

        out["Status"] = capo_customer_profiles.types.upload_job_status.serialize_json(
            value["status"]
        )
    if "status_reason" in value:
        import capo_customer_profiles.types.status_reason

        out["StatusReason"] = capo_customer_profiles.types.status_reason.serialize_json(
            value["status_reason"]
        )
    if "created_at" in value:
        import capo_customer_profiles.types.timestamp

        out["CreatedAt"] = capo_customer_profiles.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "completed_at" in value:
        import capo_customer_profiles.types.timestamp

        out["CompletedAt"] = capo_customer_profiles.types.timestamp.serialize_json(
            value["completed_at"]
        )
    if "fields" in value:
        import capo_customer_profiles.types.field_map

        out["Fields"] = capo_customer_profiles.types.field_map.serialize_json(
            value["fields"]
        )
    if "unique_key" in value:
        out["UniqueKey"] = value["unique_key"]
    if "results_summary" in value:
        import capo_customer_profiles.types.results_summary

        out["ResultsSummary"] = (
            capo_customer_profiles.types.results_summary.serialize_json(
                value["results_summary"]
            )
        )
    if "data_expiry" in value:
        out["DataExpiry"] = value["data_expiry"]
    return out


def deserialize_json(data: dict) -> GetUploadJobResponse:
    out: GetUploadJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("JobId") is not None:
        out["job_id"] = data["JobId"]
    if data.get("DisplayName") is not None:
        out["display_name"] = data["DisplayName"]
    if data.get("Status") is not None:
        import capo_customer_profiles.types.upload_job_status

        out["status"] = capo_customer_profiles.types.upload_job_status.deserialize_json(
            data["Status"]
        )
    if data.get("StatusReason") is not None:
        import capo_customer_profiles.types.status_reason

        out["status_reason"] = (
            capo_customer_profiles.types.status_reason.deserialize_json(
                data["StatusReason"]
            )
        )
    if data.get("CreatedAt") is not None:
        import capo_customer_profiles.types.timestamp

        out["created_at"] = capo_customer_profiles.types.timestamp.deserialize_json(
            data["CreatedAt"]
        )
    if data.get("CompletedAt") is not None:
        import capo_customer_profiles.types.timestamp

        out["completed_at"] = capo_customer_profiles.types.timestamp.deserialize_json(
            data["CompletedAt"]
        )
    if data.get("Fields") is not None:
        import capo_customer_profiles.types.field_map

        out["fields"] = capo_customer_profiles.types.field_map.deserialize_json(
            data["Fields"]
        )
    if data.get("UniqueKey") is not None:
        out["unique_key"] = data["UniqueKey"]
    if data.get("ResultsSummary") is not None:
        import capo_customer_profiles.types.results_summary

        out["results_summary"] = (
            capo_customer_profiles.types.results_summary.deserialize_json(
                data["ResultsSummary"]
            )
        )
    if data.get("DataExpiry") is not None:
        out["data_expiry"] = data["DataExpiry"]
    return out


def redact_sensitive(value: GetUploadJobResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "fields" in value:
        out["fields"] = "*** Sensitive Data Redacted ***"
    return out
