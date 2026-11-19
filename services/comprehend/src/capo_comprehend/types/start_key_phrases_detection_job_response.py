"""Generated from Smithy shape ``com.amazonaws.comprehend#StartKeyPhrasesDetectionJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.comprehend_arn
    import capo_comprehend.types.job_id
    import capo_comprehend.types.job_status


class StartKeyPhrasesDetectionJobResponse(TypedDict, closed=True):
    job_id: NotRequired["capo_comprehend.types.job_id.JobId"]
    """<p>The identifier generated for the job. To get the status of a job, use this identifier with the operation.</p>"""
    job_arn: NotRequired["capo_comprehend.types.comprehend_arn.ComprehendArn"]
    """<p>The Amazon Resource Name (ARN) of the key phrase detection job. It is a unique, fully qualified identifier for the job. It includes the Amazon Web Services account, Amazon Web Services Region, and the job ID. The format of the ARN is as follows:</p> <p> <code>arn:<partition>:comprehend:<region>:<account-id>:key-phrases-detection-job/<job-id></code> </p> <p>The following is an example job ARN:</p> <p> <code>arn:aws:comprehend:us-west-2:111122223333:key-phrases-detection-job/1234abcd12ab34cd56ef1234567890ab</code> </p>"""
    job_status: NotRequired["capo_comprehend.types.job_status.JobStatus"]
    """<p>The status of the job. </p> <ul> <li> <p>SUBMITTED - The job has been received and is queued for processing.</p> </li> <li> <p>IN_PROGRESS - Amazon Comprehend is processing the job.</p> </li> <li> <p>COMPLETED - The job was successfully completed and the output is available.</p> </li> <li> <p>FAILED - The job did not complete. To get details, use the operation.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartKeyPhrasesDetectionJobResponse) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["JobId"] = value["job_id"]
    if "job_arn" in value:
        out["JobArn"] = value["job_arn"]
    if "job_status" in value:
        import capo_comprehend.types.job_status

        out["JobStatus"] = capo_comprehend.types.job_status.serialize_aws_json_1_1(
            value["job_status"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartKeyPhrasesDetectionJobResponse:
    out: StartKeyPhrasesDetectionJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("JobId") is not None:
        out["job_id"] = data["JobId"]
    if data.get("JobArn") is not None:
        out["job_arn"] = data["JobArn"]
    if data.get("JobStatus") is not None:
        import capo_comprehend.types.job_status

        out["job_status"] = capo_comprehend.types.job_status.deserialize_aws_json_1_1(
            data["JobStatus"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StartKeyPhrasesDetectionJobResponse) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["JobId"] = value["job_id"]
    if "job_arn" in value:
        out["JobArn"] = value["job_arn"]
    if "job_status" in value:
        import capo_comprehend.types.job_status

        out["JobStatus"] = capo_comprehend.types.job_status.serialize_cbor(
            value["job_status"]
        )
    return out


def deserialize_cbor(data: dict) -> StartKeyPhrasesDetectionJobResponse:
    out: StartKeyPhrasesDetectionJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("JobId") is not None:
        out["job_id"] = data["JobId"]
    if data.get("JobArn") is not None:
        out["job_arn"] = data["JobArn"]
    if data.get("JobStatus") is not None:
        import capo_comprehend.types.job_status

        out["job_status"] = capo_comprehend.types.job_status.deserialize_cbor(
            data["JobStatus"]
        )
    return out
