"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#ProfilingStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeguruprofiler.types.aggregated_profile_time
    import capo_codeguruprofiler.types.timestamp


class ProfilingStatus(TypedDict, closed=True):
    latest_agent_profile_reported_at: NotRequired[
        "capo_codeguruprofiler.types.timestamp.Timestamp"
    ]
    """<p>The date and time when the most recent profile was received. Specify using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC.</p>"""
    latest_aggregated_profile: NotRequired[
        "capo_codeguruprofiler.types.aggregated_profile_time.AggregatedProfileTime"
    ]
    """<p> An <a href="https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_AggregatedProfileTime.html"> <code>AggregatedProfileTime</code> </a> object that contains the aggregation period and start time for an aggregated profile. </p>"""
    latest_agent_orchestrated_at: NotRequired[
        "capo_codeguruprofiler.types.timestamp.Timestamp"
    ]
    """<p>The date and time when the profiling agent most recently pinged back. Specify using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProfilingStatus) -> dict:
    out: dict = {}
    if "latest_agent_profile_reported_at" in value:
        import capo_codeguruprofiler.types.timestamp

        out["latestAgentProfileReportedAt"] = (
            capo_codeguruprofiler.types.timestamp.serialize_json(
                value["latest_agent_profile_reported_at"]
            )
        )
    if "latest_aggregated_profile" in value:
        import capo_codeguruprofiler.types.aggregated_profile_time

        out["latestAggregatedProfile"] = (
            capo_codeguruprofiler.types.aggregated_profile_time.serialize_json(
                value["latest_aggregated_profile"]
            )
        )
    if "latest_agent_orchestrated_at" in value:
        import capo_codeguruprofiler.types.timestamp

        out["latestAgentOrchestratedAt"] = (
            capo_codeguruprofiler.types.timestamp.serialize_json(
                value["latest_agent_orchestrated_at"]
            )
        )
    return out


def deserialize_json(data: dict) -> ProfilingStatus:
    out: ProfilingStatus = {}  # type: ignore[typeddict-item]
    if data.get("latestAgentProfileReportedAt") is not None:
        import capo_codeguruprofiler.types.timestamp

        out["latest_agent_profile_reported_at"] = (
            capo_codeguruprofiler.types.timestamp.deserialize_json(
                data["latestAgentProfileReportedAt"]
            )
        )
    if data.get("latestAggregatedProfile") is not None:
        import capo_codeguruprofiler.types.aggregated_profile_time

        out["latest_aggregated_profile"] = (
            capo_codeguruprofiler.types.aggregated_profile_time.deserialize_json(
                data["latestAggregatedProfile"]
            )
        )
    if data.get("latestAgentOrchestratedAt") is not None:
        import capo_codeguruprofiler.types.timestamp

        out["latest_agent_orchestrated_at"] = (
            capo_codeguruprofiler.types.timestamp.deserialize_json(
                data["latestAgentOrchestratedAt"]
            )
        )
    return out
