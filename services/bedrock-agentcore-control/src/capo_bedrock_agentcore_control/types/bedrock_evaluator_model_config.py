"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#BedrockEvaluatorModelConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.additional_model_request_fields
    import capo_bedrock_agentcore_control.types.inference_configuration
    import capo_bedrock_agentcore_control.types.model_id


class BedrockEvaluatorModelConfig(TypedDict, closed=True):
    model_id: "capo_bedrock_agentcore_control.types.model_id.ModelId"
    """<p> The identifier of the Amazon Bedrock model to use for evaluation. Must be a supported foundation model available in your region. </p>"""
    inference_config: NotRequired[
        "capo_bedrock_agentcore_control.types.inference_configuration.InferenceConfiguration"
    ]
    """<p> The inference configuration parameters that control model behavior during evaluation, including temperature, token limits, and sampling settings. </p>"""
    additional_model_request_fields: NotRequired[
        "capo_bedrock_agentcore_control.types.additional_model_request_fields.AdditionalModelRequestFields"
    ]
    """<p> Additional model-specific request fields to customize model behavior beyond the standard inference configuration. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BedrockEvaluatorModelConfig) -> dict:
    out: dict = {}
    out["modelId"] = value["model_id"]
    if "inference_config" in value:
        import capo_bedrock_agentcore_control.types.inference_configuration

        out["inferenceConfig"] = (
            capo_bedrock_agentcore_control.types.inference_configuration.serialize_json(
                value["inference_config"]
            )
        )
    if "additional_model_request_fields" in value:
        out["additionalModelRequestFields"] = value["additional_model_request_fields"]
    return out


def deserialize_json(data: dict) -> BedrockEvaluatorModelConfig:
    out: BedrockEvaluatorModelConfig = {}  # type: ignore[typeddict-item]
    if data.get("modelId") is not None:
        out["model_id"] = data["modelId"]
    else:
        out["model_id"] = ""
    if data.get("inferenceConfig") is not None:
        import capo_bedrock_agentcore_control.types.inference_configuration

        out["inference_config"] = (
            capo_bedrock_agentcore_control.types.inference_configuration.deserialize_json(
                data["inferenceConfig"]
            )
        )
    if data.get("additionalModelRequestFields") is not None:
        out["additional_model_request_fields"] = data["additionalModelRequestFields"]
    return out
