"""Generated from Smithy shape ``com.amazonaws.iotsitewise#JobSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.id
    import capo_iotsitewise.types.job_status
    import capo_iotsitewise.types.name


class JobSummary(TypedDict, closed=True):
    id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the job.</p>"""
    name: "capo_iotsitewise.types.name.Name"
    """<p>The unique name that helps identify the job request.</p>"""
    status: "capo_iotsitewise.types.job_status.JobStatus"
    """<p>The status of the bulk import job can be one of following values:</p> <ul> <li> <p> <code>PENDING</code> – IoT SiteWise is waiting for the current bulk import job to finish.</p> </li> <li> <p> <code>CANCELLED</code> – The bulk import job has been canceled.</p> </li> <li> <p> <code>RUNNING</code> – IoT SiteWise is processing your request to import your data from Amazon S3.</p> </li> <li> <p> <code>COMPLETED</code> – IoT SiteWise successfully completed your request to import data from Amazon S3.</p> </li> <li> <p> <code>FAILED</code> – IoT SiteWise couldn't process your request to import data from Amazon S3. You can use logs saved in the specified error report location in Amazon S3 to troubleshoot issues.</p> </li> <li> <p> <code>COMPLETED_WITH_FAILURES</code> – IoT SiteWise completed your request to import data from Amazon S3 with errors. You can use logs saved in the specified error report location in Amazon S3 to troubleshoot issues.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobSummary) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["name"] = value["name"]
    import capo_iotsitewise.types.job_status

    out["status"] = capo_iotsitewise.types.job_status.serialize_json(value["status"])
    return out


def deserialize_json(data: dict) -> JobSummary:
    out: JobSummary = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("status") is not None:
        import capo_iotsitewise.types.job_status

        out["status"] = capo_iotsitewise.types.job_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast("capo_iotsitewise.types.job_status.JobStatus", "")
    return out
