"""Generated from Smithy shape ``com.amazonaws.directconnect#AssociateConnectionWithLagRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_direct_connect.types.connection_id
    import capo_direct_connect.types.lag_id


class AssociateConnectionWithLagRequest(TypedDict, closed=True):
    connection_id: "capo_direct_connect.types.connection_id.ConnectionId"
    """<p>The ID of the connection.</p>"""
    lag_id: "capo_direct_connect.types.lag_id.LagId"
    """<p>The ID of the LAG with which to associate the connection.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociateConnectionWithLagRequest) -> dict:
    out: dict = {}
    out["connectionId"] = value["connection_id"]
    out["lagId"] = value["lag_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociateConnectionWithLagRequest:
    out: AssociateConnectionWithLagRequest = {}  # type: ignore[typeddict-item]
    if data.get("connectionId") is not None:
        out["connection_id"] = data["connectionId"]
    else:
        out["connection_id"] = ""
    if data.get("lagId") is not None:
        out["lag_id"] = data["lagId"]
    else:
        out["lag_id"] = ""
    return out
