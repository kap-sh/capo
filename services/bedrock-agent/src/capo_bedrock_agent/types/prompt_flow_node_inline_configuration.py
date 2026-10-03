"""Generated from Smithy shape ``com.amazonaws.bedrockagent#PromptFlowNodeInlineConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.flow_prompt_model_identifier
    import capo_bedrock_agent.types.prompt_inference_configuration
    import capo_bedrock_agent.types.prompt_template_configuration
    import capo_bedrock_agent.types.prompt_template_type


class PromptFlowNodeInlineConfiguration(TypedDict, closed=True):
    template_type: "capo_bedrock_agent.types.prompt_template_type.PromptTemplateType"
    """<p>The type of prompt template.</p>"""
    template_configuration: "capo_bedrock_agent.types.prompt_template_configuration.PromptTemplateConfiguration"
    """<p>Contains a prompt and variables in the prompt that can be replaced with values at runtime.</p>"""
    model_id: "capo_bedrock_agent.types.flow_prompt_model_identifier.FlowPromptModelIdentifier"
    """<p>The unique identifier of the model or <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html">inference profile</a> to run inference with.</p>"""
    inference_configuration: NotRequired[
        "capo_bedrock_agent.types.prompt_inference_configuration.PromptInferenceConfiguration"
    ]
    """<p>Contains inference configurations for the prompt.</p>"""
    additional_model_request_fields: NotRequired["object"]
    """<p>Additional fields to be included in the model request for the Prompt node.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PromptFlowNodeInlineConfiguration) -> dict:
    out: dict = {}
    import capo_bedrock_agent.types.prompt_template_type

    out["templateType"] = capo_bedrock_agent.types.prompt_template_type.serialize_json(
        value.get("template_type", "TEXT")
    )
    import capo_bedrock_agent.types.prompt_template_configuration

    out["templateConfiguration"] = (
        capo_bedrock_agent.types.prompt_template_configuration.serialize_json(
            value["template_configuration"]
        )
    )
    out["modelId"] = value.get("model_id", "")
    if "inference_configuration" in value:
        import capo_bedrock_agent.types.prompt_inference_configuration

        out["inferenceConfiguration"] = (
            capo_bedrock_agent.types.prompt_inference_configuration.serialize_json(
                value["inference_configuration"]
            )
        )
    if "additional_model_request_fields" in value:
        out["additionalModelRequestFields"] = value["additional_model_request_fields"]
    return out


def deserialize_json(data: dict) -> PromptFlowNodeInlineConfiguration:
    out: PromptFlowNodeInlineConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("templateType") is not None:
        import capo_bedrock_agent.types.prompt_template_type

        out["template_type"] = (
            capo_bedrock_agent.types.prompt_template_type.deserialize_json(
                data["templateType"]
            )
        )
    else:
        out["template_type"] = "TEXT"
    if data.get("templateConfiguration") is not None:
        import capo_bedrock_agent.types.prompt_template_configuration

        out["template_configuration"] = (
            capo_bedrock_agent.types.prompt_template_configuration.deserialize_json(
                data["templateConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "PromptFlowNodeInlineConfiguration.template_configuration required"
        )
    if data.get("modelId") is not None:
        out["model_id"] = data["modelId"]
    else:
        out["model_id"] = ""
    if data.get("inferenceConfiguration") is not None:
        import capo_bedrock_agent.types.prompt_inference_configuration

        out["inference_configuration"] = (
            capo_bedrock_agent.types.prompt_inference_configuration.deserialize_json(
                data["inferenceConfiguration"]
            )
        )
    if data.get("additionalModelRequestFields") is not None:
        out["additional_model_request_fields"] = data["additionalModelRequestFields"]
    return out
