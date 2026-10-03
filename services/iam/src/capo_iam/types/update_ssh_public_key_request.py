"""Generated from Smithy shape ``com.amazonaws.iam#UpdateSSHPublicKeyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iam._protocol.xml import Element
from capo_iam.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iam.types.public_key_id_type
    import capo_iam.types.status_type
    import capo_iam.types.user_name_type


class UpdateSSHPublicKeyRequest(TypedDict, closed=True):
    user_name: "capo_iam.types.user_name_type.userNameType"
    """<p>The name of the IAM user associated with the SSH public key.</p> <p>This parameter allows (through its <a href="http://wikipedia.org/wiki/regex">regex pattern</a>) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-</p>"""
    ssh_public_key_id: "capo_iam.types.public_key_id_type.publicKeyIdType"
    """<p>The unique identifier for the SSH public key.</p> <p>This parameter allows (through its <a href="http://wikipedia.org/wiki/regex">regex pattern</a>) a string of characters that can consist of any upper or lowercased letter or digit.</p>"""
    status: "capo_iam.types.status_type.statusType"
    """<p>The status to assign to the SSH public key. <code>Active</code> means that the key can be used for authentication with an CodeCommit repository. <code>Inactive</code> means that the key cannot be used.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: UpdateSSHPublicKeyRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}UserName", str(value["user_name"])))
    pairs.append((f"{key_prefix}SSHPublicKeyId", str(value["ssh_public_key_id"])))
    import capo_iam.types.status_type

    capo_iam.types.status_type.serialize_query(
        value["status"], pairs, f"{key_prefix}Status"
    )


def deserialize_query(el: Element) -> UpdateSSHPublicKeyRequest:
    out: UpdateSSHPublicKeyRequest = {}  # type: ignore[typeddict-item]
    child_user_name = el.find("UserName")
    if child_user_name is not None:
        out["user_name"] = str(child_user_name.text or "")
    else:
        raise DeserializationError("UpdateSSHPublicKeyRequest.user_name required")
    child_ssh_public_key_id = el.find("SSHPublicKeyId")
    if child_ssh_public_key_id is not None:
        out["ssh_public_key_id"] = str(child_ssh_public_key_id.text or "")
    else:
        raise DeserializationError(
            "UpdateSSHPublicKeyRequest.ssh_public_key_id required"
        )
    child_status = el.find("Status")
    if child_status is not None:
        import capo_iam.types.status_type

        out["status"] = capo_iam.types.status_type.deserialize_query(child_status)
    else:
        raise DeserializationError("UpdateSSHPublicKeyRequest.status required")
    return out
