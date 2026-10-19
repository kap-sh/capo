"""Generated from Smithy shape ``com.amazonaws.iotsitewise#WorkspaceEncryptionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.encryption_type
    import capo_iotsitewise.types.kms_key_id


class WorkspaceEncryptionConfiguration(TypedDict, closed=True):
    encryption_type: "capo_iotsitewise.types.encryption_type.EncryptionType"
    """<p>The encryption scheme for the workspace. <code>SITEWISE_DEFAULT_ENCRYPTION</code> encrypts data with the IoT SiteWise default key. <code>KMS_BASED_ENCRYPTION</code> encrypts data with the customer managed KMS key identified by <code>kmsKeyId</code>.</p>"""
    kms_key_id: NotRequired["capo_iotsitewise.types.kms_key_id.KmsKeyId"]
    """<p>The customer managed KMS key used when <code>encryptionType</code> is <code>KMS_BASED_ENCRYPTION</code>. Accepts a key ID, key ARN, or key alias. Required for <code>KMS_BASED_ENCRYPTION</code>; must be omitted for <code>SITEWISE_DEFAULT_ENCRYPTION</code>. After a workspace's customer managed key configuration becomes active, the key can't be changed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkspaceEncryptionConfiguration) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.encryption_type

    out["encryptionType"] = capo_iotsitewise.types.encryption_type.serialize_json(
        value["encryption_type"]
    )
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    return out


def deserialize_json(data: dict) -> WorkspaceEncryptionConfiguration:
    out: WorkspaceEncryptionConfiguration = {}  # type: ignore[typeddict-item]
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
