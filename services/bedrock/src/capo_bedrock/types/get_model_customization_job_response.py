"""Generated from Smithy shape ``com.amazonaws.bedrock#GetModelCustomizationJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.custom_model_arn
    import capo_bedrock.types.custom_model_name
    import capo_bedrock.types.customization_config
    import capo_bedrock.types.customization_type
    import capo_bedrock.types.error_message
    import capo_bedrock.types.foundation_model_arn
    import capo_bedrock.types.idempotency_token
    import capo_bedrock.types.job_name
    import capo_bedrock.types.kms_key_arn
    import capo_bedrock.types.model_customization_hyper_parameters
    import capo_bedrock.types.model_customization_job_arn
    import capo_bedrock.types.model_customization_job_status
    import capo_bedrock.types.output_data_config
    import capo_bedrock.types.role_arn
    import capo_bedrock.types.status_details
    import capo_bedrock.types.timestamp
    import capo_bedrock.types.training_data_config
    import capo_bedrock.types.training_metrics
    import capo_bedrock.types.validation_data_config
    import capo_bedrock.types.validation_metrics
    import capo_bedrock.types.vpc_config


class GetModelCustomizationJobResponse(TypedDict, closed=True):
    job_arn: "capo_bedrock.types.model_customization_job_arn.ModelCustomizationJobArn"
    """<p>The Amazon Resource Name (ARN) of the customization job.</p>"""
    job_name: "capo_bedrock.types.job_name.JobName"
    """<p>The name of the customization job.</p>"""
    output_model_name: "capo_bedrock.types.custom_model_name.CustomModelName"
    """<p>The name of the output model.</p>"""
    output_model_arn: NotRequired["capo_bedrock.types.custom_model_arn.CustomModelArn"]
    """<p>The Amazon Resource Name (ARN) of the output model.</p>"""
    client_request_token: NotRequired[
        "capo_bedrock.types.idempotency_token.IdempotencyToken"
    ]
    """<p>The token that you specified in the <code>CreateCustomizationJob</code> request.</p>"""
    role_arn: "capo_bedrock.types.role_arn.RoleArn"
    """<p>The Amazon Resource Name (ARN) of the IAM role.</p>"""
    status: NotRequired[
        "capo_bedrock.types.model_customization_job_status.ModelCustomizationJobStatus"
    ]
    """<p>The status of the job. A successful job transitions from in-progress to completed when the output model is ready to use. If the job failed, the failure message contains information about why the job failed.</p>"""
    status_details: NotRequired["capo_bedrock.types.status_details.StatusDetails"]
    """<p>For a Distillation job, the details about the statuses of the sub-tasks of the customization job. </p>"""
    failure_message: NotRequired["capo_bedrock.types.error_message.ErrorMessage"]
    """<p>Information about why the job failed.</p>"""
    creation_time: "capo_bedrock.types.timestamp.Timestamp"
    """<p>Time that the resource was created.</p>"""
    last_modified_time: NotRequired["capo_bedrock.types.timestamp.Timestamp"]
    """<p>Time that the resource was last modified.</p>"""
    end_time: NotRequired["capo_bedrock.types.timestamp.Timestamp"]
    """<p>Time that the resource transitioned to terminal state.</p>"""
    base_model_arn: "capo_bedrock.types.foundation_model_arn.FoundationModelArn"
    """<p>Amazon Resource Name (ARN) of the base model.</p>"""
    hyper_parameters: NotRequired[
        "capo_bedrock.types.model_customization_hyper_parameters.ModelCustomizationHyperParameters"
    ]
    """<p>The hyperparameter values for the job. For details on the format for different models, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models-hp.html">Custom model hyperparameters</a>.</p>"""
    training_data_config: "capo_bedrock.types.training_data_config.TrainingDataConfig"
    """<p>Contains information about the training dataset.</p>"""
    validation_data_config: (
        "capo_bedrock.types.validation_data_config.ValidationDataConfig"
    )
    """<p>Contains information about the validation dataset.</p>"""
    output_data_config: "capo_bedrock.types.output_data_config.OutputDataConfig"
    """<p>Output data configuration </p>"""
    customization_type: NotRequired[
        "capo_bedrock.types.customization_type.CustomizationType"
    ]
    """<p>The type of model customization.</p>"""
    output_model_kms_key_arn: NotRequired["capo_bedrock.types.kms_key_arn.KmsKeyArn"]
    """<p>The custom model is encrypted at rest using this key.</p>"""
    training_metrics: NotRequired["capo_bedrock.types.training_metrics.TrainingMetrics"]
    """<p>Contains training metrics from the job creation.</p>"""
    validation_metrics: NotRequired[
        "capo_bedrock.types.validation_metrics.ValidationMetrics"
    ]
    """<p>The loss metric for each validator that you provided in the createjob request.</p>"""
    vpc_config: NotRequired["capo_bedrock.types.vpc_config.VpcConfig"]
    """<p>VPC configuration for the custom model job.</p>"""
    customization_config: NotRequired[
        "capo_bedrock.types.customization_config.CustomizationConfig"
    ]
    """<p>The customization configuration for the model customization job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetModelCustomizationJobResponse) -> dict:
    out: dict = {}
    out["jobArn"] = value["job_arn"]
    out["jobName"] = value["job_name"]
    out["outputModelName"] = value["output_model_name"]
    if "output_model_arn" in value:
        out["outputModelArn"] = value["output_model_arn"]
    if "client_request_token" in value:
        out["clientRequestToken"] = value["client_request_token"]
    out["roleArn"] = value["role_arn"]
    if "status" in value:
        import capo_bedrock.types.model_customization_job_status

        out["status"] = (
            capo_bedrock.types.model_customization_job_status.serialize_json(
                value["status"]
            )
        )
    if "status_details" in value:
        import capo_bedrock.types.status_details

        out["statusDetails"] = capo_bedrock.types.status_details.serialize_json(
            value["status_details"]
        )
    if "failure_message" in value:
        out["failureMessage"] = value["failure_message"]
    import capo_bedrock.types.timestamp

    out["creationTime"] = capo_bedrock.types.timestamp.serialize_json(
        value["creation_time"]
    )
    if "last_modified_time" in value:
        import capo_bedrock.types.timestamp

        out["lastModifiedTime"] = capo_bedrock.types.timestamp.serialize_json(
            value["last_modified_time"]
        )
    if "end_time" in value:
        import capo_bedrock.types.timestamp

        out["endTime"] = capo_bedrock.types.timestamp.serialize_json(value["end_time"])
    out["baseModelArn"] = value["base_model_arn"]
    if "hyper_parameters" in value:
        import capo_bedrock.types.model_customization_hyper_parameters

        out["hyperParameters"] = (
            capo_bedrock.types.model_customization_hyper_parameters.serialize_json(
                value["hyper_parameters"]
            )
        )
    import capo_bedrock.types.training_data_config

    out["trainingDataConfig"] = capo_bedrock.types.training_data_config.serialize_json(
        value["training_data_config"]
    )
    import capo_bedrock.types.validation_data_config

    out["validationDataConfig"] = (
        capo_bedrock.types.validation_data_config.serialize_json(
            value["validation_data_config"]
        )
    )
    import capo_bedrock.types.output_data_config

    out["outputDataConfig"] = capo_bedrock.types.output_data_config.serialize_json(
        value["output_data_config"]
    )
    if "customization_type" in value:
        import capo_bedrock.types.customization_type

        out["customizationType"] = capo_bedrock.types.customization_type.serialize_json(
            value["customization_type"]
        )
    if "output_model_kms_key_arn" in value:
        out["outputModelKmsKeyArn"] = value["output_model_kms_key_arn"]
    if "training_metrics" in value:
        import capo_bedrock.types.training_metrics

        out["trainingMetrics"] = capo_bedrock.types.training_metrics.serialize_json(
            value["training_metrics"]
        )
    if "validation_metrics" in value:
        import capo_bedrock.types.validation_metrics

        out["validationMetrics"] = capo_bedrock.types.validation_metrics.serialize_json(
            value["validation_metrics"]
        )
    if "vpc_config" in value:
        import capo_bedrock.types.vpc_config

        out["vpcConfig"] = capo_bedrock.types.vpc_config.serialize_json(
            value["vpc_config"]
        )
    if "customization_config" in value:
        import capo_bedrock.types.customization_config

        out["customizationConfig"] = (
            capo_bedrock.types.customization_config.serialize_json(
                value["customization_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetModelCustomizationJobResponse:
    out: GetModelCustomizationJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("jobArn") is not None:
        out["job_arn"] = data["jobArn"]
    else:
        raise DeserializationError("GetModelCustomizationJobResponse.job_arn required")
    if data.get("jobName") is not None:
        out["job_name"] = data["jobName"]
    else:
        raise DeserializationError("GetModelCustomizationJobResponse.job_name required")
    if data.get("outputModelName") is not None:
        out["output_model_name"] = data["outputModelName"]
    else:
        raise DeserializationError(
            "GetModelCustomizationJobResponse.output_model_name required"
        )
    if data.get("outputModelArn") is not None:
        out["output_model_arn"] = data["outputModelArn"]
    if data.get("clientRequestToken") is not None:
        out["client_request_token"] = data["clientRequestToken"]
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("GetModelCustomizationJobResponse.role_arn required")
    if data.get("status") is not None:
        import capo_bedrock.types.model_customization_job_status

        out["status"] = (
            capo_bedrock.types.model_customization_job_status.deserialize_json(
                data["status"]
            )
        )
    if data.get("statusDetails") is not None:
        import capo_bedrock.types.status_details

        out["status_details"] = capo_bedrock.types.status_details.deserialize_json(
            data["statusDetails"]
        )
    if data.get("failureMessage") is not None:
        out["failure_message"] = data["failureMessage"]
    if data.get("creationTime") is not None:
        import capo_bedrock.types.timestamp

        out["creation_time"] = capo_bedrock.types.timestamp.deserialize_json(
            data["creationTime"]
        )
    else:
        raise DeserializationError(
            "GetModelCustomizationJobResponse.creation_time required"
        )
    if data.get("lastModifiedTime") is not None:
        import capo_bedrock.types.timestamp

        out["last_modified_time"] = capo_bedrock.types.timestamp.deserialize_json(
            data["lastModifiedTime"]
        )
    if data.get("endTime") is not None:
        import capo_bedrock.types.timestamp

        out["end_time"] = capo_bedrock.types.timestamp.deserialize_json(data["endTime"])
    if data.get("baseModelArn") is not None:
        out["base_model_arn"] = data["baseModelArn"]
    else:
        raise DeserializationError(
            "GetModelCustomizationJobResponse.base_model_arn required"
        )
    if data.get("hyperParameters") is not None:
        import capo_bedrock.types.model_customization_hyper_parameters

        out["hyper_parameters"] = (
            capo_bedrock.types.model_customization_hyper_parameters.deserialize_json(
                data["hyperParameters"]
            )
        )
    if data.get("trainingDataConfig") is not None:
        import capo_bedrock.types.training_data_config

        out["training_data_config"] = (
            capo_bedrock.types.training_data_config.deserialize_json(
                data["trainingDataConfig"]
            )
        )
    else:
        raise DeserializationError(
            "GetModelCustomizationJobResponse.training_data_config required"
        )
    if data.get("validationDataConfig") is not None:
        import capo_bedrock.types.validation_data_config

        out["validation_data_config"] = (
            capo_bedrock.types.validation_data_config.deserialize_json(
                data["validationDataConfig"]
            )
        )
    else:
        raise DeserializationError(
            "GetModelCustomizationJobResponse.validation_data_config required"
        )
    if data.get("outputDataConfig") is not None:
        import capo_bedrock.types.output_data_config

        out["output_data_config"] = (
            capo_bedrock.types.output_data_config.deserialize_json(
                data["outputDataConfig"]
            )
        )
    else:
        raise DeserializationError(
            "GetModelCustomizationJobResponse.output_data_config required"
        )
    if data.get("customizationType") is not None:
        import capo_bedrock.types.customization_type

        out["customization_type"] = (
            capo_bedrock.types.customization_type.deserialize_json(
                data["customizationType"]
            )
        )
    if data.get("outputModelKmsKeyArn") is not None:
        out["output_model_kms_key_arn"] = data["outputModelKmsKeyArn"]
    if data.get("trainingMetrics") is not None:
        import capo_bedrock.types.training_metrics

        out["training_metrics"] = capo_bedrock.types.training_metrics.deserialize_json(
            data["trainingMetrics"]
        )
    if data.get("validationMetrics") is not None:
        import capo_bedrock.types.validation_metrics

        out["validation_metrics"] = (
            capo_bedrock.types.validation_metrics.deserialize_json(
                data["validationMetrics"]
            )
        )
    if data.get("vpcConfig") is not None:
        import capo_bedrock.types.vpc_config

        out["vpc_config"] = capo_bedrock.types.vpc_config.deserialize_json(
            data["vpcConfig"]
        )
    if data.get("customizationConfig") is not None:
        import capo_bedrock.types.customization_config

        out["customization_config"] = (
            capo_bedrock.types.customization_config.deserialize_json(
                data["customizationConfig"]
            )
        )
    return out
