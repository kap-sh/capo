"""Generated from Smithy shape ``com.amazonaws.wafv2#GetRevenueStatisticsSummaryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_wafv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_wafv2.types.currency
    import capo_wafv2.types.monetization_filter_list
    import capo_wafv2.types.scope
    import capo_wafv2.types.time_window


class GetRevenueStatisticsSummaryRequest(TypedDict, closed=True):
    time_window: "capo_wafv2.types.time_window.TimeWindow"
    """<p>The time range for the revenue summary query. Specify start and end timestamps.</p>"""
    scope: "capo_wafv2.types.scope.Scope"
    """<p>Specifies whether this is for a Amazon CloudFront distribution (<code>CLOUDFRONT</code>) or for a regional application (<code>REGIONAL</code>). AI bot monetization is only available for <code>CLOUDFRONT</code> scope.</p>"""
    currency: "capo_wafv2.types.currency.Currency"
    """<p>The currency for the revenue amounts in the response. Currently only <code>USDC</code> is supported.</p>"""
    filters: NotRequired[
        "capo_wafv2.types.monetization_filter_list.MonetizationFilterList"
    ]
    """<p>Optional filters to narrow the results. You can filter by source name, category, organization, intent, verified status, content path, web ACL ARN, or currency mode.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetRevenueStatisticsSummaryRequest) -> dict:
    out: dict = {}
    import capo_wafv2.types.time_window

    out["TimeWindow"] = capo_wafv2.types.time_window.serialize_aws_json_1_1(
        value["time_window"]
    )
    import capo_wafv2.types.scope

    out["Scope"] = capo_wafv2.types.scope.serialize_aws_json_1_1(value["scope"])
    import capo_wafv2.types.currency

    out["Currency"] = capo_wafv2.types.currency.serialize_aws_json_1_1(
        value["currency"]
    )
    if "filters" in value:
        import capo_wafv2.types.monetization_filter_list

        out["Filters"] = (
            capo_wafv2.types.monetization_filter_list.serialize_aws_json_1_1(
                value["filters"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetRevenueStatisticsSummaryRequest:
    out: GetRevenueStatisticsSummaryRequest = {}  # type: ignore[typeddict-item]
    if data.get("TimeWindow") is not None:
        import capo_wafv2.types.time_window

        out["time_window"] = capo_wafv2.types.time_window.deserialize_aws_json_1_1(
            data["TimeWindow"]
        )
    else:
        raise DeserializationError(
            "GetRevenueStatisticsSummaryRequest.time_window required"
        )
    if data.get("Scope") is not None:
        import capo_wafv2.types.scope

        out["scope"] = capo_wafv2.types.scope.deserialize_aws_json_1_1(data["Scope"])
    else:
        import typing

        out["scope"] = typing.cast("capo_wafv2.types.scope.Scope", "")
    if data.get("Currency") is not None:
        import capo_wafv2.types.currency

        out["currency"] = capo_wafv2.types.currency.deserialize_aws_json_1_1(
            data["Currency"]
        )
    else:
        import typing

        out["currency"] = typing.cast("capo_wafv2.types.currency.Currency", "")
    if data.get("Filters") is not None:
        import capo_wafv2.types.monetization_filter_list

        out["filters"] = (
            capo_wafv2.types.monetization_filter_list.deserialize_aws_json_1_1(
                data["Filters"]
            )
        )
    return out
