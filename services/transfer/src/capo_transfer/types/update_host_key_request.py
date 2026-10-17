"""Generated from Smithy shape ``com.amazonaws.transfer#UpdateHostKeyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_transfer.types.host_key_description
    import capo_transfer.types.host_key_id
    import capo_transfer.types.server_id


class UpdateHostKeyRequest(TypedDict, closed=True):
    server_id: "capo_transfer.types.server_id.ServerId"
    """<p>The identifier of the server that contains the host key that you are updating.</p>"""
    host_key_id: "capo_transfer.types.host_key_id.HostKeyId"
    """<p>The identifier of the host key that you are updating.</p>"""
    description: "capo_transfer.types.host_key_description.HostKeyDescription"
    """<p>An updated description for the host key.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateHostKeyRequest) -> dict:
    out: dict = {}
    out["ServerId"] = value["server_id"]
    out["HostKeyId"] = value["host_key_id"]
    out["Description"] = value["description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateHostKeyRequest:
    out: UpdateHostKeyRequest = {}  # type: ignore[typeddict-item]
    if data.get("ServerId") is not None:
        out["server_id"] = data["ServerId"]
    else:
        raise DeserializationError("UpdateHostKeyRequest.server_id required")
    if data.get("HostKeyId") is not None:
        out["host_key_id"] = data["HostKeyId"]
    else:
        raise DeserializationError("UpdateHostKeyRequest.host_key_id required")
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    else:
        raise DeserializationError("UpdateHostKeyRequest.description required")
    return out
