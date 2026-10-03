"""Generated from Smithy shape ``com.amazonaws.bedrock#ModelConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.additional_model_request_fields
    import capo_bedrock.types.advanced_prompt_optimization_model_identifier
    import capo_bedrock.types.inference_configuration


class ModelConfiguration(TypedDict, closed=True):
    model_id: "capo_bedrock.types.advanced_prompt_optimization_model_identifier.AdvancedPromptOptimizationModelIdentifier"
    """<p>The model to use for optimization. The value depends on the resource that you use:</p> <ul> <li> <p>If you use a base model, specify the model ID or its ARN. For a list of model IDs, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-cards.html">Models at a glance</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use a cross-Region (system-defined) inference profile, specify the inference profile ID or its ARN. For a list of inference profile IDs, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference-support.html">Supported Regions and models for inference profiles</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use an application inference profile, specify its full ARN, including the account ID and Region.</p> </li> </ul>"""
    inference_config: NotRequired[
        "capo_bedrock.types.inference_configuration.InferenceConfiguration"
    ]
    """<p>The inference configuration for the model, including parameters such as maximum tokens, temperature, and top-p.</p>"""
    additional_model_request_fields: NotRequired[
        "capo_bedrock.types.additional_model_request_fields.AdditionalModelRequestFields"
    ]
    """<p>Additional model request fields. Use this to pass model-specific parameters that are not included in the standard inference configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ModelConfiguration) -> dict:
    out: dict = {}
    out["modelId"] = value["model_id"]
    if "inference_config" in value:
        import capo_bedrock.types.inference_configuration

        out["inferenceConfig"] = (
            capo_bedrock.types.inference_configuration.serialize_json(
                value["inference_config"]
            )
        )
    if "additional_model_request_fields" in value:
        import capo_bedrock.types.additional_model_request_fields

        out["additionalModelRequestFields"] = (
            capo_bedrock.types.additional_model_request_fields.serialize_json(
                value["additional_model_request_fields"]
            )
        )
    return out


def deserialize_json(data: dict) -> ModelConfiguration:
    out: ModelConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("modelId") is not None:
        out["model_id"] = data["modelId"]
    else:
        raise DeserializationError("ModelConfiguration.model_id required")
    if data.get("inferenceConfig") is not None:
        import capo_bedrock.types.inference_configuration

        out["inference_config"] = (
            capo_bedrock.types.inference_configuration.deserialize_json(
                data["inferenceConfig"]
            )
        )
    if data.get("additionalModelRequestFields") is not None:
        import capo_bedrock.types.additional_model_request_fields

        out["additional_model_request_fields"] = (
            capo_bedrock.types.additional_model_request_fields.deserialize_json(
                data["additionalModelRequestFields"]
            )
        )
    return out
