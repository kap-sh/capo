"""Generated from Smithy shape ``com.amazonaws.sagemaker#AutoMLChannel``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.auto_ml_channel_type
    import capo_sagemaker.types.auto_ml_data_source
    import capo_sagemaker.types.compression_type
    import capo_sagemaker.types.content_type
    import capo_sagemaker.types.sample_weight_attribute_name
    import capo_sagemaker.types.target_attribute_name


class AutoMLChannel(TypedDict, closed=True):
    data_source: NotRequired[
        "capo_sagemaker.types.auto_ml_data_source.AutoMLDataSource"
    ]
    """<p>The data source for an AutoML channel.</p>"""
    compression_type: NotRequired[
        "capo_sagemaker.types.compression_type.CompressionType"
    ]
    """<p>You can use <code>Gzip</code> or <code>None</code>. The default value is <code>None</code>.</p>"""
    target_attribute_name: NotRequired[
        "capo_sagemaker.types.target_attribute_name.TargetAttributeName"
    ]
    """<p>The name of the target variable in supervised learning, usually represented by 'y'.</p>"""
    content_type: NotRequired["capo_sagemaker.types.content_type.ContentType"]
    """<p>The content type of the data from the input source. You can use <code>text/csv;header=present</code> or <code>x-application/vnd.amazon+parquet</code>. The default value is <code>text/csv;header=present</code>.</p>"""
    channel_type: NotRequired[
        "capo_sagemaker.types.auto_ml_channel_type.AutoMLChannelType"
    ]
    """<p>The channel type (optional) is an <code>enum</code> string. The default value is <code>training</code>. Channels for training and validation must share the same <code>ContentType</code> and <code>TargetAttributeName</code>. For information on specifying training and validation channel types, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-datasets-problem-types.html#autopilot-data-sources-training-or-validation">How to specify training and validation datasets</a>.</p>"""
    sample_weight_attribute_name: NotRequired[
        "capo_sagemaker.types.sample_weight_attribute_name.SampleWeightAttributeName"
    ]
    """<p>If specified, this column name indicates which column of the dataset should be treated as sample weights for use by the objective metric during the training, evaluation, and the selection of the best model. This column is not considered as a predictive feature. For more information on Autopilot metrics, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-metrics-validation.html">Metrics and validation</a>.</p> <p>Sample weights should be numeric, non-negative, with larger values indicating which rows are more important than others. Data points that have invalid or no weight value are excluded.</p> <p>Support for sample weights is available in <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLAlgorithmConfig.html">Ensembling</a> mode only.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutoMLChannel) -> dict:
    out: dict = {}
    if "data_source" in value:
        import capo_sagemaker.types.auto_ml_data_source

        out["DataSource"] = (
            capo_sagemaker.types.auto_ml_data_source.serialize_aws_json_1_1(
                value["data_source"]
            )
        )
    if "compression_type" in value:
        import capo_sagemaker.types.compression_type

        out["CompressionType"] = (
            capo_sagemaker.types.compression_type.serialize_aws_json_1_1(
                value["compression_type"]
            )
        )
    if "target_attribute_name" in value:
        out["TargetAttributeName"] = value["target_attribute_name"]
    if "content_type" in value:
        out["ContentType"] = value["content_type"]
    if "channel_type" in value:
        import capo_sagemaker.types.auto_ml_channel_type

        out["ChannelType"] = (
            capo_sagemaker.types.auto_ml_channel_type.serialize_aws_json_1_1(
                value["channel_type"]
            )
        )
    if "sample_weight_attribute_name" in value:
        out["SampleWeightAttributeName"] = value["sample_weight_attribute_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AutoMLChannel:
    out: AutoMLChannel = {}  # type: ignore[typeddict-item]
    if data.get("DataSource") is not None:
        import capo_sagemaker.types.auto_ml_data_source

        out["data_source"] = (
            capo_sagemaker.types.auto_ml_data_source.deserialize_aws_json_1_1(
                data["DataSource"]
            )
        )
    if data.get("CompressionType") is not None:
        import capo_sagemaker.types.compression_type

        out["compression_type"] = (
            capo_sagemaker.types.compression_type.deserialize_aws_json_1_1(
                data["CompressionType"]
            )
        )
    if data.get("TargetAttributeName") is not None:
        out["target_attribute_name"] = data["TargetAttributeName"]
    if data.get("ContentType") is not None:
        out["content_type"] = data["ContentType"]
    if data.get("ChannelType") is not None:
        import capo_sagemaker.types.auto_ml_channel_type

        out["channel_type"] = (
            capo_sagemaker.types.auto_ml_channel_type.deserialize_aws_json_1_1(
                data["ChannelType"]
            )
        )
    if data.get("SampleWeightAttributeName") is not None:
        out["sample_weight_attribute_name"] = data["SampleWeightAttributeName"]
    return out
