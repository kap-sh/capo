"""Generated from Smithy shape ``com.amazonaws.wickr#PermittedWickrEnterpriseNetwork``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_wickr.types.generic_string
    import capo_wickr.types.network_id


class PermittedWickrEnterpriseNetwork(TypedDict, closed=True):
    domain: "capo_wickr.types.generic_string.GenericString"
    """<p>The domain identifier for the permitted Wickr enterprise network.</p>"""
    network_id: "capo_wickr.types.network_id.NetworkId"
    """<p>The network ID of the permitted Wickr enterprise network.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PermittedWickrEnterpriseNetwork) -> dict:
    out: dict = {}
    out["domain"] = value["domain"]
    out["networkId"] = value["network_id"]
    return out


def deserialize_json(data: dict) -> PermittedWickrEnterpriseNetwork:
    out: PermittedWickrEnterpriseNetwork = {}  # type: ignore[typeddict-item]
    if data.get("domain") is not None:
        out["domain"] = data["domain"]
    else:
        out["domain"] = ""
    if data.get("networkId") is not None:
        out["network_id"] = data["networkId"]
    else:
        out["network_id"] = ""
    return out
