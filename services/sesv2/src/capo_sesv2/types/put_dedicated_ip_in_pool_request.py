"""Generated from Smithy shape ``com.amazonaws.sesv2#PutDedicatedIpInPoolRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.ip
    import capo_sesv2.types.pool_name


class PutDedicatedIpInPoolRequest(TypedDict, closed=True):
    ip: "capo_sesv2.types.ip.Ip"
    """<p>The IP address that you want to move to the dedicated IP pool. The value you specify has to be a dedicated IP address that's associated with your Amazon Web Services account.</p>"""
    destination_pool_name: "capo_sesv2.types.pool_name.PoolName"
    """<p>The name of the IP pool that you want to add the dedicated IP address to. You have to specify an IP pool that already exists.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutDedicatedIpInPoolRequest) -> dict:
    out: dict = {}
    out["DestinationPoolName"] = value["destination_pool_name"]
    return out


def deserialize_json(data: dict) -> PutDedicatedIpInPoolRequest:
    out: PutDedicatedIpInPoolRequest = {}  # type: ignore[typeddict-item]
    if data.get("DestinationPoolName") is not None:
        out["destination_pool_name"] = data["DestinationPoolName"]
    else:
        out["destination_pool_name"] = ""
    return out
