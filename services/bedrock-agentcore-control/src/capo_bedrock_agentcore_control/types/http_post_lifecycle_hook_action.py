"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#HttpPostLifecycleHookAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.lifecycle_hook_path
    import capo_bedrock_agentcore_control.types.server_port


class HttpPostLifecycleHookAction(TypedDict, closed=True):
    path: "capo_bedrock_agentcore_control.types.lifecycle_hook_path.LifecycleHookPath"
    """<p>The path in the agent's container that AgentCore Runtime sends the <code>POST</code> request to.</p>"""
    port: NotRequired["capo_bedrock_agentcore_control.types.server_port.ServerPort"]
    """<p>The port in the agent's container that AgentCore Runtime sends the <code>POST</code> request to. If you don't specify a port, the default is the runtime's server port: the port in the protocol configuration if one is set, otherwise the protocol's default port.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HttpPostLifecycleHookAction) -> dict:
    out: dict = {}
    out["path"] = value["path"]
    if "port" in value:
        out["port"] = value["port"]
    return out


def deserialize_json(data: dict) -> HttpPostLifecycleHookAction:
    out: HttpPostLifecycleHookAction = {}  # type: ignore[typeddict-item]
    if data.get("path") is not None:
        out["path"] = data["path"]
    else:
        out["path"] = ""
    if data.get("port") is not None:
        out["port"] = data["port"]
    return out
