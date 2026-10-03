"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#OrchestrationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.additional_model_request_fields
    import capo_bedrock_agent_runtime.types.inference_config
    import capo_bedrock_agent_runtime.types.performance_configuration
    import capo_bedrock_agent_runtime.types.prompt_template
    import capo_bedrock_agent_runtime.types.query_transformation_configuration


class OrchestrationConfiguration(TypedDict, closed=True):
    prompt_template: NotRequired[
        "capo_bedrock_agent_runtime.types.prompt_template.PromptTemplate"
    ]
    """<p>Contains the template for the prompt that's sent to the model. Orchestration prompts must include the <code>$conversation_history$</code> and <code>$output_format_instructions$</code> variables. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-placeholders.html">Use placeholder variables</a> in the user guide.</p>"""
    inference_config: NotRequired[
        "capo_bedrock_agent_runtime.types.inference_config.InferenceConfig"
    ]
    """<p> Configuration settings for inference when using RetrieveAndGenerate to generate responses while using a knowledge base as a source. </p>"""
    additional_model_request_fields: NotRequired[
        "capo_bedrock_agent_runtime.types.additional_model_request_fields.AdditionalModelRequestFields"
    ]
    """<p> Additional model parameters and corresponding values not included in the textInferenceConfig structure for a knowledge base. This allows users to provide custom model parameters specific to the language model being used. </p>"""
    query_transformation_configuration: NotRequired[
        "capo_bedrock_agent_runtime.types.query_transformation_configuration.QueryTransformationConfiguration"
    ]
    """<p>To split up the prompt and retrieve multiple sources, set the transformation type to <code>QUERY_DECOMPOSITION</code>.</p>"""
    performance_config: NotRequired[
        "capo_bedrock_agent_runtime.types.performance_configuration.PerformanceConfiguration"
    ]
    """<p>The latency configuration for the model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OrchestrationConfiguration) -> dict:
    out: dict = {}
    if "prompt_template" in value:
        import capo_bedrock_agent_runtime.types.prompt_template

        out["promptTemplate"] = (
            capo_bedrock_agent_runtime.types.prompt_template.serialize_json(
                value["prompt_template"]
            )
        )
    if "inference_config" in value:
        import capo_bedrock_agent_runtime.types.inference_config

        out["inferenceConfig"] = (
            capo_bedrock_agent_runtime.types.inference_config.serialize_json(
                value["inference_config"]
            )
        )
    if "additional_model_request_fields" in value:
        import capo_bedrock_agent_runtime.types.additional_model_request_fields

        out["additionalModelRequestFields"] = (
            capo_bedrock_agent_runtime.types.additional_model_request_fields.serialize_json(
                value["additional_model_request_fields"]
            )
        )
    if "query_transformation_configuration" in value:
        import capo_bedrock_agent_runtime.types.query_transformation_configuration

        out["queryTransformationConfiguration"] = (
            capo_bedrock_agent_runtime.types.query_transformation_configuration.serialize_json(
                value["query_transformation_configuration"]
            )
        )
    if "performance_config" in value:
        import capo_bedrock_agent_runtime.types.performance_configuration

        out["performanceConfig"] = (
            capo_bedrock_agent_runtime.types.performance_configuration.serialize_json(
                value["performance_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> OrchestrationConfiguration:
    out: OrchestrationConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("promptTemplate") is not None:
        import capo_bedrock_agent_runtime.types.prompt_template

        out["prompt_template"] = (
            capo_bedrock_agent_runtime.types.prompt_template.deserialize_json(
                data["promptTemplate"]
            )
        )
    if data.get("inferenceConfig") is not None:
        import capo_bedrock_agent_runtime.types.inference_config

        out["inference_config"] = (
            capo_bedrock_agent_runtime.types.inference_config.deserialize_json(
                data["inferenceConfig"]
            )
        )
    if data.get("additionalModelRequestFields") is not None:
        import capo_bedrock_agent_runtime.types.additional_model_request_fields

        out["additional_model_request_fields"] = (
            capo_bedrock_agent_runtime.types.additional_model_request_fields.deserialize_json(
                data["additionalModelRequestFields"]
            )
        )
    if data.get("queryTransformationConfiguration") is not None:
        import capo_bedrock_agent_runtime.types.query_transformation_configuration

        out["query_transformation_configuration"] = (
            capo_bedrock_agent_runtime.types.query_transformation_configuration.deserialize_json(
                data["queryTransformationConfiguration"]
            )
        )
    if data.get("performanceConfig") is not None:
        import capo_bedrock_agent_runtime.types.performance_configuration

        out["performance_config"] = (
            capo_bedrock_agent_runtime.types.performance_configuration.deserialize_json(
                data["performanceConfig"]
            )
        )
    return out
