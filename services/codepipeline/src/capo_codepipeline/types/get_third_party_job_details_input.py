"""Generated from Smithy shape ``com.amazonaws.codepipeline#GetThirdPartyJobDetailsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.client_token
    import capo_codepipeline.types.third_party_job_id


class GetThirdPartyJobDetailsInput(TypedDict, closed=True):
    job_id: "capo_codepipeline.types.third_party_job_id.ThirdPartyJobId"
    """<p>The unique system-generated ID used for identifying the job.</p>"""
    client_token: "capo_codepipeline.types.client_token.ClientToken"
    """<p>The clientToken portion of the clientId and clientToken pair used to verify that the calling entity is allowed access to the job and its details.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetThirdPartyJobDetailsInput) -> dict:
    out: dict = {}
    out["jobId"] = value["job_id"]
    out["clientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetThirdPartyJobDetailsInput:
    out: GetThirdPartyJobDetailsInput = {}  # type: ignore[typeddict-item]
    if data.get("jobId") is not None:
        out["job_id"] = data["jobId"]
    else:
        out["job_id"] = ""
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    else:
        out["client_token"] = ""
    return out
