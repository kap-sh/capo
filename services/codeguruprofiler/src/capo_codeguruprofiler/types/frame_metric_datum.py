"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#FrameMetricDatum``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_codeguruprofiler.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codeguruprofiler.types.frame_metric
    import capo_codeguruprofiler.types.frame_metric_values


class FrameMetricDatum(TypedDict, closed=True):
    frame_metric: "capo_codeguruprofiler.types.frame_metric.FrameMetric"
    values: "capo_codeguruprofiler.types.frame_metric_values.FrameMetricValues"
    """<p> A list of values that are associated with a frame metric. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FrameMetricDatum) -> dict:
    out: dict = {}
    import capo_codeguruprofiler.types.frame_metric

    out["frameMetric"] = capo_codeguruprofiler.types.frame_metric.serialize_json(
        value["frame_metric"]
    )
    import capo_codeguruprofiler.types.frame_metric_values

    out["values"] = capo_codeguruprofiler.types.frame_metric_values.serialize_json(
        value["values"]
    )
    return out


def deserialize_json(data: dict) -> FrameMetricDatum:
    out: FrameMetricDatum = {}  # type: ignore[typeddict-item]
    if data.get("frameMetric") is not None:
        import capo_codeguruprofiler.types.frame_metric

        out["frame_metric"] = capo_codeguruprofiler.types.frame_metric.deserialize_json(
            data["frameMetric"]
        )
    else:
        raise DeserializationError("FrameMetricDatum.frame_metric required")
    if data.get("values") is not None:
        import capo_codeguruprofiler.types.frame_metric_values

        out["values"] = (
            capo_codeguruprofiler.types.frame_metric_values.deserialize_json(
                data["values"]
            )
        )
    else:
        out["values"] = []
    return out
