"""Generated from Smithy shape ``com.amazonaws.dataexchange#ExportServerSideEncryption``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dataexchange.types.__string
    import capo_dataexchange.types.server_side_encryption_types


class ExportServerSideEncryption(TypedDict, closed=True):
    kms_key_arn: NotRequired["capo_dataexchange.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the AWS KMS key you want to use to encrypt the Amazon S3 objects. This parameter is required if you choose aws:kms as an encryption type.</p>"""
    type: (
        "capo_dataexchange.types.server_side_encryption_types.ServerSideEncryptionTypes"
    )
    """<p>The type of server side encryption used for encrypting the objects in Amazon S3.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExportServerSideEncryption) -> dict:
    out: dict = {}
    if "kms_key_arn" in value:
        out["KmsKeyArn"] = value["kms_key_arn"]
    out["Type"] = value["type"]
    return out


def deserialize_json(data: dict) -> ExportServerSideEncryption:
    out: ExportServerSideEncryption = {}  # type: ignore[typeddict-item]
    if data.get("KmsKeyArn") is not None:
        out["kms_key_arn"] = data["KmsKeyArn"]
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    else:
        out["type"] = ""
    return out
