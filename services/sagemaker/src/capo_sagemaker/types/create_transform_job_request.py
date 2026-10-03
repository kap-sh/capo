"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateTransformJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.batch_data_capture_config
    import capo_sagemaker.types.batch_strategy
    import capo_sagemaker.types.data_processing
    import capo_sagemaker.types.experiment_config
    import capo_sagemaker.types.max_concurrent_transforms
    import capo_sagemaker.types.max_payload_in_mb
    import capo_sagemaker.types.model_client_config
    import capo_sagemaker.types.model_name
    import capo_sagemaker.types.tag_list
    import capo_sagemaker.types.transform_environment_map
    import capo_sagemaker.types.transform_input
    import capo_sagemaker.types.transform_job_name
    import capo_sagemaker.types.transform_output
    import capo_sagemaker.types.transform_resources


class CreateTransformJobRequest(TypedDict, closed=True):
    transform_job_name: NotRequired[
        "capo_sagemaker.types.transform_job_name.TransformJobName"
    ]
    """<p>The name of the transform job. The name must be unique within an Amazon Web Services Region in an Amazon Web Services account. </p>"""
    model_name: NotRequired["capo_sagemaker.types.model_name.ModelName"]
    """<p>The name of the model that you want to use for the transform job. <code>ModelName</code> must be the name of an existing Amazon SageMaker model within an Amazon Web Services Region in an Amazon Web Services account.</p>"""
    max_concurrent_transforms: NotRequired[
        "capo_sagemaker.types.max_concurrent_transforms.MaxConcurrentTransforms"
    ]
    """<p>The maximum number of parallel requests that can be sent to each instance in a transform job. If <code>MaxConcurrentTransforms</code> is set to <code>0</code> or left unset, Amazon SageMaker checks the optional execution-parameters to determine the settings for your chosen algorithm. If the execution-parameters endpoint is not enabled, the default value is <code>1</code>. For more information on execution-parameters, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms-batch-code.html#your-algorithms-batch-code-how-containe-serves-requests">How Containers Serve Requests</a>. For built-in algorithms, you don't need to set a value for <code>MaxConcurrentTransforms</code>.</p>"""
    model_client_config: NotRequired[
        "capo_sagemaker.types.model_client_config.ModelClientConfig"
    ]
    """<p>Configures the timeout and maximum number of retries for processing a transform job invocation.</p>"""
    max_payload_in_mb: NotRequired[
        "capo_sagemaker.types.max_payload_in_mb.MaxPayloadInMB"
    ]
    """<p>The maximum allowed size of the payload, in MB. A <i>payload</i> is the data portion of a record (without metadata). The value in <code>MaxPayloadInMB</code> must be greater than, or equal to, the size of a single record. To estimate the size of a record in MB, divide the size of your dataset by the number of records. To ensure that the records fit within the maximum payload size, we recommend using a slightly larger value. The default value is <code>6</code> MB. </p> <p>The value of <code>MaxPayloadInMB</code> cannot be greater than 100 MB. If you specify the <code>MaxConcurrentTransforms</code> parameter, the value of <code>(MaxConcurrentTransforms * MaxPayloadInMB)</code> also cannot exceed 100 MB.</p> <p>For cases where the payload might be arbitrarily large and is transmitted using HTTP chunked encoding, set the value to <code>0</code>. This feature works only in supported algorithms. Currently, Amazon SageMaker built-in algorithms do not support HTTP chunked encoding.</p>"""
    batch_strategy: NotRequired["capo_sagemaker.types.batch_strategy.BatchStrategy"]
    """<p>Specifies the number of records to include in a mini-batch for an HTTP inference request. A <i>record</i> <i/> is a single unit of input data that inference can be made on. For example, a single line in a CSV file is a record. </p> <p>To enable the batch strategy, you must set the <code>SplitType</code> property to <code>Line</code>, <code>RecordIO</code>, or <code>TFRecord</code>.</p> <p>To use only one record when making an HTTP invocation request to a container, set <code>BatchStrategy</code> to <code>SingleRecord</code> and <code>SplitType</code> to <code>Line</code>.</p> <p>To fit as many records in a mini-batch as can fit within the <code>MaxPayloadInMB</code> limit, set <code>BatchStrategy</code> to <code>MultiRecord</code> and <code>SplitType</code> to <code>Line</code>.</p>"""
    environment: NotRequired[
        "capo_sagemaker.types.transform_environment_map.TransformEnvironmentMap"
    ]
    """<p>The environment variables to set in the Docker container. Don't include any sensitive data in your environment variables. We support up to 16 key and values entries in the map.</p>"""
    transform_input: NotRequired["capo_sagemaker.types.transform_input.TransformInput"]
    """<p>Describes the input source and the way the transform job consumes it.</p>"""
    transform_output: NotRequired[
        "capo_sagemaker.types.transform_output.TransformOutput"
    ]
    """<p>Describes the results of the transform job.</p>"""
    data_capture_config: NotRequired[
        "capo_sagemaker.types.batch_data_capture_config.BatchDataCaptureConfig"
    ]
    """<p>Configuration to control how SageMaker captures inference data.</p>"""
    transform_resources: NotRequired[
        "capo_sagemaker.types.transform_resources.TransformResources"
    ]
    """<p>Describes the resources, including ML instance types and ML instance count, to use for the transform job.</p>"""
    data_processing: NotRequired["capo_sagemaker.types.data_processing.DataProcessing"]
    """<p>The data structure used to specify the data to be used for inference in a batch transform job and to associate the data that is relevant to the prediction results in the output. The input filter provided allows you to exclude input data that is not needed for inference in a batch transform job. The output filter provided allows you to include input data relevant to interpreting the predictions in the output from the job. For more information, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/batch-transform-data-processing.html">Associate Prediction Results with their Corresponding Input Records</a>.</p>"""
    tags: NotRequired["capo_sagemaker.types.tag_list.TagList"]
    """<p>(Optional) An array of key-value pairs. For more information, see <a href="https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html#allocation-what">Using Cost Allocation Tags</a> in the <i>Amazon Web Services Billing and Cost Management User Guide</i>.</p>"""
    experiment_config: NotRequired[
        "capo_sagemaker.types.experiment_config.ExperimentConfig"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateTransformJobRequest) -> dict:
    out: dict = {}
    if "transform_job_name" in value:
        out["TransformJobName"] = value["transform_job_name"]
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
    if "data_processing" in value:
        import capo_sagemaker.types.data_processing

        out["DataProcessing"] = (
            capo_sagemaker.types.data_processing.serialize_aws_json_1_1(
                value["data_processing"]
            )
        )
    if "tags" in value:
        import capo_sagemaker.types.tag_list

        out["Tags"] = capo_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "experiment_config" in value:
        import capo_sagemaker.types.experiment_config

        out["ExperimentConfig"] = (
            capo_sagemaker.types.experiment_config.serialize_aws_json_1_1(
                value["experiment_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateTransformJobRequest:
    out: CreateTransformJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("TransformJobName") is not None:
        out["transform_job_name"] = data["TransformJobName"]
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
    if data.get("DataProcessing") is not None:
        import capo_sagemaker.types.data_processing

        out["data_processing"] = (
            capo_sagemaker.types.data_processing.deserialize_aws_json_1_1(
                data["DataProcessing"]
            )
        )
    if data.get("Tags") is not None:
        import capo_sagemaker.types.tag_list

        out["tags"] = capo_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if data.get("ExperimentConfig") is not None:
        import capo_sagemaker.types.experiment_config

        out["experiment_config"] = (
            capo_sagemaker.types.experiment_config.deserialize_aws_json_1_1(
                data["ExperimentConfig"]
            )
        )
    return out
