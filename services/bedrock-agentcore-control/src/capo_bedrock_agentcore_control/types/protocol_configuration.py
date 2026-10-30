"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ProtocolConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.server_path
    import capo_bedrock_agentcore_control.types.server_port
    import capo_bedrock_agentcore_control.types.server_protocol


class ProtocolConfiguration(TypedDict, closed=True):
    server_protocol: (
        "capo_bedrock_agentcore_control.types.server_protocol.ServerProtocol"
    )
    """<p>The server protocol for the agent runtime. This field specifies which protocol the agent runtime uses to communicate with clients.</p>"""
    port: NotRequired["capo_bedrock_agentcore_control.types.server_port.ServerPort"]
    """<p>The port on which the agent server listens. The port must be between <code>8000</code> and <code>12000</code>, excluding the reserved port <code>8443</code>. When this field is omitted, the default is <code>8080</code> for <code>HTTP</code> and <code>AGUI</code>, <code>8000</code> for <code>MCP</code>, and <code>9000</code> for <code>A2A</code>.</p>"""
    path: NotRequired["capo_bedrock_agentcore_control.types.server_path.ServerPath"]
    """<p>The path on which the agent server accepts requests. The path must begin with <code>/</code>. When this field is omitted, the default is <code>/invocations</code> for <code>HTTP</code> and <code>AGUI</code>, <code>/mcp</code> for <code>MCP</code>, and <code>/</code> for <code>A2A</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProtocolConfiguration) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.server_protocol

    out["serverProtocol"] = (
        capo_bedrock_agentcore_control.types.server_protocol.serialize_json(
            value["server_protocol"]
        )
    )
    if "port" in value:
        out["port"] = value["port"]
    if "path" in value:
        out["path"] = value["path"]
    return out


def deserialize_json(data: dict) -> ProtocolConfiguration:
    out: ProtocolConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("serverProtocol") is not None:
        import capo_bedrock_agentcore_control.types.server_protocol

        out["server_protocol"] = (
            capo_bedrock_agentcore_control.types.server_protocol.deserialize_json(
                data["serverProtocol"]
            )
        )
    else:
        import typing

        out["server_protocol"] = typing.cast(
            "capo_bedrock_agentcore_control.types.server_protocol.ServerProtocol", ""
        )
    if data.get("port") is not None:
        out["port"] = data["port"]
    if data.get("path") is not None:
        out["path"] = data["path"]
    return out
