"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailAssessmentListMap``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.guardrail_assessment_list

GuardrailAssessmentListMap: TypeAlias = dict[
    "str",
    "capo_bedrock_runtime.types.guardrail_assessment_list.GuardrailAssessmentList",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: GuardrailAssessmentListMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_bedrock_runtime.types.guardrail_assessment_list

        out[key] = capo_bedrock_runtime.types.guardrail_assessment_list.serialize_json(
            value
        )
    return out


def deserialize_json(data: dict) -> GuardrailAssessmentListMap:
    out: GuardrailAssessmentListMap = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_bedrock_runtime.types.guardrail_assessment_list

        out[key] = (
            capo_bedrock_runtime.types.guardrail_assessment_list.deserialize_json(value)
        )
    return out


def redact_sensitive(value: GuardrailAssessmentListMap) -> dict[str, Any]:
    import capo_bedrock_runtime.types.guardrail_assessment_list

    return {
        key: capo_bedrock_runtime.types.guardrail_assessment_list.redact_sensitive(item)
        for key, item in value.items()
    }
