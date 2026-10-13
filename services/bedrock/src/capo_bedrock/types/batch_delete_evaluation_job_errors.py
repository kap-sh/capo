"""Generated from Smithy shape ``com.amazonaws.bedrock#BatchDeleteEvaluationJobErrors``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.batch_delete_evaluation_job_error

BatchDeleteEvaluationJobErrors: TypeAlias = list[
    "capo_bedrock.types.batch_delete_evaluation_job_error.BatchDeleteEvaluationJobError"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteEvaluationJobErrors) -> list:
    import capo_bedrock.types.batch_delete_evaluation_job_error

    out: list = []
    for item in value:
        out.append(
            capo_bedrock.types.batch_delete_evaluation_job_error.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> BatchDeleteEvaluationJobErrors:
    import capo_bedrock.types.batch_delete_evaluation_job_error

    out: BatchDeleteEvaluationJobErrors = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock.types.batch_delete_evaluation_job_error.deserialize_json(item)
        )
    return out


def redact_sensitive(value: BatchDeleteEvaluationJobErrors) -> list[Any]:
    import capo_bedrock.types.batch_delete_evaluation_job_error

    return [
        capo_bedrock.types.batch_delete_evaluation_job_error.redact_sensitive(item)
        for item in value
    ]
