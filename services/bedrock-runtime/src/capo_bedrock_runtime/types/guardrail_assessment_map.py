"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailAssessmentMap``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.guardrail_assessment

GuardrailAssessmentMap: TypeAlias = dict[
    "str", "capo_bedrock_runtime.types.guardrail_assessment.GuardrailAssessment"
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: GuardrailAssessmentMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_bedrock_runtime.types.guardrail_assessment

        out[key] = capo_bedrock_runtime.types.guardrail_assessment.serialize_json(value)
    return out


def deserialize_json(data: dict) -> GuardrailAssessmentMap:
    out: GuardrailAssessmentMap = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_bedrock_runtime.types.guardrail_assessment

        out[key] = capo_bedrock_runtime.types.guardrail_assessment.deserialize_json(
            value
        )
    return out


def redact_sensitive(value: GuardrailAssessmentMap) -> dict[str, Any]:
    import capo_bedrock_runtime.types.guardrail_assessment

    return {
        key: capo_bedrock_runtime.types.guardrail_assessment.redact_sensitive(item)
        for key, item in value.items()
    }
