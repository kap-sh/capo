"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailAssessmentList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.guardrail_assessment

GuardrailAssessmentList: TypeAlias = list[
    "capo_bedrock_runtime.types.guardrail_assessment.GuardrailAssessment"
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailAssessmentList) -> list:
    import capo_bedrock_runtime.types.guardrail_assessment

    out: list = []
    for item in value:
        out.append(capo_bedrock_runtime.types.guardrail_assessment.serialize_json(item))
    return out


def deserialize_json(data: list) -> GuardrailAssessmentList:
    import capo_bedrock_runtime.types.guardrail_assessment

    out: GuardrailAssessmentList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_runtime.types.guardrail_assessment.deserialize_json(item)
        )
    return out


def redact_sensitive(value: GuardrailAssessmentList) -> list[Any]:
    import capo_bedrock_runtime.types.guardrail_assessment

    return [
        capo_bedrock_runtime.types.guardrail_assessment.redact_sensitive(item)
        for item in value
    ]
