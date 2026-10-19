"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#SessionStorageConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.mount_path


class SessionStorageConfiguration(TypedDict, closed=True):
    mount_path: "capo_bedrock_agentcore_control.types.mount_path.MountPath"
    """<p>The mount path for the session storage filesystem inside the AgentCore Runtime. The path must be under <code>/mnt</code> with exactly one subdirectory level (for example, <code>/mnt/data</code>).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SessionStorageConfiguration) -> dict:
    out: dict = {}
    out["mountPath"] = value["mount_path"]
    return out


def deserialize_json(data: dict) -> SessionStorageConfiguration:
    out: SessionStorageConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("mountPath") is not None:
        out["mount_path"] = data["mountPath"]
    else:
        out["mount_path"] = ""
    return out
