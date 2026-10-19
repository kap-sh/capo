"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#Anomaly``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_codeguruprofiler.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codeguruprofiler.types.anomaly_instances
    import capo_codeguruprofiler.types.metric


class Anomaly(TypedDict, closed=True):
    metric: "capo_codeguruprofiler.types.metric.Metric"
    """<p> Details about the metric that the analysis used when it detected the anomaly. The metric includes the name of the frame that was analyzed with the type and thread states used to derive the metric value for that frame. </p>"""
    reason: "str"
    """<p>The reason for which metric was flagged as anomalous.</p>"""
    instances: "capo_codeguruprofiler.types.anomaly_instances.AnomalyInstances"
    """<p> A list of the instances of the detected anomalies during the requested period. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Anomaly) -> dict:
    out: dict = {}
    import capo_codeguruprofiler.types.metric

    out["metric"] = capo_codeguruprofiler.types.metric.serialize_json(value["metric"])
    out["reason"] = value["reason"]
    import capo_codeguruprofiler.types.anomaly_instances

    out["instances"] = capo_codeguruprofiler.types.anomaly_instances.serialize_json(
        value["instances"]
    )
    return out


def deserialize_json(data: dict) -> Anomaly:
    out: Anomaly = {}  # type: ignore[typeddict-item]
    if data.get("metric") is not None:
        import capo_codeguruprofiler.types.metric

        out["metric"] = capo_codeguruprofiler.types.metric.deserialize_json(
            data["metric"]
        )
    else:
        raise DeserializationError("Anomaly.metric required")
    if data.get("reason") is not None:
        out["reason"] = data["reason"]
    else:
        out["reason"] = ""
    if data.get("instances") is not None:
        import capo_codeguruprofiler.types.anomaly_instances

        out["instances"] = (
            capo_codeguruprofiler.types.anomaly_instances.deserialize_json(
                data["instances"]
            )
        )
    else:
        out["instances"] = []
    return out
