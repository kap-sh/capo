"""Generated from Smithy shape ``com.amazonaws.voiceid#DescribeFraudsterRegistrationJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_voice_id.types.domain_id
    import capo_voice_id.types.job_id


class DescribeFraudsterRegistrationJobRequest(TypedDict, closed=True):
    domain_id: "capo_voice_id.types.domain_id.DomainId"
    """<p>The identifier of the domain that contains the fraudster registration job.</p>"""
    job_id: "capo_voice_id.types.job_id.JobId"
    """<p>The identifier of the fraudster registration job you are describing.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeFraudsterRegistrationJobRequest) -> dict:
    out: dict = {}
    out["DomainId"] = value["domain_id"]
    out["JobId"] = value["job_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeFraudsterRegistrationJobRequest:
    out: DescribeFraudsterRegistrationJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("DomainId") is not None:
        out["domain_id"] = data["DomainId"]
    else:
        out["domain_id"] = ""
    if data.get("JobId") is not None:
        out["job_id"] = data["JobId"]
    else:
        out["job_id"] = ""
    return out
