"""Generated from Smithy shape ``com.amazonaws.costexplorer#GetCostForecastRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cost_explorer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cost_explorer.types.billing_view_arn
    import capo_cost_explorer.types.date_interval
    import capo_cost_explorer.types.expression
    import capo_cost_explorer.types.granularity
    import capo_cost_explorer.types.metric
    import capo_cost_explorer.types.prediction_interval_level


class GetCostForecastRequest(TypedDict, closed=True):
    time_period: "capo_cost_explorer.types.date_interval.DateInterval"
    """<p>The period of time that you want the forecast to cover. The start date must be equal to or no later than the current date to avoid a validation error.</p>"""
    metric: "capo_cost_explorer.types.metric.Metric"
    """<p>Which metric Cost Explorer uses to create your forecast. For more information about blended and unblended rates, see <a href="http://aws.amazon.com/premiumsupport/knowledge-center/blended-rates-intro/">Why does the "blended" annotation appear on some line items in my bill?</a>. </p> <p>Valid values for a <code>GetCostForecast</code> call are the following:</p> <ul> <li> <p>AMORTIZED_COST</p> </li> <li> <p>BLENDED_COST</p> </li> <li> <p>NET_AMORTIZED_COST</p> </li> <li> <p>NET_UNBLENDED_COST</p> </li> <li> <p>UNBLENDED_COST</p> </li> </ul>"""
    granularity: "capo_cost_explorer.types.granularity.Granularity"
    """<p>How granular you want the forecast to be. You can get 3 months of <code>DAILY</code> forecasts or 18 months of <code>MONTHLY</code> forecasts.</p> <p>The <code>GetCostForecast</code> operation supports only <code>DAILY</code> and <code>MONTHLY</code> granularities.</p>"""
    filter: NotRequired["capo_cost_explorer.types.expression.Expression"]
    """<p>The filters that you want to use to filter your forecast. The <code>GetCostForecast</code> API supports filtering by the following dimensions:</p> <ul> <li> <p> <code>AZ</code> </p> </li> <li> <p> <code>INSTANCE_TYPE</code> </p> </li> <li> <p> <code>LINKED_ACCOUNT</code> </p> </li> <li> <p> <code>OPERATION</code> </p> </li> <li> <p> <code>PURCHASE_TYPE</code> </p> </li> <li> <p> <code>REGION</code> </p> </li> <li> <p> <code>SERVICE</code> </p> </li> <li> <p> <code>USAGE_TYPE</code> </p> </li> <li> <p> <code>USAGE_TYPE_GROUP</code> </p> </li> <li> <p> <code>RECORD_TYPE</code> </p> </li> <li> <p> <code>OPERATING_SYSTEM</code> </p> </li> <li> <p> <code>TENANCY</code> </p> </li> <li> <p> <code>SCOPE</code> </p> </li> <li> <p> <code>PLATFORM</code> </p> </li> <li> <p> <code>SUBSCRIPTION_ID</code> </p> </li> <li> <p> <code>LEGAL_ENTITY_NAME</code> </p> </li> <li> <p> <code>DEPLOYMENT_OPTION</code> </p> </li> <li> <p> <code>DATABASE_ENGINE</code> </p> </li> <li> <p> <code>INSTANCE_TYPE_FAMILY</code> </p> </li> <li> <p> <code>BILLING_ENTITY</code> </p> </li> <li> <p> <code>RESERVATION_ID</code> </p> </li> <li> <p> <code>SAVINGS_PLAN_ARN</code> </p> </li> </ul>"""
    billing_view_arn: NotRequired[
        "capo_cost_explorer.types.billing_view_arn.BillingViewArn"
    ]
    """<p>The Amazon Resource Name (ARN) that uniquely identifies a specific billing view. The ARN is used to specify which particular billing view you want to interact with or retrieve information from when making API calls related to Amazon Web Services Billing and Cost Management features. The BillingViewArn can be retrieved by calling the ListBillingViews API.</p>"""
    prediction_interval_level: NotRequired[
        "capo_cost_explorer.types.prediction_interval_level.PredictionIntervalLevel"
    ]
    """<p>Cost Explorer always returns the mean forecast as a single point. You can request a prediction interval around the mean by specifying a confidence level. The higher the confidence level, the more confident Cost Explorer is about the actual value falling in the prediction interval. Higher confidence levels result in wider prediction intervals.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetCostForecastRequest) -> dict:
    out: dict = {}
    import capo_cost_explorer.types.date_interval

    out["TimePeriod"] = capo_cost_explorer.types.date_interval.serialize_aws_json_1_1(
        value["time_period"]
    )
    import capo_cost_explorer.types.metric

    out["Metric"] = capo_cost_explorer.types.metric.serialize_aws_json_1_1(
        value["metric"]
    )
    import capo_cost_explorer.types.granularity

    out["Granularity"] = capo_cost_explorer.types.granularity.serialize_aws_json_1_1(
        value["granularity"]
    )
    if "filter" in value:
        import capo_cost_explorer.types.expression

        out["Filter"] = capo_cost_explorer.types.expression.serialize_aws_json_1_1(
            value["filter"]
        )
    if "billing_view_arn" in value:
        out["BillingViewArn"] = value["billing_view_arn"]
    if "prediction_interval_level" in value:
        out["PredictionIntervalLevel"] = value["prediction_interval_level"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetCostForecastRequest:
    out: GetCostForecastRequest = {}  # type: ignore[typeddict-item]
    if data.get("TimePeriod") is not None:
        import capo_cost_explorer.types.date_interval

        out["time_period"] = (
            capo_cost_explorer.types.date_interval.deserialize_aws_json_1_1(
                data["TimePeriod"]
            )
        )
    else:
        raise DeserializationError("GetCostForecastRequest.time_period required")
    if data.get("Metric") is not None:
        import capo_cost_explorer.types.metric

        out["metric"] = capo_cost_explorer.types.metric.deserialize_aws_json_1_1(
            data["Metric"]
        )
    else:
        raise DeserializationError("GetCostForecastRequest.metric required")
    if data.get("Granularity") is not None:
        import capo_cost_explorer.types.granularity

        out["granularity"] = (
            capo_cost_explorer.types.granularity.deserialize_aws_json_1_1(
                data["Granularity"]
            )
        )
    else:
        raise DeserializationError("GetCostForecastRequest.granularity required")
    if data.get("Filter") is not None:
        import capo_cost_explorer.types.expression

        out["filter"] = capo_cost_explorer.types.expression.deserialize_aws_json_1_1(
            data["Filter"]
        )
    if data.get("BillingViewArn") is not None:
        out["billing_view_arn"] = data["BillingViewArn"]
    if data.get("PredictionIntervalLevel") is not None:
        out["prediction_interval_level"] = data["PredictionIntervalLevel"]
    return out
