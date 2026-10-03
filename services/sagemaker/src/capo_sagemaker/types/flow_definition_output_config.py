"""Generated from Smithy shape ``com.amazonaws.sagemaker#FlowDefinitionOutputConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.kms_key_id
    import capo_sagemaker.types.s3_uri


class FlowDefinitionOutputConfig(TypedDict, closed=True):
    s3_output_path: NotRequired["capo_sagemaker.types.s3_uri.S3Uri"]
    """<p>The Amazon S3 path where the object containing human output will be made available.</p> <p>To learn more about the format of Amazon A2I output data, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/a2i-output-data.html">Amazon A2I Output Data</a>.</p>"""
    kms_key_id: NotRequired["capo_sagemaker.types.kms_key_id.KmsKeyId"]
    """<p>The Amazon Key Management Service (KMS) key ID for server-side encryption.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FlowDefinitionOutputConfig) -> dict:
    out: dict = {}
    if "s3_output_path" in value:
        out["S3OutputPath"] = value["s3_output_path"]
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FlowDefinitionOutputConfig:
    out: FlowDefinitionOutputConfig = {}  # type: ignore[typeddict-item]
    if data.get("S3OutputPath") is not None:
        out["s3_output_path"] = data["S3OutputPath"]
    if data.get("KmsKeyId") is not None:
        out["kms_key_id"] = data["KmsKeyId"]
    return out
