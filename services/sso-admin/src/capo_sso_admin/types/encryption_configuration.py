"""Generated from Smithy shape ``com.amazonaws.ssoadmin#EncryptionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sso_admin.types.kms_key_arn
    import capo_sso_admin.types.kms_key_type


class EncryptionConfiguration(TypedDict, closed=True):
    key_type: "capo_sso_admin.types.kms_key_type.KmsKeyType"
    """<p>The type of KMS key used for encryption.</p>"""
    kms_key_arn: NotRequired["capo_sso_admin.types.kms_key_arn.KmsKeyArn"]
    """<p>The ARN of the KMS key used to encrypt data. Required when KeyType is CUSTOMER_MANAGED_KEY. Cannot be specified when KeyType is AWS_OWNED_KMS_KEY.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EncryptionConfiguration) -> dict:
    out: dict = {}
    import capo_sso_admin.types.kms_key_type

    out["KeyType"] = capo_sso_admin.types.kms_key_type.serialize_aws_json_1_1(
        value["key_type"]
    )
    if "kms_key_arn" in value:
        out["KmsKeyArn"] = value["kms_key_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EncryptionConfiguration:
    out: EncryptionConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("KeyType") is not None:
        import capo_sso_admin.types.kms_key_type

        out["key_type"] = capo_sso_admin.types.kms_key_type.deserialize_aws_json_1_1(
            data["KeyType"]
        )
    else:
        import typing

        out["key_type"] = typing.cast(
            "capo_sso_admin.types.kms_key_type.KmsKeyType", ""
        )
    if data.get("KmsKeyArn") is not None:
        out["kms_key_arn"] = data["KmsKeyArn"]
    return out
