"""Generated from Smithy shape ``com.amazonaws.cloudtrail#StartDashboardRefreshRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudtrail.types.dashboard_arn
    import capo_cloudtrail.types.query_parameter_values


class StartDashboardRefreshRequest(TypedDict, closed=True):
    dashboard_id: "capo_cloudtrail.types.dashboard_arn.DashboardArn"
    """<p> The name or ARN of the dashboard. </p>"""
    query_parameter_values: NotRequired[
        "capo_cloudtrail.types.query_parameter_values.QueryParameterValues"
    ]
    """<p> The query parameter values for the dashboard </p> <p>For custom dashboards, the following query parameters are valid: <code>$StartTime$</code>, <code>$EndTime$</code>, and <code>$Period$</code>.</p> <p>For managed dashboards, the following query parameters are valid: <code>$StartTime$</code>, <code>$EndTime$</code>, <code>$Period$</code>, and <code>$EventDataStoreId$</code>. The <code>$EventDataStoreId$</code> query parameter is required.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartDashboardRefreshRequest) -> dict:
    out: dict = {}
    out["DashboardId"] = value["dashboard_id"]
    if "query_parameter_values" in value:
        import capo_cloudtrail.types.query_parameter_values

        out["QueryParameterValues"] = (
            capo_cloudtrail.types.query_parameter_values.serialize_aws_json_1_1(
                value["query_parameter_values"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartDashboardRefreshRequest:
    out: StartDashboardRefreshRequest = {}  # type: ignore[typeddict-item]
    if data.get("DashboardId") is not None:
        out["dashboard_id"] = data["DashboardId"]
    else:
        out["dashboard_id"] = ""
    if data.get("QueryParameterValues") is not None:
        import capo_cloudtrail.types.query_parameter_values

        out["query_parameter_values"] = (
            capo_cloudtrail.types.query_parameter_values.deserialize_aws_json_1_1(
                data["QueryParameterValues"]
            )
        )
    return out
