"""Generated from Smithy shape ``com.amazonaws.codepipeline#AcknowledgeJobInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.job_id
    import capo_codepipeline.types.nonce


class AcknowledgeJobInput(TypedDict, closed=True):
    job_id: "capo_codepipeline.types.job_id.JobId"
    """<p>The unique system-generated ID of the job for which you want to confirm receipt.</p>"""
    nonce: "capo_codepipeline.types.nonce.Nonce"
    """<p>A system-generated random number that CodePipeline uses to ensure that the job is being worked on by only one job worker. Get this number from the response of the <a>PollForJobs</a> request that returned this job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AcknowledgeJobInput) -> dict:
    out: dict = {}
    out["jobId"] = value["job_id"]
    out["nonce"] = value["nonce"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AcknowledgeJobInput:
    out: AcknowledgeJobInput = {}  # type: ignore[typeddict-item]
    if data.get("jobId") is not None:
        out["job_id"] = data["jobId"]
    else:
        out["job_id"] = ""
    if data.get("nonce") is not None:
        out["nonce"] = data["nonce"]
    else:
        out["nonce"] = ""
    return out
