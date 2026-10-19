"""Generated from Smithy shape ``com.amazonaws.directconnect#AssociateHostedConnectionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_direct_connect.types.connection_id


class AssociateHostedConnectionRequest(TypedDict, closed=True):
    connection_id: "capo_direct_connect.types.connection_id.ConnectionId"
    """<p>The ID of the hosted connection.</p>"""
    parent_connection_id: "capo_direct_connect.types.connection_id.ConnectionId"
    """<p>The ID of the interconnect or the LAG.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociateHostedConnectionRequest) -> dict:
    out: dict = {}
    out["connectionId"] = value["connection_id"]
    out["parentConnectionId"] = value["parent_connection_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociateHostedConnectionRequest:
    out: AssociateHostedConnectionRequest = {}  # type: ignore[typeddict-item]
    if data.get("connectionId") is not None:
        out["connection_id"] = data["connectionId"]
    else:
        out["connection_id"] = ""
    if data.get("parentConnectionId") is not None:
        out["parent_connection_id"] = data["parentConnectionId"]
    else:
        out["parent_connection_id"] = ""
    return out
