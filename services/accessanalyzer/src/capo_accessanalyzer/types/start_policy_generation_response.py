"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#StartPolicyGenerationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_accessanalyzer.types.job_id


class StartPolicyGenerationResponse(TypedDict, closed=True):
    job_id: "capo_accessanalyzer.types.job_id.JobId"
    """<p>The <code>JobId</code> that is returned by the <code>StartPolicyGeneration</code> operation. The <code>JobId</code> can be used with <code>GetGeneratedPolicy</code> to retrieve the generated policies or used with <code>CancelPolicyGeneration</code> to cancel the policy generation request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartPolicyGenerationResponse) -> dict:
    out: dict = {}
    out["jobId"] = value["job_id"]
    return out


def deserialize_json(data: dict) -> StartPolicyGenerationResponse:
    out: StartPolicyGenerationResponse = {}  # type: ignore[typeddict-item]
    if data.get("jobId") is not None:
        out["job_id"] = data["jobId"]
    else:
        out["job_id"] = ""
    return out
