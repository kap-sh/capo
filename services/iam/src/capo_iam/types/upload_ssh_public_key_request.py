"""Generated from Smithy shape ``com.amazonaws.iam#UploadSSHPublicKeyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iam._protocol.xml import Element
from capo_iam.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iam.types.public_key_material_type
    import capo_iam.types.user_name_type


class UploadSSHPublicKeyRequest(TypedDict, closed=True):
    user_name: "capo_iam.types.user_name_type.userNameType"
    """<p>The name of the IAM user to associate the SSH public key with.</p> <p>This parameter allows (through its <a href="http://wikipedia.org/wiki/regex">regex pattern</a>) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-</p>"""
    ssh_public_key_body: "capo_iam.types.public_key_material_type.publicKeyMaterialType"
    r"""<p>The SSH public key. The public key must be encoded in ssh-rsa format or PEM format. The minimum bit-length of the public key is 2048 bits. For example, you can generate a 2048-bit key, and the resulting PEM file is 1679 bytes long.</p> <p>The <a href="http://wikipedia.org/wiki/regex">regex pattern</a> used to validate this parameter is a string of characters consisting of the following:</p> <ul> <li> <p>Any printable ASCII character ranging from the space character (<code>\u0020</code>) through the end of the ASCII character range</p> </li> <li> <p>The printable characters in the Basic Latin and Latin-1 Supplement character set (through <code>\u00FF</code>)</p> </li> <li> <p>The special characters tab (<code>\u0009</code>), line feed (<code>\u000A</code>), and carriage return (<code>\u000D</code>)</p> </li> </ul>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: UploadSSHPublicKeyRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}UserName", str(value["user_name"])))
    pairs.append((f"{key_prefix}SSHPublicKeyBody", str(value["ssh_public_key_body"])))


def deserialize_query(el: Element) -> UploadSSHPublicKeyRequest:
    out: UploadSSHPublicKeyRequest = {}  # type: ignore[typeddict-item]
    child_user_name = el.find("UserName")
    if child_user_name is not None:
        out["user_name"] = str(child_user_name.text or "")
    else:
        raise DeserializationError("UploadSSHPublicKeyRequest.user_name required")
    child_ssh_public_key_body = el.find("SSHPublicKeyBody")
    if child_ssh_public_key_body is not None:
        out["ssh_public_key_body"] = str(child_ssh_public_key_body.text or "")
    else:
        raise DeserializationError(
            "UploadSSHPublicKeyRequest.ssh_public_key_body required"
        )
    return out
