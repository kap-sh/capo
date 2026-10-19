"""Generated from Smithy shape ``com.amazonaws.iot#CreateCustomMetricRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.client_request_token
    import capo_iot.types.custom_metric_display_name
    import capo_iot.types.custom_metric_type
    import capo_iot.types.metric_name
    import capo_iot.types.tag_list


class CreateCustomMetricRequest(TypedDict, closed=True):
    metric_name: "capo_iot.types.metric_name.MetricName"
    """<p> The name of the custom metric. This will be used in the metric report submitted from the device/thing. The name can't begin with <code>aws:</code>. You can't change the name after you define it.</p>"""
    display_name: NotRequired[
        "capo_iot.types.custom_metric_display_name.CustomMetricDisplayName"
    ]
    """<p> The friendly name in the console for the custom metric. This name doesn't have to be unique. Don't use this name as the metric identifier in the device metric report. You can update the friendly name after you define it.</p>"""
    metric_type: "capo_iot.types.custom_metric_type.CustomMetricType"
    """<p> The type of the custom metric. </p> <important> <p>The type <code>number</code> only takes a single metric value as an input, but when you submit the metrics value in the DeviceMetrics report, you must pass it as an array with a single value.</p> </important>"""
    tags: NotRequired["capo_iot.types.tag_list.TagList"]
    """<p> Metadata that can be used to manage the custom metric. </p>"""
    client_request_token: "capo_iot.types.client_request_token.ClientRequestToken"
    """<p>Each custom metric must have a unique client request token. If you try to create a new custom metric that already exists with a different token, an exception occurs. If you omit this value, Amazon Web Services SDKs will automatically generate a unique client request. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCustomMetricRequest) -> dict:
    out: dict = {}
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    import capo_iot.types.custom_metric_type

    out["metricType"] = capo_iot.types.custom_metric_type.serialize_json(
        value["metric_type"]
    )
    if "tags" in value:
        import capo_iot.types.tag_list

        out["tags"] = capo_iot.types.tag_list.serialize_json(value["tags"])
    out["clientRequestToken"] = value["client_request_token"]
    return out


def deserialize_json(data: dict) -> CreateCustomMetricRequest:
    out: CreateCustomMetricRequest = {}  # type: ignore[typeddict-item]
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    if data.get("metricType") is not None:
        import capo_iot.types.custom_metric_type

        out["metric_type"] = capo_iot.types.custom_metric_type.deserialize_json(
            data["metricType"]
        )
    else:
        import typing

        out["metric_type"] = typing.cast(
            "capo_iot.types.custom_metric_type.CustomMetricType", ""
        )
    if data.get("tags") is not None:
        import capo_iot.types.tag_list

        out["tags"] = capo_iot.types.tag_list.deserialize_json(data["tags"])
    if data.get("clientRequestToken") is not None:
        out["client_request_token"] = data["clientRequestToken"]
    else:
        out["client_request_token"] = ""
    return out
