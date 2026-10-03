"""Generated from Smithy shape ``com.amazonaws.devopsguru#KMSServerSideEncryptionIntegrationConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_guru.types.kms_key_id
    import capo_devops_guru.types.opt_in_status
    import capo_devops_guru.types.server_side_encryption_type


class KMSServerSideEncryptionIntegrationConfig(TypedDict, closed=True):
    kms_key_id: NotRequired["capo_devops_guru.types.kms_key_id.KMSKeyId"]
    """<p> Describes the specified KMS key.</p> <p>To specify a KMS key, use its key ID, key ARN, alias name, or alias ARN. When using an alias name, prefix it with "alias/". If you specify a predefined Amazon Web Services alias (an Amazon Web Services alias with no key ID), Amazon Web Services KMS associates the alias with an Amazon Web Services managed key and returns its KeyId and Arn in the response. To specify a KMS key in a different Amazon Web Services account, you must use the key ARN or alias ARN.</p> <p>For example: </p> <p>Key ID: 1234abcd-12ab-34cd-56ef-1234567890ab</p> <p>Key ARN: arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab</p> <p>Alias name: alias/ExampleAlias</p> <p>Alias ARN: arn:aws:kms:us-east-2:111122223333:alias/ExampleAlias</p>"""
    opt_in_status: NotRequired["capo_devops_guru.types.opt_in_status.OptInStatus"]
    """<p> Specifies if DevOps Guru is enabled for KMS integration. </p>"""
    type: NotRequired[
        "capo_devops_guru.types.server_side_encryption_type.ServerSideEncryptionType"
    ]
    """<p> The type of KMS key used. Customer managed keys are the KMS keys that you create. Amazon Web Services owned keys are keys that are owned and managed by DevOps Guru. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KMSServerSideEncryptionIntegrationConfig) -> dict:
    out: dict = {}
    if "kms_key_id" in value:
        out["KMSKeyId"] = value["kms_key_id"]
    if "opt_in_status" in value:
        import capo_devops_guru.types.opt_in_status

        out["OptInStatus"] = capo_devops_guru.types.opt_in_status.serialize_json(
            value["opt_in_status"]
        )
    if "type" in value:
        import capo_devops_guru.types.server_side_encryption_type

        out["Type"] = capo_devops_guru.types.server_side_encryption_type.serialize_json(
            value["type"]
        )
    return out


def deserialize_json(data: dict) -> KMSServerSideEncryptionIntegrationConfig:
    out: KMSServerSideEncryptionIntegrationConfig = {}  # type: ignore[typeddict-item]
    if data.get("KMSKeyId") is not None:
        out["kms_key_id"] = data["KMSKeyId"]
    if data.get("OptInStatus") is not None:
        import capo_devops_guru.types.opt_in_status

        out["opt_in_status"] = capo_devops_guru.types.opt_in_status.deserialize_json(
            data["OptInStatus"]
        )
    if data.get("Type") is not None:
        import capo_devops_guru.types.server_side_encryption_type

        out["type"] = (
            capo_devops_guru.types.server_side_encryption_type.deserialize_json(
                data["Type"]
            )
        )
    return out
