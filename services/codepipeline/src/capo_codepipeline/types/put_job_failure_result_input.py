"""Generated from Smithy shape ``com.amazonaws.codepipeline#PutJobFailureResultInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_codepipeline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codepipeline.types.failure_details
    import capo_codepipeline.types.job_id


class PutJobFailureResultInput(TypedDict, closed=True):
    job_id: "capo_codepipeline.types.job_id.JobId"
    """<p>The unique system-generated ID of the job that failed. This is the same ID returned from <code>PollForJobs</code>.</p>"""
    failure_details: "capo_codepipeline.types.failure_details.FailureDetails"
    """<p>The details about the failure of a job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutJobFailureResultInput) -> dict:
    out: dict = {}
    out["jobId"] = value["job_id"]
    import capo_codepipeline.types.failure_details

    out["failureDetails"] = (
        capo_codepipeline.types.failure_details.serialize_aws_json_1_1(
            value["failure_details"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutJobFailureResultInput:
    out: PutJobFailureResultInput = {}  # type: ignore[typeddict-item]
    if data.get("jobId") is not None:
        out["job_id"] = data["jobId"]
    else:
        out["job_id"] = ""
    if data.get("failureDetails") is not None:
        import capo_codepipeline.types.failure_details

        out["failure_details"] = (
            capo_codepipeline.types.failure_details.deserialize_aws_json_1_1(
                data["failureDetails"]
            )
        )
    else:
        raise DeserializationError("PutJobFailureResultInput.failure_details required")
    return out
