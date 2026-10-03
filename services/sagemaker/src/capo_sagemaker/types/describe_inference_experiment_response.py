"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeInferenceExperimentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.endpoint_metadata
    import capo_sagemaker.types.inference_experiment_arn
    import capo_sagemaker.types.inference_experiment_data_storage_config
    import capo_sagemaker.types.inference_experiment_description
    import capo_sagemaker.types.inference_experiment_name
    import capo_sagemaker.types.inference_experiment_schedule
    import capo_sagemaker.types.inference_experiment_status
    import capo_sagemaker.types.inference_experiment_status_reason
    import capo_sagemaker.types.inference_experiment_type
    import capo_sagemaker.types.kms_key_id
    import capo_sagemaker.types.model_variant_config_summary_list
    import capo_sagemaker.types.role_arn
    import capo_sagemaker.types.shadow_mode_config
    import capo_sagemaker.types.timestamp


class DescribeInferenceExperimentResponse(TypedDict, closed=True):
    arn: NotRequired[
        "capo_sagemaker.types.inference_experiment_arn.InferenceExperimentArn"
    ]
    """<p>The ARN of the inference experiment being described.</p>"""
    name: NotRequired[
        "capo_sagemaker.types.inference_experiment_name.InferenceExperimentName"
    ]
    """<p>The name of the inference experiment.</p>"""
    type: NotRequired[
        "capo_sagemaker.types.inference_experiment_type.InferenceExperimentType"
    ]
    """<p>The type of the inference experiment.</p>"""
    schedule: NotRequired[
        "capo_sagemaker.types.inference_experiment_schedule.InferenceExperimentSchedule"
    ]
    """<p>The duration for which the inference experiment ran or will run.</p>"""
    status: NotRequired[
        "capo_sagemaker.types.inference_experiment_status.InferenceExperimentStatus"
    ]
    """<p> The status of the inference experiment. The following are the possible statuses for an inference experiment: </p> <ul> <li> <p> <code>Creating</code> - Amazon SageMaker is creating your experiment. </p> </li> <li> <p> <code>Created</code> - Amazon SageMaker has finished the creation of your experiment and will begin the experiment at the scheduled time. </p> </li> <li> <p> <code>Updating</code> - When you make changes to your experiment, your experiment shows as updating. </p> </li> <li> <p> <code>Starting</code> - Amazon SageMaker is beginning your experiment. </p> </li> <li> <p> <code>Running</code> - Your experiment is in progress. </p> </li> <li> <p> <code>Stopping</code> - Amazon SageMaker is stopping your experiment. </p> </li> <li> <p> <code>Completed</code> - Your experiment has completed. </p> </li> <li> <p> <code>Cancelled</code> - When you conclude your experiment early using the <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_StopInferenceExperiment.html">StopInferenceExperiment</a> API, or if any operation fails with an unexpected error, it shows as cancelled. </p> </li> </ul>"""
    status_reason: NotRequired[
        "capo_sagemaker.types.inference_experiment_status_reason.InferenceExperimentStatusReason"
    ]
    """<p> The error message or client-specified <code>Reason</code> from the <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_StopInferenceExperiment.html">StopInferenceExperiment</a> API, that explains the status of the inference experiment. </p>"""
    description: NotRequired[
        "capo_sagemaker.types.inference_experiment_description.InferenceExperimentDescription"
    ]
    """<p>The description of the inference experiment.</p>"""
    creation_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The timestamp at which you created the inference experiment.</p>"""
    completion_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p> The timestamp at which the inference experiment was completed. </p>"""
    last_modified_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The timestamp at which you last modified the inference experiment.</p>"""
    role_arn: NotRequired["capo_sagemaker.types.role_arn.RoleArn"]
    """<p> The ARN of the IAM role that Amazon SageMaker can assume to access model artifacts and container images, and manage Amazon SageMaker Inference endpoints for model deployment. </p>"""
    endpoint_metadata: NotRequired[
        "capo_sagemaker.types.endpoint_metadata.EndpointMetadata"
    ]
    """<p>The metadata of the endpoint on which the inference experiment ran.</p>"""
    model_variants: NotRequired[
        "capo_sagemaker.types.model_variant_config_summary_list.ModelVariantConfigSummaryList"
    ]
    """<p> An array of <code>ModelVariantConfigSummary</code> objects. There is one for each variant in the inference experiment. Each <code>ModelVariantConfigSummary</code> object in the array describes the infrastructure configuration for deploying the corresponding variant. </p>"""
    data_storage_config: NotRequired[
        "capo_sagemaker.types.inference_experiment_data_storage_config.InferenceExperimentDataStorageConfig"
    ]
    """<p>The Amazon S3 location and configuration for storing inference request and response data.</p>"""
    shadow_mode_config: NotRequired[
        "capo_sagemaker.types.shadow_mode_config.ShadowModeConfig"
    ]
    """<p> The configuration of <code>ShadowMode</code> inference experiment type, which shows the production variant that takes all the inference requests, and the shadow variant to which Amazon SageMaker replicates a percentage of the inference requests. For the shadow variant it also shows the percentage of requests that Amazon SageMaker replicates. </p>"""
    kms_key: NotRequired["capo_sagemaker.types.kms_key_id.KmsKeyId"]
    """<p> The Amazon Web Services Key Management Service (Amazon Web Services KMS) key that Amazon SageMaker uses to encrypt data on the storage volume attached to the ML compute instance that hosts the endpoint. For more information, see <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateInferenceExperiment.html">CreateInferenceExperiment</a>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeInferenceExperimentResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "type" in value:
        import capo_sagemaker.types.inference_experiment_type

        out["Type"] = (
            capo_sagemaker.types.inference_experiment_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    if "schedule" in value:
        import capo_sagemaker.types.inference_experiment_schedule

        out["Schedule"] = (
            capo_sagemaker.types.inference_experiment_schedule.serialize_aws_json_1_1(
                value["schedule"]
            )
        )
    if "status" in value:
        import capo_sagemaker.types.inference_experiment_status

        out["Status"] = (
            capo_sagemaker.types.inference_experiment_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "status_reason" in value:
        out["StatusReason"] = value["status_reason"]
    if "description" in value:
        out["Description"] = value["description"]
    if "creation_time" in value:
        import capo_sagemaker.types.timestamp

        out["CreationTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "completion_time" in value:
        import capo_sagemaker.types.timestamp

        out["CompletionTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["completion_time"]
        )
    if "last_modified_time" in value:
        import capo_sagemaker.types.timestamp

        out["LastModifiedTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["last_modified_time"]
        )
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "endpoint_metadata" in value:
        import capo_sagemaker.types.endpoint_metadata

        out["EndpointMetadata"] = (
            capo_sagemaker.types.endpoint_metadata.serialize_aws_json_1_1(
                value["endpoint_metadata"]
            )
        )
    if "model_variants" in value:
        import capo_sagemaker.types.model_variant_config_summary_list

        out["ModelVariants"] = (
            capo_sagemaker.types.model_variant_config_summary_list.serialize_aws_json_1_1(
                value["model_variants"]
            )
        )
    if "data_storage_config" in value:
        import capo_sagemaker.types.inference_experiment_data_storage_config

        out["DataStorageConfig"] = (
            capo_sagemaker.types.inference_experiment_data_storage_config.serialize_aws_json_1_1(
                value["data_storage_config"]
            )
        )
    if "shadow_mode_config" in value:
        import capo_sagemaker.types.shadow_mode_config

        out["ShadowModeConfig"] = (
            capo_sagemaker.types.shadow_mode_config.serialize_aws_json_1_1(
                value["shadow_mode_config"]
            )
        )
    if "kms_key" in value:
        out["KmsKey"] = value["kms_key"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeInferenceExperimentResponse:
    out: DescribeInferenceExperimentResponse = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Type") is not None:
        import capo_sagemaker.types.inference_experiment_type

        out["type"] = (
            capo_sagemaker.types.inference_experiment_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    if data.get("Schedule") is not None:
        import capo_sagemaker.types.inference_experiment_schedule

        out["schedule"] = (
            capo_sagemaker.types.inference_experiment_schedule.deserialize_aws_json_1_1(
                data["Schedule"]
            )
        )
    if data.get("Status") is not None:
        import capo_sagemaker.types.inference_experiment_status

        out["status"] = (
            capo_sagemaker.types.inference_experiment_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if data.get("StatusReason") is not None:
        out["status_reason"] = data["StatusReason"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("CreationTime") is not None:
        import capo_sagemaker.types.timestamp

        out["creation_time"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if data.get("CompletionTime") is not None:
        import capo_sagemaker.types.timestamp

        out["completion_time"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CompletionTime"]
            )
        )
    if data.get("LastModifiedTime") is not None:
        import capo_sagemaker.types.timestamp

        out["last_modified_time"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    if data.get("EndpointMetadata") is not None:
        import capo_sagemaker.types.endpoint_metadata

        out["endpoint_metadata"] = (
            capo_sagemaker.types.endpoint_metadata.deserialize_aws_json_1_1(
                data["EndpointMetadata"]
            )
        )
    if data.get("ModelVariants") is not None:
        import capo_sagemaker.types.model_variant_config_summary_list

        out["model_variants"] = (
            capo_sagemaker.types.model_variant_config_summary_list.deserialize_aws_json_1_1(
                data["ModelVariants"]
            )
        )
    if data.get("DataStorageConfig") is not None:
        import capo_sagemaker.types.inference_experiment_data_storage_config

        out["data_storage_config"] = (
            capo_sagemaker.types.inference_experiment_data_storage_config.deserialize_aws_json_1_1(
                data["DataStorageConfig"]
            )
        )
    if data.get("ShadowModeConfig") is not None:
        import capo_sagemaker.types.shadow_mode_config

        out["shadow_mode_config"] = (
            capo_sagemaker.types.shadow_mode_config.deserialize_aws_json_1_1(
                data["ShadowModeConfig"]
            )
        )
    if data.get("KmsKey") is not None:
        out["kms_key"] = data["KmsKey"]
    return out
