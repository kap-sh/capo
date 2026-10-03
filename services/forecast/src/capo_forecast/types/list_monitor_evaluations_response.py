"""Generated from Smithy shape ``com.amazonaws.forecast#ListMonitorEvaluationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_forecast.types.next_token
    import capo_forecast.types.predictor_monitor_evaluations


class ListMonitorEvaluationsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_forecast.types.next_token.NextToken"]
    """<p>If the response is truncated, Amazon Forecast returns this token. To retrieve the next set of results, use the token in the next request. Tokens expire after 24 hours.</p>"""
    predictor_monitor_evaluations: NotRequired[
        "capo_forecast.types.predictor_monitor_evaluations.PredictorMonitorEvaluations"
    ]
    """<p>The monitoring results and predictor events collected by the monitor resource during different windows of time.</p> <p>For information about monitoring see <a href="https://docs.aws.amazon.com/forecast/latest/dg/predictor-monitoring-results.html">Viewing Monitoring Results</a>. For more information about retrieving monitoring results see <a href="https://docs.aws.amazon.com/forecast/latest/dg/predictor-monitoring-results.html">Viewing Monitoring Results</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListMonitorEvaluationsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "predictor_monitor_evaluations" in value:
        import capo_forecast.types.predictor_monitor_evaluations

        out["PredictorMonitorEvaluations"] = (
            capo_forecast.types.predictor_monitor_evaluations.serialize_aws_json_1_1(
                value["predictor_monitor_evaluations"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListMonitorEvaluationsResponse:
    out: ListMonitorEvaluationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("PredictorMonitorEvaluations") is not None:
        import capo_forecast.types.predictor_monitor_evaluations

        out["predictor_monitor_evaluations"] = (
            capo_forecast.types.predictor_monitor_evaluations.deserialize_aws_json_1_1(
                data["PredictorMonitorEvaluations"]
            )
        )
    return out
