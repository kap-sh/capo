"""Generated from Smithy shape ``com.amazonaws.bedrock#BatchDeleteAdvancedPromptOptimizationJobItem``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.advanced_prompt_optimization_job_identifier
    import capo_bedrock.types.advanced_prompt_optimization_job_status


class BatchDeleteAdvancedPromptOptimizationJobItem(TypedDict, closed=True):
    job_identifier: "capo_bedrock.types.advanced_prompt_optimization_job_identifier.AdvancedPromptOptimizationJobIdentifier"
    """<p>The identifier of the deleted job.</p>"""
    job_status: "capo_bedrock.types.advanced_prompt_optimization_job_status.AdvancedPromptOptimizationJobStatus"
    """<p>The status of the deleted job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteAdvancedPromptOptimizationJobItem) -> dict:
    out: dict = {}
    out["jobIdentifier"] = value["job_identifier"]
    import capo_bedrock.types.advanced_prompt_optimization_job_status

    out["jobStatus"] = (
        capo_bedrock.types.advanced_prompt_optimization_job_status.serialize_json(
            value["job_status"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchDeleteAdvancedPromptOptimizationJobItem:
    out: BatchDeleteAdvancedPromptOptimizationJobItem = {}  # type: ignore[typeddict-item]
    if data.get("jobIdentifier") is not None:
        out["job_identifier"] = data["jobIdentifier"]
    else:
        out["job_identifier"] = ""
    if data.get("jobStatus") is not None:
        import capo_bedrock.types.advanced_prompt_optimization_job_status

        out["job_status"] = (
            capo_bedrock.types.advanced_prompt_optimization_job_status.deserialize_json(
                data["jobStatus"]
            )
        )
    else:
        import typing

        out["job_status"] = typing.cast(
            "capo_bedrock.types.advanced_prompt_optimization_job_status.AdvancedPromptOptimizationJobStatus",
            "",
        )
    return out
