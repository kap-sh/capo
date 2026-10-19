"""Generated from Smithy shape ``com.amazonaws.iot#UpdateEncryptionConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.encryption_type
    import capo_iot.types.kms_access_role_arn
    import capo_iot.types.kms_key_arn


class UpdateEncryptionConfigurationRequest(TypedDict, closed=True):
    encryption_type: "capo_iot.types.encryption_type.EncryptionType"
    """<p>The type of the KMS key.</p>"""
    kms_key_arn: NotRequired["capo_iot.types.kms_key_arn.KmsKeyArn"]
    """<p>The ARN of the customer managedKMS key.</p>"""
    kms_access_role_arn: NotRequired[
        "capo_iot.types.kms_access_role_arn.KmsAccessRoleArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the IAM role assumed by Amazon Web Services IoT Core to call KMS on behalf of the customer.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateEncryptionConfigurationRequest) -> dict:
    out: dict = {}
    import capo_iot.types.encryption_type

    out["encryptionType"] = capo_iot.types.encryption_type.serialize_json(
        value["encryption_type"]
    )
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    if "kms_access_role_arn" in value:
        out["kmsAccessRoleArn"] = value["kms_access_role_arn"]
    return out


def deserialize_json(data: dict) -> UpdateEncryptionConfigurationRequest:
    out: UpdateEncryptionConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("encryptionType") is not None:
        import capo_iot.types.encryption_type

        out["encryption_type"] = capo_iot.types.encryption_type.deserialize_json(
            data["encryptionType"]
        )
    else:
        import typing

        out["encryption_type"] = typing.cast(
            "capo_iot.types.encryption_type.EncryptionType", ""
        )
    if data.get("kmsKeyArn") is not None:
        out["kms_key_arn"] = data["kmsKeyArn"]
    if data.get("kmsAccessRoleArn") is not None:
        out["kms_access_role_arn"] = data["kmsAccessRoleArn"]
    return out
