"""Generated from Smithy shape ``com.amazonaws.transfer#UpdateHostKeyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_transfer.types.host_key_id
    import capo_transfer.types.server_id


class UpdateHostKeyResponse(TypedDict, closed=True):
    server_id: "capo_transfer.types.server_id.ServerId"
    """<p>Returns the server identifier for the server that contains the updated host key.</p>"""
    host_key_id: "capo_transfer.types.host_key_id.HostKeyId"
    """<p>Returns the host key identifier for the updated host key.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateHostKeyResponse) -> dict:
    out: dict = {}
    out["ServerId"] = value["server_id"]
    out["HostKeyId"] = value["host_key_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateHostKeyResponse:
    out: UpdateHostKeyResponse = {}  # type: ignore[typeddict-item]
    if data.get("ServerId") is not None:
        out["server_id"] = data["ServerId"]
    else:
        out["server_id"] = ""
    if data.get("HostKeyId") is not None:
        out["host_key_id"] = data["HostKeyId"]
    else:
        out["host_key_id"] = ""
    return out
