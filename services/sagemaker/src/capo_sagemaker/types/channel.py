"""Generated from Smithy shape ``com.amazonaws.sagemaker#Channel``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.channel_name
    import capo_sagemaker.types.compression_type
    import capo_sagemaker.types.content_type
    import capo_sagemaker.types.data_source
    import capo_sagemaker.types.record_wrapper
    import capo_sagemaker.types.shuffle_config
    import capo_sagemaker.types.training_input_mode


class Channel(TypedDict, closed=True):
    channel_name: NotRequired["capo_sagemaker.types.channel_name.ChannelName"]
    """<p>The name of the channel. </p>"""
    data_source: NotRequired["capo_sagemaker.types.data_source.DataSource"]
    """<p>The location of the channel data.</p>"""
    content_type: NotRequired["capo_sagemaker.types.content_type.ContentType"]
    """<p>The MIME type of the data.</p>"""
    compression_type: NotRequired[
        "capo_sagemaker.types.compression_type.CompressionType"
    ]
    """<p>If training data is compressed, the compression type. The default value is <code>None</code>. <code>CompressionType</code> is used only in Pipe input mode. In File mode, leave this field unset or set it to None.</p>"""
    record_wrapper_type: NotRequired[
        "capo_sagemaker.types.record_wrapper.RecordWrapper"
    ]
    """<p/> <p>Specify RecordIO as the value when input data is in raw format but the training algorithm requires the RecordIO format. In this case, SageMaker wraps each individual S3 object in a RecordIO record. If the input data is already in RecordIO format, you don't need to set this attribute. For more information, see <a href="https://mxnet.apache.org/api/architecture/note_data_loading#data-format">Create a Dataset Using RecordIO</a>. </p> <p>In File mode, leave this field unset or set it to None.</p>"""
    input_mode: NotRequired[
        "capo_sagemaker.types.training_input_mode.TrainingInputMode"
    ]
    """<p>(Optional) The input mode to use for the data channel in a training job. If you don't set a value for <code>InputMode</code>, SageMaker uses the value set for <code>TrainingInputMode</code>. Use this parameter to override the <code>TrainingInputMode</code> setting in a <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AlgorithmSpecification.html">AlgorithmSpecification</a> request when you have a channel that needs a different input mode from the training job's general setting. To download the data from Amazon Simple Storage Service (Amazon S3) to the provisioned ML storage volume, and mount the directory to a Docker volume, use <code>File</code> input mode. To stream data directly from Amazon S3 to the container, choose <code>Pipe</code> input mode.</p> <p>To use a model for incremental training, choose <code>File</code> input model.</p>"""
    shuffle_config: NotRequired["capo_sagemaker.types.shuffle_config.ShuffleConfig"]
    """<p>A configuration for a shuffle option for input data in a channel. If you use <code>S3Prefix</code> for <code>S3DataType</code>, this shuffles the results of the S3 key prefix matches. If you use <code>ManifestFile</code>, the order of the S3 object references in the <code>ManifestFile</code> is shuffled. If you use <code>AugmentedManifestFile</code>, the order of the JSON lines in the <code>AugmentedManifestFile</code> is shuffled. The shuffling order is determined using the <code>Seed</code> value.</p> <p>For Pipe input mode, shuffling is done at the start of every epoch. With large datasets this ensures that the order of the training data is different for each epoch, it helps reduce bias and possible overfitting. In a multi-node training job when ShuffleConfig is combined with <code>S3DataDistributionType</code> of <code>ShardedByS3Key</code>, the data is shuffled across nodes so that the content sent to a particular node on the first epoch might be sent to a different node on the second epoch.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Channel) -> dict:
    out: dict = {}
    if "channel_name" in value:
        out["ChannelName"] = value["channel_name"]
    if "data_source" in value:
        import capo_sagemaker.types.data_source

        out["DataSource"] = capo_sagemaker.types.data_source.serialize_aws_json_1_1(
            value["data_source"]
        )
    if "content_type" in value:
        out["ContentType"] = value["content_type"]
    if "compression_type" in value:
        import capo_sagemaker.types.compression_type

        out["CompressionType"] = (
            capo_sagemaker.types.compression_type.serialize_aws_json_1_1(
                value["compression_type"]
            )
        )
    if "record_wrapper_type" in value:
        import capo_sagemaker.types.record_wrapper

        out["RecordWrapperType"] = (
            capo_sagemaker.types.record_wrapper.serialize_aws_json_1_1(
                value["record_wrapper_type"]
            )
        )
    if "input_mode" in value:
        import capo_sagemaker.types.training_input_mode

        out["InputMode"] = (
            capo_sagemaker.types.training_input_mode.serialize_aws_json_1_1(
                value["input_mode"]
            )
        )
    if "shuffle_config" in value:
        import capo_sagemaker.types.shuffle_config

        out["ShuffleConfig"] = (
            capo_sagemaker.types.shuffle_config.serialize_aws_json_1_1(
                value["shuffle_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Channel:
    out: Channel = {}  # type: ignore[typeddict-item]
    if data.get("ChannelName") is not None:
        out["channel_name"] = data["ChannelName"]
    if data.get("DataSource") is not None:
        import capo_sagemaker.types.data_source

        out["data_source"] = capo_sagemaker.types.data_source.deserialize_aws_json_1_1(
            data["DataSource"]
        )
    if data.get("ContentType") is not None:
        out["content_type"] = data["ContentType"]
    if data.get("CompressionType") is not None:
        import capo_sagemaker.types.compression_type

        out["compression_type"] = (
            capo_sagemaker.types.compression_type.deserialize_aws_json_1_1(
                data["CompressionType"]
            )
        )
    if data.get("RecordWrapperType") is not None:
        import capo_sagemaker.types.record_wrapper

        out["record_wrapper_type"] = (
            capo_sagemaker.types.record_wrapper.deserialize_aws_json_1_1(
                data["RecordWrapperType"]
            )
        )
    if data.get("InputMode") is not None:
        import capo_sagemaker.types.training_input_mode

        out["input_mode"] = (
            capo_sagemaker.types.training_input_mode.deserialize_aws_json_1_1(
                data["InputMode"]
            )
        )
    if data.get("ShuffleConfig") is not None:
        import capo_sagemaker.types.shuffle_config

        out["shuffle_config"] = (
            capo_sagemaker.types.shuffle_config.deserialize_aws_json_1_1(
                data["ShuffleConfig"]
            )
        )
    return out
