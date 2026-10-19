"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#EncryptionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.encryption_strategy
    import capo_cloudwatchomni.types.kms_key_arn


class EncryptionConfiguration(TypedDict, closed=True):
    encryption_strategy: (
        "capo_cloudwatchomni.types.encryption_strategy.EncryptionStrategy"
    )
    """Which kind of key to use. Required."""
    kms_key_arn: NotRequired["capo_cloudwatchomni.types.kms_key_arn.KmsKeyArn"]
    """Customer managed KMS key ARN. Required when `encryptionStrategy` is CUSTOMER_MANAGED, and must be omitted when it is AWS_OWNED. Must be a symmetric ENCRYPT_DECRYPT key in the caller's account and region."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EncryptionConfiguration) -> dict:
    out: dict = {}
    import capo_cloudwatchomni.types.encryption_strategy

    out["encryptionStrategy"] = (
        capo_cloudwatchomni.types.encryption_strategy.serialize_cbor(
            value["encryption_strategy"]
        )
    )
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    return out


def deserialize_cbor(data: dict) -> EncryptionConfiguration:
    out: EncryptionConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("encryptionStrategy") is not None:
        import capo_cloudwatchomni.types.encryption_strategy

        out["encryption_strategy"] = (
            capo_cloudwatchomni.types.encryption_strategy.deserialize_cbor(
                data["encryptionStrategy"]
            )
        )
    else:
        import typing

        out["encryption_strategy"] = typing.cast(
            "capo_cloudwatchomni.types.encryption_strategy.EncryptionStrategy", ""
        )
    if data.get("kmsKeyArn") is not None:
        out["kms_key_arn"] = data["kmsKeyArn"]
    return out
