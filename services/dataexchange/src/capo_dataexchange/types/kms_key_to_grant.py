"""Generated from Smithy shape ``com.amazonaws.dataexchange#KmsKeyToGrant``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_dataexchange.types.kms_key_arn


class KmsKeyToGrant(TypedDict, closed=True):
    kms_key_arn: "capo_dataexchange.types.kms_key_arn.KmsKeyArn"
    """<p>The AWS KMS CMK (Key Management System Customer Managed Key) used to encrypt S3 objects in the shared S3 Bucket. AWS Data exchange will create a KMS grant for each subscriber to allow them to access and decrypt their entitled data that is encrypted using this KMS key specified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KmsKeyToGrant) -> dict:
    out: dict = {}
    out["KmsKeyArn"] = value["kms_key_arn"]
    return out


def deserialize_json(data: dict) -> KmsKeyToGrant:
    out: KmsKeyToGrant = {}  # type: ignore[typeddict-item]
    if data.get("KmsKeyArn") is not None:
        out["kms_key_arn"] = data["KmsKeyArn"]
    else:
        out["kms_key_arn"] = ""
    return out
