"""Generated from Smithy shape ``com.amazonaws.sagemaker#LabelingJobS3DataSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.s3_uri


class LabelingJobS3DataSource(TypedDict, closed=True):
    manifest_s3_uri: NotRequired["capo_sagemaker.types.s3_uri.S3Uri"]
    """<p>The Amazon S3 location of the manifest file that describes the input data objects. </p> <p>The input manifest file referenced in <code>ManifestS3Uri</code> must contain one of the following keys: <code>source-ref</code> or <code>source</code>. The value of the keys are interpreted as follows:</p> <ul> <li> <p> <code>source-ref</code>: The source of the object is the Amazon S3 object specified in the value. Use this value when the object is a binary object, such as an image.</p> </li> <li> <p> <code>source</code>: The source of the object is the value. Use this value when the object is a text value.</p> </li> </ul> <p>If you are a new user of Ground Truth, it is recommended you review <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/sms-input-data-input-manifest.html">Use an Input Manifest File </a> in the Amazon SageMaker Developer Guide to learn how to create an input manifest file.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LabelingJobS3DataSource) -> dict:
    out: dict = {}
    if "manifest_s3_uri" in value:
        out["ManifestS3Uri"] = value["manifest_s3_uri"]
    return out


def deserialize_aws_json_1_1(data: dict) -> LabelingJobS3DataSource:
    out: LabelingJobS3DataSource = {}  # type: ignore[typeddict-item]
    if data.get("ManifestS3Uri") is not None:
        out["manifest_s3_uri"] = data["ManifestS3Uri"]
    return out
