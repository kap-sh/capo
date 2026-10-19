"""Generated from Smithy shape ``com.amazonaws.ecs#MetricConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.metric_names_list
    import capo_ecs.types.metric_resolution_seconds


class MetricConfiguration(TypedDict, closed=True):
    metric_names: "capo_ecs.types.metric_names_list.MetricNamesList"
    """<p>The list of metric names to configure. The supported metric names are <code>CPUUtilization</code> and <code>MemoryUtilization</code>.</p>"""
    resolution_seconds: (
        "capo_ecs.types.metric_resolution_seconds.MetricResolutionSeconds"
    )
    """<p>The resolution, in seconds, at which to collect the metrics. The valid values are <code>20</code> and <code>60</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetricConfiguration) -> dict:
    out: dict = {}
    import capo_ecs.types.metric_names_list

    out["metricNames"] = capo_ecs.types.metric_names_list.serialize_aws_json_1_1(
        value["metric_names"]
    )
    out["resolutionSeconds"] = value["resolution_seconds"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MetricConfiguration:
    out: MetricConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("metricNames") is not None:
        import capo_ecs.types.metric_names_list

        out["metric_names"] = capo_ecs.types.metric_names_list.deserialize_aws_json_1_1(
            data["metricNames"]
        )
    else:
        out["metric_names"] = []
    if data.get("resolutionSeconds") is not None:
        out["resolution_seconds"] = data["resolutionSeconds"]
    else:
        out["resolution_seconds"] = 0
    return out
