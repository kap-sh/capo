"""Generated from Smithy shape ``com.amazonaws.sfn#EncryptionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sfn.types.encryption_type
    import capo_sfn.types.kms_data_key_reuse_period_seconds
    import capo_sfn.types.kms_key_id


class EncryptionConfiguration(TypedDict, closed=True):
    kms_key_id: NotRequired["capo_sfn.types.kms_key_id.KmsKeyId"]
    """<p>An alias, alias ARN, key ID, or key ARN of a symmetric encryption KMS key to encrypt data. To specify a KMS key in a different Amazon Web Services account, you must use the key ARN or alias ARN.</p>"""
    kms_data_key_reuse_period_seconds: NotRequired[
        "capo_sfn.types.kms_data_key_reuse_period_seconds.KmsDataKeyReusePeriodSeconds"
    ]
    """<p>Maximum duration that Step Functions will reuse data keys. When the period expires, Step Functions will call <code>GenerateDataKey</code>. Only applies to customer managed keys.</p>"""
    type: "capo_sfn.types.encryption_type.EncryptionType"
    """<p>Encryption type</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EncryptionConfiguration) -> dict:
    out: dict = {}
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    if "kms_data_key_reuse_period_seconds" in value:
        out["kmsDataKeyReusePeriodSeconds"] = value["kms_data_key_reuse_period_seconds"]
    import capo_sfn.types.encryption_type

    out["type"] = capo_sfn.types.encryption_type.serialize_aws_json_1_0(value["type"])
    return out


def deserialize_aws_json_1_0(data: dict) -> EncryptionConfiguration:
    out: EncryptionConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("kmsKeyId") is not None:
        out["kms_key_id"] = data["kmsKeyId"]
    if data.get("kmsDataKeyReusePeriodSeconds") is not None:
        out["kms_data_key_reuse_period_seconds"] = data["kmsDataKeyReusePeriodSeconds"]
    if data.get("type") is not None:
        import capo_sfn.types.encryption_type

        out["type"] = capo_sfn.types.encryption_type.deserialize_aws_json_1_0(
            data["type"]
        )
    else:
        import typing

        out["type"] = typing.cast("capo_sfn.types.encryption_type.EncryptionType", "")
    return out
