"""Generated from Smithy shape ``com.amazonaws.mwaaserverless#EncryptionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mwaa_serverless.types.encryption_type


class EncryptionConfiguration(TypedDict, closed=True):
    type: "capo_mwaa_serverless.types.encryption_type.EncryptionType"
    """<p>The type of encryption to use. Values are <code>AWS_MANAGED_KEY</code> (Amazon Web Services manages the encryption key) or <code>CUSTOMER_MANAGED_KEY</code> (you provide a KMS key).</p>"""
    kms_key_id: NotRequired["str"]
    """<p>The ID or ARN of the Amazon Web Services KMS key to use for encryption. Required when <code>Type</code> is <code>CUSTOMER_MANAGED_KEY</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EncryptionConfiguration) -> dict:
    out: dict = {}
    import capo_mwaa_serverless.types.encryption_type

    out["Type"] = capo_mwaa_serverless.types.encryption_type.serialize_aws_json_1_0(
        value["type"]
    )
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> EncryptionConfiguration:
    out: EncryptionConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        import capo_mwaa_serverless.types.encryption_type

        out["type"] = (
            capo_mwaa_serverless.types.encryption_type.deserialize_aws_json_1_0(
                data["Type"]
            )
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_mwaa_serverless.types.encryption_type.EncryptionType", ""
        )
    if data.get("KmsKeyId") is not None:
        out["kms_key_id"] = data["KmsKeyId"]
    return out
