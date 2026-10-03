"""Generated from Smithy shape ``com.amazonaws.bedrock#CreateModelCustomizationJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.base_model_identifier
    import capo_bedrock.types.custom_model_name
    import capo_bedrock.types.customization_config
    import capo_bedrock.types.customization_type
    import capo_bedrock.types.idempotency_token
    import capo_bedrock.types.job_name
    import capo_bedrock.types.kms_key_id
    import capo_bedrock.types.model_customization_hyper_parameters
    import capo_bedrock.types.output_data_config
    import capo_bedrock.types.role_arn
    import capo_bedrock.types.tag_list
    import capo_bedrock.types.training_data_config
    import capo_bedrock.types.validation_data_config
    import capo_bedrock.types.vpc_config


class CreateModelCustomizationJobRequest(TypedDict, closed=True):
    job_name: "capo_bedrock.types.job_name.JobName"
    """<p>A name for the fine-tuning job.</p>"""
    custom_model_name: "capo_bedrock.types.custom_model_name.CustomModelName"
    """<p>A name for the resulting custom model.</p>"""
    role_arn: "capo_bedrock.types.role_arn.RoleArn"
    """<p>The Amazon Resource Name (ARN) of an IAM service role that Amazon Bedrock can assume to perform tasks on your behalf. For example, during model training, Amazon Bedrock needs your permission to read input data from an S3 bucket, write model artifacts to an S3 bucket. To pass this role to Amazon Bedrock, the caller of this API must have the <code>iam:PassRole</code> permission. </p>"""
    client_request_token: NotRequired[
        "capo_bedrock.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>"""
    base_model_identifier: (
        "capo_bedrock.types.base_model_identifier.BaseModelIdentifier"
    )
    """<p>Name of the base model.</p>"""
    customization_type: NotRequired[
        "capo_bedrock.types.customization_type.CustomizationType"
    ]
    """<p>The customization type.</p>"""
    custom_model_kms_key_id: NotRequired["capo_bedrock.types.kms_key_id.KmsKeyId"]
    """<p>The custom model is encrypted at rest using this key.</p>"""
    job_tags: NotRequired["capo_bedrock.types.tag_list.TagList"]
    """<p>Tags to attach to the job.</p>"""
    custom_model_tags: NotRequired["capo_bedrock.types.tag_list.TagList"]
    """<p>Tags to attach to the resulting custom model.</p>"""
    training_data_config: "capo_bedrock.types.training_data_config.TrainingDataConfig"
    """<p>Information about the training dataset.</p>"""
    validation_data_config: NotRequired[
        "capo_bedrock.types.validation_data_config.ValidationDataConfig"
    ]
    """<p>Information about the validation dataset. </p>"""
    output_data_config: "capo_bedrock.types.output_data_config.OutputDataConfig"
    """<p>S3 location for the output data.</p>"""
    hyper_parameters: NotRequired[
        "capo_bedrock.types.model_customization_hyper_parameters.ModelCustomizationHyperParameters"
    ]
    """<p>Parameters related to tuning the model. For details on the format for different models, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models-hp.html">Custom model hyperparameters</a>.</p>"""
    vpc_config: NotRequired["capo_bedrock.types.vpc_config.VpcConfig"]
    """<p>The configuration of the Virtual Private Cloud (VPC) that contains the resources that you're using for this job. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/vpc-model-customization.html">Protect your model customization jobs using a VPC</a>.</p>"""
    customization_config: NotRequired[
        "capo_bedrock.types.customization_config.CustomizationConfig"
    ]
    """<p>The customization configuration for the model customization job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateModelCustomizationJobRequest) -> dict:
    out: dict = {}
    out["jobName"] = value["job_name"]
    out["customModelName"] = value["custom_model_name"]
    out["roleArn"] = value["role_arn"]
    if "client_request_token" in value:
        out["clientRequestToken"] = value["client_request_token"]
    out["baseModelIdentifier"] = value["base_model_identifier"]
    if "customization_type" in value:
        import capo_bedrock.types.customization_type

        out["customizationType"] = capo_bedrock.types.customization_type.serialize_json(
            value["customization_type"]
        )
    if "custom_model_kms_key_id" in value:
        out["customModelKmsKeyId"] = value["custom_model_kms_key_id"]
    if "job_tags" in value:
        import capo_bedrock.types.tag_list

        out["jobTags"] = capo_bedrock.types.tag_list.serialize_json(value["job_tags"])
    if "custom_model_tags" in value:
        import capo_bedrock.types.tag_list

        out["customModelTags"] = capo_bedrock.types.tag_list.serialize_json(
            value["custom_model_tags"]
        )
    import capo_bedrock.types.training_data_config

    out["trainingDataConfig"] = capo_bedrock.types.training_data_config.serialize_json(
        value["training_data_config"]
    )
    if "validation_data_config" in value:
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
    if "hyper_parameters" in value:
        import capo_bedrock.types.model_customization_hyper_parameters

        out["hyperParameters"] = (
            capo_bedrock.types.model_customization_hyper_parameters.serialize_json(
                value["hyper_parameters"]
            )
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


def deserialize_json(data: dict) -> CreateModelCustomizationJobRequest:
    out: CreateModelCustomizationJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("jobName") is not None:
        out["job_name"] = data["jobName"]
    else:
        raise DeserializationError(
            "CreateModelCustomizationJobRequest.job_name required"
        )
    if data.get("customModelName") is not None:
        out["custom_model_name"] = data["customModelName"]
    else:
        raise DeserializationError(
            "CreateModelCustomizationJobRequest.custom_model_name required"
        )
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError(
            "CreateModelCustomizationJobRequest.role_arn required"
        )
    if data.get("clientRequestToken") is not None:
        out["client_request_token"] = data["clientRequestToken"]
    if data.get("baseModelIdentifier") is not None:
        out["base_model_identifier"] = data["baseModelIdentifier"]
    else:
        raise DeserializationError(
            "CreateModelCustomizationJobRequest.base_model_identifier required"
        )
    if data.get("customizationType") is not None:
        import capo_bedrock.types.customization_type

        out["customization_type"] = (
            capo_bedrock.types.customization_type.deserialize_json(
                data["customizationType"]
            )
        )
    if data.get("customModelKmsKeyId") is not None:
        out["custom_model_kms_key_id"] = data["customModelKmsKeyId"]
    if data.get("jobTags") is not None:
        import capo_bedrock.types.tag_list

        out["job_tags"] = capo_bedrock.types.tag_list.deserialize_json(data["jobTags"])
    if data.get("customModelTags") is not None:
        import capo_bedrock.types.tag_list

        out["custom_model_tags"] = capo_bedrock.types.tag_list.deserialize_json(
            data["customModelTags"]
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
            "CreateModelCustomizationJobRequest.training_data_config required"
        )
    if data.get("validationDataConfig") is not None:
        import capo_bedrock.types.validation_data_config

        out["validation_data_config"] = (
            capo_bedrock.types.validation_data_config.deserialize_json(
                data["validationDataConfig"]
            )
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
            "CreateModelCustomizationJobRequest.output_data_config required"
        )
    if data.get("hyperParameters") is not None:
        import capo_bedrock.types.model_customization_hyper_parameters

        out["hyper_parameters"] = (
            capo_bedrock.types.model_customization_hyper_parameters.deserialize_json(
                data["hyperParameters"]
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
