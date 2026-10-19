"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#CreateProfilingGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeguruprofiler.types.agent_orchestration_config
    import capo_codeguruprofiler.types.client_token
    import capo_codeguruprofiler.types.compute_platform
    import capo_codeguruprofiler.types.profiling_group_name
    import capo_codeguruprofiler.types.tags_map


class CreateProfilingGroupRequest(TypedDict, closed=True):
    profiling_group_name: (
        "capo_codeguruprofiler.types.profiling_group_name.ProfilingGroupName"
    )
    """<p>The name of the profiling group to create.</p>"""
    compute_platform: NotRequired[
        "capo_codeguruprofiler.types.compute_platform.ComputePlatform"
    ]
    """<p> The compute platform of the profiling group. Use <code>AWSLambda</code> if your application runs on AWS Lambda. Use <code>Default</code> if your application runs on a compute platform that is not AWS Lambda, such an Amazon EC2 instance, an on-premises server, or a different platform. If not specified, <code>Default</code> is used. </p>"""
    client_token: "capo_codeguruprofiler.types.client_token.ClientToken"
    """<p> Amazon CodeGuru Profiler uses this universally unique identifier (UUID) to prevent the accidental creation of duplicate profiling groups if there are failures and retries. </p>"""
    agent_orchestration_config: NotRequired[
        "capo_codeguruprofiler.types.agent_orchestration_config.AgentOrchestrationConfig"
    ]
    """<p> Specifies whether profiling is enabled or disabled for the created profiling group. </p>"""
    tags: NotRequired["capo_codeguruprofiler.types.tags_map.TagsMap"]
    """<p> A list of tags to add to the created profiling group. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateProfilingGroupRequest) -> dict:
    out: dict = {}
    out["profilingGroupName"] = value["profiling_group_name"]
    if "compute_platform" in value:
        out["computePlatform"] = value["compute_platform"]
    if "agent_orchestration_config" in value:
        import capo_codeguruprofiler.types.agent_orchestration_config

        out["agentOrchestrationConfig"] = (
            capo_codeguruprofiler.types.agent_orchestration_config.serialize_json(
                value["agent_orchestration_config"]
            )
        )
    if "tags" in value:
        import capo_codeguruprofiler.types.tags_map

        out["tags"] = capo_codeguruprofiler.types.tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateProfilingGroupRequest:
    out: CreateProfilingGroupRequest = {}  # type: ignore[typeddict-item]
    if data.get("profilingGroupName") is not None:
        out["profiling_group_name"] = data["profilingGroupName"]
    else:
        out["profiling_group_name"] = ""
    if data.get("computePlatform") is not None:
        out["compute_platform"] = data["computePlatform"]
    if data.get("agentOrchestrationConfig") is not None:
        import capo_codeguruprofiler.types.agent_orchestration_config

        out["agent_orchestration_config"] = (
            capo_codeguruprofiler.types.agent_orchestration_config.deserialize_json(
                data["agentOrchestrationConfig"]
            )
        )
    if data.get("tags") is not None:
        import capo_codeguruprofiler.types.tags_map

        out["tags"] = capo_codeguruprofiler.types.tags_map.deserialize_json(
            data["tags"]
        )
    return out
