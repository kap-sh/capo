"""Generated from Smithy shape ``com.amazonaws.codepipeline#ThirdPartyJob``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.client_id
    import capo_codepipeline.types.job_id


class ThirdPartyJob(TypedDict, closed=True):
    client_id: NotRequired["capo_codepipeline.types.client_id.ClientId"]
    """<p>The <code>clientToken</code> portion of the <code>clientId</code> and <code>clientToken</code> pair used to verify that the calling entity is allowed access to the job and its details.</p>"""
    job_id: NotRequired["capo_codepipeline.types.job_id.JobId"]
    """<p>The identifier used to identify the job in CodePipeline.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ThirdPartyJob) -> dict:
    out: dict = {}
    if "client_id" in value:
        out["clientId"] = value["client_id"]
    if "job_id" in value:
        out["jobId"] = value["job_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ThirdPartyJob:
    out: ThirdPartyJob = {}  # type: ignore[typeddict-item]
    if data.get("clientId") is not None:
        out["client_id"] = data["clientId"]
    if data.get("jobId") is not None:
        out["job_id"] = data["jobId"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ThirdPartyJob) -> dict:
    out: dict = {}
    if "client_id" in value:
        out["clientId"] = value["client_id"]
    if "job_id" in value:
        out["jobId"] = value["job_id"]
    return out


def deserialize_cbor(data: dict) -> ThirdPartyJob:
    out: ThirdPartyJob = {}  # type: ignore[typeddict-item]
    if data.get("clientId") is not None:
        out["client_id"] = data["clientId"]
    if data.get("jobId") is not None:
        out["job_id"] = data["jobId"]
    return out
