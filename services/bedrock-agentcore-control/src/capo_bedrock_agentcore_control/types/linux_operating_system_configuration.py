"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#LinuxOperatingSystemConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.privilege_mode


class LinuxOperatingSystemConfiguration(TypedDict, closed=True):
    privilege_mode: NotRequired[
        "capo_bedrock_agentcore_control.types.privilege_mode.PrivilegeMode"
    ]
    """<p>The privilege mode of the agents. If you omit this field, the agents run in <code>STANDARD</code> privilege mode. The following values are possible:</p> <ul> <li> <p> <code>STANDARD</code> – The agent runs without elevated privileges. This is the default.</p> </li> <li> <p> <code>PRIVILEGED</code> – The agent runs with elevated privileges on its instance. Use this mode for agents that build container images, run containers, or install system packages. A session that runs a <code>PRIVILEGED</code> agent runs only that agent.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: LinuxOperatingSystemConfiguration) -> dict:
    out: dict = {}
    if "privilege_mode" in value:
        import capo_bedrock_agentcore_control.types.privilege_mode

        out["privilegeMode"] = (
            capo_bedrock_agentcore_control.types.privilege_mode.serialize_json(
                value["privilege_mode"]
            )
        )
    return out


def deserialize_json(data: dict) -> LinuxOperatingSystemConfiguration:
    out: LinuxOperatingSystemConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("privilegeMode") is not None:
        import capo_bedrock_agentcore_control.types.privilege_mode

        out["privilege_mode"] = (
            capo_bedrock_agentcore_control.types.privilege_mode.deserialize_json(
                data["privilegeMode"]
            )
        )
    return out
