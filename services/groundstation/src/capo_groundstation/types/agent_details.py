"""Generated from Smithy shape ``com.amazonaws.groundstation#AgentDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_groundstation.types.agent_cpu_cores_list
    import capo_groundstation.types.component_version_list
    import capo_groundstation.types.instance_id
    import capo_groundstation.types.instance_type
    import capo_groundstation.types.version_string


class AgentDetails(TypedDict, closed=True):
    agent_version: "capo_groundstation.types.version_string.VersionString"
    """<p>Current agent version.</p>"""
    instance_id: "capo_groundstation.types.instance_id.InstanceId"
    """<p>ID of EC2 instance agent is running on.</p>"""
    instance_type: "capo_groundstation.types.instance_type.InstanceType"
    """<p>Type of EC2 instance agent is running on.</p>"""
    reserved_cpu_cores: NotRequired[
        "capo_groundstation.types.agent_cpu_cores_list.AgentCpuCoresList"
    ]
    """<note> <p>This field should not be used. Use agentCpuCores instead.</p> </note> <p>List of CPU cores reserved for processes other than the agent running on the EC2 instance.</p>"""
    agent_cpu_cores: NotRequired[
        "capo_groundstation.types.agent_cpu_cores_list.AgentCpuCoresList"
    ]
    """<p>List of CPU cores reserved for the agent.</p>"""
    component_versions: (
        "capo_groundstation.types.component_version_list.ComponentVersionList"
    )
    """<p>List of versions being used by agent components.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgentDetails) -> dict:
    out: dict = {}
    out["agentVersion"] = value["agent_version"]
    out["instanceId"] = value["instance_id"]
    out["instanceType"] = value["instance_type"]
    if "reserved_cpu_cores" in value:
        import capo_groundstation.types.agent_cpu_cores_list

        out["reservedCpuCores"] = (
            capo_groundstation.types.agent_cpu_cores_list.serialize_json(
                value["reserved_cpu_cores"]
            )
        )
    if "agent_cpu_cores" in value:
        import capo_groundstation.types.agent_cpu_cores_list

        out["agentCpuCores"] = (
            capo_groundstation.types.agent_cpu_cores_list.serialize_json(
                value["agent_cpu_cores"]
            )
        )
    import capo_groundstation.types.component_version_list

    out["componentVersions"] = (
        capo_groundstation.types.component_version_list.serialize_json(
            value["component_versions"]
        )
    )
    return out


def deserialize_json(data: dict) -> AgentDetails:
    out: AgentDetails = {}  # type: ignore[typeddict-item]
    if data.get("agentVersion") is not None:
        out["agent_version"] = data["agentVersion"]
    else:
        out["agent_version"] = ""
    if data.get("instanceId") is not None:
        out["instance_id"] = data["instanceId"]
    else:
        out["instance_id"] = ""
    if data.get("instanceType") is not None:
        out["instance_type"] = data["instanceType"]
    else:
        out["instance_type"] = ""
    if data.get("reservedCpuCores") is not None:
        import capo_groundstation.types.agent_cpu_cores_list

        out["reserved_cpu_cores"] = (
            capo_groundstation.types.agent_cpu_cores_list.deserialize_json(
                data["reservedCpuCores"]
            )
        )
    if data.get("agentCpuCores") is not None:
        import capo_groundstation.types.agent_cpu_cores_list

        out["agent_cpu_cores"] = (
            capo_groundstation.types.agent_cpu_cores_list.deserialize_json(
                data["agentCpuCores"]
            )
        )
    if data.get("componentVersions") is not None:
        import capo_groundstation.types.component_version_list

        out["component_versions"] = (
            capo_groundstation.types.component_version_list.deserialize_json(
                data["componentVersions"]
            )
        )
    else:
        out["component_versions"] = []
    return out
