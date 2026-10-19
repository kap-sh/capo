"""Generated from Smithy shape ``com.amazonaws.devopsagent#MCPServerNewRelicConfiguration``."""

from typing_extensions import TypedDict


class MCPServerNewRelicConfiguration(TypedDict, closed=True):
    account_id: "str"
    """<p>New Relic Account ID</p>"""
    endpoint: "str"
    """<p>MCP server endpoint URL (e.g., https://mcp.newrelic.com/mcp/)</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MCPServerNewRelicConfiguration) -> dict:
    out: dict = {}
    out["accountId"] = value["account_id"]
    out["endpoint"] = value["endpoint"]
    return out


def deserialize_json(data: dict) -> MCPServerNewRelicConfiguration:
    out: MCPServerNewRelicConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    else:
        out["account_id"] = ""
    if data.get("endpoint") is not None:
        out["endpoint"] = data["endpoint"]
    else:
        out["endpoint"] = ""
    return out
