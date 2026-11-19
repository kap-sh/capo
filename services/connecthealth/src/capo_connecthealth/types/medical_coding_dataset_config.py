"""Generated from Smithy shape ``com.amazonaws.connecthealth#MedicalCodingDatasetConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connecthealth.types.s3_uri


class MedicalCodingDatasetConfig(TypedDict, closed=True):
    s3_input_path: "capo_connecthealth.types.s3_uri.S3Uri"
    """<p>The Amazon S3 location of your coded examples. You need s3:GetObject and s3:ListBucket permissions for it, and kms:Decrypt if you encrypt it with an AWS KMS key.</p>"""
    s3_output_path: "capo_connecthealth.types.s3_uri.S3Uri"
    """<p>The Amazon S3 location where Amazon Connect Health writes the evaluation scores for the dataset. You need s3:PutObject permission for it, and kms:GenerateDataKey if you encrypt it with an AWS KMS key.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MedicalCodingDatasetConfig) -> dict:
    out: dict = {}
    out["s3InputPath"] = value["s3_input_path"]
    out["s3OutputPath"] = value["s3_output_path"]
    return out


def deserialize_json(data: dict) -> MedicalCodingDatasetConfig:
    out: MedicalCodingDatasetConfig = {}  # type: ignore[typeddict-item]
    if data.get("s3InputPath") is not None:
        out["s3_input_path"] = data["s3InputPath"]
    else:
        out["s3_input_path"] = ""
    if data.get("s3OutputPath") is not None:
        out["s3_output_path"] = data["s3OutputPath"]
    else:
        out["s3_output_path"] = ""
    return out
