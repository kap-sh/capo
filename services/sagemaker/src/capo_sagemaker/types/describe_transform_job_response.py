"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeTransformJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.auto_ml_job_arn
    import capo_sagemaker.types.batch_data_capture_config
    import capo_sagemaker.types.batch_strategy
    import capo_sagemaker.types.data_processing
    import capo_sagemaker.types.experiment_config
    import capo_sagemaker.types.failure_reason
    import capo_sagemaker.types.labeling_job_arn
    import capo_sagemaker.types.max_concurrent_transforms
    import capo_sagemaker.types.max_payload_in_mb
    import capo_sagemaker.types.model_client_config
    import capo_sagemaker.types.model_name
    import capo_sagemaker.types.timestamp
    import capo_sagemaker.types.transform_environment_map
    import capo_sagemaker.types.transform_input
    import capo_sagemaker.types.transform_job_arn
    import capo_sagemaker.types.transform_job_name
    import capo_sagemaker.types.transform_job_status
    import capo_sagemaker.types.transform_output
    import capo_sagemaker.types.transform_resources


class DescribeTransformJobResponse(TypedDict, closed=True):
    transform_job_name: NotRequired[
        "capo_sagemaker.types.transform_job_name.TransformJobName"
    ]
    """<p>The name of the transform job.</p>"""
    transform_job_arn: NotRequired[
        "capo_sagemaker.types.transform_job_arn.TransformJobArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the transform job.</p>"""
    transform_job_status: NotRequired[
        "capo_sagemaker.types.transform_job_status.TransformJobStatus"
    ]
    """<p>The status of the transform job. If the transform job failed, the reason is returned in the <code>FailureReason</code> field.</p>"""
    failure_reason: NotRequired["capo_sagemaker.types.failure_reason.FailureReason"]
    """<p>If the transform job failed, <code>FailureReason</code> describes why it failed. A transform job creates a log file, which includes error messages, and stores it as an Amazon S3 object. For more information, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/logging-cloudwatch.html">Log Amazon SageMaker Events with Amazon CloudWatch</a>.</p>"""
    model_name: NotRequired["capo_sagemaker.types.model_name.ModelName"]
    """<p>The name of the model used in the transform job.</p>"""
    max_concurrent_transforms: NotRequired[
        "capo_sagemaker.types.max_concurrent_transforms.MaxConcurrentTransforms"
    ]
    """<p>The maximum number of parallel requests on each instance node that can be launched in a transform job. The default value is 1.</p>"""
    model_client_config: NotRequired[
        "capo_sagemaker.types.model_client_config.ModelClientConfig"
    ]
    """<p>The timeout and maximum number of retries for processing a transform job invocation.</p>"""
    max_payload_in_mb: NotRequired[
        "capo_sagemaker.types.max_payload_in_mb.MaxPayloadInMB"
    ]
    """<p>The maximum payload size, in MB, used in the transform job.</p>"""
    batch_strategy: NotRequired["capo_sagemaker.types.batch_strategy.BatchStrategy"]
    """<p>Specifies the number of records to include in a mini-batch for an HTTP inference request. A <i>record</i> <i/> is a single unit of input data that inference can be made on. For example, a single line in a CSV file is a record. </p> <p>To enable the batch strategy, you must set <code>SplitType</code> to <code>Line</code>, <code>RecordIO</code>, or <code>TFRecord</code>.</p>"""
    environment: NotRequired[
        "capo_sagemaker.types.transform_environment_map.TransformEnvironmentMap"
    ]
    """<p>The environment variables to set in the Docker container. We support up to 16 key and values entries in the map.</p>"""
    transform_input: NotRequired["capo_sagemaker.types.transform_input.TransformInput"]
    """<p>Describes the dataset to be transformed and the Amazon S3 location where it is stored.</p>"""
    transform_output: NotRequired[
        "capo_sagemaker.types.transform_output.TransformOutput"
    ]
    """<p>Identifies the Amazon S3 location where you want Amazon SageMaker to save the results from the transform job.</p>"""
    data_capture_config: NotRequired[
        "capo_sagemaker.types.batch_data_capture_config.BatchDataCaptureConfig"
    ]
    """<p>Configuration to control how SageMaker captures inference data.</p>"""
    transform_resources: NotRequired[
        "capo_sagemaker.types.transform_resources.TransformResources"
    ]
    """<p>Describes the resources, including ML instance types and ML instance count, to use for the transform job.</p>"""
    creation_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>A timestamp that shows when the transform Job was created.</p>"""
    transform_start_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>Indicates when the transform job starts on ML instances. You are billed for the time interval between this time and the value of <code>TransformEndTime</code>.</p>"""
    transform_end_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>Indicates when the transform job has been completed, or has stopped or failed. You are billed for the time interval between this time and the value of <code>TransformStartTime</code>.</p>"""
    labeling_job_arn: NotRequired[
        "capo_sagemaker.types.labeling_job_arn.LabelingJobArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the Amazon SageMaker Ground Truth labeling job that created the transform or training job.</p>"""
    auto_ml_job_arn: NotRequired["capo_sagemaker.types.auto_ml_job_arn.AutoMLJobArn"]
    """<p>The Amazon Resource Name (ARN) of the AutoML transform job.</p>"""
    data_processing: NotRequired["capo_sagemaker.types.data_processing.DataProcessing"]
    experiment_config: NotRequired[
        "capo_sagemaker.types.experiment_config.ExperimentConfig"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeTransformJobResponse) -> dict:
    out: dict = {}
    if "transform_job_name" in value:
        out["TransformJobName"] = value["transform_job_name"]
    if "transform_job_arn" in value:
        out["TransformJobArn"] = value["transform_job_arn"]
    if "transform_job_status" in value:
        import capo_sagemaker.types.transform_job_status

        out["TransformJobStatus"] = (
            capo_sagemaker.types.transform_job_status.serialize_aws_json_1_1(
                value["transform_job_status"]
            )
        )
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    if "model_name" in value:
        out["ModelName"] = value["model_name"]
    if "max_concurrent_transforms" in value:
        out["MaxConcurrentTransforms"] = value["max_concurrent_transforms"]
    if "model_client_config" in value:
        import capo_sagemaker.types.model_client_config

        out["ModelClientConfig"] = (
            capo_sagemaker.types.model_client_config.serialize_aws_json_1_1(
                value["model_client_config"]
            )
        )
    if "max_payload_in_mb" in value:
        out["MaxPayloadInMB"] = value["max_payload_in_mb"]
    if "batch_strategy" in value:
        import capo_sagemaker.types.batch_strategy

        out["BatchStrategy"] = (
            capo_sagemaker.types.batch_strategy.serialize_aws_json_1_1(
                value["batch_strategy"]
            )
        )
    if "environment" in value:
        import capo_sagemaker.types.transform_environment_map

        out["Environment"] = (
            capo_sagemaker.types.transform_environment_map.serialize_aws_json_1_1(
                value["environment"]
            )
        )
    if "transform_input" in value:
        import capo_sagemaker.types.transform_input

        out["TransformInput"] = (
            capo_sagemaker.types.transform_input.serialize_aws_json_1_1(
                value["transform_input"]
            )
        )
    if "transform_output" in value:
        import capo_sagemaker.types.transform_output

        out["TransformOutput"] = (
            capo_sagemaker.types.transform_output.serialize_aws_json_1_1(
                value["transform_output"]
            )
        )
    if "data_capture_config" in value:
        import capo_sagemaker.types.batch_data_capture_config

        out["DataCaptureConfig"] = (
            capo_sagemaker.types.batch_data_capture_config.serialize_aws_json_1_1(
                value["data_capture_config"]
            )
        )
    if "transform_resources" in value:
        import capo_sagemaker.types.transform_resources

        out["TransformResources"] = (
            capo_sagemaker.types.transform_resources.serialize_aws_json_1_1(
                value["transform_resources"]
            )
        )
    if "creation_time" in value:
        import capo_sagemaker.types.timestamp

        out["CreationTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "transform_start_time" in value:
        import capo_sagemaker.types.timestamp

        out["TransformStartTime"] = (
            capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["transform_start_time"]
            )
        )
    if "transform_end_time" in value:
        import capo_sagemaker.types.timestamp

        out["TransformEndTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["transform_end_time"]
        )
    if "labeling_job_arn" in value:
        out["LabelingJobArn"] = value["labeling_job_arn"]
    if "auto_ml_job_arn" in value:
        out["AutoMLJobArn"] = value["auto_ml_job_arn"]
    if "data_processing" in value:
        import capo_sagemaker.types.data_processing

        out["DataProcessing"] = (
            capo_sagemaker.types.data_processing.serialize_aws_json_1_1(
                value["data_processing"]
            )
        )
    if "experiment_config" in value:
        import capo_sagemaker.types.experiment_config

        out["ExperimentConfig"] = (
            capo_sagemaker.types.experiment_config.serialize_aws_json_1_1(
                value["experiment_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeTransformJobResponse:
    out: DescribeTransformJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("TransformJobName") is not None:
        out["transform_job_name"] = data["TransformJobName"]
    if data.get("TransformJobArn") is not None:
        out["transform_job_arn"] = data["TransformJobArn"]
    if data.get("TransformJobStatus") is not None:
        import capo_sagemaker.types.transform_job_status

        out["transform_job_status"] = (
            capo_sagemaker.types.transform_job_status.deserialize_aws_json_1_1(
                data["TransformJobStatus"]
            )
        )
    if data.get("FailureReason") is not None:
        out["failure_reason"] = data["FailureReason"]
    if data.get("ModelName") is not None:
        out["model_name"] = data["ModelName"]
    if data.get("MaxConcurrentTransforms") is not None:
        out["max_concurrent_transforms"] = data["MaxConcurrentTransforms"]
    if data.get("ModelClientConfig") is not None:
        import capo_sagemaker.types.model_client_config

        out["model_client_config"] = (
            capo_sagemaker.types.model_client_config.deserialize_aws_json_1_1(
                data["ModelClientConfig"]
            )
        )
    if data.get("MaxPayloadInMB") is not None:
        out["max_payload_in_mb"] = data["MaxPayloadInMB"]
    if data.get("BatchStrategy") is not None:
        import capo_sagemaker.types.batch_strategy

        out["batch_strategy"] = (
            capo_sagemaker.types.batch_strategy.deserialize_aws_json_1_1(
                data["BatchStrategy"]
            )
        )
    if data.get("Environment") is not None:
        import capo_sagemaker.types.transform_environment_map

        out["environment"] = (
            capo_sagemaker.types.transform_environment_map.deserialize_aws_json_1_1(
                data["Environment"]
            )
        )
    if data.get("TransformInput") is not None:
        import capo_sagemaker.types.transform_input

        out["transform_input"] = (
            capo_sagemaker.types.transform_input.deserialize_aws_json_1_1(
                data["TransformInput"]
            )
        )
    if data.get("TransformOutput") is not None:
        import capo_sagemaker.types.transform_output

        out["transform_output"] = (
            capo_sagemaker.types.transform_output.deserialize_aws_json_1_1(
                data["TransformOutput"]
            )
        )
    if data.get("DataCaptureConfig") is not None:
        import capo_sagemaker.types.batch_data_capture_config

        out["data_capture_config"] = (
            capo_sagemaker.types.batch_data_capture_config.deserialize_aws_json_1_1(
                data["DataCaptureConfig"]
            )
        )
    if data.get("TransformResources") is not None:
        import capo_sagemaker.types.transform_resources

        out["transform_resources"] = (
            capo_sagemaker.types.transform_resources.deserialize_aws_json_1_1(
                data["TransformResources"]
            )
        )
    if data.get("CreationTime") is not None:
        import capo_sagemaker.types.timestamp

        out["creation_time"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if data.get("TransformStartTime") is not None:
        import capo_sagemaker.types.timestamp

        out["transform_start_time"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["TransformStartTime"]
            )
        )
    if data.get("TransformEndTime") is not None:
        import capo_sagemaker.types.timestamp

        out["transform_end_time"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["TransformEndTime"]
            )
        )
    if data.get("LabelingJobArn") is not None:
        out["labeling_job_arn"] = data["LabelingJobArn"]
    if data.get("AutoMLJobArn") is not None:
        out["auto_ml_job_arn"] = data["AutoMLJobArn"]
    if data.get("DataProcessing") is not None:
        import capo_sagemaker.types.data_processing

        out["data_processing"] = (
            capo_sagemaker.types.data_processing.deserialize_aws_json_1_1(
                data["DataProcessing"]
            )
        )
    if data.get("ExperimentConfig") is not None:
        import capo_sagemaker.types.experiment_config

        out["experiment_config"] = (
            capo_sagemaker.types.experiment_config.deserialize_aws_json_1_1(
                data["ExperimentConfig"]
            )
        )
    return out
