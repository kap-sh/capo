"""Generated from Smithy shape ``com.amazonaws.sagemaker#UpdateModelPackageInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.additional_inference_specifications
    import capo_sagemaker.types.approval_description
    import capo_sagemaker.types.client_token
    import capo_sagemaker.types.customer_metadata_key_list
    import capo_sagemaker.types.customer_metadata_map
    import capo_sagemaker.types.inference_specification
    import capo_sagemaker.types.model_approval_status
    import capo_sagemaker.types.model_life_cycle
    import capo_sagemaker.types.model_package_arn
    import capo_sagemaker.types.model_package_model_card
    import capo_sagemaker.types.model_package_registration_type
    import capo_sagemaker.types.model_package_source_uri


class UpdateModelPackageInput(TypedDict, closed=True):
    model_package_arn: NotRequired[
        "capo_sagemaker.types.model_package_arn.ModelPackageArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the model package.</p>"""
    model_approval_status: NotRequired[
        "capo_sagemaker.types.model_approval_status.ModelApprovalStatus"
    ]
    """<p>The approval status of the model.</p>"""
    model_package_registration_type: NotRequired[
        "capo_sagemaker.types.model_package_registration_type.ModelPackageRegistrationType"
    ]
    """<p> The package registration type of the model package input. </p>"""
    approval_description: NotRequired[
        "capo_sagemaker.types.approval_description.ApprovalDescription"
    ]
    """<p>A description for the approval status of the model.</p>"""
    customer_metadata_properties: NotRequired[
        "capo_sagemaker.types.customer_metadata_map.CustomerMetadataMap"
    ]
    """<p>The metadata properties associated with the model package versions.</p>"""
    customer_metadata_properties_to_remove: NotRequired[
        "capo_sagemaker.types.customer_metadata_key_list.CustomerMetadataKeyList"
    ]
    """<p>The metadata properties associated with the model package versions to remove.</p>"""
    additional_inference_specifications_to_add: NotRequired[
        "capo_sagemaker.types.additional_inference_specifications.AdditionalInferenceSpecifications"
    ]
    """<p>An array of additional Inference Specification objects to be added to the existing array additional Inference Specification. Total number of additional Inference Specifications can not exceed 15. Each additional Inference Specification specifies artifacts based on this model package that can be used on inference endpoints. Generally used with SageMaker Neo to store the compiled artifacts.</p>"""
    inference_specification: NotRequired[
        "capo_sagemaker.types.inference_specification.InferenceSpecification"
    ]
    """<p>Specifies details about inference jobs that you can run with models based on this model package, including the following information:</p> <ul> <li> <p>The Amazon ECR paths of containers that contain the inference code and model artifacts.</p> </li> <li> <p>The instance types that the model package supports for transform jobs and real-time endpoints used for inference.</p> </li> <li> <p>The input and output content formats that the model package supports for inference.</p> </li> </ul>"""
    source_uri: NotRequired[
        "capo_sagemaker.types.model_package_source_uri.ModelPackageSourceUri"
    ]
    """<p>The URI of the source for the model package.</p>"""
    model_card: NotRequired[
        "capo_sagemaker.types.model_package_model_card.ModelPackageModelCard"
    ]
    """<p>The model card associated with the model package. Since <code>ModelPackageModelCard</code> is tied to a model package, it is a specific usage of a model card and its schema is simplified compared to the schema of <code>ModelCard</code>. The <code>ModelPackageModelCard</code> schema does not include <code>model_package_details</code>, and <code>model_overview</code> is composed of the <code>model_creator</code> and <code>model_artifact</code> properties. For more information about the model package model card schema, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry-details.html#model-card-schema">Model package model card schema</a>. For more information about the model card associated with the model package, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry-details.html">View the Details of a Model Version</a>.</p>"""
    model_life_cycle: NotRequired[
        "capo_sagemaker.types.model_life_cycle.ModelLifeCycle"
    ]
    """<p> A structure describing the current state of the model in its life cycle. </p>"""
    client_token: NotRequired["capo_sagemaker.types.client_token.ClientToken"]
    """<p> A unique token that guarantees that the call to this API is idempotent. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateModelPackageInput) -> dict:
    out: dict = {}
    if "model_package_arn" in value:
        out["ModelPackageArn"] = value["model_package_arn"]
    if "model_approval_status" in value:
        import capo_sagemaker.types.model_approval_status

        out["ModelApprovalStatus"] = (
            capo_sagemaker.types.model_approval_status.serialize_aws_json_1_1(
                value["model_approval_status"]
            )
        )
    if "model_package_registration_type" in value:
        import capo_sagemaker.types.model_package_registration_type

        out["ModelPackageRegistrationType"] = (
            capo_sagemaker.types.model_package_registration_type.serialize_aws_json_1_1(
                value["model_package_registration_type"]
            )
        )
    if "approval_description" in value:
        out["ApprovalDescription"] = value["approval_description"]
    if "customer_metadata_properties" in value:
        import capo_sagemaker.types.customer_metadata_map

        out["CustomerMetadataProperties"] = (
            capo_sagemaker.types.customer_metadata_map.serialize_aws_json_1_1(
                value["customer_metadata_properties"]
            )
        )
    if "customer_metadata_properties_to_remove" in value:
        import capo_sagemaker.types.customer_metadata_key_list

        out["CustomerMetadataPropertiesToRemove"] = (
            capo_sagemaker.types.customer_metadata_key_list.serialize_aws_json_1_1(
                value["customer_metadata_properties_to_remove"]
            )
        )
    if "additional_inference_specifications_to_add" in value:
        import capo_sagemaker.types.additional_inference_specifications

        out["AdditionalInferenceSpecificationsToAdd"] = (
            capo_sagemaker.types.additional_inference_specifications.serialize_aws_json_1_1(
                value["additional_inference_specifications_to_add"]
            )
        )
    if "inference_specification" in value:
        import capo_sagemaker.types.inference_specification

        out["InferenceSpecification"] = (
            capo_sagemaker.types.inference_specification.serialize_aws_json_1_1(
                value["inference_specification"]
            )
        )
    if "source_uri" in value:
        out["SourceUri"] = value["source_uri"]
    if "model_card" in value:
        import capo_sagemaker.types.model_package_model_card

        out["ModelCard"] = (
            capo_sagemaker.types.model_package_model_card.serialize_aws_json_1_1(
                value["model_card"]
            )
        )
    if "model_life_cycle" in value:
        import capo_sagemaker.types.model_life_cycle

        out["ModelLifeCycle"] = (
            capo_sagemaker.types.model_life_cycle.serialize_aws_json_1_1(
                value["model_life_cycle"]
            )
        )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateModelPackageInput:
    out: UpdateModelPackageInput = {}  # type: ignore[typeddict-item]
    if data.get("ModelPackageArn") is not None:
        out["model_package_arn"] = data["ModelPackageArn"]
    if data.get("ModelApprovalStatus") is not None:
        import capo_sagemaker.types.model_approval_status

        out["model_approval_status"] = (
            capo_sagemaker.types.model_approval_status.deserialize_aws_json_1_1(
                data["ModelApprovalStatus"]
            )
        )
    if data.get("ModelPackageRegistrationType") is not None:
        import capo_sagemaker.types.model_package_registration_type

        out["model_package_registration_type"] = (
            capo_sagemaker.types.model_package_registration_type.deserialize_aws_json_1_1(
                data["ModelPackageRegistrationType"]
            )
        )
    if data.get("ApprovalDescription") is not None:
        out["approval_description"] = data["ApprovalDescription"]
    if data.get("CustomerMetadataProperties") is not None:
        import capo_sagemaker.types.customer_metadata_map

        out["customer_metadata_properties"] = (
            capo_sagemaker.types.customer_metadata_map.deserialize_aws_json_1_1(
                data["CustomerMetadataProperties"]
            )
        )
    if data.get("CustomerMetadataPropertiesToRemove") is not None:
        import capo_sagemaker.types.customer_metadata_key_list

        out["customer_metadata_properties_to_remove"] = (
            capo_sagemaker.types.customer_metadata_key_list.deserialize_aws_json_1_1(
                data["CustomerMetadataPropertiesToRemove"]
            )
        )
    if data.get("AdditionalInferenceSpecificationsToAdd") is not None:
        import capo_sagemaker.types.additional_inference_specifications

        out["additional_inference_specifications_to_add"] = (
            capo_sagemaker.types.additional_inference_specifications.deserialize_aws_json_1_1(
                data["AdditionalInferenceSpecificationsToAdd"]
            )
        )
    if data.get("InferenceSpecification") is not None:
        import capo_sagemaker.types.inference_specification

        out["inference_specification"] = (
            capo_sagemaker.types.inference_specification.deserialize_aws_json_1_1(
                data["InferenceSpecification"]
            )
        )
    if data.get("SourceUri") is not None:
        out["source_uri"] = data["SourceUri"]
    if data.get("ModelCard") is not None:
        import capo_sagemaker.types.model_package_model_card

        out["model_card"] = (
            capo_sagemaker.types.model_package_model_card.deserialize_aws_json_1_1(
                data["ModelCard"]
            )
        )
    if data.get("ModelLifeCycle") is not None:
        import capo_sagemaker.types.model_life_cycle

        out["model_life_cycle"] = (
            capo_sagemaker.types.model_life_cycle.deserialize_aws_json_1_1(
                data["ModelLifeCycle"]
            )
        )
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out
