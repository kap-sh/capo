"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#AgentConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_codeguruprofiler.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codeguruprofiler.types.agent_parameters


class AgentConfiguration(TypedDict, closed=True):
    should_profile: "bool"
    """<p> A <code>Boolean</code> that specifies whether the profiling agent collects profiling data or not. Set to <code>true</code> to enable profiling. </p>"""
    period_in_seconds: "int"
    """<p> How long a profiling agent should send profiling data using <a href="https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ConfigureAgent.html"> <code>ConfigureAgent</code> </a>. For example, if this is set to 300, the profiling agent calls <a href="https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ConfigureAgent.html"> <code>ConfigureAgent</code> </a> every 5 minutes to submit the profiled data collected during that period. </p>"""
    agent_parameters: NotRequired[
        "capo_codeguruprofiler.types.agent_parameters.AgentParameters"
    ]
    """<p> Parameters used by the profiler. The valid parameters are: </p> <ul> <li> <p> <code>MaxStackDepth</code> - The maximum depth of the stacks in the code that is represented in the profile. For example, if CodeGuru Profiler finds a method <code>A</code>, which calls method <code>B</code>, which calls method <code>C</code>, which calls method <code>D</code>, then the depth is 4. If the <code>maxDepth</code> is set to 2, then the profiler evaluates <code>A</code> and <code>B</code>. </p> </li> <li> <p> <code>MemoryUsageLimitPercent</code> - The percentage of memory that is used by the profiler.</p> </li> <li> <p> <code>MinimumTimeForReportingInMilliseconds</code> - The minimum time in milliseconds between sending reports. </p> </li> <li> <p> <code>ReportingIntervalInMilliseconds</code> - The reporting interval in milliseconds used to report profiles. </p> </li> <li> <p> <code>SamplingIntervalInMilliseconds</code> - The sampling interval in milliseconds that is used to profile samples. </p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgentConfiguration) -> dict:
    out: dict = {}
    out["shouldProfile"] = value["should_profile"]
    out["periodInSeconds"] = value["period_in_seconds"]
    if "agent_parameters" in value:
        import capo_codeguruprofiler.types.agent_parameters

        out["agentParameters"] = (
            capo_codeguruprofiler.types.agent_parameters.serialize_json(
                value["agent_parameters"]
            )
        )
    return out


def deserialize_json(data: dict) -> AgentConfiguration:
    out: AgentConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("shouldProfile") is not None:
        out["should_profile"] = data["shouldProfile"]
    else:
        raise DeserializationError("AgentConfiguration.should_profile required")
    if data.get("periodInSeconds") is not None:
        out["period_in_seconds"] = data["periodInSeconds"]
    else:
        raise DeserializationError("AgentConfiguration.period_in_seconds required")
    if data.get("agentParameters") is not None:
        import capo_codeguruprofiler.types.agent_parameters

        out["agent_parameters"] = (
            capo_codeguruprofiler.types.agent_parameters.deserialize_json(
                data["agentParameters"]
            )
        )
    return out
