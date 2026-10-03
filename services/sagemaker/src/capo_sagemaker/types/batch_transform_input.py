"""Generated from Smithy shape ``com.amazonaws.sagemaker#BatchTransformInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.destination_s3_uri
    import capo_sagemaker.types.exclude_features_attribute
    import capo_sagemaker.types.monitoring_dataset_format
    import capo_sagemaker.types.monitoring_time_offset_string
    import capo_sagemaker.types.probability_threshold_attribute
    import capo_sagemaker.types.processing_local_path
    import capo_sagemaker.types.processing_s3_data_distribution_type
    import capo_sagemaker.types.processing_s3_input_mode
    import capo_sagemaker.types.string


class BatchTransformInput(TypedDict, closed=True):
    data_captured_destination_s3_uri: NotRequired[
        "capo_sagemaker.types.destination_s3_uri.DestinationS3Uri"
    ]
    """<p>The Amazon S3 location being used to capture the data.</p>"""
    dataset_format: NotRequired[
        "capo_sagemaker.types.monitoring_dataset_format.MonitoringDatasetFormat"
    ]
    """<p>The dataset format for your batch transform job.</p>"""
    local_path: NotRequired[
        "capo_sagemaker.types.processing_local_path.ProcessingLocalPath"
    ]
    """<p>Path to the filesystem where the batch transform data is available to the container.</p>"""
    s3_input_mode: NotRequired[
        "capo_sagemaker.types.processing_s3_input_mode.ProcessingS3InputMode"
    ]
    """<p>Whether the <code>Pipe</code> or <code>File</code> is used as the input mode for transferring data for the monitoring job. <code>Pipe</code> mode is recommended for large datasets. <code>File</code> mode is useful for small files that fit in memory. Defaults to <code>File</code>.</p>"""
    s3_data_distribution_type: NotRequired[
        "capo_sagemaker.types.processing_s3_data_distribution_type.ProcessingS3DataDistributionType"
    ]
    """<p>Whether input data distributed in Amazon S3 is fully replicated or sharded by an S3 key. Defaults to <code>FullyReplicated</code> </p>"""
    features_attribute: NotRequired["capo_sagemaker.types.string.String"]
    """<p>The attributes of the input data that are the input features.</p>"""
    inference_attribute: NotRequired["capo_sagemaker.types.string.String"]
    """<p>The attribute of the input data that represents the ground truth label.</p>"""
    probability_attribute: NotRequired["capo_sagemaker.types.string.String"]
    """<p>In a classification problem, the attribute that represents the class probability.</p>"""
    probability_threshold_attribute: NotRequired[
        "capo_sagemaker.types.probability_threshold_attribute.ProbabilityThresholdAttribute"
    ]
    """<p>The threshold for the class probability to be evaluated as a positive result.</p>"""
    start_time_offset: NotRequired[
        "capo_sagemaker.types.monitoring_time_offset_string.MonitoringTimeOffsetString"
    ]
    """<p>If specified, monitoring jobs substract this time from the start time. For information about using offsets for scheduling monitoring jobs, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-model-quality-schedule.html">Schedule Model Quality Monitoring Jobs</a>.</p>"""
    end_time_offset: NotRequired[
        "capo_sagemaker.types.monitoring_time_offset_string.MonitoringTimeOffsetString"
    ]
    """<p>If specified, monitoring jobs subtract this time from the end time. For information about using offsets for scheduling monitoring jobs, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-model-quality-schedule.html">Schedule Model Quality Monitoring Jobs</a>.</p>"""
    exclude_features_attribute: NotRequired[
        "capo_sagemaker.types.exclude_features_attribute.ExcludeFeaturesAttribute"
    ]
    """<p>The attributes of the input data to exclude from the analysis.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchTransformInput) -> dict:
    out: dict = {}
    if "data_captured_destination_s3_uri" in value:
        out["DataCapturedDestinationS3Uri"] = value["data_captured_destination_s3_uri"]
    if "dataset_format" in value:
        import capo_sagemaker.types.monitoring_dataset_format

        out["DatasetFormat"] = (
            capo_sagemaker.types.monitoring_dataset_format.serialize_aws_json_1_1(
                value["dataset_format"]
            )
        )
    if "local_path" in value:
        out["LocalPath"] = value["local_path"]
    if "s3_input_mode" in value:
        import capo_sagemaker.types.processing_s3_input_mode

        out["S3InputMode"] = (
            capo_sagemaker.types.processing_s3_input_mode.serialize_aws_json_1_1(
                value["s3_input_mode"]
            )
        )
    if "s3_data_distribution_type" in value:
        import capo_sagemaker.types.processing_s3_data_distribution_type

        out["S3DataDistributionType"] = (
            capo_sagemaker.types.processing_s3_data_distribution_type.serialize_aws_json_1_1(
                value["s3_data_distribution_type"]
            )
        )
    if "features_attribute" in value:
        out["FeaturesAttribute"] = value["features_attribute"]
    if "inference_attribute" in value:
        out["InferenceAttribute"] = value["inference_attribute"]
    if "probability_attribute" in value:
        out["ProbabilityAttribute"] = value["probability_attribute"]
    if "probability_threshold_attribute" in value:
        out["ProbabilityThresholdAttribute"] = (
            "NaN"
            if value["probability_threshold_attribute"]
            != value["probability_threshold_attribute"]
            else "Infinity"
            if value["probability_threshold_attribute"] == float("inf")
            else "-Infinity"
            if value["probability_threshold_attribute"] == float("-inf")
            else value["probability_threshold_attribute"]
        )
    if "start_time_offset" in value:
        out["StartTimeOffset"] = value["start_time_offset"]
    if "end_time_offset" in value:
        out["EndTimeOffset"] = value["end_time_offset"]
    if "exclude_features_attribute" in value:
        out["ExcludeFeaturesAttribute"] = value["exclude_features_attribute"]
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchTransformInput:
    out: BatchTransformInput = {}  # type: ignore[typeddict-item]
    if data.get("DataCapturedDestinationS3Uri") is not None:
        out["data_captured_destination_s3_uri"] = data["DataCapturedDestinationS3Uri"]
    if data.get("DatasetFormat") is not None:
        import capo_sagemaker.types.monitoring_dataset_format

        out["dataset_format"] = (
            capo_sagemaker.types.monitoring_dataset_format.deserialize_aws_json_1_1(
                data["DatasetFormat"]
            )
        )
    if data.get("LocalPath") is not None:
        out["local_path"] = data["LocalPath"]
    if data.get("S3InputMode") is not None:
        import capo_sagemaker.types.processing_s3_input_mode

        out["s3_input_mode"] = (
            capo_sagemaker.types.processing_s3_input_mode.deserialize_aws_json_1_1(
                data["S3InputMode"]
            )
        )
    if data.get("S3DataDistributionType") is not None:
        import capo_sagemaker.types.processing_s3_data_distribution_type

        out["s3_data_distribution_type"] = (
            capo_sagemaker.types.processing_s3_data_distribution_type.deserialize_aws_json_1_1(
                data["S3DataDistributionType"]
            )
        )
    if data.get("FeaturesAttribute") is not None:
        out["features_attribute"] = data["FeaturesAttribute"]
    if data.get("InferenceAttribute") is not None:
        out["inference_attribute"] = data["InferenceAttribute"]
    if data.get("ProbabilityAttribute") is not None:
        out["probability_attribute"] = data["ProbabilityAttribute"]
    if data.get("ProbabilityThresholdAttribute") is not None:
        out["probability_threshold_attribute"] = float(
            data["ProbabilityThresholdAttribute"]
        )
    if data.get("StartTimeOffset") is not None:
        out["start_time_offset"] = data["StartTimeOffset"]
    if data.get("EndTimeOffset") is not None:
        out["end_time_offset"] = data["EndTimeOffset"]
    if data.get("ExcludeFeaturesAttribute") is not None:
        out["exclude_features_attribute"] = data["ExcludeFeaturesAttribute"]
    return out
