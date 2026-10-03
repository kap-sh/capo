"""Generated from Smithy shape ``com.amazonaws.sagemaker#TransformInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.compression_type
    import capo_sagemaker.types.content_type
    import capo_sagemaker.types.split_type
    import capo_sagemaker.types.transform_data_source


class TransformInput(TypedDict, closed=True):
    data_source: NotRequired[
        "capo_sagemaker.types.transform_data_source.TransformDataSource"
    ]
    """<p>Describes the location of the channel data, which is, the S3 location of the input data that the model can consume.</p>"""
    content_type: NotRequired["capo_sagemaker.types.content_type.ContentType"]
    """<p>The multipurpose internet mail extension (MIME) type of the data. Amazon SageMaker uses the MIME type with each http call to transfer data to the transform job.</p>"""
    compression_type: NotRequired[
        "capo_sagemaker.types.compression_type.CompressionType"
    ]
    """<p>If your transform data is compressed, specify the compression type. Amazon SageMaker automatically decompresses the data for the transform job accordingly. The default value is <code>None</code>.</p>"""
    split_type: NotRequired["capo_sagemaker.types.split_type.SplitType"]
    """<p>The method to use to split the transform job's data files into smaller batches. Splitting is necessary when the total size of each object is too large to fit in a single request. You can also use data splitting to improve performance by processing multiple concurrent mini-batches. The default value for <code>SplitType</code> is <code>None</code>, which indicates that input data files are not split, and request payloads contain the entire contents of an input object. Set the value of this parameter to <code>Line</code> to split records on a newline character boundary. <code>SplitType</code> also supports a number of record-oriented binary data formats. Currently, the supported record formats are:</p> <ul> <li> <p>RecordIO</p> </li> <li> <p>TFRecord</p> </li> </ul> <p>When splitting is enabled, the size of a mini-batch depends on the values of the <code>BatchStrategy</code> and <code>MaxPayloadInMB</code> parameters. When the value of <code>BatchStrategy</code> is <code>MultiRecord</code>, Amazon SageMaker sends the maximum number of records in each request, up to the <code>MaxPayloadInMB</code> limit. If the value of <code>BatchStrategy</code> is <code>SingleRecord</code>, Amazon SageMaker sends individual records in each request.</p> <note> <p>Some data formats represent a record as a binary payload wrapped with extra padding bytes. When splitting is applied to a binary data format, padding is removed if the value of <code>BatchStrategy</code> is set to <code>SingleRecord</code>. Padding is not removed if the value of <code>BatchStrategy</code> is set to <code>MultiRecord</code>.</p> <p>For more information about <code>RecordIO</code>, see <a href="https://mxnet.apache.org/api/faq/recordio">Create a Dataset Using RecordIO</a> in the MXNet documentation. For more information about <code>TFRecord</code>, see <a href="https://www.tensorflow.org/guide/data#consuming_tfrecord_data">Consuming TFRecord data</a> in the TensorFlow documentation.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TransformInput) -> dict:
    out: dict = {}
    if "data_source" in value:
        import capo_sagemaker.types.transform_data_source

        out["DataSource"] = (
            capo_sagemaker.types.transform_data_source.serialize_aws_json_1_1(
                value["data_source"]
            )
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
    if "split_type" in value:
        import capo_sagemaker.types.split_type

        out["SplitType"] = capo_sagemaker.types.split_type.serialize_aws_json_1_1(
            value["split_type"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TransformInput:
    out: TransformInput = {}  # type: ignore[typeddict-item]
    if data.get("DataSource") is not None:
        import capo_sagemaker.types.transform_data_source

        out["data_source"] = (
            capo_sagemaker.types.transform_data_source.deserialize_aws_json_1_1(
                data["DataSource"]
            )
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
    if data.get("SplitType") is not None:
        import capo_sagemaker.types.split_type

        out["split_type"] = capo_sagemaker.types.split_type.deserialize_aws_json_1_1(
            data["SplitType"]
        )
    return out
