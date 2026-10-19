"""Generated from Smithy shape ``com.amazonaws.transfer#DeleteSshPublicKeyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_transfer.types.server_id
    import capo_transfer.types.ssh_public_key_id
    import capo_transfer.types.user_name


class DeleteSshPublicKeyRequest(TypedDict, closed=True):
    server_id: "capo_transfer.types.server_id.ServerId"
    """<p>A system-assigned unique identifier for a file transfer protocol-enabled server instance that has the user assigned to it.</p>"""
    ssh_public_key_id: "capo_transfer.types.ssh_public_key_id.SshPublicKeyId"
    """<p>A unique identifier used to reference your user's specific SSH key.</p>"""
    user_name: "capo_transfer.types.user_name.UserName"
    """<p>A unique string that identifies a user whose public key is being deleted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteSshPublicKeyRequest) -> dict:
    out: dict = {}
    out["ServerId"] = value["server_id"]
    out["SshPublicKeyId"] = value["ssh_public_key_id"]
    out["UserName"] = value["user_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteSshPublicKeyRequest:
    out: DeleteSshPublicKeyRequest = {}  # type: ignore[typeddict-item]
    if data.get("ServerId") is not None:
        out["server_id"] = data["ServerId"]
    else:
        out["server_id"] = ""
    if data.get("SshPublicKeyId") is not None:
        out["ssh_public_key_id"] = data["SshPublicKeyId"]
    else:
        out["ssh_public_key_id"] = ""
    if data.get("UserName") is not None:
        out["user_name"] = data["UserName"]
    else:
        out["user_name"] = ""
    return out
