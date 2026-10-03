"""Generated from Smithy shape ``com.amazonaws.sagemaker#LabelingJobOutputConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.kms_key_id
    import capo_sagemaker.types.s3_uri
    import capo_sagemaker.types.sns_topic_arn


class LabelingJobOutputConfig(TypedDict, closed=True):
    s3_output_path: NotRequired["capo_sagemaker.types.s3_uri.S3Uri"]
    """<p>The Amazon S3 location to write output data.</p>"""
    kms_key_id: NotRequired["capo_sagemaker.types.kms_key_id.KmsKeyId"]
    """<p>The Amazon Web Services Key Management Service ID of the key used to encrypt the output data, if any.</p> <p>If you provide your own KMS key ID, you must add the required permissions to your KMS key described in <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/sms-security-permission.html#sms-security-kms-permissions">Encrypt Output Data and Storage Volume with Amazon Web Services KMS</a>.</p> <p>If you don't provide a KMS key ID, Amazon SageMaker uses the default Amazon Web Services KMS key for Amazon S3 for your role's account to encrypt your output data.</p> <p>If you use a bucket policy with an <code>s3:PutObject</code> permission that only allows objects with server-side encryption, set the condition key of <code>s3:x-amz-server-side-encryption</code> to <code>"aws:kms"</code>. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingKMSEncryption.html">KMS-Managed Encryption Keys</a> in the <i>Amazon Simple Storage Service Developer Guide.</i> </p>"""
    sns_topic_arn: NotRequired["capo_sagemaker.types.sns_topic_arn.SnsTopicArn"]
    """<p>An Amazon Simple Notification Service (Amazon SNS) output topic ARN. Provide a <code>SnsTopicArn</code> if you want to do real time chaining to another streaming job and receive an Amazon SNS notifications each time a data object is submitted by a worker.</p> <p>If you provide an <code>SnsTopicArn</code> in <code>OutputConfig</code>, when workers complete labeling tasks, Ground Truth will send labeling task output data to the SNS output topic you specify here. </p> <p>To learn more, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/sms-streaming-labeling-job.html#sms-streaming-how-it-works-output-data">Receive Output Data from a Streaming Labeling Job</a>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LabelingJobOutputConfig) -> dict:
    out: dict = {}
    if "s3_output_path" in value:
        out["S3OutputPath"] = value["s3_output_path"]
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    if "sns_topic_arn" in value:
        out["SnsTopicArn"] = value["sns_topic_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> LabelingJobOutputConfig:
    out: LabelingJobOutputConfig = {}  # type: ignore[typeddict-item]
    if data.get("S3OutputPath") is not None:
        out["s3_output_path"] = data["S3OutputPath"]
    if data.get("KmsKeyId") is not None:
        out["kms_key_id"] = data["KmsKeyId"]
    if data.get("SnsTopicArn") is not None:
        out["sns_topic_arn"] = data["SnsTopicArn"]
    return out
