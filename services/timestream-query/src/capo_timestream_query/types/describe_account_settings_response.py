"""Generated from Smithy shape ``com.amazonaws.timestreamquery#DescribeAccountSettingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_timestream_query.types.max_query_capacity
    import capo_timestream_query.types.query_compute_response
    import capo_timestream_query.types.query_pricing_model


class DescribeAccountSettingsResponse(TypedDict, closed=True):
    max_query_tcu: NotRequired[
        "capo_timestream_query.types.max_query_capacity.MaxQueryCapacity"
    ]
    """<p>The maximum number of <a href="https://docs.aws.amazon.com/timestream/latest/developerguide/tcu.html">Timestream compute units</a> (TCUs) the service will use at any point in time to serve your queries. To run queries, you must set a minimum capacity of 4 TCU. You can set the maximum number of TCU in multiples of 4, for example, 4, 8, 16, 32, and so on. This configuration is applicable only for on-demand usage of (TCUs). </p>"""
    query_pricing_model: NotRequired[
        "capo_timestream_query.types.query_pricing_model.QueryPricingModel"
    ]
    """<p>The pricing model for queries in your account.</p> <note> <p>The <code>QueryPricingModel</code> parameter is used by several Timestream operations; however, the <code>UpdateAccountSettings</code> API operation doesn't recognize any values other than <code>COMPUTE_UNITS</code>.</p> </note>"""
    query_compute: NotRequired[
        "capo_timestream_query.types.query_compute_response.QueryComputeResponse"
    ]
    """<p>An object that contains the usage settings for Timestream Compute Units (TCUs) in your account for the query workload. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeAccountSettingsResponse) -> dict:
    out: dict = {}
    if "max_query_tcu" in value:
        out["MaxQueryTCU"] = value["max_query_tcu"]
    if "query_pricing_model" in value:
        import capo_timestream_query.types.query_pricing_model

        out["QueryPricingModel"] = (
            capo_timestream_query.types.query_pricing_model.serialize_aws_json_1_0(
                value["query_pricing_model"]
            )
        )
    if "query_compute" in value:
        import capo_timestream_query.types.query_compute_response

        out["QueryCompute"] = (
            capo_timestream_query.types.query_compute_response.serialize_aws_json_1_0(
                value["query_compute"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeAccountSettingsResponse:
    out: DescribeAccountSettingsResponse = {}  # type: ignore[typeddict-item]
    if data.get("MaxQueryTCU") is not None:
        out["max_query_tcu"] = data["MaxQueryTCU"]
    if data.get("QueryPricingModel") is not None:
        import capo_timestream_query.types.query_pricing_model

        out["query_pricing_model"] = (
            capo_timestream_query.types.query_pricing_model.deserialize_aws_json_1_0(
                data["QueryPricingModel"]
            )
        )
    if data.get("QueryCompute") is not None:
        import capo_timestream_query.types.query_compute_response

        out["query_compute"] = (
            capo_timestream_query.types.query_compute_response.deserialize_aws_json_1_0(
                data["QueryCompute"]
            )
        )
    return out
