"""Generated from Smithy shape ``com.amazonaws.iotsitewise#Metric``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.expression
    import capo_iotsitewise.types.expression_variables
    import capo_iotsitewise.types.metric_processing_config
    import capo_iotsitewise.types.metric_window


class Metric(TypedDict, closed=True):
    expression: "capo_iotsitewise.types.expression.Expression"
    """<p>The mathematical expression that defines the metric aggregation function. You can specify up to 10 variables per expression. You can specify up to 10 functions per expression. </p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>"""
    variables: "capo_iotsitewise.types.expression_variables.ExpressionVariables"
    """<p>The list of variables used in the expression.</p>"""
    window: "capo_iotsitewise.types.metric_window.MetricWindow"
    """<p>The window (time interval) over which IoT SiteWise computes the metric's aggregation expression. IoT SiteWise computes one data point per <code>window</code>.</p>"""
    processing_config: NotRequired[
        "capo_iotsitewise.types.metric_processing_config.MetricProcessingConfig"
    ]
    """<p>The processing configuration for the given metric property. You can configure metrics to be computed at the edge or in the Amazon Web Services Cloud. By default, metrics are forwarded to the cloud.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Metric) -> dict:
    out: dict = {}
    out["expression"] = value.get("expression", "")
    import capo_iotsitewise.types.expression_variables

    out["variables"] = capo_iotsitewise.types.expression_variables.serialize_json(
        value.get("variables", [])
    )
    import capo_iotsitewise.types.metric_window

    out["window"] = capo_iotsitewise.types.metric_window.serialize_json(value["window"])
    if "processing_config" in value:
        import capo_iotsitewise.types.metric_processing_config

        out["processingConfig"] = (
            capo_iotsitewise.types.metric_processing_config.serialize_json(
                value["processing_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> Metric:
    out: Metric = {}  # type: ignore[typeddict-item]
    if data.get("expression") is not None:
        out["expression"] = data["expression"]
    else:
        out["expression"] = ""
    if data.get("variables") is not None:
        import capo_iotsitewise.types.expression_variables

        out["variables"] = capo_iotsitewise.types.expression_variables.deserialize_json(
            data["variables"]
        )
    else:
        out["variables"] = []
    if data.get("window") is not None:
        import capo_iotsitewise.types.metric_window

        out["window"] = capo_iotsitewise.types.metric_window.deserialize_json(
            data["window"]
        )
    else:
        raise DeserializationError("Metric.window required")
    if data.get("processingConfig") is not None:
        import capo_iotsitewise.types.metric_processing_config

        out["processing_config"] = (
            capo_iotsitewise.types.metric_processing_config.deserialize_json(
                data["processingConfig"]
            )
        )
    return out
