"""Generated from Smithy shape ``com.amazonaws.iam#GetSSHPublicKeyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iam._protocol.xml import Element
from capo_iam.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iam.types.encoding_type
    import capo_iam.types.public_key_id_type
    import capo_iam.types.user_name_type


class GetSSHPublicKeyRequest(TypedDict, closed=True):
    user_name: "capo_iam.types.user_name_type.userNameType"
    """<p>The name of the IAM user associated with the SSH public key.</p> <p>This parameter allows (through its <a href="http://wikipedia.org/wiki/regex">regex pattern</a>) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-</p>"""
    ssh_public_key_id: "capo_iam.types.public_key_id_type.publicKeyIdType"
    """<p>The unique identifier for the SSH public key.</p> <p>This parameter allows (through its <a href="http://wikipedia.org/wiki/regex">regex pattern</a>) a string of characters that can consist of any upper or lowercased letter or digit.</p>"""
    encoding: "capo_iam.types.encoding_type.encodingType"
    """<p>Specifies the public key encoding format to use in the response. To retrieve the public key in ssh-rsa format, use <code>SSH</code>. To retrieve the public key in PEM format, use <code>PEM</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetSSHPublicKeyRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}UserName", str(value["user_name"])))
    pairs.append((f"{key_prefix}SSHPublicKeyId", str(value["ssh_public_key_id"])))
    import capo_iam.types.encoding_type

    capo_iam.types.encoding_type.serialize_query(
        value["encoding"], pairs, f"{key_prefix}Encoding"
    )


def deserialize_query(el: Element) -> GetSSHPublicKeyRequest:
    out: GetSSHPublicKeyRequest = {}  # type: ignore[typeddict-item]
    child_user_name = el.find("UserName")
    if child_user_name is not None:
        out["user_name"] = str(child_user_name.text or "")
    else:
        raise DeserializationError("GetSSHPublicKeyRequest.user_name required")
    child_ssh_public_key_id = el.find("SSHPublicKeyId")
    if child_ssh_public_key_id is not None:
        out["ssh_public_key_id"] = str(child_ssh_public_key_id.text or "")
    else:
        raise DeserializationError("GetSSHPublicKeyRequest.ssh_public_key_id required")
    child_encoding = el.find("Encoding")
    if child_encoding is not None:
        import capo_iam.types.encoding_type

        out["encoding"] = capo_iam.types.encoding_type.deserialize_query(child_encoding)
    else:
        raise DeserializationError("GetSSHPublicKeyRequest.encoding required")
    return out
