"""Generated from Smithy shape ``com.amazonaws.devopsagent#MCPServerAuthorizationDiscoveryConfig``."""

from typing_extensions import TypedDict


class MCPServerAuthorizationDiscoveryConfig(TypedDict, closed=True):
    return_to_endpoint: "str"
    """<p>The endpoint to return to after OAuth flow completes (must be AWS console domain)</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MCPServerAuthorizationDiscoveryConfig) -> dict:
    out: dict = {}
    out["returnToEndpoint"] = value["return_to_endpoint"]
    return out


def deserialize_json(data: dict) -> MCPServerAuthorizationDiscoveryConfig:
    out: MCPServerAuthorizationDiscoveryConfig = {}  # type: ignore[typeddict-item]
    if data.get("returnToEndpoint") is not None:
        out["return_to_endpoint"] = data["returnToEndpoint"]
    else:
        out["return_to_endpoint"] = ""
    return out
