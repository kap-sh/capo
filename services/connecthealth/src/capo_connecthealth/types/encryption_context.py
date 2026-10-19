"""Generated from Smithy shape ``com.amazonaws.connecthealth#EncryptionContext``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connecthealth.types.encryption_type
    import capo_connecthealth.types.kms_key_arn


class EncryptionContext(TypedDict, closed=True):
    encryption_type: "capo_connecthealth.types.encryption_type.EncryptionType"
    """<p>The type of encryption key used.</p>"""
    kms_key_arn: NotRequired["capo_connecthealth.types.kms_key_arn.KmsKeyArn"]
    """<p>The ARN of the KMS key. Only present when encryptionType is CUSTOMER_MANAGED_KEY.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EncryptionContext) -> dict:
    out: dict = {}
    import capo_connecthealth.types.encryption_type

    out["encryptionType"] = capo_connecthealth.types.encryption_type.serialize_json(
        value["encryption_type"]
    )
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    return out


def deserialize_json(data: dict) -> EncryptionContext:
    out: EncryptionContext = {}  # type: ignore[typeddict-item]
    if data.get("encryptionType") is not None:
        import capo_connecthealth.types.encryption_type

        out["encryption_type"] = (
            capo_connecthealth.types.encryption_type.deserialize_json(
                data["encryptionType"]
            )
        )
    else:
        import typing

        out["encryption_type"] = typing.cast(
            "capo_connecthealth.types.encryption_type.EncryptionType", ""
        )
    if data.get("kmsKeyArn") is not None:
        out["kms_key_arn"] = data["kmsKeyArn"]
    return out
