"""Generated from Smithy shape ``com.amazonaws.iam#SSHPublicKeyMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iam._protocol.xml import Element
from capo_iam.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iam.types.date_type
    import capo_iam.types.public_key_id_type
    import capo_iam.types.status_type
    import capo_iam.types.user_name_type


class SSHPublicKeyMetadata(TypedDict, closed=True):
    user_name: "capo_iam.types.user_name_type.userNameType"
    """<p>The name of the IAM user associated with the SSH public key.</p>"""
    ssh_public_key_id: "capo_iam.types.public_key_id_type.publicKeyIdType"
    """<p>The unique identifier for the SSH public key.</p>"""
    status: "capo_iam.types.status_type.statusType"
    """<p>The status of the SSH public key. <code>Active</code> means that the key can be used for authentication with an CodeCommit repository. <code>Inactive</code> means that the key cannot be used.</p>"""
    upload_date: "capo_iam.types.date_type.dateType"
    """<p>The date and time, in <a href="http://www.iso.org/iso/iso8601">ISO 8601 date-time format</a>, when the SSH public key was uploaded.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: SSHPublicKeyMetadata, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}UserName", str(value["user_name"])))
    pairs.append((f"{key_prefix}SSHPublicKeyId", str(value["ssh_public_key_id"])))
    import capo_iam.types.status_type

    capo_iam.types.status_type.serialize_query(
        value["status"], pairs, f"{key_prefix}Status"
    )
    import capo_iam.types.date_type

    capo_iam.types.date_type.serialize_query(
        value["upload_date"], pairs, f"{key_prefix}UploadDate"
    )


def deserialize_query(el: Element) -> SSHPublicKeyMetadata:
    out: SSHPublicKeyMetadata = {}  # type: ignore[typeddict-item]
    child_user_name = el.find("UserName")
    if child_user_name is not None:
        out["user_name"] = str(child_user_name.text or "")
    else:
        raise DeserializationError("SSHPublicKeyMetadata.user_name required")
    child_ssh_public_key_id = el.find("SSHPublicKeyId")
    if child_ssh_public_key_id is not None:
        out["ssh_public_key_id"] = str(child_ssh_public_key_id.text or "")
    else:
        raise DeserializationError("SSHPublicKeyMetadata.ssh_public_key_id required")
    child_status = el.find("Status")
    if child_status is not None:
        import capo_iam.types.status_type

        out["status"] = capo_iam.types.status_type.deserialize_query(child_status)
    else:
        raise DeserializationError("SSHPublicKeyMetadata.status required")
    child_upload_date = el.find("UploadDate")
    if child_upload_date is not None:
        import capo_iam.types.date_type

        out["upload_date"] = capo_iam.types.date_type.deserialize_query(
            child_upload_date
        )
    else:
        raise DeserializationError("SSHPublicKeyMetadata.upload_date required")
    return out
