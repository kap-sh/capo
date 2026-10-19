"""Generated from Smithy shape ``com.amazonaws.transfer#UpdateHostKeyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transfer.types.host_key_description
    import capo_transfer.types.host_key_id
    import capo_transfer.types.host_key_storage_type
    import capo_transfer.types.kms_key
    import capo_transfer.types.server_id


class UpdateHostKeyRequest(TypedDict, closed=True):
    server_id: "capo_transfer.types.server_id.ServerId"
    """<p>The identifier of the server that contains the host key that you are updating.</p>"""
    host_key_id: "capo_transfer.types.host_key_id.HostKeyId"
    """<p>The identifier of the host key that you are updating.</p>"""
    description: NotRequired[
        "capo_transfer.types.host_key_description.HostKeyDescription"
    ]
    """<p>An updated description for the host key.</p>"""
    storage_type: NotRequired[
        "capo_transfer.types.host_key_storage_type.HostKeyStorageType"
    ]
    """<p>Specifies whether the host key is stored by Transfer Family (<code>SERVICE_MANAGED</code>) or in Secrets Manager (<code>SECRETS_MANAGER</code>). When you specify <code>SECRETS_MANAGER</code>, Transfer Family stores the private host key material in an Secrets Manager secret.</p>"""
    kms_key: NotRequired["capo_transfer.types.kms_key.KmsKey"]
    """<p>The Amazon Resource Name (ARN) of the KMS key used to encrypt the Secrets Manager secret that stores the host key. If you specify a customer managed key, its key policy must allow the <code>AWSServiceRoleForTransfer</code> service-linked role to decrypt the secret. If you don't specify a value, Transfer Family uses the Amazon Web Services managed key for Secrets Manager.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateHostKeyRequest) -> dict:
    out: dict = {}
    out["ServerId"] = value["server_id"]
    out["HostKeyId"] = value["host_key_id"]
    if "description" in value:
        out["Description"] = value["description"]
    if "storage_type" in value:
        import capo_transfer.types.host_key_storage_type

        out["StorageType"] = (
            capo_transfer.types.host_key_storage_type.serialize_aws_json_1_1(
                value["storage_type"]
            )
        )
    if "kms_key" in value:
        out["KmsKey"] = value["kms_key"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateHostKeyRequest:
    out: UpdateHostKeyRequest = {}  # type: ignore[typeddict-item]
    if data.get("ServerId") is not None:
        out["server_id"] = data["ServerId"]
    else:
        out["server_id"] = ""
    if data.get("HostKeyId") is not None:
        out["host_key_id"] = data["HostKeyId"]
    else:
        out["host_key_id"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("StorageType") is not None:
        import capo_transfer.types.host_key_storage_type

        out["storage_type"] = (
            capo_transfer.types.host_key_storage_type.deserialize_aws_json_1_1(
                data["StorageType"]
            )
        )
    if data.get("KmsKey") is not None:
        out["kms_key"] = data["KmsKey"]
    return out
