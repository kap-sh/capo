"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BedrockModelSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.bedrock_guardrail_configuration
    import capo_lex_models_v2.types.bedrock_model_arn
    import capo_lex_models_v2.types.bedrock_model_custom_prompt
    import capo_lex_models_v2.types.bedrock_trace_status


class BedrockModelSpecification(TypedDict, closed=True):
    model_arn: "capo_lex_models_v2.types.bedrock_model_arn.BedrockModelArn"
    """<p>The ARN of the foundation model used in descriptive bot building.</p>"""
    guardrail: NotRequired[
        "capo_lex_models_v2.types.bedrock_guardrail_configuration.BedrockGuardrailConfiguration"
    ]
    """<p>The guardrail configuration in the Bedrock model specification details.</p>"""
    trace_status: NotRequired[
        "capo_lex_models_v2.types.bedrock_trace_status.BedrockTraceStatus"
    ]
    """<p>The Bedrock trace status in the Bedrock model specification details.</p>"""
    custom_prompt: NotRequired[
        "capo_lex_models_v2.types.bedrock_model_custom_prompt.BedrockModelCustomPrompt"
    ]
    """<p>The custom prompt used in the Bedrock model specification details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BedrockModelSpecification) -> dict:
    out: dict = {}
    out["modelArn"] = value["model_arn"]
    if "guardrail" in value:
        import capo_lex_models_v2.types.bedrock_guardrail_configuration

        out["guardrail"] = (
            capo_lex_models_v2.types.bedrock_guardrail_configuration.serialize_json(
                value["guardrail"]
            )
        )
    if "trace_status" in value:
        import capo_lex_models_v2.types.bedrock_trace_status

        out["traceStatus"] = (
            capo_lex_models_v2.types.bedrock_trace_status.serialize_json(
                value["trace_status"]
            )
        )
    if "custom_prompt" in value:
        out["customPrompt"] = value["custom_prompt"]
    return out


def deserialize_json(data: dict) -> BedrockModelSpecification:
    out: BedrockModelSpecification = {}  # type: ignore[typeddict-item]
    if data.get("modelArn") is not None:
        out["model_arn"] = data["modelArn"]
    else:
        out["model_arn"] = ""
    if data.get("guardrail") is not None:
        import capo_lex_models_v2.types.bedrock_guardrail_configuration

        out["guardrail"] = (
            capo_lex_models_v2.types.bedrock_guardrail_configuration.deserialize_json(
                data["guardrail"]
            )
        )
    if data.get("traceStatus") is not None:
        import capo_lex_models_v2.types.bedrock_trace_status

        out["trace_status"] = (
            capo_lex_models_v2.types.bedrock_trace_status.deserialize_json(
                data["traceStatus"]
            )
        )
    if data.get("customPrompt") is not None:
        out["custom_prompt"] = data["customPrompt"]
    return out
