"""Generated from Smithy shape ``com.amazonaws.transfer#ListedHostKey``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transfer.types.arn
    import capo_transfer.types.date_imported
    import capo_transfer.types.host_key_description
    import capo_transfer.types.host_key_fingerprint
    import capo_transfer.types.host_key_id
    import capo_transfer.types.host_key_storage_type
    import capo_transfer.types.host_key_type
    import capo_transfer.types.secret_id


class ListedHostKey(TypedDict, closed=True):
    arn: "capo_transfer.types.arn.Arn"
    """<p>The unique Amazon Resource Name (ARN) of the host key.</p>"""
    host_key_id: NotRequired["capo_transfer.types.host_key_id.HostKeyId"]
    """<p>A unique identifier for the host key.</p>"""
    fingerprint: NotRequired[
        "capo_transfer.types.host_key_fingerprint.HostKeyFingerprint"
    ]
    """<p>The public key fingerprint, which is a short sequence of bytes used to identify the longer public key.</p>"""
    description: NotRequired[
        "capo_transfer.types.host_key_description.HostKeyDescription"
    ]
    """<p>The current description for the host key. You can change it by calling the <code>UpdateHostKey</code> operation and providing a new description.</p>"""
    type: NotRequired["capo_transfer.types.host_key_type.HostKeyType"]
    """<p>The encryption algorithm that is used for the host key. The <code>Type</code> parameter is specified by using one of the following values:</p> <ul> <li> <p> <code>ssh-rsa</code> </p> </li> <li> <p> <code>ssh-ed25519</code> </p> </li> <li> <p> <code>ecdsa-sha2-nistp256</code> </p> </li> <li> <p> <code>ecdsa-sha2-nistp384</code> </p> </li> <li> <p> <code>ecdsa-sha2-nistp521</code> </p> </li> </ul>"""
    date_imported: NotRequired["capo_transfer.types.date_imported.DateImported"]
    """<p>The date on which the host key was added to the server.</p>"""
    storage_type: NotRequired[
        "capo_transfer.types.host_key_storage_type.HostKeyStorageType"
    ]
    """<p>Specifies whether the host key is stored by Transfer Family (<code>SERVICE_MANAGED</code>) or in Secrets Manager (<code>SECRETS_MANAGER</code>).</p>"""
    secret_id: NotRequired["capo_transfer.types.secret_id.SecretId"]
    """<p>The ARN of the Secrets Manager secret that stores the host key material, when <code>StorageType</code> is <code>SECRETS_MANAGER</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListedHostKey) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    if "host_key_id" in value:
        out["HostKeyId"] = value["host_key_id"]
    if "fingerprint" in value:
        out["Fingerprint"] = value["fingerprint"]
    if "description" in value:
        out["Description"] = value["description"]
    if "type" in value:
        out["Type"] = value["type"]
    if "date_imported" in value:
        import capo_transfer.types.date_imported

        out["DateImported"] = capo_transfer.types.date_imported.serialize_aws_json_1_1(
            value["date_imported"]
        )
    if "storage_type" in value:
        import capo_transfer.types.host_key_storage_type

        out["StorageType"] = (
            capo_transfer.types.host_key_storage_type.serialize_aws_json_1_1(
                value["storage_type"]
            )
        )
    if "secret_id" in value:
        out["SecretId"] = value["secret_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListedHostKey:
    out: ListedHostKey = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    if data.get("HostKeyId") is not None:
        out["host_key_id"] = data["HostKeyId"]
    if data.get("Fingerprint") is not None:
        out["fingerprint"] = data["Fingerprint"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    if data.get("DateImported") is not None:
        import capo_transfer.types.date_imported

        out["date_imported"] = (
            capo_transfer.types.date_imported.deserialize_aws_json_1_1(
                data["DateImported"]
            )
        )
    if data.get("StorageType") is not None:
        import capo_transfer.types.host_key_storage_type

        out["storage_type"] = (
            capo_transfer.types.host_key_storage_type.deserialize_aws_json_1_1(
                data["StorageType"]
            )
        )
    if data.get("SecretId") is not None:
        out["secret_id"] = data["SecretId"]
    return out
