"""Generated from Smithy shape ``com.amazonaws.ecs#VersionInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.string


class VersionInfo(TypedDict, closed=True):
    agent_version: NotRequired["capo_ecs.types.string.String"]
    """<p>The version number of the Amazon ECS container agent.</p>"""
    agent_hash: NotRequired["capo_ecs.types.string.String"]
    """<p>The Git commit hash for the Amazon ECS container agent build on the <a href="https://github.com/aws/amazon-ecs-agent">amazon-ecs-agent </a> GitHub repository.</p>"""
    docker_version: NotRequired["capo_ecs.types.string.String"]
    """<p>The Docker version that's running on the container instance.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VersionInfo) -> dict:
    out: dict = {}
    if "agent_version" in value:
        out["agentVersion"] = value["agent_version"]
    if "agent_hash" in value:
        out["agentHash"] = value["agent_hash"]
    if "docker_version" in value:
        out["dockerVersion"] = value["docker_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> VersionInfo:
    out: VersionInfo = {}  # type: ignore[typeddict-item]
    if data.get("agentVersion") is not None:
        out["agent_version"] = data["agentVersion"]
    if data.get("agentHash") is not None:
        out["agent_hash"] = data["agentHash"]
    if data.get("dockerVersion") is not None:
        out["docker_version"] = data["dockerVersion"]
    return out
