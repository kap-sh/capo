"""Generated from Smithy shape ``com.amazonaws.sagemaker#PipelineExecutionStepMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.auto_ml_job_step_metadata
    import capo_sagemaker.types.bedrock_custom_model_deployment_metadata
    import capo_sagemaker.types.bedrock_custom_model_metadata
    import capo_sagemaker.types.bedrock_model_import_metadata
    import capo_sagemaker.types.bedrock_provisioned_model_throughput_metadata
    import capo_sagemaker.types.callback_step_metadata
    import capo_sagemaker.types.clarify_check_step_metadata
    import capo_sagemaker.types.condition_step_metadata
    import capo_sagemaker.types.emr_step_metadata
    import capo_sagemaker.types.endpoint_config_step_metadata
    import capo_sagemaker.types.endpoint_step_metadata
    import capo_sagemaker.types.fail_step_metadata
    import capo_sagemaker.types.inference_component_metadata
    import capo_sagemaker.types.job_step_metadata
    import capo_sagemaker.types.lambda_step_metadata
    import capo_sagemaker.types.lineage_metadata
    import capo_sagemaker.types.model_step_metadata
    import capo_sagemaker.types.processing_job_step_metadata
    import capo_sagemaker.types.quality_check_step_metadata
    import capo_sagemaker.types.register_model_step_metadata
    import capo_sagemaker.types.training_job_step_metadata
    import capo_sagemaker.types.transform_job_step_metadata
    import capo_sagemaker.types.tuning_job_step_meta_data

PipelineExecutionStepMetadata = TypedDict(
    "PipelineExecutionStepMetadata",
    {
        "training_job": NotRequired[
            "capo_sagemaker.types.training_job_step_metadata.TrainingJobStepMetadata"
        ],
        "processing_job": NotRequired[
            "capo_sagemaker.types.processing_job_step_metadata.ProcessingJobStepMetadata"
        ],
        "transform_job": NotRequired[
            "capo_sagemaker.types.transform_job_step_metadata.TransformJobStepMetadata"
        ],
        "tuning_job": NotRequired[
            "capo_sagemaker.types.tuning_job_step_meta_data.TuningJobStepMetaData"
        ],
        "model": NotRequired[
            "capo_sagemaker.types.model_step_metadata.ModelStepMetadata"
        ],
        "register_model": NotRequired[
            "capo_sagemaker.types.register_model_step_metadata.RegisterModelStepMetadata"
        ],
        "condition": NotRequired[
            "capo_sagemaker.types.condition_step_metadata.ConditionStepMetadata"
        ],
        "callback": NotRequired[
            "capo_sagemaker.types.callback_step_metadata.CallbackStepMetadata"
        ],
        "lambda": NotRequired[
            "capo_sagemaker.types.lambda_step_metadata.LambdaStepMetadata"
        ],
        "emr": NotRequired["capo_sagemaker.types.emr_step_metadata.EMRStepMetadata"],
        "quality_check": NotRequired[
            "capo_sagemaker.types.quality_check_step_metadata.QualityCheckStepMetadata"
        ],
        "clarify_check": NotRequired[
            "capo_sagemaker.types.clarify_check_step_metadata.ClarifyCheckStepMetadata"
        ],
        "fail": NotRequired["capo_sagemaker.types.fail_step_metadata.FailStepMetadata"],
        "auto_ml_job": NotRequired[
            "capo_sagemaker.types.auto_ml_job_step_metadata.AutoMLJobStepMetadata"
        ],
        "endpoint": NotRequired[
            "capo_sagemaker.types.endpoint_step_metadata.EndpointStepMetadata"
        ],
        "endpoint_config": NotRequired[
            "capo_sagemaker.types.endpoint_config_step_metadata.EndpointConfigStepMetadata"
        ],
        "bedrock_custom_model": NotRequired[
            "capo_sagemaker.types.bedrock_custom_model_metadata.BedrockCustomModelMetadata"
        ],
        "bedrock_custom_model_deployment": NotRequired[
            "capo_sagemaker.types.bedrock_custom_model_deployment_metadata.BedrockCustomModelDeploymentMetadata"
        ],
        "bedrock_provisioned_model_throughput": NotRequired[
            "capo_sagemaker.types.bedrock_provisioned_model_throughput_metadata.BedrockProvisionedModelThroughputMetadata"
        ],
        "bedrock_model_import": NotRequired[
            "capo_sagemaker.types.bedrock_model_import_metadata.BedrockModelImportMetadata"
        ],
        "inference_component": NotRequired[
            "capo_sagemaker.types.inference_component_metadata.InferenceComponentMetadata"
        ],
        "lineage": NotRequired["capo_sagemaker.types.lineage_metadata.LineageMetadata"],
        "job": NotRequired["capo_sagemaker.types.job_step_metadata.JobStepMetadata"],
    },
    closed=True,
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PipelineExecutionStepMetadata) -> dict:
    out: dict = {}
    if "training_job" in value:
        import capo_sagemaker.types.training_job_step_metadata

        out["TrainingJob"] = (
            capo_sagemaker.types.training_job_step_metadata.serialize_aws_json_1_1(
                value["training_job"]
            )
        )
    if "processing_job" in value:
        import capo_sagemaker.types.processing_job_step_metadata

        out["ProcessingJob"] = (
            capo_sagemaker.types.processing_job_step_metadata.serialize_aws_json_1_1(
                value["processing_job"]
            )
        )
    if "transform_job" in value:
        import capo_sagemaker.types.transform_job_step_metadata

        out["TransformJob"] = (
            capo_sagemaker.types.transform_job_step_metadata.serialize_aws_json_1_1(
                value["transform_job"]
            )
        )
    if "tuning_job" in value:
        import capo_sagemaker.types.tuning_job_step_meta_data

        out["TuningJob"] = (
            capo_sagemaker.types.tuning_job_step_meta_data.serialize_aws_json_1_1(
                value["tuning_job"]
            )
        )
    if "model" in value:
        import capo_sagemaker.types.model_step_metadata

        out["Model"] = capo_sagemaker.types.model_step_metadata.serialize_aws_json_1_1(
            value["model"]
        )
    if "register_model" in value:
        import capo_sagemaker.types.register_model_step_metadata

        out["RegisterModel"] = (
            capo_sagemaker.types.register_model_step_metadata.serialize_aws_json_1_1(
                value["register_model"]
            )
        )
    if "condition" in value:
        import capo_sagemaker.types.condition_step_metadata

        out["Condition"] = (
            capo_sagemaker.types.condition_step_metadata.serialize_aws_json_1_1(
                value["condition"]
            )
        )
    if "callback" in value:
        import capo_sagemaker.types.callback_step_metadata

        out["Callback"] = (
            capo_sagemaker.types.callback_step_metadata.serialize_aws_json_1_1(
                value["callback"]
            )
        )
    if "lambda" in value:
        import capo_sagemaker.types.lambda_step_metadata

        out["Lambda"] = (
            capo_sagemaker.types.lambda_step_metadata.serialize_aws_json_1_1(
                value["lambda"]
            )
        )
    if "emr" in value:
        import capo_sagemaker.types.emr_step_metadata

        out["EMR"] = capo_sagemaker.types.emr_step_metadata.serialize_aws_json_1_1(
            value["emr"]
        )
    if "quality_check" in value:
        import capo_sagemaker.types.quality_check_step_metadata

        out["QualityCheck"] = (
            capo_sagemaker.types.quality_check_step_metadata.serialize_aws_json_1_1(
                value["quality_check"]
            )
        )
    if "clarify_check" in value:
        import capo_sagemaker.types.clarify_check_step_metadata

        out["ClarifyCheck"] = (
            capo_sagemaker.types.clarify_check_step_metadata.serialize_aws_json_1_1(
                value["clarify_check"]
            )
        )
    if "fail" in value:
        import capo_sagemaker.types.fail_step_metadata

        out["Fail"] = capo_sagemaker.types.fail_step_metadata.serialize_aws_json_1_1(
            value["fail"]
        )
    if "auto_ml_job" in value:
        import capo_sagemaker.types.auto_ml_job_step_metadata

        out["AutoMLJob"] = (
            capo_sagemaker.types.auto_ml_job_step_metadata.serialize_aws_json_1_1(
                value["auto_ml_job"]
            )
        )
    if "endpoint" in value:
        import capo_sagemaker.types.endpoint_step_metadata

        out["Endpoint"] = (
            capo_sagemaker.types.endpoint_step_metadata.serialize_aws_json_1_1(
                value["endpoint"]
            )
        )
    if "endpoint_config" in value:
        import capo_sagemaker.types.endpoint_config_step_metadata

        out["EndpointConfig"] = (
            capo_sagemaker.types.endpoint_config_step_metadata.serialize_aws_json_1_1(
                value["endpoint_config"]
            )
        )
    if "bedrock_custom_model" in value:
        import capo_sagemaker.types.bedrock_custom_model_metadata

        out["BedrockCustomModel"] = (
            capo_sagemaker.types.bedrock_custom_model_metadata.serialize_aws_json_1_1(
                value["bedrock_custom_model"]
            )
        )
    if "bedrock_custom_model_deployment" in value:
        import capo_sagemaker.types.bedrock_custom_model_deployment_metadata

        out["BedrockCustomModelDeployment"] = (
            capo_sagemaker.types.bedrock_custom_model_deployment_metadata.serialize_aws_json_1_1(
                value["bedrock_custom_model_deployment"]
            )
        )
    if "bedrock_provisioned_model_throughput" in value:
        import capo_sagemaker.types.bedrock_provisioned_model_throughput_metadata

        out["BedrockProvisionedModelThroughput"] = (
            capo_sagemaker.types.bedrock_provisioned_model_throughput_metadata.serialize_aws_json_1_1(
                value["bedrock_provisioned_model_throughput"]
            )
        )
    if "bedrock_model_import" in value:
        import capo_sagemaker.types.bedrock_model_import_metadata

        out["BedrockModelImport"] = (
            capo_sagemaker.types.bedrock_model_import_metadata.serialize_aws_json_1_1(
                value["bedrock_model_import"]
            )
        )
    if "inference_component" in value:
        import capo_sagemaker.types.inference_component_metadata

        out["InferenceComponent"] = (
            capo_sagemaker.types.inference_component_metadata.serialize_aws_json_1_1(
                value["inference_component"]
            )
        )
    if "lineage" in value:
        import capo_sagemaker.types.lineage_metadata

        out["Lineage"] = capo_sagemaker.types.lineage_metadata.serialize_aws_json_1_1(
            value["lineage"]
        )
    if "job" in value:
        import capo_sagemaker.types.job_step_metadata

        out["Job"] = capo_sagemaker.types.job_step_metadata.serialize_aws_json_1_1(
            value["job"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PipelineExecutionStepMetadata:
    out: PipelineExecutionStepMetadata = {}  # type: ignore[typeddict-item]
    if data.get("TrainingJob") is not None:
        import capo_sagemaker.types.training_job_step_metadata

        out["training_job"] = (
            capo_sagemaker.types.training_job_step_metadata.deserialize_aws_json_1_1(
                data["TrainingJob"]
            )
        )
    if data.get("ProcessingJob") is not None:
        import capo_sagemaker.types.processing_job_step_metadata

        out["processing_job"] = (
            capo_sagemaker.types.processing_job_step_metadata.deserialize_aws_json_1_1(
                data["ProcessingJob"]
            )
        )
    if data.get("TransformJob") is not None:
        import capo_sagemaker.types.transform_job_step_metadata

        out["transform_job"] = (
            capo_sagemaker.types.transform_job_step_metadata.deserialize_aws_json_1_1(
                data["TransformJob"]
            )
        )
    if data.get("TuningJob") is not None:
        import capo_sagemaker.types.tuning_job_step_meta_data

        out["tuning_job"] = (
            capo_sagemaker.types.tuning_job_step_meta_data.deserialize_aws_json_1_1(
                data["TuningJob"]
            )
        )
    if data.get("Model") is not None:
        import capo_sagemaker.types.model_step_metadata

        out["model"] = (
            capo_sagemaker.types.model_step_metadata.deserialize_aws_json_1_1(
                data["Model"]
            )
        )
    if data.get("RegisterModel") is not None:
        import capo_sagemaker.types.register_model_step_metadata

        out["register_model"] = (
            capo_sagemaker.types.register_model_step_metadata.deserialize_aws_json_1_1(
                data["RegisterModel"]
            )
        )
    if data.get("Condition") is not None:
        import capo_sagemaker.types.condition_step_metadata

        out["condition"] = (
            capo_sagemaker.types.condition_step_metadata.deserialize_aws_json_1_1(
                data["Condition"]
            )
        )
    if data.get("Callback") is not None:
        import capo_sagemaker.types.callback_step_metadata

        out["callback"] = (
            capo_sagemaker.types.callback_step_metadata.deserialize_aws_json_1_1(
                data["Callback"]
            )
        )
    if data.get("Lambda") is not None:
        import capo_sagemaker.types.lambda_step_metadata

        out["lambda"] = (
            capo_sagemaker.types.lambda_step_metadata.deserialize_aws_json_1_1(
                data["Lambda"]
            )
        )
    if data.get("EMR") is not None:
        import capo_sagemaker.types.emr_step_metadata

        out["emr"] = capo_sagemaker.types.emr_step_metadata.deserialize_aws_json_1_1(
            data["EMR"]
        )
    if data.get("QualityCheck") is not None:
        import capo_sagemaker.types.quality_check_step_metadata

        out["quality_check"] = (
            capo_sagemaker.types.quality_check_step_metadata.deserialize_aws_json_1_1(
                data["QualityCheck"]
            )
        )
    if data.get("ClarifyCheck") is not None:
        import capo_sagemaker.types.clarify_check_step_metadata

        out["clarify_check"] = (
            capo_sagemaker.types.clarify_check_step_metadata.deserialize_aws_json_1_1(
                data["ClarifyCheck"]
            )
        )
    if data.get("Fail") is not None:
        import capo_sagemaker.types.fail_step_metadata

        out["fail"] = capo_sagemaker.types.fail_step_metadata.deserialize_aws_json_1_1(
            data["Fail"]
        )
    if data.get("AutoMLJob") is not None:
        import capo_sagemaker.types.auto_ml_job_step_metadata

        out["auto_ml_job"] = (
            capo_sagemaker.types.auto_ml_job_step_metadata.deserialize_aws_json_1_1(
                data["AutoMLJob"]
            )
        )
    if data.get("Endpoint") is not None:
        import capo_sagemaker.types.endpoint_step_metadata

        out["endpoint"] = (
            capo_sagemaker.types.endpoint_step_metadata.deserialize_aws_json_1_1(
                data["Endpoint"]
            )
        )
    if data.get("EndpointConfig") is not None:
        import capo_sagemaker.types.endpoint_config_step_metadata

        out["endpoint_config"] = (
            capo_sagemaker.types.endpoint_config_step_metadata.deserialize_aws_json_1_1(
                data["EndpointConfig"]
            )
        )
    if data.get("BedrockCustomModel") is not None:
        import capo_sagemaker.types.bedrock_custom_model_metadata

        out["bedrock_custom_model"] = (
            capo_sagemaker.types.bedrock_custom_model_metadata.deserialize_aws_json_1_1(
                data["BedrockCustomModel"]
            )
        )
    if data.get("BedrockCustomModelDeployment") is not None:
        import capo_sagemaker.types.bedrock_custom_model_deployment_metadata

        out["bedrock_custom_model_deployment"] = (
            capo_sagemaker.types.bedrock_custom_model_deployment_metadata.deserialize_aws_json_1_1(
                data["BedrockCustomModelDeployment"]
            )
        )
    if data.get("BedrockProvisionedModelThroughput") is not None:
        import capo_sagemaker.types.bedrock_provisioned_model_throughput_metadata

        out["bedrock_provisioned_model_throughput"] = (
            capo_sagemaker.types.bedrock_provisioned_model_throughput_metadata.deserialize_aws_json_1_1(
                data["BedrockProvisionedModelThroughput"]
            )
        )
    if data.get("BedrockModelImport") is not None:
        import capo_sagemaker.types.bedrock_model_import_metadata

        out["bedrock_model_import"] = (
            capo_sagemaker.types.bedrock_model_import_metadata.deserialize_aws_json_1_1(
                data["BedrockModelImport"]
            )
        )
    if data.get("InferenceComponent") is not None:
        import capo_sagemaker.types.inference_component_metadata

        out["inference_component"] = (
            capo_sagemaker.types.inference_component_metadata.deserialize_aws_json_1_1(
                data["InferenceComponent"]
            )
        )
    if data.get("Lineage") is not None:
        import capo_sagemaker.types.lineage_metadata

        out["lineage"] = capo_sagemaker.types.lineage_metadata.deserialize_aws_json_1_1(
            data["Lineage"]
        )
    if data.get("Job") is not None:
        import capo_sagemaker.types.job_step_metadata

        out["job"] = capo_sagemaker.types.job_step_metadata.deserialize_aws_json_1_1(
            data["Job"]
        )
    return out
