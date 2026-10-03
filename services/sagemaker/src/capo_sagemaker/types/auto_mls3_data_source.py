"""Generated from Smithy shape ``com.amazonaws.sagemaker#AutoMLS3DataSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.auto_mls3_data_type
    import capo_sagemaker.types.s3_uri


class AutoMLS3DataSource(TypedDict, closed=True):
    s3_data_type: NotRequired[
        "capo_sagemaker.types.auto_mls3_data_type.AutoMLS3DataType"
    ]
    """<p>The data type. </p> <ul> <li> <p>If you choose <code>S3Prefix</code>, <code>S3Uri</code> identifies a key name prefix. SageMaker AI uses all objects that match the specified key name prefix for model training.</p> <p>The <code>S3Prefix</code> should have the following format:</p> <p> <code>s3://DOC-EXAMPLE-BUCKET/DOC-EXAMPLE-FOLDER-OR-FILE</code> </p> </li> <li> <p>If you choose <code>ManifestFile</code>, <code>S3Uri</code> identifies an object that is a manifest file containing a list of object keys that you want SageMaker AI to use for model training.</p> <p>A <code>ManifestFile</code> should have the format shown below:</p> <p> <code>[ {"prefix": "s3://DOC-EXAMPLE-BUCKET/DOC-EXAMPLE-FOLDER/DOC-EXAMPLE-PREFIX/"}, </code> </p> <p> <code>"DOC-EXAMPLE-RELATIVE-PATH/DOC-EXAMPLE-FOLDER/DATA-1",</code> </p> <p> <code>"DOC-EXAMPLE-RELATIVE-PATH/DOC-EXAMPLE-FOLDER/DATA-2",</code> </p> <p> <code>... "DOC-EXAMPLE-RELATIVE-PATH/DOC-EXAMPLE-FOLDER/DATA-N" ]</code> </p> </li> <li> <p>If you choose <code>AugmentedManifestFile</code>, <code>S3Uri</code> identifies an object that is an augmented manifest file in JSON lines format. This file contains the data you want to use for model training. <code>AugmentedManifestFile</code> is available for V2 API jobs only (for example, for jobs created by calling <code>CreateAutoMLJobV2</code>).</p> <p>Here is a minimal, single-record example of an <code>AugmentedManifestFile</code>:</p> <p> <code>{"source-ref": "s3://DOC-EXAMPLE-BUCKET/DOC-EXAMPLE-FOLDER/cats/cat.jpg",</code> </p> <p> <code>"label-metadata": {"class-name": "cat"</code> }</p> <p>For more information on <code>AugmentedManifestFile</code>, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/augmented-manifest.html">Provide Dataset Metadata to Training Jobs with an Augmented Manifest File</a>.</p> </li> </ul>"""
    s3_uri: NotRequired["capo_sagemaker.types.s3_uri.S3Uri"]
    """<p>The URL to the Amazon S3 data source. The Uri refers to the Amazon S3 prefix or ManifestFile depending on the data type.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutoMLS3DataSource) -> dict:
    out: dict = {}
    if "s3_data_type" in value:
        import capo_sagemaker.types.auto_mls3_data_type

        out["S3DataType"] = (
            capo_sagemaker.types.auto_mls3_data_type.serialize_aws_json_1_1(
                value["s3_data_type"]
            )
        )
    if "s3_uri" in value:
        out["S3Uri"] = value["s3_uri"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AutoMLS3DataSource:
    out: AutoMLS3DataSource = {}  # type: ignore[typeddict-item]
    if data.get("S3DataType") is not None:
        import capo_sagemaker.types.auto_mls3_data_type

        out["s3_data_type"] = (
            capo_sagemaker.types.auto_mls3_data_type.deserialize_aws_json_1_1(
                data["S3DataType"]
            )
        )
    if data.get("S3Uri") is not None:
        out["s3_uri"] = data["S3Uri"]
    return out
