"""Generated from Smithy shape ``com.amazonaws.sagemaker#OutputDataConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.kms_key_id
    import capo_sagemaker.types.output_compression_type
    import capo_sagemaker.types.s3_uri


class OutputDataConfig(TypedDict, closed=True):
    kms_key_id: NotRequired["capo_sagemaker.types.kms_key_id.KmsKeyId"]
    """<p>The Amazon Web Services Key Management Service (Amazon Web Services KMS) key that SageMaker uses to encrypt the model artifacts at rest using Amazon S3 server-side encryption. The <code>KmsKeyId</code> can be any of the following formats: </p> <ul> <li> <p>// KMS Key ID</p> <p> <code>"1234abcd-12ab-34cd-56ef-1234567890ab"</code> </p> </li> <li> <p>// Amazon Resource Name (ARN) of a KMS Key</p> <p> <code>"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"</code> </p> </li> <li> <p>// KMS Key Alias</p> <p> <code>"alias/ExampleAlias"</code> </p> </li> <li> <p>// Amazon Resource Name (ARN) of a KMS Key Alias</p> <p> <code>"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"</code> </p> </li> </ul> <p>If you use a KMS key ID or an alias of your KMS key, the SageMaker execution role must include permissions to call <code>kms:Encrypt</code>. If you don't provide a KMS key ID, SageMaker uses the default KMS key for Amazon S3 for your role's account. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingKMSEncryption.html">KMS-Managed Encryption Keys</a> in the <i>Amazon Simple Storage Service Developer Guide</i>. If the output data is stored in Amazon S3 Express One Zone, it is encrypted with server-side encryption with Amazon S3 managed keys (SSE-S3). KMS key is not supported for Amazon S3 Express One Zone</p> <p>The KMS key policy must grant permission to the IAM role that you specify in your <code>CreateTrainingJob</code>, <code>CreateTransformJob</code>, or <code>CreateHyperParameterTuningJob</code> requests. For more information, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html">Using Key Policies in Amazon Web Services KMS</a> in the <i>Amazon Web Services Key Management Service Developer Guide</i>.</p>"""
    s3_output_path: NotRequired["capo_sagemaker.types.s3_uri.S3Uri"]
    """<p>Identifies the S3 path where you want SageMaker to store the model artifacts. For example, <code>s3://bucket-name/key-name-prefix</code>. </p>"""
    compression_type: NotRequired[
        "capo_sagemaker.types.output_compression_type.OutputCompressionType"
    ]
    """<p>The model output compression type. Select <code>None</code> to output an uncompressed model, recommended for large model outputs. Defaults to gzip.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OutputDataConfig) -> dict:
    out: dict = {}
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    if "s3_output_path" in value:
        out["S3OutputPath"] = value["s3_output_path"]
    if "compression_type" in value:
        import capo_sagemaker.types.output_compression_type

        out["CompressionType"] = (
            capo_sagemaker.types.output_compression_type.serialize_aws_json_1_1(
                value["compression_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> OutputDataConfig:
    out: OutputDataConfig = {}  # type: ignore[typeddict-item]
    if data.get("KmsKeyId") is not None:
        out["kms_key_id"] = data["KmsKeyId"]
    if data.get("S3OutputPath") is not None:
        out["s3_output_path"] = data["S3OutputPath"]
    if data.get("CompressionType") is not None:
        import capo_sagemaker.types.output_compression_type

        out["compression_type"] = (
            capo_sagemaker.types.output_compression_type.deserialize_aws_json_1_1(
                data["CompressionType"]
            )
        )
    return out
