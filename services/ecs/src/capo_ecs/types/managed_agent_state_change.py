"""Generated from Smithy shape ``com.amazonaws.ecs#ManagedAgentStateChange``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.managed_agent_name
    import capo_ecs.types.string


class ManagedAgentStateChange(TypedDict, closed=True):
    container_name: "capo_ecs.types.string.String"
    """<p>The name of the container that's associated with the managed agent.</p>"""
    managed_agent_name: "capo_ecs.types.managed_agent_name.ManagedAgentName"
    """<p>The name of the managed agent.</p>"""
    status: "capo_ecs.types.string.String"
    """<p>The status of the managed agent.</p>"""
    reason: NotRequired["capo_ecs.types.string.String"]
    """<p>The reason for the status of the managed agent.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ManagedAgentStateChange) -> dict:
    out: dict = {}
    out["containerName"] = value["container_name"]
    import capo_ecs.types.managed_agent_name

    out["managedAgentName"] = capo_ecs.types.managed_agent_name.serialize_aws_json_1_1(
        value["managed_agent_name"]
    )
    out["status"] = value["status"]
    if "reason" in value:
        out["reason"] = value["reason"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ManagedAgentStateChange:
    out: ManagedAgentStateChange = {}  # type: ignore[typeddict-item]
    if data.get("containerName") is not None:
        out["container_name"] = data["containerName"]
    else:
        out["container_name"] = ""
    if data.get("managedAgentName") is not None:
        import capo_ecs.types.managed_agent_name

        out["managed_agent_name"] = (
            capo_ecs.types.managed_agent_name.deserialize_aws_json_1_1(
                data["managedAgentName"]
            )
        )
    else:
        import typing

        out["managed_agent_name"] = typing.cast(
            "capo_ecs.types.managed_agent_name.ManagedAgentName", ""
        )
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        out["status"] = ""
    if data.get("reason") is not None:
        out["reason"] = data["reason"]
    return out
