"""Generated from Smithy shape ``com.amazonaws.bedrock#BatchDeleteAdvancedPromptOptimizationJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.advanced_prompt_optimization_job_identifiers


class BatchDeleteAdvancedPromptOptimizationJobRequest(TypedDict, closed=True):
    job_identifiers: "capo_bedrock.types.advanced_prompt_optimization_job_identifiers.AdvancedPromptOptimizationJobIdentifiers"
    """<p>A list of advanced prompt optimization job identifiers (ARNs or IDs) to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteAdvancedPromptOptimizationJobRequest) -> dict:
    out: dict = {}
    import capo_bedrock.types.advanced_prompt_optimization_job_identifiers

    out["jobIdentifiers"] = (
        capo_bedrock.types.advanced_prompt_optimization_job_identifiers.serialize_json(
            value["job_identifiers"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchDeleteAdvancedPromptOptimizationJobRequest:
    out: BatchDeleteAdvancedPromptOptimizationJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("jobIdentifiers") is not None:
        import capo_bedrock.types.advanced_prompt_optimization_job_identifiers

        out["job_identifiers"] = (
            capo_bedrock.types.advanced_prompt_optimization_job_identifiers.deserialize_json(
                data["jobIdentifiers"]
            )
        )
    else:
        out["job_identifiers"] = []
    return out
