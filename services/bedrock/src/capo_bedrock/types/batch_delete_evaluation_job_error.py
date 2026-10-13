"""Generated from Smithy shape ``com.amazonaws.bedrock#BatchDeleteEvaluationJobError``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.evaluation_job_identifier


class BatchDeleteEvaluationJobError(TypedDict, closed=True):
    job_identifier: (
        "capo_bedrock.types.evaluation_job_identifier.EvaluationJobIdentifier"
    )
    """<p>The ARN of the evaluation job being deleted.</p>"""
    code: "str"
    """<p>A HTTP status code of the evaluation job being deleted.</p>"""
    message: NotRequired["str"]
    """<p>A status message about the evaluation job deletion.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteEvaluationJobError) -> dict:
    out: dict = {}
    out["jobIdentifier"] = value["job_identifier"]
    out["code"] = value["code"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> BatchDeleteEvaluationJobError:
    out: BatchDeleteEvaluationJobError = {}  # type: ignore[typeddict-item]
    if data.get("jobIdentifier") is not None:
        out["job_identifier"] = data["jobIdentifier"]
    else:
        raise DeserializationError(
            "BatchDeleteEvaluationJobError.job_identifier required"
        )
    if data.get("code") is not None:
        out["code"] = data["code"]
    else:
        raise DeserializationError("BatchDeleteEvaluationJobError.code required")
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


def redact_sensitive(value: BatchDeleteEvaluationJobError) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "job_identifier" in value:
        out["job_identifier"] = "*** Sensitive Data Redacted ***"
    return out
