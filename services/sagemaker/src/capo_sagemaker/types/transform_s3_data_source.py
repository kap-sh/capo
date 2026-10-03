"""Generated from Smithy shape ``com.amazonaws.sagemaker#TransformS3DataSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.s3_data_type
    import capo_sagemaker.types.s3_uri


class TransformS3DataSource(TypedDict, closed=True):
    s3_data_type: NotRequired["capo_sagemaker.types.s3_data_type.S3DataType"]
    """<p>If you choose <code>S3Prefix</code>, <code>S3Uri</code> identifies a key name prefix. Amazon SageMaker uses all objects with the specified key name prefix for batch transform. </p> <p>If you choose <code>ManifestFile</code>, <code>S3Uri</code> identifies an object that is a manifest file containing a list of object keys that you want Amazon SageMaker to use for batch transform. </p> <p>The following values are compatible: <code>ManifestFile</code>, <code>S3Prefix</code> </p> <p>The following value is not compatible: <code>AugmentedManifestFile</code> </p>"""
    s3_uri: NotRequired["capo_sagemaker.types.s3_uri.S3Uri"]
    """<p>Depending on the value specified for the <code>S3DataType</code>, identifies either a key name prefix or a manifest. For example:</p> <ul> <li> <p> A key name prefix might look like this: <code>s3://bucketname/exampleprefix/</code>. </p> </li> <li> <p> A manifest might look like this: <code>s3://bucketname/example.manifest</code> </p> <p> The manifest is an S3 object which is a JSON file with the following format: </p> <p> <code>[ {"prefix": "s3://customer_bucket/some/prefix/"},</code> </p> <p> <code>"relative/path/to/custdata-1",</code> </p> <p> <code>"relative/path/custdata-2",</code> </p> <p> <code>...</code> </p> <p> <code>"relative/path/custdata-N"</code> </p> <p> <code>]</code> </p> <p> The preceding JSON matches the following <code>S3Uris</code>: </p> <p> <code>s3://customer_bucket/some/prefix/relative/path/to/custdata-1</code> </p> <p> <code>s3://customer_bucket/some/prefix/relative/path/custdata-2</code> </p> <p> <code>...</code> </p> <p> <code>s3://customer_bucket/some/prefix/relative/path/custdata-N</code> </p> <p> The complete set of <code>S3Uris</code> in this manifest constitutes the input data for the channel for this datasource. The object that each <code>S3Uris</code> points to must be readable by the IAM role that Amazon SageMaker uses to perform tasks on your behalf.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TransformS3DataSource) -> dict:
    out: dict = {}
    if "s3_data_type" in value:
        import capo_sagemaker.types.s3_data_type

        out["S3DataType"] = capo_sagemaker.types.s3_data_type.serialize_aws_json_1_1(
            value["s3_data_type"]
        )
    if "s3_uri" in value:
        out["S3Uri"] = value["s3_uri"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TransformS3DataSource:
    out: TransformS3DataSource = {}  # type: ignore[typeddict-item]
    if data.get("S3DataType") is not None:
        import capo_sagemaker.types.s3_data_type

        out["s3_data_type"] = (
            capo_sagemaker.types.s3_data_type.deserialize_aws_json_1_1(
                data["S3DataType"]
            )
        )
    if data.get("S3Uri") is not None:
        out["s3_uri"] = data["S3Uri"]
    return out
