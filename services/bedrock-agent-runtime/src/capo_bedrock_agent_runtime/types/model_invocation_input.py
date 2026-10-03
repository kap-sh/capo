"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#ModelInvocationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.creation_mode
    import capo_bedrock_agent_runtime.types.inference_configuration
    import capo_bedrock_agent_runtime.types.lambda_arn
    import capo_bedrock_agent_runtime.types.model_identifier
    import capo_bedrock_agent_runtime.types.prompt_text
    import capo_bedrock_agent_runtime.types.prompt_type
    import capo_bedrock_agent_runtime.types.trace_id


class ModelInvocationInput(TypedDict, closed=True):
    trace_id: NotRequired["capo_bedrock_agent_runtime.types.trace_id.TraceId"]
    """<p>The unique identifier of the trace.</p>"""
    text: NotRequired["capo_bedrock_agent_runtime.types.prompt_text.PromptText"]
    """<p>The text that prompted the agent at this step.</p>"""
    type: NotRequired["capo_bedrock_agent_runtime.types.prompt_type.PromptType"]
    """<p>The step in the agent sequence.</p>"""
    override_lambda: NotRequired[
        "capo_bedrock_agent_runtime.types.lambda_arn.LambdaArn"
    ]
    """<p>The ARN of the Lambda function to use when parsing the raw foundation model output in parts of the agent sequence.</p>"""
    prompt_creation_mode: NotRequired[
        "capo_bedrock_agent_runtime.types.creation_mode.CreationMode"
    ]
    """<p>Specifies whether the default prompt template was <code>OVERRIDDEN</code>. If it was, the <code>basePromptTemplate</code> that was set in the <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_PromptOverrideConfiguration.html">PromptOverrideConfiguration</a> object when the agent was created or updated is used instead.</p>"""
    inference_configuration: NotRequired[
        "capo_bedrock_agent_runtime.types.inference_configuration.InferenceConfiguration"
    ]
    """<p>Specifications about the inference parameters that were provided alongside the prompt. These are specified in the <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_PromptOverrideConfiguration.html">PromptOverrideConfiguration</a> object that was set when the agent was created or updated. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html">Inference parameters for foundation models</a>.</p>"""
    parser_mode: NotRequired[
        "capo_bedrock_agent_runtime.types.creation_mode.CreationMode"
    ]
    """<p>Specifies whether to override the default parser Lambda function when parsing the raw foundation model output in the part of the agent sequence defined by the <code>promptType</code>.</p>"""
    foundation_model: NotRequired[
        "capo_bedrock_agent_runtime.types.model_identifier.ModelIdentifier"
    ]
    """<p>The identifier of a foundation model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ModelInvocationInput) -> dict:
    out: dict = {}
    if "trace_id" in value:
        out["traceId"] = value["trace_id"]
    if "text" in value:
        out["text"] = value["text"]
    if "type" in value:
        import capo_bedrock_agent_runtime.types.prompt_type

        out["type"] = capo_bedrock_agent_runtime.types.prompt_type.serialize_json(
            value["type"]
        )
    if "override_lambda" in value:
        out["overrideLambda"] = value["override_lambda"]
    if "prompt_creation_mode" in value:
        import capo_bedrock_agent_runtime.types.creation_mode

        out["promptCreationMode"] = (
            capo_bedrock_agent_runtime.types.creation_mode.serialize_json(
                value["prompt_creation_mode"]
            )
        )
    if "inference_configuration" in value:
        import capo_bedrock_agent_runtime.types.inference_configuration

        out["inferenceConfiguration"] = (
            capo_bedrock_agent_runtime.types.inference_configuration.serialize_json(
                value["inference_configuration"]
            )
        )
    if "parser_mode" in value:
        import capo_bedrock_agent_runtime.types.creation_mode

        out["parserMode"] = (
            capo_bedrock_agent_runtime.types.creation_mode.serialize_json(
                value["parser_mode"]
            )
        )
    if "foundation_model" in value:
        out["foundationModel"] = value["foundation_model"]
    return out


def deserialize_json(data: dict) -> ModelInvocationInput:
    out: ModelInvocationInput = {}  # type: ignore[typeddict-item]
    if data.get("traceId") is not None:
        out["trace_id"] = data["traceId"]
    if data.get("text") is not None:
        out["text"] = data["text"]
    if data.get("type") is not None:
        import capo_bedrock_agent_runtime.types.prompt_type

        out["type"] = capo_bedrock_agent_runtime.types.prompt_type.deserialize_json(
            data["type"]
        )
    if data.get("overrideLambda") is not None:
        out["override_lambda"] = data["overrideLambda"]
    if data.get("promptCreationMode") is not None:
        import capo_bedrock_agent_runtime.types.creation_mode

        out["prompt_creation_mode"] = (
            capo_bedrock_agent_runtime.types.creation_mode.deserialize_json(
                data["promptCreationMode"]
            )
        )
    if data.get("inferenceConfiguration") is not None:
        import capo_bedrock_agent_runtime.types.inference_configuration

        out["inference_configuration"] = (
            capo_bedrock_agent_runtime.types.inference_configuration.deserialize_json(
                data["inferenceConfiguration"]
            )
        )
    if data.get("parserMode") is not None:
        import capo_bedrock_agent_runtime.types.creation_mode

        out["parser_mode"] = (
            capo_bedrock_agent_runtime.types.creation_mode.deserialize_json(
                data["parserMode"]
            )
        )
    if data.get("foundationModel") is not None:
        out["foundation_model"] = data["foundationModel"]
    return out
