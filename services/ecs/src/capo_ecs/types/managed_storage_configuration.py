"""Generated from Smithy shape ``com.amazonaws.ecs#ManagedStorageConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.string


class ManagedStorageConfiguration(TypedDict, closed=True):
    kms_key_id: NotRequired["capo_ecs.types.string.String"]
    """<p>Specify a Key Management Service key ID to encrypt Amazon ECS managed storage.</p> <p> When you specify a <code>kmsKeyId</code>, Amazon ECS uses the key to encrypt data volumes managed by Amazon ECS that are attached to tasks in the cluster. The following data volumes are managed by Amazon ECS: Amazon EBS. For more information about encryption of Amazon EBS volumes attached to Amazon ECS tasks, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ebs-kms-encryption.html">Encrypt data stored in Amazon EBS volumes for Amazon ECS</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <p>The key must be a single Region key.</p>"""
    fargate_ephemeral_storage_kms_key_id: NotRequired["capo_ecs.types.string.String"]
    """<p>Specify the Key Management Service key ID for Fargate ephemeral storage.</p> <p>When you specify a <code>fargateEphemeralStorageKmsKeyId</code>, Amazon Web Services Fargate uses the key to encrypt data at rest in ephemeral storage. For more information about Fargate ephemeral storage encryption, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/fargate-storage-encryption.html">Customer managed keys for Amazon Web Services Fargate ephemeral storage for Amazon ECS</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <p>The key must be a single Region key.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ManagedStorageConfiguration) -> dict:
    out: dict = {}
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    if "fargate_ephemeral_storage_kms_key_id" in value:
        out["fargateEphemeralStorageKmsKeyId"] = value[
            "fargate_ephemeral_storage_kms_key_id"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> ManagedStorageConfiguration:
    out: ManagedStorageConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("kmsKeyId") is not None:
        out["kms_key_id"] = data["kmsKeyId"]
    if data.get("fargateEphemeralStorageKmsKeyId") is not None:
        out["fargate_ephemeral_storage_kms_key_id"] = data[
            "fargateEphemeralStorageKmsKeyId"
        ]
    return out
