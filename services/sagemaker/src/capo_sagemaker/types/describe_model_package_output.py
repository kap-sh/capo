"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeModelPackageOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.additional_inference_specifications
    import capo_sagemaker.types.approval_description
    import capo_sagemaker.types.certify_for_marketplace
    import capo_sagemaker.types.creation_time
    import capo_sagemaker.types.customer_metadata_map
    import capo_sagemaker.types.drift_check_baselines
    import capo_sagemaker.types.entity_description
    import capo_sagemaker.types.entity_name
    import capo_sagemaker.types.inference_specification
    import capo_sagemaker.types.managed_storage_type
    import capo_sagemaker.types.metadata_properties
    import capo_sagemaker.types.model_approval_status
    import capo_sagemaker.types.model_life_cycle
    import capo_sagemaker.types.model_metrics
    import capo_sagemaker.types.model_package_arn
    import capo_sagemaker.types.model_package_model_card
    import capo_sagemaker.types.model_package_registration_type
    import capo_sagemaker.types.model_package_security_config
    import capo_sagemaker.types.model_package_source_uri
    import capo_sagemaker.types.model_package_status
    import capo_sagemaker.types.model_package_status_details
    import capo_sagemaker.types.model_package_validation_specification
    import capo_sagemaker.types.model_package_version
    import capo_sagemaker.types.skip_model_validation
    import capo_sagemaker.types.source_algorithm_specification
    import capo_sagemaker.types.string
    import capo_sagemaker.types.timestamp
    import capo_sagemaker.types.user_context


class DescribeModelPackageOutput(TypedDict, closed=True):
    model_package_name: NotRequired["capo_sagemaker.types.entity_name.EntityName"]
    """<p>The name of the model package being described.</p>"""
    model_package_group_name: NotRequired["capo_sagemaker.types.entity_name.EntityName"]
    """<p>If the model is a versioned model, the name of the model group that the versioned model belongs to.</p>"""
    model_package_version: NotRequired[
        "capo_sagemaker.types.model_package_version.ModelPackageVersion"
    ]
    """<p>The version of the model package.</p>"""
    model_package_registration_type: NotRequired[
        "capo_sagemaker.types.model_package_registration_type.ModelPackageRegistrationType"
    ]
    """<p> The package registration type of the model package output. </p>"""
    model_package_arn: NotRequired[
        "capo_sagemaker.types.model_package_arn.ModelPackageArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the model package.</p>"""
    model_package_description: NotRequired[
        "capo_sagemaker.types.entity_description.EntityDescription"
    ]
    """<p>A brief summary of the model package.</p>"""
    creation_time: NotRequired["capo_sagemaker.types.creation_time.CreationTime"]
    """<p>A timestamp specifying when the model package was created.</p>"""
    inference_specification: NotRequired[
        "capo_sagemaker.types.inference_specification.InferenceSpecification"
    ]
    """<p>Details about inference jobs that you can run with models based on this model package.</p>"""
    source_algorithm_specification: NotRequired[
        "capo_sagemaker.types.source_algorithm_specification.SourceAlgorithmSpecification"
    ]
    """<p>Details about the algorithm that was used to create the model package.</p>"""
    validation_specification: NotRequired[
        "capo_sagemaker.types.model_package_validation_specification.ModelPackageValidationSpecification"
    ]
    """<p>Configurations for one or more transform jobs that SageMaker runs to test the model package.</p>"""
    model_package_status: NotRequired[
        "capo_sagemaker.types.model_package_status.ModelPackageStatus"
    ]
    """<p>The current status of the model package.</p>"""
    model_package_status_details: NotRequired[
        "capo_sagemaker.types.model_package_status_details.ModelPackageStatusDetails"
    ]
    """<p>Details about the current status of the model package.</p>"""
    certify_for_marketplace: NotRequired[
        "capo_sagemaker.types.certify_for_marketplace.CertifyForMarketplace"
    ]
    """<p>Whether the model package is certified for listing on Amazon Web Services Marketplace.</p>"""
    model_approval_status: NotRequired[
        "capo_sagemaker.types.model_approval_status.ModelApprovalStatus"
    ]
    """<p>The approval status of the model package.</p>"""
    created_by: NotRequired["capo_sagemaker.types.user_context.UserContext"]
    metadata_properties: NotRequired[
        "capo_sagemaker.types.metadata_properties.MetadataProperties"
    ]
    model_metrics: NotRequired["capo_sagemaker.types.model_metrics.ModelMetrics"]
    """<p>Metrics for the model.</p>"""
    last_modified_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The last time that the model package was modified.</p>"""
    last_modified_by: NotRequired["capo_sagemaker.types.user_context.UserContext"]
    approval_description: NotRequired[
        "capo_sagemaker.types.approval_description.ApprovalDescription"
    ]
    """<p>A description provided for the model approval.</p>"""
    domain: NotRequired["capo_sagemaker.types.string.String"]
    """<p>The machine learning domain of the model package you specified. Common machine learning domains include computer vision and natural language processing.</p>"""
    task: NotRequired["capo_sagemaker.types.string.String"]
    """<p>The machine learning task you specified that your model package accomplishes. Common machine learning tasks include object detection and image classification.</p>"""
    sample_payload_url: NotRequired["capo_sagemaker.types.string.String"]
    """<p>The Amazon Simple Storage Service (Amazon S3) path where the sample payload are stored. This path points to a single gzip compressed tar archive (.tar.gz suffix).</p>"""
    customer_metadata_properties: NotRequired[
        "capo_sagemaker.types.customer_metadata_map.CustomerMetadataMap"
    ]
    """<p>The metadata properties associated with the model package versions.</p>"""
    drift_check_baselines: NotRequired[
        "capo_sagemaker.types.drift_check_baselines.DriftCheckBaselines"
    ]
    """<p>Represents the drift check baselines that can be used when the model monitor is set using the model package. For more information, see the topic on <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/pipelines-quality-clarify-baseline-lifecycle.html#pipelines-quality-clarify-baseline-drift-detection">Drift Detection against Previous Baselines in SageMaker Pipelines</a> in the <i>Amazon SageMaker Developer Guide</i>. </p>"""
    additional_inference_specifications: NotRequired[
        "capo_sagemaker.types.additional_inference_specifications.AdditionalInferenceSpecifications"
    ]
    """<p>An array of additional Inference Specification objects. Each additional Inference Specification specifies artifacts based on this model package that can be used on inference endpoints. Generally used with SageMaker Neo to store the compiled artifacts.</p>"""
    skip_model_validation: NotRequired[
        "capo_sagemaker.types.skip_model_validation.SkipModelValidation"
    ]
    """<p>Indicates if you want to skip model validation.</p>"""
    source_uri: NotRequired[
        "capo_sagemaker.types.model_package_source_uri.ModelPackageSourceUri"
    ]
    """<p>The URI of the source for the model package.</p>"""
    security_config: NotRequired[
        "capo_sagemaker.types.model_package_security_config.ModelPackageSecurityConfig"
    ]
    """<p>The KMS Key ID (<code>KMSKeyId</code>) used for encryption of model package information.</p>"""
    model_card: NotRequired[
        "capo_sagemaker.types.model_package_model_card.ModelPackageModelCard"
    ]
    """<p>The model card associated with the model package. Since <code>ModelPackageModelCard</code> is tied to a model package, it is a specific usage of a model card and its schema is simplified compared to the schema of <code>ModelCard</code>. The <code>ModelPackageModelCard</code> schema does not include <code>model_package_details</code>, and <code>model_overview</code> is composed of the <code>model_creator</code> and <code>model_artifact</code> properties. For more information about the model package model card schema, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry-details.html#model-card-schema">Model package model card schema</a>. For more information about the model card associated with the model package, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry-details.html">View the Details of a Model Version</a>.</p> <p>When you set <code>IncludedData</code> to <code>MetadataOnly</code> in the request, <code>ModelCardStatus</code> is preserved and <code>ModelCardContent</code> is sanitized to include only the following JSON paths, when present in the model card:</p> <ul> <li> <p> <code>model_overview.model_id</code> </p> </li> <li> <p> <code>model_overview.model_name</code> </p> </li> <li> <p> <code>intended_uses.risk_rating</code> </p> </li> <li> <p> <code>model_package_details.model_package_group_name</code> </p> </li> <li> <p> <code>model_package_details.model_package_arn</code> </p> </li> </ul> <p>Because the <code>ModelPackageModelCard</code> schema does not include <code>model_package_details</code> and limits <code>model_overview</code> to <code>model_creator</code> and <code>model_artifact</code>, the sanitized <code>ModelCardContent</code> for a model package typically contains only <code>intended_uses.risk_rating</code> if it was provided when the model card was created. To retrieve the complete <code>ModelCardContent</code>, set <code>IncludedData</code> to <code>AllData</code> or omit the parameter.</p>"""
    model_life_cycle: NotRequired[
        "capo_sagemaker.types.model_life_cycle.ModelLifeCycle"
    ]
    """<p> A structure describing the current state of the model in its life cycle. </p>"""
    managed_storage_type: NotRequired[
        "capo_sagemaker.types.managed_storage_type.ManagedStorageType"
    ]
    """<p>The storage type of the model package.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeModelPackageOutput) -> dict:
    out: dict = {}
    if "model_package_name" in value:
        out["ModelPackageName"] = value["model_package_name"]
    if "model_package_group_name" in value:
        out["ModelPackageGroupName"] = value["model_package_group_name"]
    if "model_package_version" in value:
        out["ModelPackageVersion"] = value["model_package_version"]
    if "model_package_registration_type" in value:
        import capo_sagemaker.types.model_package_registration_type

        out["ModelPackageRegistrationType"] = (
            capo_sagemaker.types.model_package_registration_type.serialize_aws_json_1_1(
                value["model_package_registration_type"]
            )
        )
    if "model_package_arn" in value:
        out["ModelPackageArn"] = value["model_package_arn"]
    if "model_package_description" in value:
        out["ModelPackageDescription"] = value["model_package_description"]
    if "creation_time" in value:
        import capo_sagemaker.types.creation_time

        out["CreationTime"] = capo_sagemaker.types.creation_time.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "inference_specification" in value:
        import capo_sagemaker.types.inference_specification

        out["InferenceSpecification"] = (
            capo_sagemaker.types.inference_specification.serialize_aws_json_1_1(
                value["inference_specification"]
            )
        )
    if "source_algorithm_specification" in value:
        import capo_sagemaker.types.source_algorithm_specification

        out["SourceAlgorithmSpecification"] = (
            capo_sagemaker.types.source_algorithm_specification.serialize_aws_json_1_1(
                value["source_algorithm_specification"]
            )
        )
    if "validation_specification" in value:
        import capo_sagemaker.types.model_package_validation_specification

        out["ValidationSpecification"] = (
            capo_sagemaker.types.model_package_validation_specification.serialize_aws_json_1_1(
                value["validation_specification"]
            )
        )
    if "model_package_status" in value:
        import capo_sagemaker.types.model_package_status

        out["ModelPackageStatus"] = (
            capo_sagemaker.types.model_package_status.serialize_aws_json_1_1(
                value["model_package_status"]
            )
        )
    if "model_package_status_details" in value:
        import capo_sagemaker.types.model_package_status_details

        out["ModelPackageStatusDetails"] = (
            capo_sagemaker.types.model_package_status_details.serialize_aws_json_1_1(
                value["model_package_status_details"]
            )
        )
    if "certify_for_marketplace" in value:
        out["CertifyForMarketplace"] = value["certify_for_marketplace"]
    if "model_approval_status" in value:
        import capo_sagemaker.types.model_approval_status

        out["ModelApprovalStatus"] = (
            capo_sagemaker.types.model_approval_status.serialize_aws_json_1_1(
                value["model_approval_status"]
            )
        )
    if "created_by" in value:
        import capo_sagemaker.types.user_context

        out["CreatedBy"] = capo_sagemaker.types.user_context.serialize_aws_json_1_1(
            value["created_by"]
        )
    if "metadata_properties" in value:
        import capo_sagemaker.types.metadata_properties

        out["MetadataProperties"] = (
            capo_sagemaker.types.metadata_properties.serialize_aws_json_1_1(
                value["metadata_properties"]
            )
        )
    if "model_metrics" in value:
        import capo_sagemaker.types.model_metrics

        out["ModelMetrics"] = capo_sagemaker.types.model_metrics.serialize_aws_json_1_1(
            value["model_metrics"]
        )
    if "last_modified_time" in value:
        import capo_sagemaker.types.timestamp

        out["LastModifiedTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["last_modified_time"]
        )
    if "last_modified_by" in value:
        import capo_sagemaker.types.user_context

        out["LastModifiedBy"] = (
            capo_sagemaker.types.user_context.serialize_aws_json_1_1(
                value["last_modified_by"]
            )
        )
    if "approval_description" in value:
        out["ApprovalDescription"] = value["approval_description"]
    if "domain" in value:
        out["Domain"] = value["domain"]
    if "task" in value:
        out["Task"] = value["task"]
    if "sample_payload_url" in value:
        out["SamplePayloadUrl"] = value["sample_payload_url"]
    if "customer_metadata_properties" in value:
        import capo_sagemaker.types.customer_metadata_map

        out["CustomerMetadataProperties"] = (
            capo_sagemaker.types.customer_metadata_map.serialize_aws_json_1_1(
                value["customer_metadata_properties"]
            )
        )
    if "drift_check_baselines" in value:
        import capo_sagemaker.types.drift_check_baselines

        out["DriftCheckBaselines"] = (
            capo_sagemaker.types.drift_check_baselines.serialize_aws_json_1_1(
                value["drift_check_baselines"]
            )
        )
    if "additional_inference_specifications" in value:
        import capo_sagemaker.types.additional_inference_specifications

        out["AdditionalInferenceSpecifications"] = (
            capo_sagemaker.types.additional_inference_specifications.serialize_aws_json_1_1(
                value["additional_inference_specifications"]
            )
        )
    if "skip_model_validation" in value:
        import capo_sagemaker.types.skip_model_validation

        out["SkipModelValidation"] = (
            capo_sagemaker.types.skip_model_validation.serialize_aws_json_1_1(
                value["skip_model_validation"]
            )
        )
    if "source_uri" in value:
        out["SourceUri"] = value["source_uri"]
    if "security_config" in value:
        import capo_sagemaker.types.model_package_security_config

        out["SecurityConfig"] = (
            capo_sagemaker.types.model_package_security_config.serialize_aws_json_1_1(
                value["security_config"]
            )
        )
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
    if "managed_storage_type" in value:
        import capo_sagemaker.types.managed_storage_type

        out["ManagedStorageType"] = (
            capo_sagemaker.types.managed_storage_type.serialize_aws_json_1_1(
                value["managed_storage_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeModelPackageOutput:
    out: DescribeModelPackageOutput = {}  # type: ignore[typeddict-item]
    if data.get("ModelPackageName") is not None:
        out["model_package_name"] = data["ModelPackageName"]
    if data.get("ModelPackageGroupName") is not None:
        out["model_package_group_name"] = data["ModelPackageGroupName"]
    if data.get("ModelPackageVersion") is not None:
        out["model_package_version"] = data["ModelPackageVersion"]
    if data.get("ModelPackageRegistrationType") is not None:
        import capo_sagemaker.types.model_package_registration_type

        out["model_package_registration_type"] = (
            capo_sagemaker.types.model_package_registration_type.deserialize_aws_json_1_1(
                data["ModelPackageRegistrationType"]
            )
        )
    if data.get("ModelPackageArn") is not None:
        out["model_package_arn"] = data["ModelPackageArn"]
    if data.get("ModelPackageDescription") is not None:
        out["model_package_description"] = data["ModelPackageDescription"]
    if data.get("CreationTime") is not None:
        import capo_sagemaker.types.creation_time

        out["creation_time"] = (
            capo_sagemaker.types.creation_time.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if data.get("InferenceSpecification") is not None:
        import capo_sagemaker.types.inference_specification

        out["inference_specification"] = (
            capo_sagemaker.types.inference_specification.deserialize_aws_json_1_1(
                data["InferenceSpecification"]
            )
        )
    if data.get("SourceAlgorithmSpecification") is not None:
        import capo_sagemaker.types.source_algorithm_specification

        out["source_algorithm_specification"] = (
            capo_sagemaker.types.source_algorithm_specification.deserialize_aws_json_1_1(
                data["SourceAlgorithmSpecification"]
            )
        )
    if data.get("ValidationSpecification") is not None:
        import capo_sagemaker.types.model_package_validation_specification

        out["validation_specification"] = (
            capo_sagemaker.types.model_package_validation_specification.deserialize_aws_json_1_1(
                data["ValidationSpecification"]
            )
        )
    if data.get("ModelPackageStatus") is not None:
        import capo_sagemaker.types.model_package_status

        out["model_package_status"] = (
            capo_sagemaker.types.model_package_status.deserialize_aws_json_1_1(
                data["ModelPackageStatus"]
            )
        )
    if data.get("ModelPackageStatusDetails") is not None:
        import capo_sagemaker.types.model_package_status_details

        out["model_package_status_details"] = (
            capo_sagemaker.types.model_package_status_details.deserialize_aws_json_1_1(
                data["ModelPackageStatusDetails"]
            )
        )
    if data.get("CertifyForMarketplace") is not None:
        out["certify_for_marketplace"] = data["CertifyForMarketplace"]
    if data.get("ModelApprovalStatus") is not None:
        import capo_sagemaker.types.model_approval_status

        out["model_approval_status"] = (
            capo_sagemaker.types.model_approval_status.deserialize_aws_json_1_1(
                data["ModelApprovalStatus"]
            )
        )
    if data.get("CreatedBy") is not None:
        import capo_sagemaker.types.user_context

        out["created_by"] = capo_sagemaker.types.user_context.deserialize_aws_json_1_1(
            data["CreatedBy"]
        )
    if data.get("MetadataProperties") is not None:
        import capo_sagemaker.types.metadata_properties

        out["metadata_properties"] = (
            capo_sagemaker.types.metadata_properties.deserialize_aws_json_1_1(
                data["MetadataProperties"]
            )
        )
    if data.get("ModelMetrics") is not None:
        import capo_sagemaker.types.model_metrics

        out["model_metrics"] = (
            capo_sagemaker.types.model_metrics.deserialize_aws_json_1_1(
                data["ModelMetrics"]
            )
        )
    if data.get("LastModifiedTime") is not None:
        import capo_sagemaker.types.timestamp

        out["last_modified_time"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if data.get("LastModifiedBy") is not None:
        import capo_sagemaker.types.user_context

        out["last_modified_by"] = (
            capo_sagemaker.types.user_context.deserialize_aws_json_1_1(
                data["LastModifiedBy"]
            )
        )
    if data.get("ApprovalDescription") is not None:
        out["approval_description"] = data["ApprovalDescription"]
    if data.get("Domain") is not None:
        out["domain"] = data["Domain"]
    if data.get("Task") is not None:
        out["task"] = data["Task"]
    if data.get("SamplePayloadUrl") is not None:
        out["sample_payload_url"] = data["SamplePayloadUrl"]
    if data.get("CustomerMetadataProperties") is not None:
        import capo_sagemaker.types.customer_metadata_map

        out["customer_metadata_properties"] = (
            capo_sagemaker.types.customer_metadata_map.deserialize_aws_json_1_1(
                data["CustomerMetadataProperties"]
            )
        )
    if data.get("DriftCheckBaselines") is not None:
        import capo_sagemaker.types.drift_check_baselines

        out["drift_check_baselines"] = (
            capo_sagemaker.types.drift_check_baselines.deserialize_aws_json_1_1(
                data["DriftCheckBaselines"]
            )
        )
    if data.get("AdditionalInferenceSpecifications") is not None:
        import capo_sagemaker.types.additional_inference_specifications

        out["additional_inference_specifications"] = (
            capo_sagemaker.types.additional_inference_specifications.deserialize_aws_json_1_1(
                data["AdditionalInferenceSpecifications"]
            )
        )
    if data.get("SkipModelValidation") is not None:
        import capo_sagemaker.types.skip_model_validation

        out["skip_model_validation"] = (
            capo_sagemaker.types.skip_model_validation.deserialize_aws_json_1_1(
                data["SkipModelValidation"]
            )
        )
    if data.get("SourceUri") is not None:
        out["source_uri"] = data["SourceUri"]
    if data.get("SecurityConfig") is not None:
        import capo_sagemaker.types.model_package_security_config

        out["security_config"] = (
            capo_sagemaker.types.model_package_security_config.deserialize_aws_json_1_1(
                data["SecurityConfig"]
            )
        )
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
    if data.get("ManagedStorageType") is not None:
        import capo_sagemaker.types.managed_storage_type

        out["managed_storage_type"] = (
            capo_sagemaker.types.managed_storage_type.deserialize_aws_json_1_1(
                data["ManagedStorageType"]
            )
        )
    return out
