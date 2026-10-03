"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateInferenceComponentInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.endpoint_name
    import capo_sagemaker.types.inference_component_name
    import capo_sagemaker.types.inference_component_runtime_config
    import capo_sagemaker.types.inference_component_specification
    import capo_sagemaker.types.inference_component_specification_list
    import capo_sagemaker.types.tag_list
    import capo_sagemaker.types.variant_name


class CreateInferenceComponentInput(TypedDict, closed=True):
    inference_component_name: NotRequired[
        "capo_sagemaker.types.inference_component_name.InferenceComponentName"
    ]
    """<p>A unique name to assign to the inference component.</p>"""
    endpoint_name: NotRequired["capo_sagemaker.types.endpoint_name.EndpointName"]
    """<p>The name of an existing endpoint where you host the inference component.</p>"""
    variant_name: NotRequired["capo_sagemaker.types.variant_name.VariantName"]
    """<p>The name of an existing production variant where you host the inference component.</p>"""
    specification: NotRequired[
        "capo_sagemaker.types.inference_component_specification.InferenceComponentSpecification"
    ]
    """<p>Details about the resources to deploy with this inference component, including the model, container, and compute resources.</p>"""
    specifications: NotRequired[
        "capo_sagemaker.types.inference_component_specification_list.InferenceComponentSpecificationList"
    ]
    """<p>A list of specification objects for the inference component, one per instance type. Use this parameter when you want to deploy a different model or resource configuration for the inference component on each instance type. You can use either this parameter or the singular <code>Specification</code> parameter, but not both.</p>"""
    runtime_config: NotRequired[
        "capo_sagemaker.types.inference_component_runtime_config.InferenceComponentRuntimeConfig"
    ]
    """<p>Runtime settings for a model that is deployed with an inference component.</p>"""
    tags: NotRequired["capo_sagemaker.types.tag_list.TagList"]
    """<p>A list of key-value pairs associated with the model. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html">Tagging Amazon Web Services resources</a> in the <i>Amazon Web Services General Reference</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateInferenceComponentInput) -> dict:
    out: dict = {}
    if "inference_component_name" in value:
        out["InferenceComponentName"] = value["inference_component_name"]
    if "endpoint_name" in value:
        out["EndpointName"] = value["endpoint_name"]
    if "variant_name" in value:
        out["VariantName"] = value["variant_name"]
    if "specification" in value:
        import capo_sagemaker.types.inference_component_specification

        out["Specification"] = (
            capo_sagemaker.types.inference_component_specification.serialize_aws_json_1_1(
                value["specification"]
            )
        )
    if "specifications" in value:
        import capo_sagemaker.types.inference_component_specification_list

        out["Specifications"] = (
            capo_sagemaker.types.inference_component_specification_list.serialize_aws_json_1_1(
                value["specifications"]
            )
        )
    if "runtime_config" in value:
        import capo_sagemaker.types.inference_component_runtime_config

        out["RuntimeConfig"] = (
            capo_sagemaker.types.inference_component_runtime_config.serialize_aws_json_1_1(
                value["runtime_config"]
            )
        )
    if "tags" in value:
        import capo_sagemaker.types.tag_list

        out["Tags"] = capo_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateInferenceComponentInput:
    out: CreateInferenceComponentInput = {}  # type: ignore[typeddict-item]
    if data.get("InferenceComponentName") is not None:
        out["inference_component_name"] = data["InferenceComponentName"]
    if data.get("EndpointName") is not None:
        out["endpoint_name"] = data["EndpointName"]
    if data.get("VariantName") is not None:
        out["variant_name"] = data["VariantName"]
    if data.get("Specification") is not None:
        import capo_sagemaker.types.inference_component_specification

        out["specification"] = (
            capo_sagemaker.types.inference_component_specification.deserialize_aws_json_1_1(
                data["Specification"]
            )
        )
    if data.get("Specifications") is not None:
        import capo_sagemaker.types.inference_component_specification_list

        out["specifications"] = (
            capo_sagemaker.types.inference_component_specification_list.deserialize_aws_json_1_1(
                data["Specifications"]
            )
        )
    if data.get("RuntimeConfig") is not None:
        import capo_sagemaker.types.inference_component_runtime_config

        out["runtime_config"] = (
            capo_sagemaker.types.inference_component_runtime_config.deserialize_aws_json_1_1(
                data["RuntimeConfig"]
            )
        )
    if data.get("Tags") is not None:
        import capo_sagemaker.types.tag_list

        out["tags"] = capo_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
