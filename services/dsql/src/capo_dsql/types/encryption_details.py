"""Generated from Smithy shape ``com.amazonaws.dsql#EncryptionDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dsql.types.encryption_status
    import capo_dsql.types.encryption_type
    import capo_dsql.types.kms_key_arn


class EncryptionDetails(TypedDict, closed=True):
    encryption_type: "capo_dsql.types.encryption_type.EncryptionType"
    """<p>The type of encryption that protects the data on your cluster.</p>"""
    kms_key_arn: NotRequired["capo_dsql.types.kms_key_arn.KmsKeyArn"]
    """<p>The ARN of the KMS key that encrypts data in the cluster.</p>"""
    encryption_status: "capo_dsql.types.encryption_status.EncryptionStatus"
    """<p>The status of encryption for the cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EncryptionDetails) -> dict:
    out: dict = {}
    import capo_dsql.types.encryption_type

    out["encryptionType"] = capo_dsql.types.encryption_type.serialize_json(
        value["encryption_type"]
    )
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    import capo_dsql.types.encryption_status

    out["encryptionStatus"] = capo_dsql.types.encryption_status.serialize_json(
        value["encryption_status"]
    )
    return out


def deserialize_json(data: dict) -> EncryptionDetails:
    out: EncryptionDetails = {}  # type: ignore[typeddict-item]
    if data.get("encryptionType") is not None:
        import capo_dsql.types.encryption_type

        out["encryption_type"] = capo_dsql.types.encryption_type.deserialize_json(
            data["encryptionType"]
        )
    else:
        import typing

        out["encryption_type"] = typing.cast(
            "capo_dsql.types.encryption_type.EncryptionType", ""
        )
    if data.get("kmsKeyArn") is not None:
        out["kms_key_arn"] = data["kmsKeyArn"]
    if data.get("encryptionStatus") is not None:
        import capo_dsql.types.encryption_status

        out["encryption_status"] = capo_dsql.types.encryption_status.deserialize_json(
            data["encryptionStatus"]
        )
    else:
        import typing

        out["encryption_status"] = typing.cast(
            "capo_dsql.types.encryption_status.EncryptionStatus", ""
        )
    return out
