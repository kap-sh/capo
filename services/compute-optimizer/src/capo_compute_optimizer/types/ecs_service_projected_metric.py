"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#ECSServiceProjectedMetric``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.ecs_service_metric_name
    import capo_compute_optimizer.types.metric_values
    import capo_compute_optimizer.types.timestamps


class ECSServiceProjectedMetric(TypedDict, closed=True):
    name: NotRequired[
        "capo_compute_optimizer.types.ecs_service_metric_name.ECSServiceMetricName"
    ]
    """<p> The name of the projected metric. </p> <p>The following metrics are available:</p> <ul> <li> <p> <code>Cpu</code> — The percentage of allocated compute units that are currently in use on the service tasks.</p> </li> <li> <p> <code>Memory</code> — The percentage of memory that's currently in use on the service tasks.</p> </li> </ul>"""
    timestamps: NotRequired["capo_compute_optimizer.types.timestamps.Timestamps"]
    """<p> The timestamps of the projected metric. </p>"""
    upper_bound_values: NotRequired[
        "capo_compute_optimizer.types.metric_values.MetricValues"
    ]
    """<p> The upper bound values for the projected metric. </p>"""
    lower_bound_values: NotRequired[
        "capo_compute_optimizer.types.metric_values.MetricValues"
    ]
    """<p> The lower bound values for the projected metric. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ECSServiceProjectedMetric) -> dict:
    out: dict = {}
    if "name" in value:
        import capo_compute_optimizer.types.ecs_service_metric_name

        out["name"] = (
            capo_compute_optimizer.types.ecs_service_metric_name.serialize_aws_json_1_0(
                value["name"]
            )
        )
    if "timestamps" in value:
        import capo_compute_optimizer.types.timestamps

        out["timestamps"] = (
            capo_compute_optimizer.types.timestamps.serialize_aws_json_1_0(
                value["timestamps"]
            )
        )
    if "upper_bound_values" in value:
        import capo_compute_optimizer.types.metric_values

        out["upperBoundValues"] = (
            capo_compute_optimizer.types.metric_values.serialize_aws_json_1_0(
                value["upper_bound_values"]
            )
        )
    if "lower_bound_values" in value:
        import capo_compute_optimizer.types.metric_values

        out["lowerBoundValues"] = (
            capo_compute_optimizer.types.metric_values.serialize_aws_json_1_0(
                value["lower_bound_values"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ECSServiceProjectedMetric:
    out: ECSServiceProjectedMetric = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        import capo_compute_optimizer.types.ecs_service_metric_name

        out["name"] = (
            capo_compute_optimizer.types.ecs_service_metric_name.deserialize_aws_json_1_0(
                data["name"]
            )
        )
    if data.get("timestamps") is not None:
        import capo_compute_optimizer.types.timestamps

        out["timestamps"] = (
            capo_compute_optimizer.types.timestamps.deserialize_aws_json_1_0(
                data["timestamps"]
            )
        )
    if data.get("upperBoundValues") is not None:
        import capo_compute_optimizer.types.metric_values

        out["upper_bound_values"] = (
            capo_compute_optimizer.types.metric_values.deserialize_aws_json_1_0(
                data["upperBoundValues"]
            )
        )
    if data.get("lowerBoundValues") is not None:
        import capo_compute_optimizer.types.metric_values

        out["lower_bound_values"] = (
            capo_compute_optimizer.types.metric_values.deserialize_aws_json_1_0(
                data["lowerBoundValues"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ECSServiceProjectedMetric) -> dict:
    out: dict = {}
    if "name" in value:
        import capo_compute_optimizer.types.ecs_service_metric_name

        out["name"] = (
            capo_compute_optimizer.types.ecs_service_metric_name.serialize_cbor(
                value["name"]
            )
        )
    if "timestamps" in value:
        import capo_compute_optimizer.types.timestamps

        out["timestamps"] = capo_compute_optimizer.types.timestamps.serialize_cbor(
            value["timestamps"]
        )
    if "upper_bound_values" in value:
        import capo_compute_optimizer.types.metric_values

        out["upperBoundValues"] = (
            capo_compute_optimizer.types.metric_values.serialize_cbor(
                value["upper_bound_values"]
            )
        )
    if "lower_bound_values" in value:
        import capo_compute_optimizer.types.metric_values

        out["lowerBoundValues"] = (
            capo_compute_optimizer.types.metric_values.serialize_cbor(
                value["lower_bound_values"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> ECSServiceProjectedMetric:
    out: ECSServiceProjectedMetric = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        import capo_compute_optimizer.types.ecs_service_metric_name

        out["name"] = (
            capo_compute_optimizer.types.ecs_service_metric_name.deserialize_cbor(
                data["name"]
            )
        )
    if data.get("timestamps") is not None:
        import capo_compute_optimizer.types.timestamps

        out["timestamps"] = capo_compute_optimizer.types.timestamps.deserialize_cbor(
            data["timestamps"]
        )
    if data.get("upperBoundValues") is not None:
        import capo_compute_optimizer.types.metric_values

        out["upper_bound_values"] = (
            capo_compute_optimizer.types.metric_values.deserialize_cbor(
                data["upperBoundValues"]
            )
        )
    if data.get("lowerBoundValues") is not None:
        import capo_compute_optimizer.types.metric_values

        out["lower_bound_values"] = (
            capo_compute_optimizer.types.metric_values.deserialize_cbor(
                data["lowerBoundValues"]
            )
        )
    return out
