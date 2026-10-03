"""Generated from Smithy shape ``com.amazonaws.rum#MetricDefinitionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rum.errors import DeserializationError

if TYPE_CHECKING:
    import capo_rum.types.dimension_keys_map
    import capo_rum.types.event_pattern
    import capo_rum.types.metric_name
    import capo_rum.types.namespace
    import capo_rum.types.unit_label
    import capo_rum.types.value_key


class MetricDefinitionRequest(TypedDict, closed=True):
    name: "capo_rum.types.metric_name.MetricName"
    """<p>The name for the metric that is defined in this structure. For custom metrics, you can specify any name that you like. For extended metrics, valid values are the following:</p> <ul> <li> <p> <code>PerformanceNavigationDuration</code> </p> </li> <li> <p> <code>PerformanceResourceDuration </code> </p> </li> <li> <p> <code>NavigationSatisfiedTransaction</code> </p> </li> <li> <p> <code>NavigationToleratedTransaction</code> </p> </li> <li> <p> <code>NavigationFrustratedTransaction</code> </p> </li> <li> <p> <code>WebVitalsCumulativeLayoutShift</code> </p> </li> <li> <p> <code>WebVitalsFirstInputDelay</code> </p> </li> <li> <p> <code>WebVitalsLargestContentfulPaint</code> </p> </li> <li> <p> <code>JsErrorCount</code> </p> </li> <li> <p> <code>HttpErrorCount</code> </p> </li> <li> <p> <code>SessionCount</code> </p> </li> </ul>"""
    value_key: NotRequired["capo_rum.types.value_key.ValueKey"]
    """<p>The field within the event object that the metric value is sourced from.</p> <p>If you omit this field, a hardcoded value of 1 is pushed as the metric value. This is useful if you want to count the number of events that the filter catches. </p> <p>If this metric is sent to CloudWatch Evidently, this field will be passed to Evidently raw. Evidently will handle data extraction from the event.</p>"""
    unit_label: NotRequired["capo_rum.types.unit_label.UnitLabel"]
    """<p>The CloudWatch metric unit to use for this metric. If you omit this field, the metric is recorded with no unit.</p>"""
    dimension_keys: NotRequired["capo_rum.types.dimension_keys_map.DimensionKeysMap"]
    """<p>Use this field only if you are sending the metric to CloudWatch.</p> <p>This field is a map of field paths to dimension names. It defines the dimensions to associate with this metric in CloudWatch. For extended metrics, valid values for the entries in this field are the following:</p> <ul> <li> <p> <code>"metadata.pageId": "PageId"</code> </p> </li> <li> <p> <code>"metadata.browserName": "BrowserName"</code> </p> </li> <li> <p> <code>"metadata.deviceType": "DeviceType"</code> </p> </li> <li> <p> <code>"metadata.osName": "OSName"</code> </p> </li> <li> <p> <code>"metadata.countryCode": "CountryCode"</code> </p> </li> <li> <p> <code>"event_details.fileType": "FileType"</code> </p> </li> </ul> <p> For both extended metrics and custom metrics, all dimensions listed in this field must also be included in <code>EventPattern</code>.</p>"""
    event_pattern: NotRequired["capo_rum.types.event_pattern.EventPattern"]
    """<p>The pattern that defines the metric, specified as a JSON object. RUM checks events that happen in a user's session against the pattern, and events that match the pattern are sent to the metric destination.</p> <p>When you define extended metrics, the metric definition is not valid if <code>EventPattern</code> is omitted.</p> <p>Example event patterns:</p> <ul> <li> <p> <code>'{ "event_type": ["com.amazon.rum.js_error_event"], "metadata": { "browserName": [ "Chrome", "Safari" ], } }'</code> </p> </li> <li> <p> <code>'{ "event_type": ["com.amazon.rum.performance_navigation_event"], "metadata": { "browserName": [ "Chrome", "Firefox" ] }, "event_details": { "duration": [{ "numeric": [ "&lt;", 2000 ] }] } }'</code> </p> </li> <li> <p> <code>'{ "event_type": ["com.amazon.rum.performance_navigation_event"], "metadata": { "browserName": [ "Chrome", "Safari" ], "countryCode": [ "US" ] }, "event_details": { "duration": [{ "numeric": [ "&gt;=", 2000, "&lt;", 8000 ] }] } }'</code> </p> </li> </ul> <p>If the metrics destination is <code>CloudWatch</code> and the event also matches a value in <code>DimensionKeys</code>, then the metric is published with the specified dimensions. </p>"""
    namespace: NotRequired["capo_rum.types.namespace.Namespace"]
    """<p>If this structure is for a custom metric instead of an extended metrics, use this parameter to define the metric namespace for that custom metric. Do not specify this parameter if this structure is for an extended metric.</p> <p>You cannot use any string that starts with <code>AWS/</code> for your namespace.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetricDefinitionRequest) -> dict:
    out: dict = {}
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


def deserialize_json(data: dict) -> MetricDefinitionRequest:
    out: MetricDefinitionRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("MetricDefinitionRequest.name required")
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
