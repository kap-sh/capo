"""Generated from Smithy shape ``com.amazonaws.bedrock#BatchDeleteEvaluationJobItems``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.batch_delete_evaluation_job_item

BatchDeleteEvaluationJobItems: TypeAlias = list[
    "capo_bedrock.types.batch_delete_evaluation_job_item.BatchDeleteEvaluationJobItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteEvaluationJobItems) -> list:
    import capo_bedrock.types.batch_delete_evaluation_job_item

    out: list = []
    for item in value:
        out.append(
            capo_bedrock.types.batch_delete_evaluation_job_item.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> BatchDeleteEvaluationJobItems:
    import capo_bedrock.types.batch_delete_evaluation_job_item

    out: BatchDeleteEvaluationJobItems = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock.types.batch_delete_evaluation_job_item.deserialize_json(item)
        )
    return out


def redact_sensitive(value: BatchDeleteEvaluationJobItems) -> list[Any]:
    import capo_bedrock.types.batch_delete_evaluation_job_item

    return [
        capo_bedrock.types.batch_delete_evaluation_job_item.redact_sensitive(item)
        for item in value
    ]
