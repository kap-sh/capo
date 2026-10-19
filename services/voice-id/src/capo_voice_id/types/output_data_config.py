"""Generated from Smithy shape ``com.amazonaws.voiceid#OutputDataConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_voice_id.types.kms_key_id
    import capo_voice_id.types.s3_uri


class OutputDataConfig(TypedDict, closed=True):
    s3_uri: "capo_voice_id.types.s3_uri.S3Uri"
    """<p>The S3 path of the folder where Voice ID writes the job output file. It has a <code>*.out</code> extension. For example, if the input file name is <code>input-file.json</code> and the output folder path is <code>s3://output-bucket/output-folder</code>, the full output file path is <code>s3://output-bucket/output-folder/job-Id/input-file.json.out</code>.</p>"""
    kms_key_id: NotRequired["capo_voice_id.types.kms_key_id.KmsKeyId"]
    """<p>The identifier of the KMS key you want Voice ID to use to encrypt the output file of a speaker enrollment job/fraudster registration job. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OutputDataConfig) -> dict:
    out: dict = {}
    out["S3Uri"] = value["s3_uri"]
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> OutputDataConfig:
    out: OutputDataConfig = {}  # type: ignore[typeddict-item]
    if data.get("S3Uri") is not None:
        out["s3_uri"] = data["S3Uri"]
    else:
        out["s3_uri"] = ""
    if data.get("KmsKeyId") is not None:
        out["kms_key_id"] = data["KmsKeyId"]
    return out
