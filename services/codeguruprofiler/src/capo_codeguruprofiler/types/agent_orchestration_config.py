"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#AgentOrchestrationConfig``."""

from typing_extensions import TypedDict


class AgentOrchestrationConfig(TypedDict, closed=True):
    profiling_enabled: "bool"
    """<p> A <code>Boolean</code> that specifies whether the profiling agent collects profiling data or not. Set to <code>true</code> to enable profiling. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgentOrchestrationConfig) -> dict:
    out: dict = {}
    out["profilingEnabled"] = value["profiling_enabled"]
    return out


def deserialize_json(data: dict) -> AgentOrchestrationConfig:
    out: AgentOrchestrationConfig = {}  # type: ignore[typeddict-item]
    if data.get("profilingEnabled") is not None:
        out["profiling_enabled"] = data["profilingEnabled"]
    else:
        out["profiling_enabled"] = False
    return out
