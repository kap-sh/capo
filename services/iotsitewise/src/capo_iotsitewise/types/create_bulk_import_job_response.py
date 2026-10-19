"""Generated from Smithy shape ``com.amazonaws.iotsitewise#CreateBulkImportJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.bulk_import_job_name
    import capo_iotsitewise.types.id
    import capo_iotsitewise.types.job_status


class CreateBulkImportJobResponse(TypedDict, closed=True):
    job_id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the job.</p>"""
    job_name: "capo_iotsitewise.types.bulk_import_job_name.BulkImportJobName"
    """<p>The unique name that helps identify the job request.</p>"""
    job_status: "capo_iotsitewise.types.job_status.JobStatus"
    """<p>The status of the bulk import job can be one of following values:</p> <ul> <li> <p> <code>PENDING</code> – IoT SiteWise is waiting for the current bulk import job to finish.</p> </li> <li> <p> <code>CANCELLED</code> – The bulk import job has been canceled.</p> </li> <li> <p> <code>RUNNING</code> – IoT SiteWise is processing your request to import your data from Amazon S3.</p> </li> <li> <p> <code>COMPLETED</code> – IoT SiteWise successfully completed your request to import data from Amazon S3.</p> </li> <li> <p> <code>FAILED</code> – IoT SiteWise couldn't process your request to import data from Amazon S3. You can use logs saved in the specified error report location in Amazon S3 to troubleshoot issues.</p> </li> <li> <p> <code>COMPLETED_WITH_FAILURES</code> – IoT SiteWise completed your request to import data from Amazon S3 with errors. You can use logs saved in the specified error report location in Amazon S3 to troubleshoot issues.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateBulkImportJobResponse) -> dict:
    out: dict = {}
    out["jobId"] = value["job_id"]
    out["jobName"] = value["job_name"]
    import capo_iotsitewise.types.job_status

    out["jobStatus"] = capo_iotsitewise.types.job_status.serialize_json(
        value["job_status"]
    )
    return out


def deserialize_json(data: dict) -> CreateBulkImportJobResponse:
    out: CreateBulkImportJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("jobId") is not None:
        out["job_id"] = data["jobId"]
    else:
        out["job_id"] = ""
    if data.get("jobName") is not None:
        out["job_name"] = data["jobName"]
    else:
        out["job_name"] = ""
    if data.get("jobStatus") is not None:
        import capo_iotsitewise.types.job_status

        out["job_status"] = capo_iotsitewise.types.job_status.deserialize_json(
            data["jobStatus"]
        )
    else:
        import typing

        out["job_status"] = typing.cast(
            "capo_iotsitewise.types.job_status.JobStatus", ""
        )
    return out
