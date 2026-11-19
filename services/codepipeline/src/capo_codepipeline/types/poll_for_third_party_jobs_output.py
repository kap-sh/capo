"""Generated from Smithy shape ``com.amazonaws.codepipeline#PollForThirdPartyJobsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.third_party_job_list


class PollForThirdPartyJobsOutput(TypedDict, closed=True):
    jobs: NotRequired["capo_codepipeline.types.third_party_job_list.ThirdPartyJobList"]
    """<p>Information about the jobs to take action on.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PollForThirdPartyJobsOutput) -> dict:
    out: dict = {}
    if "jobs" in value:
        import capo_codepipeline.types.third_party_job_list

        out["jobs"] = (
            capo_codepipeline.types.third_party_job_list.serialize_aws_json_1_1(
                value["jobs"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PollForThirdPartyJobsOutput:
    out: PollForThirdPartyJobsOutput = {}  # type: ignore[typeddict-item]
    if data.get("jobs") is not None:
        import capo_codepipeline.types.third_party_job_list

        out["jobs"] = (
            capo_codepipeline.types.third_party_job_list.deserialize_aws_json_1_1(
                data["jobs"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PollForThirdPartyJobsOutput) -> dict:
    out: dict = {}
    if "jobs" in value:
        import capo_codepipeline.types.third_party_job_list

        out["jobs"] = capo_codepipeline.types.third_party_job_list.serialize_cbor(
            value["jobs"]
        )
    return out


def deserialize_cbor(data: dict) -> PollForThirdPartyJobsOutput:
    out: PollForThirdPartyJobsOutput = {}  # type: ignore[typeddict-item]
    if data.get("jobs") is not None:
        import capo_codepipeline.types.third_party_job_list

        out["jobs"] = capo_codepipeline.types.third_party_job_list.deserialize_cbor(
            data["jobs"]
        )
    return out
