"""Generated from Smithy shape ``com.amazonaws.bedrock#BatchDeleteEvaluationJobItem``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.evaluation_job_identifier
    import capo_bedrock.types.evaluation_job_status


class BatchDeleteEvaluationJobItem(TypedDict, closed=True):
    job_identifier: (
        "capo_bedrock.types.evaluation_job_identifier.EvaluationJobIdentifier"
    )
    """<p>The Amazon Resource Name (ARN) of the evaluation job for deletion.</p>"""
    job_status: "capo_bedrock.types.evaluation_job_status.EvaluationJobStatus"
    """<p>The status of the evaluation job for deletion.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteEvaluationJobItem) -> dict:
    out: dict = {}
    out["jobIdentifier"] = value["job_identifier"]
    import capo_bedrock.types.evaluation_job_status

    out["jobStatus"] = capo_bedrock.types.evaluation_job_status.serialize_json(
        value["job_status"]
    )
    return out


def deserialize_json(data: dict) -> BatchDeleteEvaluationJobItem:
    out: BatchDeleteEvaluationJobItem = {}  # type: ignore[typeddict-item]
    if data.get("jobIdentifier") is not None:
        out["job_identifier"] = data["jobIdentifier"]
    else:
        out["job_identifier"] = ""
    if data.get("jobStatus") is not None:
        import capo_bedrock.types.evaluation_job_status

        out["job_status"] = capo_bedrock.types.evaluation_job_status.deserialize_json(
            data["jobStatus"]
        )
    else:
        import typing

        out["job_status"] = typing.cast(
            "capo_bedrock.types.evaluation_job_status.EvaluationJobStatus", ""
        )
    return out


def redact_sensitive(value: BatchDeleteEvaluationJobItem) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "job_identifier" in value:
        out["job_identifier"] = "*** Sensitive Data Redacted ***"
    return out
