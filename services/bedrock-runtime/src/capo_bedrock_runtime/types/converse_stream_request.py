"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#ConverseStreamRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.additional_model_response_field_paths
    import capo_bedrock_runtime.types.conversational_model_id
    import capo_bedrock_runtime.types.guardrail_stream_configuration
    import capo_bedrock_runtime.types.inference_configuration
    import capo_bedrock_runtime.types.messages
    import capo_bedrock_runtime.types.output_config
    import capo_bedrock_runtime.types.performance_configuration
    import capo_bedrock_runtime.types.prompt_variable_map
    import capo_bedrock_runtime.types.request_metadata
    import capo_bedrock_runtime.types.service_tier
    import capo_bedrock_runtime.types.system_content_blocks
    import capo_bedrock_runtime.types.tool_configuration


class ConverseStreamRequest(TypedDict, closed=True):
    model_id: "capo_bedrock_runtime.types.conversational_model_id.ConversationalModelId"
    """<p>Specifies the model or throughput with which to run inference, or the prompt resource to use in inference. The value depends on the resource that you use:</p> <ul> <li> <p>If you use a base model, specify the model ID or its ARN. For a list of model IDs for base models, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-ids.html#model-ids-arns">Amazon Bedrock base model IDs (on-demand throughput)</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use an inference profile, specify the inference profile ID or its ARN. For a list of inference profile IDs, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference-support.html">Supported Regions and models for cross-region inference</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use a provisioned model, specify the ARN of the Provisioned Throughput. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/prov-thru-use.html">Run inference using a Provisioned Throughput</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use a custom model, first purchase Provisioned Throughput for it. Then specify the ARN of the resulting provisioned model. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-use.html">Use a custom model in Amazon Bedrock</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>To include a prompt that was defined in <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html">Prompt management</a>, specify the ARN of the prompt version to use.</p> </li> </ul> <p>The Converse API doesn't support <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html">imported models</a>.</p>"""
    messages: NotRequired["capo_bedrock_runtime.types.messages.Messages"]
    """<p>The messages that you want to send to the model.</p>"""
    system: NotRequired[
        "capo_bedrock_runtime.types.system_content_blocks.SystemContentBlocks"
    ]
    """<p>A prompt that provides instructions or context to the model about the task it should perform, or the persona it should adopt during the conversation.</p>"""
    inference_config: NotRequired[
        "capo_bedrock_runtime.types.inference_configuration.InferenceConfiguration"
    ]
    """<p>Inference parameters to pass to the model. <code>Converse</code> and <code>ConverseStream</code> support a base set of inference parameters. If you need to pass additional parameters that the model supports, use the <code>additionalModelRequestFields</code> request field.</p>"""
    tool_config: NotRequired[
        "capo_bedrock_runtime.types.tool_configuration.ToolConfiguration"
    ]
    """<p>Configuration information for the tools that the model can use when generating a response.</p> <p>For information about models that support streaming tool use, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/conversation-inference.html#conversation-inference-supported-models-features">Supported models and model features</a>.</p>"""
    guardrail_config: NotRequired[
        "capo_bedrock_runtime.types.guardrail_stream_configuration.GuardrailStreamConfiguration"
    ]
    """<p>Configuration information for a guardrail that you want to use in the request. If you include <code>guardContent</code> blocks in the <code>content</code> field in the <code>messages</code> field, the guardrail operates only on those messages. If you include no <code>guardContent</code> blocks, the guardrail operates on all messages in the request body and in any included prompt resource.</p>"""
    additional_model_request_fields: NotRequired["object"]
    """<p>Additional inference parameters that the model supports, beyond the base set of inference parameters that <code>Converse</code> and <code>ConverseStream</code> support in the <code>inferenceConfig</code> field. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html">Model parameters</a>.</p>"""
    prompt_variables: NotRequired[
        "capo_bedrock_runtime.types.prompt_variable_map.PromptVariableMap"
    ]
    """<p>Contains a map of variables in a prompt from Prompt management to objects containing the values to fill in for them when running model invocation. This field is ignored if you don't specify a prompt resource in the <code>modelId</code> field.</p>"""
    additional_model_response_field_paths: NotRequired[
        "capo_bedrock_runtime.types.additional_model_response_field_paths.AdditionalModelResponseFieldPaths"
    ]
    """<p>Additional model parameters field paths to return in the response. <code>Converse</code> and <code>ConverseStream</code> return the requested fields as a JSON Pointer object in the <code>additionalModelResponseFields</code> field. The following is example JSON for <code>additionalModelResponseFieldPaths</code>.</p> <p> <code>[ "/stop_sequence" ]</code> </p> <p>For information about the JSON Pointer syntax, see the <a href="https://datatracker.ietf.org/doc/html/rfc6901">Internet Engineering Task Force (IETF)</a> documentation.</p> <p> <code>Converse</code> and <code>ConverseStream</code> reject an empty JSON Pointer or incorrectly structured JSON Pointer with a <code>400</code> error code. if the JSON Pointer is valid, but the requested field is not in the model response, it is ignored by <code>Converse</code>.</p>"""
    request_metadata: NotRequired[
        "capo_bedrock_runtime.types.request_metadata.RequestMetadata"
    ]
    """<p>Key-value pairs that you can use to filter invocation logs.</p>"""
    performance_config: NotRequired[
        "capo_bedrock_runtime.types.performance_configuration.PerformanceConfiguration"
    ]
    """<p>Model performance settings for the request.</p>"""
    service_tier: NotRequired["capo_bedrock_runtime.types.service_tier.ServiceTier"]
    """<p>Specifies the processing tier configuration used for serving the request.</p>"""
    output_config: NotRequired["capo_bedrock_runtime.types.output_config.OutputConfig"]
    """<p>Output configuration for a model response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConverseStreamRequest) -> dict:
    out: dict = {}
    if "messages" in value:
        import capo_bedrock_runtime.types.messages

        out["messages"] = capo_bedrock_runtime.types.messages.serialize_json(
            value["messages"]
        )
    if "system" in value:
        import capo_bedrock_runtime.types.system_content_blocks

        out["system"] = capo_bedrock_runtime.types.system_content_blocks.serialize_json(
            value["system"]
        )
    if "inference_config" in value:
        import capo_bedrock_runtime.types.inference_configuration

        out["inferenceConfig"] = (
            capo_bedrock_runtime.types.inference_configuration.serialize_json(
                value["inference_config"]
            )
        )
    if "tool_config" in value:
        import capo_bedrock_runtime.types.tool_configuration

        out["toolConfig"] = (
            capo_bedrock_runtime.types.tool_configuration.serialize_json(
                value["tool_config"]
            )
        )
    if "guardrail_config" in value:
        import capo_bedrock_runtime.types.guardrail_stream_configuration

        out["guardrailConfig"] = (
            capo_bedrock_runtime.types.guardrail_stream_configuration.serialize_json(
                value["guardrail_config"]
            )
        )
    if "additional_model_request_fields" in value:
        out["additionalModelRequestFields"] = value["additional_model_request_fields"]
    if "prompt_variables" in value:
        import capo_bedrock_runtime.types.prompt_variable_map

        out["promptVariables"] = (
            capo_bedrock_runtime.types.prompt_variable_map.serialize_json(
                value["prompt_variables"]
            )
        )
    if "additional_model_response_field_paths" in value:
        import capo_bedrock_runtime.types.additional_model_response_field_paths

        out["additionalModelResponseFieldPaths"] = (
            capo_bedrock_runtime.types.additional_model_response_field_paths.serialize_json(
                value["additional_model_response_field_paths"]
            )
        )
    if "request_metadata" in value:
        import capo_bedrock_runtime.types.request_metadata

        out["requestMetadata"] = (
            capo_bedrock_runtime.types.request_metadata.serialize_json(
                value["request_metadata"]
            )
        )
    if "performance_config" in value:
        import capo_bedrock_runtime.types.performance_configuration

        out["performanceConfig"] = (
            capo_bedrock_runtime.types.performance_configuration.serialize_json(
                value["performance_config"]
            )
        )
    if "service_tier" in value:
        import capo_bedrock_runtime.types.service_tier

        out["serviceTier"] = capo_bedrock_runtime.types.service_tier.serialize_json(
            value["service_tier"]
        )
    if "output_config" in value:
        import capo_bedrock_runtime.types.output_config

        out["outputConfig"] = capo_bedrock_runtime.types.output_config.serialize_json(
            value["output_config"]
        )
    return out


def deserialize_json(data: dict) -> ConverseStreamRequest:
    out: ConverseStreamRequest = {}  # type: ignore[typeddict-item]
    if data.get("messages") is not None:
        import capo_bedrock_runtime.types.messages

        out["messages"] = capo_bedrock_runtime.types.messages.deserialize_json(
            data["messages"]
        )
    if data.get("system") is not None:
        import capo_bedrock_runtime.types.system_content_blocks

        out["system"] = (
            capo_bedrock_runtime.types.system_content_blocks.deserialize_json(
                data["system"]
            )
        )
    if data.get("inferenceConfig") is not None:
        import capo_bedrock_runtime.types.inference_configuration

        out["inference_config"] = (
            capo_bedrock_runtime.types.inference_configuration.deserialize_json(
                data["inferenceConfig"]
            )
        )
    if data.get("toolConfig") is not None:
        import capo_bedrock_runtime.types.tool_configuration

        out["tool_config"] = (
            capo_bedrock_runtime.types.tool_configuration.deserialize_json(
                data["toolConfig"]
            )
        )
    if data.get("guardrailConfig") is not None:
        import capo_bedrock_runtime.types.guardrail_stream_configuration

        out["guardrail_config"] = (
            capo_bedrock_runtime.types.guardrail_stream_configuration.deserialize_json(
                data["guardrailConfig"]
            )
        )
    if data.get("additionalModelRequestFields") is not None:
        out["additional_model_request_fields"] = data["additionalModelRequestFields"]
    if data.get("promptVariables") is not None:
        import capo_bedrock_runtime.types.prompt_variable_map

        out["prompt_variables"] = (
            capo_bedrock_runtime.types.prompt_variable_map.deserialize_json(
                data["promptVariables"]
            )
        )
    if data.get("additionalModelResponseFieldPaths") is not None:
        import capo_bedrock_runtime.types.additional_model_response_field_paths

        out["additional_model_response_field_paths"] = (
            capo_bedrock_runtime.types.additional_model_response_field_paths.deserialize_json(
                data["additionalModelResponseFieldPaths"]
            )
        )
    if data.get("requestMetadata") is not None:
        import capo_bedrock_runtime.types.request_metadata

        out["request_metadata"] = (
            capo_bedrock_runtime.types.request_metadata.deserialize_json(
                data["requestMetadata"]
            )
        )
    if data.get("performanceConfig") is not None:
        import capo_bedrock_runtime.types.performance_configuration

        out["performance_config"] = (
            capo_bedrock_runtime.types.performance_configuration.deserialize_json(
                data["performanceConfig"]
            )
        )
    if data.get("serviceTier") is not None:
        import capo_bedrock_runtime.types.service_tier

        out["service_tier"] = capo_bedrock_runtime.types.service_tier.deserialize_json(
            data["serviceTier"]
        )
    if data.get("outputConfig") is not None:
        import capo_bedrock_runtime.types.output_config

        out["output_config"] = (
            capo_bedrock_runtime.types.output_config.deserialize_json(
                data["outputConfig"]
            )
        )
    return out
