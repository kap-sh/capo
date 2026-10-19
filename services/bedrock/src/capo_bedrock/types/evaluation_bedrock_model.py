"""Generated from Smithy shape ``com.amazonaws.bedrock#EvaluationBedrockModel``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.evaluation_bedrock_model_identifier
    import capo_bedrock.types.evaluation_model_inference_params
    import capo_bedrock.types.performance_configuration


class EvaluationBedrockModel(TypedDict, closed=True):
    model_identifier: "capo_bedrock.types.evaluation_bedrock_model_identifier.EvaluationBedrockModelIdentifier"
    """<p>The ARN of the Amazon Bedrock model or inference profile specified.</p>"""
    inference_params: "capo_bedrock.types.evaluation_model_inference_params.EvaluationModelInferenceParams"
    """<p>Each Amazon Bedrock support different inference parameters that change how the model behaves during inference.</p>"""
    performance_config: NotRequired[
        "capo_bedrock.types.performance_configuration.PerformanceConfiguration"
    ]
    """<p>Specifies performance settings for the model or inference profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationBedrockModel) -> dict:
    out: dict = {}
    out["modelIdentifier"] = value["model_identifier"]
    out["inferenceParams"] = value.get("inference_params", "{}")
    if "performance_config" in value:
        import capo_bedrock.types.performance_configuration

        out["performanceConfig"] = (
            capo_bedrock.types.performance_configuration.serialize_json(
                value["performance_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> EvaluationBedrockModel:
    out: EvaluationBedrockModel = {}  # type: ignore[typeddict-item]
    if data.get("modelIdentifier") is not None:
        out["model_identifier"] = data["modelIdentifier"]
    else:
        out["model_identifier"] = ""
    if data.get("inferenceParams") is not None:
        out["inference_params"] = data["inferenceParams"]
    else:
        out["inference_params"] = "{}"
    if data.get("performanceConfig") is not None:
        import capo_bedrock.types.performance_configuration

        out["performance_config"] = (
            capo_bedrock.types.performance_configuration.deserialize_json(
                data["performanceConfig"]
            )
        )
    return out


def redact_sensitive(value: EvaluationBedrockModel) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "inference_params" in value:
        out["inference_params"] = "*** Sensitive Data Redacted ***"
    return out
