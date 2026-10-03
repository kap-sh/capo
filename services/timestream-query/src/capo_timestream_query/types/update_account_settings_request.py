"""Generated from Smithy shape ``com.amazonaws.timestreamquery#UpdateAccountSettingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_timestream_query.types.max_query_capacity
    import capo_timestream_query.types.query_compute_request
    import capo_timestream_query.types.query_pricing_model


class UpdateAccountSettingsRequest(TypedDict, closed=True):
    max_query_tcu: NotRequired[
        "capo_timestream_query.types.max_query_capacity.MaxQueryCapacity"
    ]
    """<p>The maximum number of compute units the service will use at any point in time to serve your queries. To run queries, you must set a minimum capacity of 4 TCU. You can set the maximum number of TCU in multiples of 4, for example, 4, 8, 16, 32, and so on. The maximum value supported for <code>MaxQueryTCU</code> is 1000. To request an increase to this soft limit, contact Amazon Web Services Support. For information about the default quota for maxQueryTCU, see Default quotas. This configuration is applicable only for on-demand usage of Timestream Compute Units (TCUs).</p> <p>The maximum value supported for <code>MaxQueryTCU</code> is 1000. To request an increase to this soft limit, contact Amazon Web Services Support. For information about the default quota for <code>maxQueryTCU</code>, see <a href="https://docs.aws.amazon.com/timestream/latest/developerguide/ts-limits.html#limits.default">Default quotas</a>.</p>"""
    query_pricing_model: NotRequired[
        "capo_timestream_query.types.query_pricing_model.QueryPricingModel"
    ]
    """<p>The pricing model for queries in an account.</p> <note> <p>The <code>QueryPricingModel</code> parameter is used by several Timestream operations; however, the <code>UpdateAccountSettings</code> API operation doesn't recognize any values other than <code>COMPUTE_UNITS</code>.</p> </note>"""
    query_compute: NotRequired[
        "capo_timestream_query.types.query_compute_request.QueryComputeRequest"
    ]
    """<p>Modifies the query compute settings configured in your account, including the query pricing model and provisioned Timestream Compute Units (TCUs) in your account.</p> <note> <p>This API is idempotent, meaning that making the same request multiple times will have the same effect as making the request once.</p> </note>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateAccountSettingsRequest) -> dict:
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
        import capo_timestream_query.types.query_compute_request

        out["QueryCompute"] = (
            capo_timestream_query.types.query_compute_request.serialize_aws_json_1_0(
                value["query_compute"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateAccountSettingsRequest:
    out: UpdateAccountSettingsRequest = {}  # type: ignore[typeddict-item]
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
        import capo_timestream_query.types.query_compute_request

        out["query_compute"] = (
            capo_timestream_query.types.query_compute_request.deserialize_aws_json_1_0(
                data["QueryCompute"]
            )
        )
    return out
