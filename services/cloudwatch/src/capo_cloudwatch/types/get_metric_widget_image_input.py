"""Generated from Smithy shape ``com.amazonaws.cloudwatch#GetMetricWidgetImageInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.metric_widget
    import capo_cloudwatch.types.output_format


class GetMetricWidgetImageInput(TypedDict, closed=True):
    metric_widget: NotRequired["capo_cloudwatch.types.metric_widget.MetricWidget"]
    """<p>A JSON string that defines the bitmap graph to be retrieved. The string includes the metrics to include in the graph, statistics, annotations, title, axis limits, and so on. You can include only one <code>MetricWidget</code> parameter in each <code>GetMetricWidgetImage</code> call.</p> <p>For more information about the syntax of <code>MetricWidget</code> see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Metric-Widget-Structure.html">GetMetricWidgetImage: Metric Widget Structure and Syntax</a>.</p> <p>If any metric on the graph could not load all the requested data points, an orange triangle with an exclamation point appears next to the graph legend.</p>"""
    output_format: NotRequired["capo_cloudwatch.types.output_format.OutputFormat"]
    """<p>The format of the resulting image. Only PNG images are supported.</p> <p>The default is <code>png</code>. If you specify <code>png</code>, the API returns an HTTP response with the content-type set to <code>text/xml</code>. The image data is in a <code>MetricWidgetImage</code> field. For example:</p> <p> <code> <GetMetricWidgetImageResponse xmlns=<URLstring>></code> </p> <p> <code> <GetMetricWidgetImageResult></code> </p> <p> <code> <MetricWidgetImage></code> </p> <p> <code> iVBORw0KGgoAAAANSUhEUgAAAlgAAAGQEAYAAAAip...</code> </p> <p> <code> </MetricWidgetImage></code> </p> <p> <code> </GetMetricWidgetImageResult></code> </p> <p> <code> <ResponseMetadata></code> </p> <p> <code> <RequestId>6f0d4192-4d42-11e8-82c1-f539a07e0e3b</RequestId></code> </p> <p> <code> </ResponseMetadata></code> </p> <p> <code></GetMetricWidgetImageResponse></code> </p> <p>The <code>image/png</code> setting is intended only for custom HTTP requests. For most use cases, and all actions using an Amazon Web Services SDK, you should use <code>png</code>. If you specify <code>image/png</code>, the HTTP response has a content-type set to <code>image/png</code>, and the body of the response is a PNG image.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetMetricWidgetImageInput) -> dict:
    out: dict = {}
    if "metric_widget" in value:
        out["MetricWidget"] = value["metric_widget"]
    if "output_format" in value:
        out["OutputFormat"] = value["output_format"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetMetricWidgetImageInput:
    out: GetMetricWidgetImageInput = {}  # type: ignore[typeddict-item]
    if data.get("MetricWidget") is not None:
        out["metric_widget"] = data["MetricWidget"]
    if data.get("OutputFormat") is not None:
        out["output_format"] = data["OutputFormat"]
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: GetMetricWidgetImageInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "metric_widget" in value:
        pairs.append((f"{key_prefix}MetricWidget", str(value["metric_widget"])))
    if "output_format" in value:
        pairs.append((f"{key_prefix}OutputFormat", str(value["output_format"])))


def deserialize_query(el: Element) -> GetMetricWidgetImageInput:
    out: GetMetricWidgetImageInput = {}  # type: ignore[typeddict-item]
    child_metric_widget = el.find("MetricWidget")
    if child_metric_widget is not None:
        out["metric_widget"] = str(child_metric_widget.text or "")
    child_output_format = el.find("OutputFormat")
    if child_output_format is not None:
        out["output_format"] = str(child_output_format.text or "")
    return out
