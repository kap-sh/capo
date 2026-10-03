"""Generated from Smithy shape ``com.amazonaws.comprehend#OutputDataConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_comprehend.errors import DeserializationError

if TYPE_CHECKING:
    import capo_comprehend.types.kms_key_id
    import capo_comprehend.types.s3_uri


class OutputDataConfig(TypedDict, closed=True):
    s3_uri: "capo_comprehend.types.s3_uri.S3Uri"
    """<p>When you use the <code>OutputDataConfig</code> object with asynchronous operations, you specify the Amazon S3 location where you want to write the output data. The URI must be in the same Region as the API endpoint that you are calling. The location is used as the prefix for the actual location of the output file.</p> <p>When the topic detection job is finished, the service creates an output file in a directory specific to the job. The <code>S3Uri</code> field contains the location of the output file, called <code>output.tar.gz</code>. It is a compressed archive that contains the ouput of the operation.</p> <p> For a PII entity detection job, the output file is plain text, not a compressed archive. The output file name is the same as the input file, with <code>.out</code> appended at the end. </p>"""
    kms_key_id: NotRequired["capo_comprehend.types.kms_key_id.KmsKeyId"]
    """<p>ID for the Amazon Web Services Key Management Service (KMS) key that Amazon Comprehend uses to encrypt the output results from an analysis job. Specify the Key Id of a symmetric key, because you cannot use an asymmetric key for uploading data to S3.</p> <p>The KmsKeyId can be one of the following formats:</p> <ul> <li> <p>KMS Key ID: <code>"1234abcd-12ab-34cd-56ef-1234567890ab"</code> </p> </li> <li> <p>Amazon Resource Name (ARN) of a KMS Key: <code>"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"</code> </p> </li> <li> <p>KMS Key Alias: <code>"alias/ExampleAlias"</code> </p> </li> <li> <p>ARN of a KMS Key Alias: <code>"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"</code> </p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OutputDataConfig) -> dict:
    out: dict = {}
    out["S3Uri"] = value["s3_uri"]
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> OutputDataConfig:
    out: OutputDataConfig = {}  # type: ignore[typeddict-item]
    if data.get("S3Uri") is not None:
        out["s3_uri"] = data["S3Uri"]
    else:
        raise DeserializationError("OutputDataConfig.s3_uri required")
    if data.get("KmsKeyId") is not None:
        out["kms_key_id"] = data["KmsKeyId"]
    return out
