"""Generated from Smithy shape ``com.amazonaws.bedrock#BatchDeleteAdvancedPromptOptimizationJobError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.advanced_prompt_optimization_job_identifier


class BatchDeleteAdvancedPromptOptimizationJobError(TypedDict, closed=True):
    job_identifier: "capo_bedrock.types.advanced_prompt_optimization_job_identifier.AdvancedPromptOptimizationJobIdentifier"
    """<p>The identifier of the job that could not be deleted.</p>"""
    code: "str"
    """<p>The error code for the deletion failure.</p>"""
    message: NotRequired["str"]
    """<p>A message describing the error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteAdvancedPromptOptimizationJobError) -> dict:
    out: dict = {}
    out["jobIdentifier"] = value["job_identifier"]
    out["code"] = value["code"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> BatchDeleteAdvancedPromptOptimizationJobError:
    out: BatchDeleteAdvancedPromptOptimizationJobError = {}  # type: ignore[typeddict-item]
    if data.get("jobIdentifier") is not None:
        out["job_identifier"] = data["jobIdentifier"]
    else:
        out["job_identifier"] = ""
    if data.get("code") is not None:
        out["code"] = data["code"]
    else:
        out["code"] = ""
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out
