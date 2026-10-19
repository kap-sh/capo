"""Generated from Smithy shape ``com.amazonaws.transfer#ImportHostKeyRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transfer.types.host_key
    import capo_transfer.types.host_key_description
    import capo_transfer.types.host_key_storage_type
    import capo_transfer.types.kms_key
    import capo_transfer.types.server_id
    import capo_transfer.types.tags


class ImportHostKeyRequest(TypedDict, closed=True):
    server_id: "capo_transfer.types.server_id.ServerId"
    """<p>The identifier of the server that contains the host key that you are importing.</p>"""
    host_key_body: "capo_transfer.types.host_key.HostKey"
    """<p>The private key portion of an SSH key pair.</p> <p>Transfer Family accepts RSA, ECDSA, and ED25519 keys.</p>"""
    description: NotRequired[
        "capo_transfer.types.host_key_description.HostKeyDescription"
    ]
    """<p>The text description that identifies this host key.</p>"""
    tags: NotRequired["capo_transfer.types.tags.Tags"]
    """<p>Key-value pairs that can be used to group and search for host keys.</p>"""
    storage_type: NotRequired[
        "capo_transfer.types.host_key_storage_type.HostKeyStorageType"
    ]
    """<p>Specifies whether the host key is stored by Transfer Family (<code>SERVICE_MANAGED</code>) or in Secrets Manager (<code>SECRETS_MANAGER</code>). When you specify <code>SECRETS_MANAGER</code>, Transfer Family stores the private host key material in an Secrets Manager secret.</p>"""
    kms_key: NotRequired["capo_transfer.types.kms_key.KmsKey"]
    """<p>The Amazon Resource Name (ARN) of the KMS key used to encrypt the Secrets Manager secret that stores the host key. If you specify a customer managed key, its key policy must allow the <code>AWSServiceRoleForTransfer</code> service-linked role to decrypt the secret. If you don't specify a value, Transfer Family uses the Amazon Web Services managed key for Secrets Manager.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImportHostKeyRequest) -> dict:
    out: dict = {}
    out["ServerId"] = value["server_id"]
    out["HostKeyBody"] = value["host_key_body"]
    if "description" in value:
        out["Description"] = value["description"]
    if "tags" in value:
        import capo_transfer.types.tags

        out["Tags"] = capo_transfer.types.tags.serialize_aws_json_1_1(value["tags"])
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


def deserialize_aws_json_1_1(data: dict) -> ImportHostKeyRequest:
    out: ImportHostKeyRequest = {}  # type: ignore[typeddict-item]
    if data.get("ServerId") is not None:
        out["server_id"] = data["ServerId"]
    else:
        out["server_id"] = ""
    if data.get("HostKeyBody") is not None:
        out["host_key_body"] = data["HostKeyBody"]
    else:
        out["host_key_body"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Tags") is not None:
        import capo_transfer.types.tags

        out["tags"] = capo_transfer.types.tags.deserialize_aws_json_1_1(data["Tags"])
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


def redact_sensitive(value: ImportHostKeyRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "host_key_body" in value:
        out["host_key_body"] = "*** Sensitive Data Redacted ***"
    return out
