"""Generated from Smithy shape ``com.amazonaws.bedrockagent#PromptVariant``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.prompt_gen_ai_resource
    import capo_bedrock_agent.types.prompt_inference_configuration
    import capo_bedrock_agent.types.prompt_metadata_list
    import capo_bedrock_agent.types.prompt_model_identifier
    import capo_bedrock_agent.types.prompt_template_configuration
    import capo_bedrock_agent.types.prompt_template_type
    import capo_bedrock_agent.types.prompt_variant_name


class PromptVariant(TypedDict, closed=True):
    name: "capo_bedrock_agent.types.prompt_variant_name.PromptVariantName"
    """<p>The name of the prompt variant.</p>"""
    template_type: "capo_bedrock_agent.types.prompt_template_type.PromptTemplateType"
    """<p>The type of prompt template to use.</p>"""
    template_configuration: "capo_bedrock_agent.types.prompt_template_configuration.PromptTemplateConfiguration"
    """<p>Contains configurations for the prompt template.</p>"""
    model_id: NotRequired[
        "capo_bedrock_agent.types.prompt_model_identifier.PromptModelIdentifier"
    ]
    """<p>The unique identifier of the model or <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html">inference profile</a> with which to run inference on the prompt.</p>"""
    inference_configuration: NotRequired[
        "capo_bedrock_agent.types.prompt_inference_configuration.PromptInferenceConfiguration"
    ]
    """<p>Contains inference configurations for the prompt variant.</p>"""
    metadata: NotRequired[
        "capo_bedrock_agent.types.prompt_metadata_list.PromptMetadataList"
    ]
    """<p>An array of objects, each containing a key-value pair that defines a metadata tag and value to attach to a prompt variant.</p>"""
    additional_model_request_fields: NotRequired["object"]
    """<p>Contains model-specific inference configurations that aren't in the <code>inferenceConfiguration</code> field. To see model-specific inference parameters, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html">Inference request parameters and response fields for foundation models</a>.</p>"""
    gen_ai_resource: NotRequired[
        "capo_bedrock_agent.types.prompt_gen_ai_resource.PromptGenAiResource"
    ]
    """<p>Specifies a generative AI resource with which to use the prompt.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PromptVariant) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_bedrock_agent.types.prompt_template_type

    out["templateType"] = capo_bedrock_agent.types.prompt_template_type.serialize_json(
        value["template_type"]
    )
    import capo_bedrock_agent.types.prompt_template_configuration

    out["templateConfiguration"] = (
        capo_bedrock_agent.types.prompt_template_configuration.serialize_json(
            value["template_configuration"]
        )
    )
    if "model_id" in value:
        out["modelId"] = value["model_id"]
    if "inference_configuration" in value:
        import capo_bedrock_agent.types.prompt_inference_configuration

        out["inferenceConfiguration"] = (
            capo_bedrock_agent.types.prompt_inference_configuration.serialize_json(
                value["inference_configuration"]
            )
        )
    if "metadata" in value:
        import capo_bedrock_agent.types.prompt_metadata_list

        out["metadata"] = capo_bedrock_agent.types.prompt_metadata_list.serialize_json(
            value["metadata"]
        )
    if "additional_model_request_fields" in value:
        out["additionalModelRequestFields"] = value["additional_model_request_fields"]
    if "gen_ai_resource" in value:
        import capo_bedrock_agent.types.prompt_gen_ai_resource

        out["genAiResource"] = (
            capo_bedrock_agent.types.prompt_gen_ai_resource.serialize_json(
                value["gen_ai_resource"]
            )
        )
    return out


def deserialize_json(data: dict) -> PromptVariant:
    out: PromptVariant = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("PromptVariant.name required")
    if data.get("templateType") is not None:
        import capo_bedrock_agent.types.prompt_template_type

        out["template_type"] = (
            capo_bedrock_agent.types.prompt_template_type.deserialize_json(
                data["templateType"]
            )
        )
    else:
        raise DeserializationError("PromptVariant.template_type required")
    if data.get("templateConfiguration") is not None:
        import capo_bedrock_agent.types.prompt_template_configuration

        out["template_configuration"] = (
            capo_bedrock_agent.types.prompt_template_configuration.deserialize_json(
                data["templateConfiguration"]
            )
        )
    else:
        raise DeserializationError("PromptVariant.template_configuration required")
    if data.get("modelId") is not None:
        out["model_id"] = data["modelId"]
    if data.get("inferenceConfiguration") is not None:
        import capo_bedrock_agent.types.prompt_inference_configuration

        out["inference_configuration"] = (
            capo_bedrock_agent.types.prompt_inference_configuration.deserialize_json(
                data["inferenceConfiguration"]
            )
        )
    if data.get("metadata") is not None:
        import capo_bedrock_agent.types.prompt_metadata_list

        out["metadata"] = (
            capo_bedrock_agent.types.prompt_metadata_list.deserialize_json(
                data["metadata"]
            )
        )
    if data.get("additionalModelRequestFields") is not None:
        out["additional_model_request_fields"] = data["additionalModelRequestFields"]
    if data.get("genAiResource") is not None:
        import capo_bedrock_agent.types.prompt_gen_ai_resource

        out["gen_ai_resource"] = (
            capo_bedrock_agent.types.prompt_gen_ai_resource.deserialize_json(
                data["genAiResource"]
            )
        )
    return out
