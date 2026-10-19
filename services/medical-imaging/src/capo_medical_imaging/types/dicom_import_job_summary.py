"""Generated from Smithy shape ``com.amazonaws.medicalimaging#DICOMImportJobSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medical_imaging.types.datastore_id
    import capo_medical_imaging.types.date
    import capo_medical_imaging.types.job_id
    import capo_medical_imaging.types.job_name
    import capo_medical_imaging.types.job_status
    import capo_medical_imaging.types.message
    import capo_medical_imaging.types.role_arn


class DICOMImportJobSummary(TypedDict, closed=True):
    job_id: "capo_medical_imaging.types.job_id.JobId"
    """<p>The import job identifier.</p>"""
    job_name: "capo_medical_imaging.types.job_name.JobName"
    """<p>The import job name.</p>"""
    job_status: "capo_medical_imaging.types.job_status.JobStatus"
    """<p>The filters for listing import jobs based on status.</p>"""
    datastore_id: "capo_medical_imaging.types.datastore_id.DatastoreId"
    """<p>The data store identifier.</p>"""
    data_access_role_arn: NotRequired["capo_medical_imaging.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) that grants permissions to access medical imaging resources.</p>"""
    ended_at: NotRequired["capo_medical_imaging.types.date.Date"]
    """<p>The timestamp when an import job ended.</p>"""
    submitted_at: NotRequired["capo_medical_imaging.types.date.Date"]
    """<p>The timestamp when an import job was submitted.</p>"""
    message: NotRequired["capo_medical_imaging.types.message.Message"]
    """<p>The error message thrown if an import job fails.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DICOMImportJobSummary) -> dict:
    out: dict = {}
    out["jobId"] = value["job_id"]
    out["jobName"] = value["job_name"]
    import capo_medical_imaging.types.job_status

    out["jobStatus"] = capo_medical_imaging.types.job_status.serialize_json(
        value["job_status"]
    )
    out["datastoreId"] = value["datastore_id"]
    if "data_access_role_arn" in value:
        out["dataAccessRoleArn"] = value["data_access_role_arn"]
    if "ended_at" in value:
        import capo_medical_imaging.types.date

        out["endedAt"] = capo_medical_imaging.types.date.serialize_json(
            value["ended_at"]
        )
    if "submitted_at" in value:
        import capo_medical_imaging.types.date

        out["submittedAt"] = capo_medical_imaging.types.date.serialize_json(
            value["submitted_at"]
        )
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> DICOMImportJobSummary:
    out: DICOMImportJobSummary = {}  # type: ignore[typeddict-item]
    if data.get("jobId") is not None:
        out["job_id"] = data["jobId"]
    else:
        out["job_id"] = ""
    if data.get("jobName") is not None:
        out["job_name"] = data["jobName"]
    else:
        out["job_name"] = ""
    if data.get("jobStatus") is not None:
        import capo_medical_imaging.types.job_status

        out["job_status"] = capo_medical_imaging.types.job_status.deserialize_json(
            data["jobStatus"]
        )
    else:
        import typing

        out["job_status"] = typing.cast(
            "capo_medical_imaging.types.job_status.JobStatus", ""
        )
    if data.get("datastoreId") is not None:
        out["datastore_id"] = data["datastoreId"]
    else:
        out["datastore_id"] = ""
    if data.get("dataAccessRoleArn") is not None:
        out["data_access_role_arn"] = data["dataAccessRoleArn"]
    if data.get("endedAt") is not None:
        import capo_medical_imaging.types.date

        out["ended_at"] = capo_medical_imaging.types.date.deserialize_json(
            data["endedAt"]
        )
    if data.get("submittedAt") is not None:
        import capo_medical_imaging.types.date

        out["submitted_at"] = capo_medical_imaging.types.date.deserialize_json(
            data["submittedAt"]
        )
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out
