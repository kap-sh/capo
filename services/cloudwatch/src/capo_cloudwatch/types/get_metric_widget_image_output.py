"""Generated from Smithy shape ``com.amazonaws.cloudwatch#GetMetricWidgetImageOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.metric_widget_image


class GetMetricWidgetImageOutput(TypedDict, closed=True):
    metric_widget_image: NotRequired[
        "capo_cloudwatch.types.metric_widget_image.MetricWidgetImage"
    ]
    """<p>The image of the graph, in the output format specified. The output is base64-encoded.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetMetricWidgetImageOutput) -> dict:
    out: dict = {}
    if "metric_widget_image" in value:
        import capo_cloudwatch.types.metric_widget_image

        out["MetricWidgetImage"] = (
            capo_cloudwatch.types.metric_widget_image.serialize_aws_json_1_0(
                value["metric_widget_image"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetMetricWidgetImageOutput:
    out: GetMetricWidgetImageOutput = {}  # type: ignore[typeddict-item]
    if data.get("MetricWidgetImage") is not None:
        import capo_cloudwatch.types.metric_widget_image

        out["metric_widget_image"] = (
            capo_cloudwatch.types.metric_widget_image.deserialize_aws_json_1_0(
                data["MetricWidgetImage"]
            )
        )
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: GetMetricWidgetImageOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "metric_widget_image" in value:
        import capo_cloudwatch.types.metric_widget_image

        capo_cloudwatch.types.metric_widget_image.serialize_query(
            value["metric_widget_image"], pairs, f"{key_prefix}MetricWidgetImage"
        )


def deserialize_query(el: Element) -> GetMetricWidgetImageOutput:
    out: GetMetricWidgetImageOutput = {}  # type: ignore[typeddict-item]
    child_metric_widget_image = el.find("MetricWidgetImage")
    if child_metric_widget_image is not None:
        import capo_cloudwatch.types.metric_widget_image

        out["metric_widget_image"] = (
            capo_cloudwatch.types.metric_widget_image.deserialize_query(
                child_metric_widget_image
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetMetricWidgetImageOutput) -> dict:
    out: dict = {}
    if "metric_widget_image" in value:
        import capo_cloudwatch.types.metric_widget_image

        out["MetricWidgetImage"] = (
            capo_cloudwatch.types.metric_widget_image.serialize_cbor(
                value["metric_widget_image"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> GetMetricWidgetImageOutput:
    out: GetMetricWidgetImageOutput = {}  # type: ignore[typeddict-item]
    if data.get("MetricWidgetImage") is not None:
        import capo_cloudwatch.types.metric_widget_image

        out["metric_widget_image"] = (
            capo_cloudwatch.types.metric_widget_image.deserialize_cbor(
                data["MetricWidgetImage"]
            )
        )
    return out
