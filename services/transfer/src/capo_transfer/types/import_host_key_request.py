"""Generated from Smithy shape ``com.amazonaws.transfer#ImportHostKeyRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_transfer.types.host_key
    import capo_transfer.types.host_key_description
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
    return out


def deserialize_aws_json_1_1(data: dict) -> ImportHostKeyRequest:
    out: ImportHostKeyRequest = {}  # type: ignore[typeddict-item]
    if data.get("ServerId") is not None:
        out["server_id"] = data["ServerId"]
    else:
        raise DeserializationError("ImportHostKeyRequest.server_id required")
    if data.get("HostKeyBody") is not None:
        out["host_key_body"] = data["HostKeyBody"]
    else:
        raise DeserializationError("ImportHostKeyRequest.host_key_body required")
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Tags") is not None:
        import capo_transfer.types.tags

        out["tags"] = capo_transfer.types.tags.deserialize_aws_json_1_1(data["Tags"])
    return out


def redact_sensitive(value: ImportHostKeyRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "host_key_body" in value:
        out["host_key_body"] = "*** Sensitive Data Redacted ***"
    return out
