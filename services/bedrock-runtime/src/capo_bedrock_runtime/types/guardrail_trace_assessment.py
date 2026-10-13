"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailTraceAssessment``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.guardrail_assessment_list_map
    import capo_bedrock_runtime.types.guardrail_assessment_map
    import capo_bedrock_runtime.types.model_outputs


class GuardrailTraceAssessment(TypedDict, closed=True):
    model_output: NotRequired["capo_bedrock_runtime.types.model_outputs.ModelOutputs"]
    """<p>The output from the model.</p>"""
    input_assessment: NotRequired[
        "capo_bedrock_runtime.types.guardrail_assessment_map.GuardrailAssessmentMap"
    ]
    """<p>The input assessment.</p>"""
    output_assessments: NotRequired[
        "capo_bedrock_runtime.types.guardrail_assessment_list_map.GuardrailAssessmentListMap"
    ]
    """<p>the output assessments.</p>"""
    action_reason: NotRequired["str"]
    """<p>Provides the reason for the action taken when harmful content is detected.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailTraceAssessment) -> dict:
    out: dict = {}
    if "model_output" in value:
        import capo_bedrock_runtime.types.model_outputs

        out["modelOutput"] = capo_bedrock_runtime.types.model_outputs.serialize_json(
            value["model_output"]
        )
    if "input_assessment" in value:
        import capo_bedrock_runtime.types.guardrail_assessment_map

        out["inputAssessment"] = (
            capo_bedrock_runtime.types.guardrail_assessment_map.serialize_json(
                value["input_assessment"]
            )
        )
    if "output_assessments" in value:
        import capo_bedrock_runtime.types.guardrail_assessment_list_map

        out["outputAssessments"] = (
            capo_bedrock_runtime.types.guardrail_assessment_list_map.serialize_json(
                value["output_assessments"]
            )
        )
    if "action_reason" in value:
        out["actionReason"] = value["action_reason"]
    return out


def deserialize_json(data: dict) -> GuardrailTraceAssessment:
    out: GuardrailTraceAssessment = {}  # type: ignore[typeddict-item]
    if data.get("modelOutput") is not None:
        import capo_bedrock_runtime.types.model_outputs

        out["model_output"] = capo_bedrock_runtime.types.model_outputs.deserialize_json(
            data["modelOutput"]
        )
    if data.get("inputAssessment") is not None:
        import capo_bedrock_runtime.types.guardrail_assessment_map

        out["input_assessment"] = (
            capo_bedrock_runtime.types.guardrail_assessment_map.deserialize_json(
                data["inputAssessment"]
            )
        )
    if data.get("outputAssessments") is not None:
        import capo_bedrock_runtime.types.guardrail_assessment_list_map

        out["output_assessments"] = (
            capo_bedrock_runtime.types.guardrail_assessment_list_map.deserialize_json(
                data["outputAssessments"]
            )
        )
    if data.get("actionReason") is not None:
        out["action_reason"] = data["actionReason"]
    return out


def redact_sensitive(value: GuardrailTraceAssessment) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "input_assessment" in value:
        import capo_bedrock_runtime.types.guardrail_assessment_map

        out["input_assessment"] = (
            capo_bedrock_runtime.types.guardrail_assessment_map.redact_sensitive(
                value["input_assessment"]
            )
        )
    if "output_assessments" in value:
        import capo_bedrock_runtime.types.guardrail_assessment_list_map

        out["output_assessments"] = (
            capo_bedrock_runtime.types.guardrail_assessment_list_map.redact_sensitive(
                value["output_assessments"]
            )
        )
    return out
