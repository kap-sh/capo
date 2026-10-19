"""Generated from Smithy shape ``com.amazonaws.directconnect#ConfirmConnectionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_direct_connect.types.connection_id


class ConfirmConnectionRequest(TypedDict, closed=True):
    connection_id: "capo_direct_connect.types.connection_id.ConnectionId"
    """<p>The ID of the hosted connection.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfirmConnectionRequest) -> dict:
    out: dict = {}
    out["connectionId"] = value["connection_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ConfirmConnectionRequest:
    out: ConfirmConnectionRequest = {}  # type: ignore[typeddict-item]
    if data.get("connectionId") is not None:
        out["connection_id"] = data["connectionId"]
    else:
        out["connection_id"] = ""
    return out
