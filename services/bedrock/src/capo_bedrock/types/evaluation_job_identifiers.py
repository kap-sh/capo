"""Generated from Smithy shape ``com.amazonaws.bedrock#EvaluationJobIdentifiers``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.evaluation_job_identifier

EvaluationJobIdentifiers: TypeAlias = list[
    "capo_bedrock.types.evaluation_job_identifier.EvaluationJobIdentifier"
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationJobIdentifiers) -> list:
    return list(value)


def deserialize_json(data: list) -> EvaluationJobIdentifiers:
    return [item for item in data if item is not None]


def redact_sensitive(value: EvaluationJobIdentifiers) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
