"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#GetRecommendationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codeguruprofiler.types.anomalies
    import capo_codeguruprofiler.types.profiling_group_name
    import capo_codeguruprofiler.types.recommendations
    import capo_codeguruprofiler.types.timestamp


class GetRecommendationsResponse(TypedDict, closed=True):
    profiling_group_name: (
        "capo_codeguruprofiler.types.profiling_group_name.ProfilingGroupName"
    )
    """<p>The name of the profiling group the analysis data is about.</p>"""
    profile_start_time: "capo_codeguruprofiler.types.timestamp.Timestamp"
    """<p> The start time of the profile the analysis data is about. This is specified using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC. </p>"""
    profile_end_time: "capo_codeguruprofiler.types.timestamp.Timestamp"
    """<p> The end time of the profile the analysis data is about. This is specified using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC. </p>"""
    recommendations: "capo_codeguruprofiler.types.recommendations.Recommendations"
    """<p>The list of recommendations that the analysis found for this profile.</p>"""
    anomalies: "capo_codeguruprofiler.types.anomalies.Anomalies"
    """<p> The list of anomalies that the analysis has found for this profile. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRecommendationsResponse) -> dict:
    out: dict = {}
    out["profilingGroupName"] = value["profiling_group_name"]
    import capo_codeguruprofiler.types.timestamp

    out["profileStartTime"] = capo_codeguruprofiler.types.timestamp.serialize_json(
        value["profile_start_time"]
    )
    import capo_codeguruprofiler.types.timestamp

    out["profileEndTime"] = capo_codeguruprofiler.types.timestamp.serialize_json(
        value["profile_end_time"]
    )
    import capo_codeguruprofiler.types.recommendations

    out["recommendations"] = capo_codeguruprofiler.types.recommendations.serialize_json(
        value["recommendations"]
    )
    import capo_codeguruprofiler.types.anomalies

    out["anomalies"] = capo_codeguruprofiler.types.anomalies.serialize_json(
        value["anomalies"]
    )
    return out


def deserialize_json(data: dict) -> GetRecommendationsResponse:
    out: GetRecommendationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("profilingGroupName") is not None:
        out["profiling_group_name"] = data["profilingGroupName"]
    else:
        out["profiling_group_name"] = ""
    if data.get("profileStartTime") is not None:
        import capo_codeguruprofiler.types.timestamp

        out["profile_start_time"] = (
            capo_codeguruprofiler.types.timestamp.deserialize_json(
                data["profileStartTime"]
            )
        )
    else:
        import datetime

        out["profile_start_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("profileEndTime") is not None:
        import capo_codeguruprofiler.types.timestamp

        out["profile_end_time"] = (
            capo_codeguruprofiler.types.timestamp.deserialize_json(
                data["profileEndTime"]
            )
        )
    else:
        import datetime

        out["profile_end_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("recommendations") is not None:
        import capo_codeguruprofiler.types.recommendations

        out["recommendations"] = (
            capo_codeguruprofiler.types.recommendations.deserialize_json(
                data["recommendations"]
            )
        )
    else:
        out["recommendations"] = []
    if data.get("anomalies") is not None:
        import capo_codeguruprofiler.types.anomalies

        out["anomalies"] = capo_codeguruprofiler.types.anomalies.deserialize_json(
            data["anomalies"]
        )
    else:
        out["anomalies"] = []
    return out
