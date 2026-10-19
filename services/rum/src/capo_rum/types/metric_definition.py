"""Generated from Smithy shape ``com.amazonaws.rum#MetricDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rum.types.dimension_keys_map
    import capo_rum.types.event_pattern
    import capo_rum.types.metric_definition_id
    import capo_rum.types.metric_name
    import capo_rum.types.namespace
    import capo_rum.types.unit_label
    import capo_rum.types.value_key


class MetricDefinition(TypedDict, closed=True):
    metric_definition_id: "capo_rum.types.metric_definition_id.MetricDefinitionId"
    """<p>The ID of this metric definition.</p>"""
    name: "capo_rum.types.metric_name.MetricName"
    """<p>The name of the metric that is defined in this structure.</p>"""
    value_key: NotRequired["capo_rum.types.value_key.ValueKey"]
    """<p>The field within the event object that the metric value is sourced from.</p>"""
    unit_label: NotRequired["capo_rum.types.unit_label.UnitLabel"]
    """<p>Use this field only if you are sending this metric to CloudWatch. It defines the CloudWatch metric unit that this metric is measured in. </p>"""
    dimension_keys: NotRequired["capo_rum.types.dimension_keys_map.DimensionKeysMap"]
    """<p>This field is a map of field paths to dimension names. It defines the dimensions to associate with this metric in CloudWatch The value of this field is used only if the metric destination is <code>CloudWatch</code>. If the metric destination is <code>Evidently</code>, the value of <code>DimensionKeys</code> is ignored.</p>"""
    event_pattern: NotRequired["capo_rum.types.event_pattern.EventPattern"]
    """<p>The pattern that defines the metric. RUM checks events that happen in a user's session against the pattern, and events that match the pattern are sent to the metric destination.</p> <p>If the metrics destination is <code>CloudWatch</code> and the event also matches a value in <code>DimensionKeys</code>, then the metric is published with the specified dimensions. </p>"""
    namespace: NotRequired["capo_rum.types.namespace.Namespace"]
    """<p>If this metric definition is for a custom metric instead of an extended metric, this field displays the metric namespace that the custom metric is published to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetricDefinition) -> dict:
    out: dict = {}
    out["MetricDefinitionId"] = value["metric_definition_id"]
    out["Name"] = value["name"]
    if "value_key" in value:
        out["ValueKey"] = value["value_key"]
    if "unit_label" in value:
        out["UnitLabel"] = value["unit_label"]
    if "dimension_keys" in value:
        import capo_rum.types.dimension_keys_map

        out["DimensionKeys"] = capo_rum.types.dimension_keys_map.serialize_json(
            value["dimension_keys"]
        )
    if "event_pattern" in value:
        out["EventPattern"] = value["event_pattern"]
    if "namespace" in value:
        out["Namespace"] = value["namespace"]
    return out


def deserialize_json(data: dict) -> MetricDefinition:
    out: MetricDefinition = {}  # type: ignore[typeddict-item]
    if data.get("MetricDefinitionId") is not None:
        out["metric_definition_id"] = data["MetricDefinitionId"]
    else:
        out["metric_definition_id"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("ValueKey") is not None:
        out["value_key"] = data["ValueKey"]
    if data.get("UnitLabel") is not None:
        out["unit_label"] = data["UnitLabel"]
    if data.get("DimensionKeys") is not None:
        import capo_rum.types.dimension_keys_map

        out["dimension_keys"] = capo_rum.types.dimension_keys_map.deserialize_json(
            data["DimensionKeys"]
        )
    if data.get("EventPattern") is not None:
        out["event_pattern"] = data["EventPattern"]
    if data.get("Namespace") is not None:
        out["namespace"] = data["Namespace"]
    return out
