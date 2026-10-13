"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#AsyncInvokeSummaries``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.async_invoke_summary

AsyncInvokeSummaries: TypeAlias = list[
    "capo_bedrock_runtime.types.async_invoke_summary.AsyncInvokeSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AsyncInvokeSummaries) -> list:
    import capo_bedrock_runtime.types.async_invoke_summary

    out: list = []
    for item in value:
        out.append(capo_bedrock_runtime.types.async_invoke_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> AsyncInvokeSummaries:
    import capo_bedrock_runtime.types.async_invoke_summary

    out: AsyncInvokeSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_runtime.types.async_invoke_summary.deserialize_json(item)
        )
    return out


def redact_sensitive(value: AsyncInvokeSummaries) -> list[Any]:
    import capo_bedrock_runtime.types.async_invoke_summary

    return [
        capo_bedrock_runtime.types.async_invoke_summary.redact_sensitive(item)
        for item in value
    ]
