"""Generated from Smithy shape ``com.amazonaws.sagemaker#S3ModelDataSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.inference_hub_access_config
    import capo_sagemaker.types.model_access_config
    import capo_sagemaker.types.model_compression_type
    import capo_sagemaker.types.s3_model_data_type
    import capo_sagemaker.types.s3_model_uri
    import capo_sagemaker.types.string


class S3ModelDataSource(TypedDict, closed=True):
    s3_uri: NotRequired["capo_sagemaker.types.s3_model_uri.S3ModelUri"]
    """<p>Specifies the S3 path of ML model data to deploy.</p>"""
    s3_data_type: NotRequired["capo_sagemaker.types.s3_model_data_type.S3ModelDataType"]
    """<p>Specifies the type of ML model data to deploy.</p> <p>If you choose <code>S3Prefix</code>, <code>S3Uri</code> identifies a key name prefix. SageMaker uses all objects that match the specified key name prefix as part of the ML model data to deploy. A valid key name prefix identified by <code>S3Uri</code> always ends with a forward slash (/).</p> <p>If you choose <code>S3Object</code>, <code>S3Uri</code> identifies an object that is the ML model data to deploy.</p>"""
    compression_type: NotRequired[
        "capo_sagemaker.types.model_compression_type.ModelCompressionType"
    ]
    """<p>Specifies how the ML model data is prepared.</p> <p>If you choose <code>Gzip</code> and choose <code>S3Object</code> as the value of <code>S3DataType</code>, <code>S3Uri</code> identifies an object that is a gzip-compressed TAR archive. SageMaker will attempt to decompress and untar the object during model deployment.</p> <p>If you choose <code>None</code> and chooose <code>S3Object</code> as the value of <code>S3DataType</code>, <code>S3Uri</code> identifies an object that represents an uncompressed ML model to deploy.</p> <p>If you choose None and choose <code>S3Prefix</code> as the value of <code>S3DataType</code>, <code>S3Uri</code> identifies a key name prefix, under which all objects represents the uncompressed ML model to deploy.</p> <p>If you choose None, then SageMaker will follow rules below when creating model data files under /opt/ml/model directory for use by your inference code:</p> <ul> <li> <p>If you choose <code>S3Object</code> as the value of <code>S3DataType</code>, then SageMaker will split the key of the S3 object referenced by <code>S3Uri</code> by slash (/), and use the last part as the filename of the file holding the content of the S3 object.</p> </li> <li> <p>If you choose <code>S3Prefix</code> as the value of <code>S3DataType</code>, then for each S3 object under the key name pefix referenced by <code>S3Uri</code>, SageMaker will trim its key by the prefix, and use the remainder as the path (relative to <code>/opt/ml/model</code>) of the file holding the content of the S3 object. SageMaker will split the remainder by slash (/), using intermediate parts as directory names and the last part as filename of the file holding the content of the S3 object.</p> </li> <li> <p>Do not use any of the following as file names or directory names:</p> <ul> <li> <p>An empty or blank string</p> </li> <li> <p>A string which contains null bytes</p> </li> <li> <p>A string longer than 255 bytes</p> </li> <li> <p>A single dot (<code>.</code>)</p> </li> <li> <p>A double dot (<code>..</code>)</p> </li> </ul> </li> <li> <p>Ambiguous file names will result in model deployment failure. For example, if your uncompressed ML model consists of two S3 objects <code>s3://mybucket/model/weights</code> and <code>s3://mybucket/model/weights/part1</code> and you specify <code>s3://mybucket/model/</code> as the value of <code>S3Uri</code> and <code>S3Prefix</code> as the value of <code>S3DataType</code>, then it will result in name clash between <code>/opt/ml/model/weights</code> (a regular file) and <code>/opt/ml/model/weights/</code> (a directory).</p> </li> <li> <p>Do not organize the model artifacts in <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-folders.html">S3 console using folders</a>. When you create a folder in S3 console, S3 creates a 0-byte object with a key set to the folder name you provide. They key of the 0-byte object ends with a slash (/) which violates SageMaker restrictions on model artifact file names, leading to model deployment failure. </p> </li> </ul>"""
    model_access_config: NotRequired[
        "capo_sagemaker.types.model_access_config.ModelAccessConfig"
    ]
    """<p>Specifies the access configuration file for the ML model. You can explicitly accept the model end-user license agreement (EULA) within the <code>ModelAccessConfig</code>. You are responsible for reviewing and complying with any applicable license terms and making sure they are acceptable for your use case before downloading or using a model.</p>"""
    hub_access_config: NotRequired[
        "capo_sagemaker.types.inference_hub_access_config.InferenceHubAccessConfig"
    ]
    """<p>Configuration information for hub access.</p>"""
    manifest_s3_uri: NotRequired["capo_sagemaker.types.s3_model_uri.S3ModelUri"]
    """<p>The Amazon S3 URI of the manifest file. The manifest file is a CSV file that stores the artifact locations.</p>"""
    e_tag: NotRequired["capo_sagemaker.types.string.String"]
    """<p>The ETag associated with S3 URI.</p>"""
    manifest_etag: NotRequired["capo_sagemaker.types.string.String"]
    """<p>The ETag associated with Manifest S3 URI.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3ModelDataSource) -> dict:
    out: dict = {}
    if "s3_uri" in value:
        out["S3Uri"] = value["s3_uri"]
    if "s3_data_type" in value:
        import capo_sagemaker.types.s3_model_data_type

        out["S3DataType"] = (
            capo_sagemaker.types.s3_model_data_type.serialize_aws_json_1_1(
                value["s3_data_type"]
            )
        )
    if "compression_type" in value:
        import capo_sagemaker.types.model_compression_type

        out["CompressionType"] = (
            capo_sagemaker.types.model_compression_type.serialize_aws_json_1_1(
                value["compression_type"]
            )
        )
    if "model_access_config" in value:
        import capo_sagemaker.types.model_access_config

        out["ModelAccessConfig"] = (
            capo_sagemaker.types.model_access_config.serialize_aws_json_1_1(
                value["model_access_config"]
            )
        )
    if "hub_access_config" in value:
        import capo_sagemaker.types.inference_hub_access_config

        out["HubAccessConfig"] = (
            capo_sagemaker.types.inference_hub_access_config.serialize_aws_json_1_1(
                value["hub_access_config"]
            )
        )
    if "manifest_s3_uri" in value:
        out["ManifestS3Uri"] = value["manifest_s3_uri"]
    if "e_tag" in value:
        out["ETag"] = value["e_tag"]
    if "manifest_etag" in value:
        out["ManifestEtag"] = value["manifest_etag"]
    return out


def deserialize_aws_json_1_1(data: dict) -> S3ModelDataSource:
    out: S3ModelDataSource = {}  # type: ignore[typeddict-item]
    if data.get("S3Uri") is not None:
        out["s3_uri"] = data["S3Uri"]
    if data.get("S3DataType") is not None:
        import capo_sagemaker.types.s3_model_data_type

        out["s3_data_type"] = (
            capo_sagemaker.types.s3_model_data_type.deserialize_aws_json_1_1(
                data["S3DataType"]
            )
        )
    if data.get("CompressionType") is not None:
        import capo_sagemaker.types.model_compression_type

        out["compression_type"] = (
            capo_sagemaker.types.model_compression_type.deserialize_aws_json_1_1(
                data["CompressionType"]
            )
        )
    if data.get("ModelAccessConfig") is not None:
        import capo_sagemaker.types.model_access_config

        out["model_access_config"] = (
            capo_sagemaker.types.model_access_config.deserialize_aws_json_1_1(
                data["ModelAccessConfig"]
            )
        )
    if data.get("HubAccessConfig") is not None:
        import capo_sagemaker.types.inference_hub_access_config

        out["hub_access_config"] = (
            capo_sagemaker.types.inference_hub_access_config.deserialize_aws_json_1_1(
                data["HubAccessConfig"]
            )
        )
    if data.get("ManifestS3Uri") is not None:
        out["manifest_s3_uri"] = data["ManifestS3Uri"]
    if data.get("ETag") is not None:
        out["e_tag"] = data["ETag"]
    if data.get("ManifestEtag") is not None:
        out["manifest_etag"] = data["ManifestEtag"]
    return out
