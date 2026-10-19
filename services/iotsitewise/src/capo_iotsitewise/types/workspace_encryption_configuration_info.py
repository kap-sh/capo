"""Generated from Smithy shape ``com.amazonaws.iotsitewise#WorkspaceEncryptionConfigurationInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.arn
    import capo_iotsitewise.types.encryption_type


class WorkspaceEncryptionConfigurationInfo(TypedDict, closed=True):
    encryption_type: "capo_iotsitewise.types.encryption_type.EncryptionType"
    """<p>The type of encryption used for the workspace.</p>"""
    kms_key_arn: NotRequired["capo_iotsitewise.types.arn.ARN"]
    """<p>The key ARN of the KMS key used for KMS encryption if <code>encryptionType</code> is <code>KMS_BASED_ENCRYPTION</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkspaceEncryptionConfigurationInfo) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.encryption_type

    out["encryptionType"] = capo_iotsitewise.types.encryption_type.serialize_json(
        value["encryption_type"]
    )
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    return out


def deserialize_json(data: dict) -> WorkspaceEncryptionConfigurationInfo:
    out: WorkspaceEncryptionConfigurationInfo = {}  # type: ignore[typeddict-item]
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
    if data.get("kmsKeyArn") is not None:
        out["kms_key_arn"] = data["kmsKeyArn"]
    return out
