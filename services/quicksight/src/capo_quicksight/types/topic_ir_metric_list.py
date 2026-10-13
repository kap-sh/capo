"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicIRMetricList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.topic_ir_metric

TopicIRMetricList: TypeAlias = list[
    "capo_quicksight.types.topic_ir_metric.TopicIRMetric"
]


# --- restJson1 ser/de ---
def serialize_json(value: TopicIRMetricList) -> list:
    import capo_quicksight.types.topic_ir_metric

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.topic_ir_metric.serialize_json(item))
    return out


def deserialize_json(data: list) -> TopicIRMetricList:
    import capo_quicksight.types.topic_ir_metric

    out: TopicIRMetricList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_quicksight.types.topic_ir_metric.deserialize_json(item))
    return out


def redact_sensitive(value: TopicIRMetricList) -> list[Any]:
    import capo_quicksight.types.topic_ir_metric

    return [
        capo_quicksight.types.topic_ir_metric.redact_sensitive(item) for item in value
    ]
