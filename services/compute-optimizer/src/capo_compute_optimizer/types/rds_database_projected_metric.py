"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#RDSDatabaseProjectedMetric``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.metric_values
    import capo_compute_optimizer.types.rdsdb_metric_name
    import capo_compute_optimizer.types.timestamps


class RDSDatabaseProjectedMetric(TypedDict, closed=True):
    name: NotRequired["capo_compute_optimizer.types.rdsdb_metric_name.RDSDBMetricName"]
    """<p> The name of the projected metric. </p>"""
    timestamps: NotRequired["capo_compute_optimizer.types.timestamps.Timestamps"]
    """<p> The timestamps of the projected metric. </p>"""
    values: NotRequired["capo_compute_optimizer.types.metric_values.MetricValues"]
    """<p> The values for the projected metric. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RDSDatabaseProjectedMetric) -> dict:
    out: dict = {}
    if "name" in value:
        import capo_compute_optimizer.types.rdsdb_metric_name

        out["name"] = (
            capo_compute_optimizer.types.rdsdb_metric_name.serialize_aws_json_1_0(
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
    if "values" in value:
        import capo_compute_optimizer.types.metric_values

        out["values"] = (
            capo_compute_optimizer.types.metric_values.serialize_aws_json_1_0(
                value["values"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> RDSDatabaseProjectedMetric:
    out: RDSDatabaseProjectedMetric = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        import capo_compute_optimizer.types.rdsdb_metric_name

        out["name"] = (
            capo_compute_optimizer.types.rdsdb_metric_name.deserialize_aws_json_1_0(
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
    if data.get("values") is not None:
        import capo_compute_optimizer.types.metric_values

        out["values"] = (
            capo_compute_optimizer.types.metric_values.deserialize_aws_json_1_0(
                data["values"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RDSDatabaseProjectedMetric) -> dict:
    out: dict = {}
    if "name" in value:
        import capo_compute_optimizer.types.rdsdb_metric_name

        out["name"] = capo_compute_optimizer.types.rdsdb_metric_name.serialize_cbor(
            value["name"]
        )
    if "timestamps" in value:
        import capo_compute_optimizer.types.timestamps

        out["timestamps"] = capo_compute_optimizer.types.timestamps.serialize_cbor(
            value["timestamps"]
        )
    if "values" in value:
        import capo_compute_optimizer.types.metric_values

        out["values"] = capo_compute_optimizer.types.metric_values.serialize_cbor(
            value["values"]
        )
    return out


def deserialize_cbor(data: dict) -> RDSDatabaseProjectedMetric:
    out: RDSDatabaseProjectedMetric = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        import capo_compute_optimizer.types.rdsdb_metric_name

        out["name"] = capo_compute_optimizer.types.rdsdb_metric_name.deserialize_cbor(
            data["name"]
        )
    if data.get("timestamps") is not None:
        import capo_compute_optimizer.types.timestamps

        out["timestamps"] = capo_compute_optimizer.types.timestamps.deserialize_cbor(
            data["timestamps"]
        )
    if data.get("values") is not None:
        import capo_compute_optimizer.types.metric_values

        out["values"] = capo_compute_optimizer.types.metric_values.deserialize_cbor(
            data["values"]
        )
    return out
