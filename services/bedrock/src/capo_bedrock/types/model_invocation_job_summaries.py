"""Generated from Smithy shape ``com.amazonaws.bedrock#ModelInvocationJobSummaries``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.model_invocation_job_summary

ModelInvocationJobSummaries: TypeAlias = list[
    "capo_bedrock.types.model_invocation_job_summary.ModelInvocationJobSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ModelInvocationJobSummaries) -> list:
    import capo_bedrock.types.model_invocation_job_summary

    out: list = []
    for item in value:
        out.append(capo_bedrock.types.model_invocation_job_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ModelInvocationJobSummaries:
    import capo_bedrock.types.model_invocation_job_summary

    out: ModelInvocationJobSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock.types.model_invocation_job_summary.deserialize_json(item)
        )
    return out


def redact_sensitive(value: ModelInvocationJobSummaries) -> list[Any]:
    import capo_bedrock.types.model_invocation_job_summary

    return [
        capo_bedrock.types.model_invocation_job_summary.redact_sensitive(item)
        for item in value
    ]
