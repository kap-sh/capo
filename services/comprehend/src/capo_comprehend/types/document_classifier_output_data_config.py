"""Generated from Smithy shape ``com.amazonaws.comprehend#DocumentClassifierOutputDataConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.kms_key_id
    import capo_comprehend.types.s3_uri


class DocumentClassifierOutputDataConfig(TypedDict, closed=True):
    s3_uri: NotRequired["capo_comprehend.types.s3_uri.S3Uri"]
    """<p>When you use the <code>OutputDataConfig</code> object while creating a custom classifier, you specify the Amazon S3 location where you want to write the confusion matrix and other output files. The URI must be in the same Region as the API endpoint that you are calling. The location is used as the prefix for the actual location of this output file.</p> <p>When the custom classifier job is finished, the service creates the output file in a directory specific to the job. The <code>S3Uri</code> field contains the location of the output file, called <code>output.tar.gz</code>. It is a compressed archive that contains the confusion matrix.</p>"""
    kms_key_id: NotRequired["capo_comprehend.types.kms_key_id.KmsKeyId"]
    """<p>ID for the Amazon Web Services Key Management Service (KMS) key that Amazon Comprehend uses to encrypt the output results from an analysis job. The KmsKeyId can be one of the following formats:</p> <ul> <li> <p>KMS Key ID: <code>"1234abcd-12ab-34cd-56ef-1234567890ab"</code> </p> </li> <li> <p>Amazon Resource Name (ARN) of a KMS Key: <code>"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"</code> </p> </li> <li> <p>KMS Key Alias: <code>"alias/ExampleAlias"</code> </p> </li> <li> <p>ARN of a KMS Key Alias: <code>"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"</code> </p> </li> </ul>"""
    flywheel_stats_s3_prefix: NotRequired["capo_comprehend.types.s3_uri.S3Uri"]
    """<p>The Amazon S3 prefix for the data lake location of the flywheel statistics.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentClassifierOutputDataConfig) -> dict:
    out: dict = {}
    if "s3_uri" in value:
        out["S3Uri"] = value["s3_uri"]
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    if "flywheel_stats_s3_prefix" in value:
        out["FlywheelStatsS3Prefix"] = value["flywheel_stats_s3_prefix"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DocumentClassifierOutputDataConfig:
    out: DocumentClassifierOutputDataConfig = {}  # type: ignore[typeddict-item]
    if data.get("S3Uri") is not None:
        out["s3_uri"] = data["S3Uri"]
    if data.get("KmsKeyId") is not None:
        out["kms_key_id"] = data["KmsKeyId"]
    if data.get("FlywheelStatsS3Prefix") is not None:
        out["flywheel_stats_s3_prefix"] = data["FlywheelStatsS3Prefix"]
    return out
