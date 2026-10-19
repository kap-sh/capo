"""Generated from Smithy shape ``com.amazonaws.codepipeline#PutThirdPartyJobFailureResultInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_codepipeline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codepipeline.types.client_token
    import capo_codepipeline.types.failure_details
    import capo_codepipeline.types.third_party_job_id


class PutThirdPartyJobFailureResultInput(TypedDict, closed=True):
    job_id: "capo_codepipeline.types.third_party_job_id.ThirdPartyJobId"
    """<p>The ID of the job that failed. This is the same ID returned from <code>PollForThirdPartyJobs</code>.</p>"""
    client_token: "capo_codepipeline.types.client_token.ClientToken"
    """<p>The clientToken portion of the clientId and clientToken pair used to verify that the calling entity is allowed access to the job and its details.</p>"""
    failure_details: "capo_codepipeline.types.failure_details.FailureDetails"
    """<p>Represents information about failure details.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutThirdPartyJobFailureResultInput) -> dict:
    out: dict = {}
    out["jobId"] = value["job_id"]
    out["clientToken"] = value["client_token"]
    import capo_codepipeline.types.failure_details

    out["failureDetails"] = (
        capo_codepipeline.types.failure_details.serialize_aws_json_1_1(
            value["failure_details"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutThirdPartyJobFailureResultInput:
    out: PutThirdPartyJobFailureResultInput = {}  # type: ignore[typeddict-item]
    if data.get("jobId") is not None:
        out["job_id"] = data["jobId"]
    else:
        out["job_id"] = ""
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    else:
        out["client_token"] = ""
    if data.get("failureDetails") is not None:
        import capo_codepipeline.types.failure_details

        out["failure_details"] = (
            capo_codepipeline.types.failure_details.deserialize_aws_json_1_1(
                data["failureDetails"]
            )
        )
    else:
        raise DeserializationError(
            "PutThirdPartyJobFailureResultInput.failure_details required"
        )
    return out
