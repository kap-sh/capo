"""Generated from Smithy shape ``com.amazonaws.osis#EncryptionAtRestOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_osis.types.kms_key_arn


class EncryptionAtRestOptions(TypedDict, closed=True):
    kms_key_arn: "capo_osis.types.kms_key_arn.KmsKeyArn"
    """<p>The ARN of the KMS key used to encrypt buffer data. By default, data is encrypted using an Amazon Web Services owned key.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EncryptionAtRestOptions) -> dict:
    out: dict = {}
    out["KmsKeyArn"] = value["kms_key_arn"]
    return out


def deserialize_json(data: dict) -> EncryptionAtRestOptions:
    out: EncryptionAtRestOptions = {}  # type: ignore[typeddict-item]
    if data.get("KmsKeyArn") is not None:
        out["kms_key_arn"] = data["KmsKeyArn"]
    else:
        out["kms_key_arn"] = ""
    return out
