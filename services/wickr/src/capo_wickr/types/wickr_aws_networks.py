"""Generated from Smithy shape ``com.amazonaws.wickr#WickrAwsNetworks``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_wickr.types.generic_string
    import capo_wickr.types.network_id


class WickrAwsNetworks(TypedDict, closed=True):
    region: "capo_wickr.types.generic_string.GenericString"
    """<p>The Amazon Web Services region identifier where the network is hosted (e.g., 'us-east-1').</p>"""
    network_id: "capo_wickr.types.network_id.NetworkId"
    """<p>The network ID of the Wickr Amazon Web Services network.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WickrAwsNetworks) -> dict:
    out: dict = {}
    out["region"] = value["region"]
    out["networkId"] = value["network_id"]
    return out


def deserialize_json(data: dict) -> WickrAwsNetworks:
    out: WickrAwsNetworks = {}  # type: ignore[typeddict-item]
    if data.get("region") is not None:
        out["region"] = data["region"]
    else:
        out["region"] = ""
    if data.get("networkId") is not None:
        out["network_id"] = data["networkId"]
    else:
        out["network_id"] = ""
    return out
