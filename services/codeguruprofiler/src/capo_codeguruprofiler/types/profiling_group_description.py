"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#ProfilingGroupDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeguruprofiler.types.agent_orchestration_config
    import capo_codeguruprofiler.types.compute_platform
    import capo_codeguruprofiler.types.profiling_group_arn
    import capo_codeguruprofiler.types.profiling_group_name
    import capo_codeguruprofiler.types.profiling_status
    import capo_codeguruprofiler.types.tags_map
    import capo_codeguruprofiler.types.timestamp


class ProfilingGroupDescription(TypedDict, closed=True):
    name: NotRequired[
        "capo_codeguruprofiler.types.profiling_group_name.ProfilingGroupName"
    ]
    """<p>The name of the profiling group.</p>"""
    agent_orchestration_config: NotRequired[
        "capo_codeguruprofiler.types.agent_orchestration_config.AgentOrchestrationConfig"
    ]
    """<p> An <a href="https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_AgentOrchestrationConfig.html"> <code>AgentOrchestrationConfig</code> </a> object that indicates if the profiling group is enabled for profiled or not. </p>"""
    arn: NotRequired[
        "capo_codeguruprofiler.types.profiling_group_arn.ProfilingGroupArn"
    ]
    """<p>The Amazon Resource Name (ARN) identifying the profiling group resource.</p>"""
    created_at: NotRequired["capo_codeguruprofiler.types.timestamp.Timestamp"]
    """<p>The time when the profiling group was created. Specify using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC. </p>"""
    updated_at: NotRequired["capo_codeguruprofiler.types.timestamp.Timestamp"]
    """<p> The date and time when the profiling group was last updated. Specify using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC. </p>"""
    profiling_status: NotRequired[
        "capo_codeguruprofiler.types.profiling_status.ProfilingStatus"
    ]
    """<p> A <a href="https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ProfilingStatus.html"> <code>ProfilingStatus</code> </a> object that includes information about the last time a profile agent pinged back, the last time a profile was received, and the aggregation period and start time for the most recent aggregated profile. </p>"""
    compute_platform: NotRequired[
        "capo_codeguruprofiler.types.compute_platform.ComputePlatform"
    ]
    """<p> The compute platform of the profiling group. If it is set to <code>AWSLambda</code>, then the profiled application runs on AWS Lambda. If it is set to <code>Default</code>, then the profiled application runs on a compute platform that is not AWS Lambda, such an Amazon EC2 instance, an on-premises server, or a different platform. The default is <code>Default</code>. </p>"""
    tags: NotRequired["capo_codeguruprofiler.types.tags_map.TagsMap"]
    """<p> A list of the tags that belong to this profiling group. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProfilingGroupDescription) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "agent_orchestration_config" in value:
        import capo_codeguruprofiler.types.agent_orchestration_config

        out["agentOrchestrationConfig"] = (
            capo_codeguruprofiler.types.agent_orchestration_config.serialize_json(
                value["agent_orchestration_config"]
            )
        )
    if "arn" in value:
        out["arn"] = value["arn"]
    if "created_at" in value:
        import capo_codeguruprofiler.types.timestamp

        out["createdAt"] = capo_codeguruprofiler.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_codeguruprofiler.types.timestamp

        out["updatedAt"] = capo_codeguruprofiler.types.timestamp.serialize_json(
            value["updated_at"]
        )
    if "profiling_status" in value:
        import capo_codeguruprofiler.types.profiling_status

        out["profilingStatus"] = (
            capo_codeguruprofiler.types.profiling_status.serialize_json(
                value["profiling_status"]
            )
        )
    if "compute_platform" in value:
        out["computePlatform"] = value["compute_platform"]
    if "tags" in value:
        import capo_codeguruprofiler.types.tags_map

        out["tags"] = capo_codeguruprofiler.types.tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> ProfilingGroupDescription:
    out: ProfilingGroupDescription = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("agentOrchestrationConfig") is not None:
        import capo_codeguruprofiler.types.agent_orchestration_config

        out["agent_orchestration_config"] = (
            capo_codeguruprofiler.types.agent_orchestration_config.deserialize_json(
                data["agentOrchestrationConfig"]
            )
        )
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("createdAt") is not None:
        import capo_codeguruprofiler.types.timestamp

        out["created_at"] = capo_codeguruprofiler.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    if data.get("updatedAt") is not None:
        import capo_codeguruprofiler.types.timestamp

        out["updated_at"] = capo_codeguruprofiler.types.timestamp.deserialize_json(
            data["updatedAt"]
        )
    if data.get("profilingStatus") is not None:
        import capo_codeguruprofiler.types.profiling_status

        out["profiling_status"] = (
            capo_codeguruprofiler.types.profiling_status.deserialize_json(
                data["profilingStatus"]
            )
        )
    if data.get("computePlatform") is not None:
        out["compute_platform"] = data["computePlatform"]
    if data.get("tags") is not None:
        import capo_codeguruprofiler.types.tags_map

        out["tags"] = capo_codeguruprofiler.types.tags_map.deserialize_json(
            data["tags"]
        )
    return out
