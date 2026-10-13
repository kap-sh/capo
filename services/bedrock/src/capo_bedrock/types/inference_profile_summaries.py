"""Generated from Smithy shape ``com.amazonaws.bedrock#InferenceProfileSummaries``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.inference_profile_summary

InferenceProfileSummaries: TypeAlias = list[
    "capo_bedrock.types.inference_profile_summary.InferenceProfileSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: InferenceProfileSummaries) -> list:
    import capo_bedrock.types.inference_profile_summary

    out: list = []
    for item in value:
        out.append(capo_bedrock.types.inference_profile_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> InferenceProfileSummaries:
    import capo_bedrock.types.inference_profile_summary

    out: InferenceProfileSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(capo_bedrock.types.inference_profile_summary.deserialize_json(item))
    return out


def redact_sensitive(value: InferenceProfileSummaries) -> list[Any]:
    import capo_bedrock.types.inference_profile_summary

    return [
        capo_bedrock.types.inference_profile_summary.redact_sensitive(item)
        for item in value
    ]
