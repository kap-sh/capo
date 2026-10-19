"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormMetricConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.evaluation_form_metric_name
    import capo_connect.types.evaluation_form_metric_type


class EvaluationFormMetricConfiguration(TypedDict, closed=True):
    metric_type: (
        "capo_connect.types.evaluation_form_metric_type.EvaluationFormMetricType"
    )
    """<p>The type of metric. Currently, only <code>BUSINESS_OUTCOME</code> is supported.</p>"""
    metric_name: (
        "capo_connect.types.evaluation_form_metric_name.EvaluationFormMetricName"
    )
    """<p>The name of the metric. Valid values are:</p> <ul> <li> <p> <code>SALE_SUCCESS</code> – Sale success.</p> </li> <li> <p> <code>CSAT</code> – Customer satisfaction.</p> </li> <li> <p> <code>CHURN_PROPENSITY</code> – Churn propensity.</p> </li> <li> <p> <code>SELF_SERVICE_SUCCESS</code> – Self-service success.</p> </li> <li> <p> <code>PARTIAL_SELF_SERVICE_SUCCESS</code> – Partial self-service success.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormMetricConfiguration) -> dict:
    out: dict = {}
    import capo_connect.types.evaluation_form_metric_type

    out["MetricType"] = capo_connect.types.evaluation_form_metric_type.serialize_json(
        value["metric_type"]
    )
    out["MetricName"] = value["metric_name"]
    return out


def deserialize_json(data: dict) -> EvaluationFormMetricConfiguration:
    out: EvaluationFormMetricConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("MetricType") is not None:
        import capo_connect.types.evaluation_form_metric_type

        out["metric_type"] = (
            capo_connect.types.evaluation_form_metric_type.deserialize_json(
                data["MetricType"]
            )
        )
    else:
        import typing

        out["metric_type"] = typing.cast(
            "capo_connect.types.evaluation_form_metric_type.EvaluationFormMetricType",
            "",
        )
    if data.get("MetricName") is not None:
        out["metric_name"] = data["MetricName"]
    else:
        out["metric_name"] = ""
    return out
