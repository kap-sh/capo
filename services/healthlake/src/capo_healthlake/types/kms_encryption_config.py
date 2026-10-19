"""Generated from Smithy shape ``com.amazonaws.healthlake#KmsEncryptionConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_healthlake.types.cmk_type
    import capo_healthlake.types.encryption_key_id


class KmsEncryptionConfig(TypedDict, closed=True):
    cmk_type: "capo_healthlake.types.cmk_type.CmkType"
    """<p>The type of customer-managed-key (CMK) used for encryption.</p>"""
    kms_key_id: NotRequired["capo_healthlake.types.encryption_key_id.EncryptionKeyID"]
    """<p>The Key Management Service (KMS) encryption key id/alias used to encrypt the data store contents at rest.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: KmsEncryptionConfig) -> dict:
    out: dict = {}
    import capo_healthlake.types.cmk_type

    out["CmkType"] = capo_healthlake.types.cmk_type.serialize_aws_json_1_0(
        value["cmk_type"]
    )
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> KmsEncryptionConfig:
    out: KmsEncryptionConfig = {}  # type: ignore[typeddict-item]
    if data.get("CmkType") is not None:
        import capo_healthlake.types.cmk_type

        out["cmk_type"] = capo_healthlake.types.cmk_type.deserialize_aws_json_1_0(
            data["CmkType"]
        )
    else:
        import typing

        out["cmk_type"] = typing.cast("capo_healthlake.types.cmk_type.CmkType", "")
    if data.get("KmsKeyId") is not None:
        out["kms_key_id"] = data["KmsKeyId"]
    return out
