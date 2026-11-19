"""Generated from Smithy shape ``com.amazonaws.translate#StartTextTranslationJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_translate.types.job_id
    import capo_translate.types.job_status


class StartTextTranslationJobResponse(TypedDict, closed=True):
    job_id: NotRequired["capo_translate.types.job_id.JobId"]
    """<p>The identifier generated for the job. To get the status of a job, use this ID with the <a>DescribeTextTranslationJob</a> operation.</p>"""
    job_status: NotRequired["capo_translate.types.job_status.JobStatus"]
    """<p>The status of the job. Possible values include:</p> <ul> <li> <p> <code>SUBMITTED</code> - The job has been received and is queued for processing.</p> </li> <li> <p> <code>IN_PROGRESS</code> - Amazon Translate is processing the job.</p> </li> <li> <p> <code>COMPLETED</code> - The job was successfully completed and the output is available.</p> </li> <li> <p> <code>COMPLETED_WITH_ERROR</code> - The job was completed with errors. The errors can be analyzed in the job's output.</p> </li> <li> <p> <code>FAILED</code> - The job did not complete. To get details, use the <a>DescribeTextTranslationJob</a> operation.</p> </li> <li> <p> <code>STOP_REQUESTED</code> - The user who started the job has requested that it be stopped.</p> </li> <li> <p> <code>STOPPED</code> - The job has been stopped.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartTextTranslationJobResponse) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["JobId"] = value["job_id"]
    if "job_status" in value:
        import capo_translate.types.job_status

        out["JobStatus"] = capo_translate.types.job_status.serialize_aws_json_1_1(
            value["job_status"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartTextTranslationJobResponse:
    out: StartTextTranslationJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("JobId") is not None:
        out["job_id"] = data["JobId"]
    if data.get("JobStatus") is not None:
        import capo_translate.types.job_status

        out["job_status"] = capo_translate.types.job_status.deserialize_aws_json_1_1(
            data["JobStatus"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StartTextTranslationJobResponse) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["JobId"] = value["job_id"]
    if "job_status" in value:
        import capo_translate.types.job_status

        out["JobStatus"] = capo_translate.types.job_status.serialize_cbor(
            value["job_status"]
        )
    return out


def deserialize_cbor(data: dict) -> StartTextTranslationJobResponse:
    out: StartTextTranslationJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("JobId") is not None:
        out["job_id"] = data["JobId"]
    if data.get("JobStatus") is not None:
        import capo_translate.types.job_status

        out["job_status"] = capo_translate.types.job_status.deserialize_cbor(
            data["JobStatus"]
        )
    return out
