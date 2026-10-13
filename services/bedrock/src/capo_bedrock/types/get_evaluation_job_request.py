"""Generated from Smithy shape ``com.amazonaws.bedrock#GetEvaluationJobRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.evaluation_job_identifier


class GetEvaluationJobRequest(TypedDict, closed=True):
    job_identifier: (
        "capo_bedrock.types.evaluation_job_identifier.EvaluationJobIdentifier"
    )
    """<p>The Amazon Resource Name (ARN) of the evaluation job you want get information on.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEvaluationJobRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetEvaluationJobRequest:
    out: GetEvaluationJobRequest = {}  # type: ignore[typeddict-item]
    return out


def redact_sensitive(value: GetEvaluationJobRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "job_identifier" in value:
        out["job_identifier"] = "*** Sensitive Data Redacted ***"
    return out
