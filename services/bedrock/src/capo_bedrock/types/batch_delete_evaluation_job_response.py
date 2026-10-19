"""Generated from Smithy shape ``com.amazonaws.bedrock#BatchDeleteEvaluationJobResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.batch_delete_evaluation_job_errors
    import capo_bedrock.types.batch_delete_evaluation_job_items


class BatchDeleteEvaluationJobResponse(TypedDict, closed=True):
    errors: "capo_bedrock.types.batch_delete_evaluation_job_errors.BatchDeleteEvaluationJobErrors"
    """<p>A JSON object containing the HTTP status codes and the ARNs of evaluation jobs that failed to be deleted.</p>"""
    evaluation_jobs: "capo_bedrock.types.batch_delete_evaluation_job_items.BatchDeleteEvaluationJobItems"
    """<p>The list of evaluation jobs for deletion.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteEvaluationJobResponse) -> dict:
    out: dict = {}
    import capo_bedrock.types.batch_delete_evaluation_job_errors

    out["errors"] = (
        capo_bedrock.types.batch_delete_evaluation_job_errors.serialize_json(
            value["errors"]
        )
    )
    import capo_bedrock.types.batch_delete_evaluation_job_items

    out["evaluationJobs"] = (
        capo_bedrock.types.batch_delete_evaluation_job_items.serialize_json(
            value["evaluation_jobs"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchDeleteEvaluationJobResponse:
    out: BatchDeleteEvaluationJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("errors") is not None:
        import capo_bedrock.types.batch_delete_evaluation_job_errors

        out["errors"] = (
            capo_bedrock.types.batch_delete_evaluation_job_errors.deserialize_json(
                data["errors"]
            )
        )
    else:
        out["errors"] = []
    if data.get("evaluationJobs") is not None:
        import capo_bedrock.types.batch_delete_evaluation_job_items

        out["evaluation_jobs"] = (
            capo_bedrock.types.batch_delete_evaluation_job_items.deserialize_json(
                data["evaluationJobs"]
            )
        )
    else:
        out["evaluation_jobs"] = []
    return out


def redact_sensitive(value: BatchDeleteEvaluationJobResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "errors" in value:
        import capo_bedrock.types.batch_delete_evaluation_job_errors

        out["errors"] = (
            capo_bedrock.types.batch_delete_evaluation_job_errors.redact_sensitive(
                value["errors"]
            )
        )
    if "evaluation_jobs" in value:
        import capo_bedrock.types.batch_delete_evaluation_job_items

        out["evaluation_jobs"] = (
            capo_bedrock.types.batch_delete_evaluation_job_items.redact_sensitive(
                value["evaluation_jobs"]
            )
        )
    return out
