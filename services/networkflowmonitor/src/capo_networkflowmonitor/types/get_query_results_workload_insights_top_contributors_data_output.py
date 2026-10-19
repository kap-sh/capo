"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#GetQueryResultsWorkloadInsightsTopContributorsDataOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkflowmonitor.types.metric_unit
    import capo_networkflowmonitor.types.workload_insights_top_contributors_data_points


class GetQueryResultsWorkloadInsightsTopContributorsDataOutput(TypedDict, closed=True):
    unit: "capo_networkflowmonitor.types.metric_unit.MetricUnit"
    """<p>The units for a metric returned by the query.</p>"""
    datapoints: "capo_networkflowmonitor.types.workload_insights_top_contributors_data_points.WorkloadInsightsTopContributorsDataPoints"
    """<p>The datapoints returned by the query.</p>"""
    next_token: NotRequired["str"]
    """<p>The token for the next set of results. You receive this token from a previous call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: GetQueryResultsWorkloadInsightsTopContributorsDataOutput,
) -> dict:
    out: dict = {}
    import capo_networkflowmonitor.types.metric_unit

    out["unit"] = capo_networkflowmonitor.types.metric_unit.serialize_json(
        value["unit"]
    )
    import capo_networkflowmonitor.types.workload_insights_top_contributors_data_points

    out["datapoints"] = (
        capo_networkflowmonitor.types.workload_insights_top_contributors_data_points.serialize_json(
            value["datapoints"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(
    data: dict,
) -> GetQueryResultsWorkloadInsightsTopContributorsDataOutput:
    out: GetQueryResultsWorkloadInsightsTopContributorsDataOutput = {}  # type: ignore[typeddict-item]
    if data.get("unit") is not None:
        import capo_networkflowmonitor.types.metric_unit

        out["unit"] = capo_networkflowmonitor.types.metric_unit.deserialize_json(
            data["unit"]
        )
    else:
        import typing

        out["unit"] = typing.cast(
            "capo_networkflowmonitor.types.metric_unit.MetricUnit", ""
        )
    if data.get("datapoints") is not None:
        import capo_networkflowmonitor.types.workload_insights_top_contributors_data_points

        out["datapoints"] = (
            capo_networkflowmonitor.types.workload_insights_top_contributors_data_points.deserialize_json(
                data["datapoints"]
            )
        )
    else:
        out["datapoints"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
