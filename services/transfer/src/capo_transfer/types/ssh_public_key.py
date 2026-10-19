"""Generated from Smithy shape ``com.amazonaws.transfer#SshPublicKey``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_transfer.types.date_imported
    import capo_transfer.types.ssh_public_key_body
    import capo_transfer.types.ssh_public_key_id


class SshPublicKey(TypedDict, closed=True):
    date_imported: "capo_transfer.types.date_imported.DateImported"
    """<p>Specifies the date that the public key was added to the Transfer Family user.</p>"""
    ssh_public_key_body: "capo_transfer.types.ssh_public_key_body.SshPublicKeyBody"
    """<p>Specifies the content of the SSH public key as specified by the <code>PublicKeyId</code>.</p> <p>Transfer Family accepts RSA, ECDSA, and ED25519 keys.</p>"""
    ssh_public_key_id: "capo_transfer.types.ssh_public_key_id.SshPublicKeyId"
    """<p>Specifies the <code>SshPublicKeyId</code> parameter contains the identifier of the public key.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SshPublicKey) -> dict:
    out: dict = {}
    import capo_transfer.types.date_imported

    out["DateImported"] = capo_transfer.types.date_imported.serialize_aws_json_1_1(
        value["date_imported"]
    )
    out["SshPublicKeyBody"] = value["ssh_public_key_body"]
    out["SshPublicKeyId"] = value["ssh_public_key_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SshPublicKey:
    out: SshPublicKey = {}  # type: ignore[typeddict-item]
    if data.get("DateImported") is not None:
        import capo_transfer.types.date_imported

        out["date_imported"] = (
            capo_transfer.types.date_imported.deserialize_aws_json_1_1(
                data["DateImported"]
            )
        )
    else:
        import datetime

        out["date_imported"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("SshPublicKeyBody") is not None:
        out["ssh_public_key_body"] = data["SshPublicKeyBody"]
    else:
        out["ssh_public_key_body"] = ""
    if data.get("SshPublicKeyId") is not None:
        out["ssh_public_key_id"] = data["SshPublicKeyId"]
    else:
        out["ssh_public_key_id"] = ""
    return out
