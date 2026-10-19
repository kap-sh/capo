"""Generated from Smithy shape ``com.amazonaws.iotsitewise#PutDefaultEncryptionConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.encryption_type
    import capo_iotsitewise.types.kms_key_id


class PutDefaultEncryptionConfigurationRequest(TypedDict, closed=True):
    encryption_type: "capo_iotsitewise.types.encryption_type.EncryptionType"
    """<p>The type of encryption used for the encryption configuration.</p>"""
    kms_key_id: NotRequired["capo_iotsitewise.types.kms_key_id.KmsKeyId"]
    """<p>The Key ID of the customer managed key used for KMS encryption. This is required if you use <code>KMS_BASED_ENCRYPTION</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutDefaultEncryptionConfigurationRequest) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.encryption_type

    out["encryptionType"] = capo_iotsitewise.types.encryption_type.serialize_json(
        value["encryption_type"]
    )
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    return out


def deserialize_json(data: dict) -> PutDefaultEncryptionConfigurationRequest:
    out: PutDefaultEncryptionConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("encryptionType") is not None:
        import capo_iotsitewise.types.encryption_type

        out["encryption_type"] = (
            capo_iotsitewise.types.encryption_type.deserialize_json(
                data["encryptionType"]
            )
        )
    else:
        import typing

        out["encryption_type"] = typing.cast(
            "capo_iotsitewise.types.encryption_type.EncryptionType", ""
        )
    if data.get("kmsKeyId") is not None:
        out["kms_key_id"] = data["kmsKeyId"]
    return out
