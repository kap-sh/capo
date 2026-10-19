"""Generated from Smithy shape ``com.amazonaws.transfer#DeleteHostKeyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_transfer.types.host_key_id
    import capo_transfer.types.server_id


class DeleteHostKeyRequest(TypedDict, closed=True):
    server_id: "capo_transfer.types.server_id.ServerId"
    """<p>The identifier of the server that contains the host key that you are deleting.</p>"""
    host_key_id: "capo_transfer.types.host_key_id.HostKeyId"
    """<p>The identifier of the host key that you are deleting.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteHostKeyRequest) -> dict:
    out: dict = {}
    out["ServerId"] = value["server_id"]
    out["HostKeyId"] = value["host_key_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteHostKeyRequest:
    out: DeleteHostKeyRequest = {}  # type: ignore[typeddict-item]
    if data.get("ServerId") is not None:
        out["server_id"] = data["ServerId"]
    else:
        out["server_id"] = ""
    if data.get("HostKeyId") is not None:
        out["host_key_id"] = data["HostKeyId"]
    else:
        out["host_key_id"] = ""
    return out
