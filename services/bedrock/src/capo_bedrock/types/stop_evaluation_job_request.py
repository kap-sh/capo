"""Generated from Smithy shape ``com.amazonaws.bedrock#StopEvaluationJobRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.evaluation_job_identifier


class StopEvaluationJobRequest(TypedDict, closed=True):
    job_identifier: (
        "capo_bedrock.types.evaluation_job_identifier.EvaluationJobIdentifier"
    )
    """<p>The Amazon Resource Name (ARN) of the evaluation job you want to stop.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopEvaluationJobRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StopEvaluationJobRequest:
    out: StopEvaluationJobRequest = {}  # type: ignore[typeddict-item]
    return out


def redact_sensitive(value: StopEvaluationJobRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "job_identifier" in value:
        out["job_identifier"] = "*** Sensitive Data Redacted ***"
    return out
