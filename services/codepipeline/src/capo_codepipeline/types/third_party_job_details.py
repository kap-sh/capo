"""Generated from Smithy shape ``com.amazonaws.codepipeline#ThirdPartyJobDetails``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.nonce
    import capo_codepipeline.types.third_party_job_data
    import capo_codepipeline.types.third_party_job_id


class ThirdPartyJobDetails(TypedDict, closed=True):
    id: NotRequired["capo_codepipeline.types.third_party_job_id.ThirdPartyJobId"]
    """<p>The identifier used to identify the job details in CodePipeline.</p>"""
    data: NotRequired["capo_codepipeline.types.third_party_job_data.ThirdPartyJobData"]
    """<p>The data to be returned by the third party job worker.</p>"""
    nonce: NotRequired["capo_codepipeline.types.nonce.Nonce"]
    """<p>A system-generated random number that CodePipeline uses to ensure that the job is being worked on by only one job worker. Use this number in an <a>AcknowledgeThirdPartyJob</a> request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ThirdPartyJobDetails) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "data" in value:
        import capo_codepipeline.types.third_party_job_data

        out["data"] = (
            capo_codepipeline.types.third_party_job_data.serialize_aws_json_1_1(
                value["data"]
            )
        )
    if "nonce" in value:
        out["nonce"] = value["nonce"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ThirdPartyJobDetails:
    out: ThirdPartyJobDetails = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("data") is not None:
        import capo_codepipeline.types.third_party_job_data

        out["data"] = (
            capo_codepipeline.types.third_party_job_data.deserialize_aws_json_1_1(
                data["data"]
            )
        )
    if data.get("nonce") is not None:
        out["nonce"] = data["nonce"]
    return out


def redact_sensitive(value: ThirdPartyJobDetails) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "data" in value:
        import capo_codepipeline.types.third_party_job_data

        out["data"] = capo_codepipeline.types.third_party_job_data.redact_sensitive(
            value["data"]
        )
    return out
