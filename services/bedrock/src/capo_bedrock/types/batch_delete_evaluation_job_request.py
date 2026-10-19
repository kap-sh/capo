"""Generated from Smithy shape ``com.amazonaws.bedrock#BatchDeleteEvaluationJobRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.evaluation_job_identifiers


class BatchDeleteEvaluationJobRequest(TypedDict, closed=True):
    job_identifiers: (
        "capo_bedrock.types.evaluation_job_identifiers.EvaluationJobIdentifiers"
    )
    """<p>A list of one or more evaluation job Amazon Resource Names (ARNs) you want to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteEvaluationJobRequest) -> dict:
    out: dict = {}
    import capo_bedrock.types.evaluation_job_identifiers

    out["jobIdentifiers"] = (
        capo_bedrock.types.evaluation_job_identifiers.serialize_json(
            value["job_identifiers"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchDeleteEvaluationJobRequest:
    out: BatchDeleteEvaluationJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("jobIdentifiers") is not None:
        import capo_bedrock.types.evaluation_job_identifiers

        out["job_identifiers"] = (
            capo_bedrock.types.evaluation_job_identifiers.deserialize_json(
                data["jobIdentifiers"]
            )
        )
    else:
        out["job_identifiers"] = []
    return out


def redact_sensitive(value: BatchDeleteEvaluationJobRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "job_identifiers" in value:
        import capo_bedrock.types.evaluation_job_identifiers

        out["job_identifiers"] = (
            capo_bedrock.types.evaluation_job_identifiers.redact_sensitive(
                value["job_identifiers"]
            )
        )
    return out
