"""Generated from Smithy shape ``com.amazonaws.bedrock#FoundationModelSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.bedrock_model_id
    import capo_bedrock.types.branded_name
    import capo_bedrock.types.foundation_model_arn
    import capo_bedrock.types.foundation_model_lifecycle
    import capo_bedrock.types.inference_type_list
    import capo_bedrock.types.model_customization_list
    import capo_bedrock.types.model_modality_list


class FoundationModelSummary(TypedDict, closed=True):
    model_arn: "capo_bedrock.types.foundation_model_arn.FoundationModelArn"
    """<p>The Amazon Resource Name (ARN) of the foundation model.</p>"""
    model_id: "capo_bedrock.types.bedrock_model_id.BedrockModelId"
    """<p>The model ID of the foundation model.</p>"""
    model_name: NotRequired["capo_bedrock.types.branded_name.BrandedName"]
    """<p>The name of the model.</p>"""
    provider_name: NotRequired["capo_bedrock.types.branded_name.BrandedName"]
    """<p>The model's provider name.</p>"""
    input_modalities: NotRequired[
        "capo_bedrock.types.model_modality_list.ModelModalityList"
    ]
    """<p>The input modalities that the model supports.</p>"""
    output_modalities: NotRequired[
        "capo_bedrock.types.model_modality_list.ModelModalityList"
    ]
    """<p>The output modalities that the model supports.</p>"""
    response_streaming_supported: NotRequired["bool"]
    """<p>Indicates whether the model supports streaming.</p>"""
    customizations_supported: NotRequired[
        "capo_bedrock.types.model_customization_list.ModelCustomizationList"
    ]
    """<p>Whether the model supports fine-tuning or continual pre-training.</p>"""
    inference_types_supported: NotRequired[
        "capo_bedrock.types.inference_type_list.InferenceTypeList"
    ]
    """<p>The inference types that the model supports.</p>"""
    model_lifecycle: NotRequired[
        "capo_bedrock.types.foundation_model_lifecycle.FoundationModelLifecycle"
    ]
    """<p>Contains details about whether a model version is available or deprecated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FoundationModelSummary) -> dict:
    out: dict = {}
    out["modelArn"] = value["model_arn"]
    out["modelId"] = value["model_id"]
    if "model_name" in value:
        out["modelName"] = value["model_name"]
    if "provider_name" in value:
        out["providerName"] = value["provider_name"]
    if "input_modalities" in value:
        import capo_bedrock.types.model_modality_list

        out["inputModalities"] = capo_bedrock.types.model_modality_list.serialize_json(
            value["input_modalities"]
        )
    if "output_modalities" in value:
        import capo_bedrock.types.model_modality_list

        out["outputModalities"] = capo_bedrock.types.model_modality_list.serialize_json(
            value["output_modalities"]
        )
    if "response_streaming_supported" in value:
        out["responseStreamingSupported"] = value["response_streaming_supported"]
    if "customizations_supported" in value:
        import capo_bedrock.types.model_customization_list

        out["customizationsSupported"] = (
            capo_bedrock.types.model_customization_list.serialize_json(
                value["customizations_supported"]
            )
        )
    if "inference_types_supported" in value:
        import capo_bedrock.types.inference_type_list

        out["inferenceTypesSupported"] = (
            capo_bedrock.types.inference_type_list.serialize_json(
                value["inference_types_supported"]
            )
        )
    if "model_lifecycle" in value:
        import capo_bedrock.types.foundation_model_lifecycle

        out["modelLifecycle"] = (
            capo_bedrock.types.foundation_model_lifecycle.serialize_json(
                value["model_lifecycle"]
            )
        )
    return out


def deserialize_json(data: dict) -> FoundationModelSummary:
    out: FoundationModelSummary = {}  # type: ignore[typeddict-item]
    if data.get("modelArn") is not None:
        out["model_arn"] = data["modelArn"]
    else:
        out["model_arn"] = ""
    if data.get("modelId") is not None:
        out["model_id"] = data["modelId"]
    else:
        out["model_id"] = ""
    if data.get("modelName") is not None:
        out["model_name"] = data["modelName"]
    if data.get("providerName") is not None:
        out["provider_name"] = data["providerName"]
    if data.get("inputModalities") is not None:
        import capo_bedrock.types.model_modality_list

        out["input_modalities"] = (
            capo_bedrock.types.model_modality_list.deserialize_json(
                data["inputModalities"]
            )
        )
    if data.get("outputModalities") is not None:
        import capo_bedrock.types.model_modality_list

        out["output_modalities"] = (
            capo_bedrock.types.model_modality_list.deserialize_json(
                data["outputModalities"]
            )
        )
    if data.get("responseStreamingSupported") is not None:
        out["response_streaming_supported"] = data["responseStreamingSupported"]
    if data.get("customizationsSupported") is not None:
        import capo_bedrock.types.model_customization_list

        out["customizations_supported"] = (
            capo_bedrock.types.model_customization_list.deserialize_json(
                data["customizationsSupported"]
            )
        )
    if data.get("inferenceTypesSupported") is not None:
        import capo_bedrock.types.inference_type_list

        out["inference_types_supported"] = (
            capo_bedrock.types.inference_type_list.deserialize_json(
                data["inferenceTypesSupported"]
            )
        )
    if data.get("modelLifecycle") is not None:
        import capo_bedrock.types.foundation_model_lifecycle

        out["model_lifecycle"] = (
            capo_bedrock.types.foundation_model_lifecycle.deserialize_json(
                data["modelLifecycle"]
            )
        )
    return out
