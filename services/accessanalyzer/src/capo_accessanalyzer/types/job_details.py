"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#JobDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_accessanalyzer.types.job_error
    import capo_accessanalyzer.types.job_id
    import capo_accessanalyzer.types.job_status
    import capo_accessanalyzer.types.timestamp


class JobDetails(TypedDict, closed=True):
    job_id: "capo_accessanalyzer.types.job_id.JobId"
    """<p>The <code>JobId</code> that is returned by the <code>StartPolicyGeneration</code> operation. The <code>JobId</code> can be used with <code>GetGeneratedPolicy</code> to retrieve the generated policies or used with <code>CancelPolicyGeneration</code> to cancel the policy generation request.</p>"""
    status: "capo_accessanalyzer.types.job_status.JobStatus"
    """<p>The status of the job request.</p>"""
    started_on: "capo_accessanalyzer.types.timestamp.Timestamp"
    """<p>A timestamp of when the job was started.</p>"""
    completed_on: NotRequired["capo_accessanalyzer.types.timestamp.Timestamp"]
    """<p>A timestamp of when the job was completed.</p>"""
    job_error: NotRequired["capo_accessanalyzer.types.job_error.JobError"]
    """<p>The job error for the policy generation request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobDetails) -> dict:
    out: dict = {}
    out["jobId"] = value["job_id"]
    out["status"] = value["status"]
    import capo_accessanalyzer.types.timestamp

    out["startedOn"] = capo_accessanalyzer.types.timestamp.serialize_json(
        value["started_on"]
    )
    if "completed_on" in value:
        import capo_accessanalyzer.types.timestamp

        out["completedOn"] = capo_accessanalyzer.types.timestamp.serialize_json(
            value["completed_on"]
        )
    if "job_error" in value:
        import capo_accessanalyzer.types.job_error

        out["jobError"] = capo_accessanalyzer.types.job_error.serialize_json(
            value["job_error"]
        )
    return out


def deserialize_json(data: dict) -> JobDetails:
    out: JobDetails = {}  # type: ignore[typeddict-item]
    if data.get("jobId") is not None:
        out["job_id"] = data["jobId"]
    else:
        out["job_id"] = ""
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        out["status"] = ""
    if data.get("startedOn") is not None:
        import capo_accessanalyzer.types.timestamp

        out["started_on"] = capo_accessanalyzer.types.timestamp.deserialize_json(
            data["startedOn"]
        )
    else:
        import datetime

        out["started_on"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("completedOn") is not None:
        import capo_accessanalyzer.types.timestamp

        out["completed_on"] = capo_accessanalyzer.types.timestamp.deserialize_json(
            data["completedOn"]
        )
    if data.get("jobError") is not None:
        import capo_accessanalyzer.types.job_error

        out["job_error"] = capo_accessanalyzer.types.job_error.deserialize_json(
            data["jobError"]
        )
    return out
