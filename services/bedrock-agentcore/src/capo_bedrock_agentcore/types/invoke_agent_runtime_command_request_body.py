"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#InvokeAgentRuntimeCommandRequestBody``."""

from typing_extensions import NotRequired, TypedDict


class InvokeAgentRuntimeCommandRequestBody(TypedDict, closed=True):
    command: "str"
    """<p>The shell command to execute on the agent runtime. This command is executed in the runtime environment and its output is streamed back to the caller.</p>"""
    timeout: NotRequired["int"]
    """<p>The maximum duration in seconds to wait for the command to complete. If the command execution exceeds this timeout, it will be terminated. Default is 300 seconds. Minimum is 1 second. Maximum is 3600 seconds.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvokeAgentRuntimeCommandRequestBody) -> dict:
    out: dict = {}
    out["command"] = value["command"]
    if "timeout" in value:
        out["timeout"] = value["timeout"]
    return out


def deserialize_json(data: dict) -> InvokeAgentRuntimeCommandRequestBody:
    out: InvokeAgentRuntimeCommandRequestBody = {}  # type: ignore[typeddict-item]
    if data.get("command") is not None:
        out["command"] = data["command"]
    else:
        out["command"] = ""
    if data.get("timeout") is not None:
        out["timeout"] = data["timeout"]
    return out
