"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClarifyExplainerConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.clarify_enable_explanations
    import capo_sagemaker.types.clarify_inference_config
    import capo_sagemaker.types.clarify_shap_config


class ClarifyExplainerConfig(TypedDict, closed=True):
    enable_explanations: NotRequired[
        "capo_sagemaker.types.clarify_enable_explanations.ClarifyEnableExplanations"
    ]
    """<p>A JMESPath boolean expression used to filter which records to explain. Explanations are activated by default. See <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-online-explainability-create-endpoint.html#clarify-online-explainability-create-endpoint-enable"> <code>EnableExplanations</code> </a>for additional information.</p>"""
    inference_config: NotRequired[
        "capo_sagemaker.types.clarify_inference_config.ClarifyInferenceConfig"
    ]
    """<p>The inference configuration parameter for the model container.</p>"""
    shap_config: NotRequired[
        "capo_sagemaker.types.clarify_shap_config.ClarifyShapConfig"
    ]
    """<p>The configuration for SHAP analysis.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClarifyExplainerConfig) -> dict:
    out: dict = {}
    if "enable_explanations" in value:
        out["EnableExplanations"] = value["enable_explanations"]
    if "inference_config" in value:
        import capo_sagemaker.types.clarify_inference_config

        out["InferenceConfig"] = (
            capo_sagemaker.types.clarify_inference_config.serialize_aws_json_1_1(
                value["inference_config"]
            )
        )
    if "shap_config" in value:
        import capo_sagemaker.types.clarify_shap_config

        out["ShapConfig"] = (
            capo_sagemaker.types.clarify_shap_config.serialize_aws_json_1_1(
                value["shap_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ClarifyExplainerConfig:
    out: ClarifyExplainerConfig = {}  # type: ignore[typeddict-item]
    if data.get("EnableExplanations") is not None:
        out["enable_explanations"] = data["EnableExplanations"]
    if data.get("InferenceConfig") is not None:
        import capo_sagemaker.types.clarify_inference_config

        out["inference_config"] = (
            capo_sagemaker.types.clarify_inference_config.deserialize_aws_json_1_1(
                data["InferenceConfig"]
            )
        )
    if data.get("ShapConfig") is not None:
        import capo_sagemaker.types.clarify_shap_config

        out["shap_config"] = (
            capo_sagemaker.types.clarify_shap_config.deserialize_aws_json_1_1(
                data["ShapConfig"]
            )
        )
    return out
