"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateInferenceExperimentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.endpoint_name
    import capo_sagemaker.types.inference_experiment_data_storage_config
    import capo_sagemaker.types.inference_experiment_description
    import capo_sagemaker.types.inference_experiment_name
    import capo_sagemaker.types.inference_experiment_schedule
    import capo_sagemaker.types.inference_experiment_type
    import capo_sagemaker.types.kms_key_id
    import capo_sagemaker.types.model_variant_config_list
    import capo_sagemaker.types.role_arn
    import capo_sagemaker.types.shadow_mode_config
    import capo_sagemaker.types.tag_list


class CreateInferenceExperimentRequest(TypedDict, closed=True):
    name: NotRequired[
        "capo_sagemaker.types.inference_experiment_name.InferenceExperimentName"
    ]
    """<p>The name for the inference experiment.</p>"""
    type: NotRequired[
        "capo_sagemaker.types.inference_experiment_type.InferenceExperimentType"
    ]
    """<p> The type of the inference experiment that you want to run. The following types of experiments are possible: </p> <ul> <li> <p> <code>ShadowMode</code>: You can use this type to validate a shadow variant. For more information, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/shadow-tests.html">Shadow tests</a>. </p> </li> </ul>"""
    schedule: NotRequired[
        "capo_sagemaker.types.inference_experiment_schedule.InferenceExperimentSchedule"
    ]
    """<p> The duration for which you want the inference experiment to run. If you don't specify this field, the experiment automatically starts immediately upon creation and concludes after 7 days. </p>"""
    description: NotRequired[
        "capo_sagemaker.types.inference_experiment_description.InferenceExperimentDescription"
    ]
    """<p>A description for the inference experiment.</p>"""
    role_arn: NotRequired["capo_sagemaker.types.role_arn.RoleArn"]
    """<p> The ARN of the IAM role that Amazon SageMaker can assume to access model artifacts and container images, and manage Amazon SageMaker Inference endpoints for model deployment. </p>"""
    endpoint_name: NotRequired["capo_sagemaker.types.endpoint_name.EndpointName"]
    """<p> The name of the Amazon SageMaker endpoint on which you want to run the inference experiment. </p>"""
    model_variants: NotRequired[
        "capo_sagemaker.types.model_variant_config_list.ModelVariantConfigList"
    ]
    """<p> An array of <code>ModelVariantConfig</code> objects. There is one for each variant in the inference experiment. Each <code>ModelVariantConfig</code> object in the array describes the infrastructure configuration for the corresponding variant. </p>"""
    data_storage_config: NotRequired[
        "capo_sagemaker.types.inference_experiment_data_storage_config.InferenceExperimentDataStorageConfig"
    ]
    """<p> The Amazon S3 location and configuration for storing inference request and response data. </p> <p> This is an optional parameter that you can use for data capture. For more information, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-data-capture.html">Capture data</a>. </p>"""
    shadow_mode_config: NotRequired[
        "capo_sagemaker.types.shadow_mode_config.ShadowModeConfig"
    ]
    """<p> The configuration of <code>ShadowMode</code> inference experiment type. Use this field to specify a production variant which takes all the inference requests, and a shadow variant to which Amazon SageMaker replicates a percentage of the inference requests. For the shadow variant also specify the percentage of requests that Amazon SageMaker replicates. </p>"""
    kms_key: NotRequired["capo_sagemaker.types.kms_key_id.KmsKeyId"]
    """<p> The Amazon Web Services Key Management Service (Amazon Web Services KMS) key that Amazon SageMaker uses to encrypt data on the storage volume attached to the ML compute instance that hosts the endpoint. The <code>KmsKey</code> can be any of the following formats: </p> <ul> <li> <p>KMS key ID</p> <p> <code>"1234abcd-12ab-34cd-56ef-1234567890ab"</code> </p> </li> <li> <p>Amazon Resource Name (ARN) of a KMS key</p> <p> <code>"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"</code> </p> </li> <li> <p>KMS key Alias</p> <p> <code>"alias/ExampleAlias"</code> </p> </li> <li> <p>Amazon Resource Name (ARN) of a KMS key Alias</p> <p> <code>"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"</code> </p> </li> </ul> <p> If you use a KMS key ID or an alias of your KMS key, the Amazon SageMaker execution role must include permissions to call <code>kms:Encrypt</code>. If you don't provide a KMS key ID, Amazon SageMaker uses the default KMS key for Amazon S3 for your role's account. Amazon SageMaker uses server-side encryption with KMS managed keys for <code>OutputDataConfig</code>. If you use a bucket policy with an <code>s3:PutObject</code> permission that only allows objects with server-side encryption, set the condition key of <code>s3:x-amz-server-side-encryption</code> to <code>"aws:kms"</code>. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingKMSEncryption.html">KMS managed Encryption Keys</a> in the <i>Amazon Simple Storage Service Developer Guide.</i> </p> <p> The KMS key policy must grant permission to the IAM role that you specify in your <code>CreateEndpoint</code> and <code>UpdateEndpoint</code> requests. For more information, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html">Using Key Policies in Amazon Web Services KMS</a> in the <i>Amazon Web Services Key Management Service Developer Guide</i>. </p>"""
    tags: NotRequired["capo_sagemaker.types.tag_list.TagList"]
    """<p> Array of key-value pairs. You can use tags to categorize your Amazon Web Services resources in different ways, for example, by purpose, owner, or environment. For more information, see <a href="https://docs.aws.amazon.com/ARG/latest/userguide/tagging.html">Tagging your Amazon Web Services Resources</a>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateInferenceExperimentRequest) -> dict:
    out: dict = {}
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
    if "description" in value:
        out["Description"] = value["description"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "endpoint_name" in value:
        out["EndpointName"] = value["endpoint_name"]
    if "model_variants" in value:
        import capo_sagemaker.types.model_variant_config_list

        out["ModelVariants"] = (
            capo_sagemaker.types.model_variant_config_list.serialize_aws_json_1_1(
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
    if "tags" in value:
        import capo_sagemaker.types.tag_list

        out["Tags"] = capo_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateInferenceExperimentRequest:
    out: CreateInferenceExperimentRequest = {}  # type: ignore[typeddict-item]
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
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    if data.get("EndpointName") is not None:
        out["endpoint_name"] = data["EndpointName"]
    if data.get("ModelVariants") is not None:
        import capo_sagemaker.types.model_variant_config_list

        out["model_variants"] = (
            capo_sagemaker.types.model_variant_config_list.deserialize_aws_json_1_1(
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
    if data.get("Tags") is not None:
        import capo_sagemaker.types.tag_list

        out["tags"] = capo_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
