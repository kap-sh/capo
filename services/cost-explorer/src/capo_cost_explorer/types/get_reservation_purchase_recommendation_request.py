"""Generated from Smithy shape ``com.amazonaws.costexplorer#GetReservationPurchaseRecommendationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cost_explorer.types.account_scope
    import capo_cost_explorer.types.expression
    import capo_cost_explorer.types.generic_string
    import capo_cost_explorer.types.lookback_period_in_days
    import capo_cost_explorer.types.next_page_token
    import capo_cost_explorer.types.payment_option
    import capo_cost_explorer.types.recommendations_page_size
    import capo_cost_explorer.types.service_specification
    import capo_cost_explorer.types.term_in_years


class GetReservationPurchaseRecommendationRequest(TypedDict, closed=True):
    account_id: NotRequired["capo_cost_explorer.types.generic_string.GenericString"]
    """<p>The account ID that's associated with the recommendation. </p>"""
    service: "capo_cost_explorer.types.generic_string.GenericString"
    """<p>The specific service that you want recommendations for.</p>"""
    filter: NotRequired["capo_cost_explorer.types.expression.Expression"]
    account_scope: NotRequired["capo_cost_explorer.types.account_scope.AccountScope"]
    """<p>The account scope that you want your recommendations for. Amazon Web Services calculates recommendations including the management account and member accounts if the value is set to <code>PAYER</code>. If the value is <code>LINKED</code>, recommendations are calculated for individual member accounts only.</p>"""
    lookback_period_in_days: NotRequired[
        "capo_cost_explorer.types.lookback_period_in_days.LookbackPeriodInDays"
    ]
    """<p>The number of previous days that you want Amazon Web Services to consider when it calculates your recommendations.</p>"""
    term_in_years: NotRequired["capo_cost_explorer.types.term_in_years.TermInYears"]
    """<p>The reservation term that you want recommendations for.</p>"""
    payment_option: NotRequired["capo_cost_explorer.types.payment_option.PaymentOption"]
    """<p>The reservation purchase option that you want recommendations for.</p>"""
    service_specification: NotRequired[
        "capo_cost_explorer.types.service_specification.ServiceSpecification"
    ]
    """<p>The hardware specifications for the service instances that you want recommendations for, such as standard or convertible Amazon EC2 instances.</p>"""
    page_size: NotRequired[
        "capo_cost_explorer.types.recommendations_page_size.RecommendationsPageSize"
    ]
    """<p>The number of recommendations that you want returned in a single response object.</p>"""
    next_page_token: NotRequired[
        "capo_cost_explorer.types.next_page_token.NextPageToken"
    ]
    """<p>The pagination token that indicates the next set of results that you want to retrieve.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetReservationPurchaseRecommendationRequest) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    out["Service"] = value["service"]
    if "filter" in value:
        import capo_cost_explorer.types.expression

        out["Filter"] = capo_cost_explorer.types.expression.serialize_aws_json_1_1(
            value["filter"]
        )
    if "account_scope" in value:
        import capo_cost_explorer.types.account_scope

        out["AccountScope"] = (
            capo_cost_explorer.types.account_scope.serialize_aws_json_1_1(
                value["account_scope"]
            )
        )
    if "lookback_period_in_days" in value:
        import capo_cost_explorer.types.lookback_period_in_days

        out["LookbackPeriodInDays"] = (
            capo_cost_explorer.types.lookback_period_in_days.serialize_aws_json_1_1(
                value["lookback_period_in_days"]
            )
        )
    if "term_in_years" in value:
        import capo_cost_explorer.types.term_in_years

        out["TermInYears"] = (
            capo_cost_explorer.types.term_in_years.serialize_aws_json_1_1(
                value["term_in_years"]
            )
        )
    if "payment_option" in value:
        import capo_cost_explorer.types.payment_option

        out["PaymentOption"] = (
            capo_cost_explorer.types.payment_option.serialize_aws_json_1_1(
                value["payment_option"]
            )
        )
    if "service_specification" in value:
        import capo_cost_explorer.types.service_specification

        out["ServiceSpecification"] = (
            capo_cost_explorer.types.service_specification.serialize_aws_json_1_1(
                value["service_specification"]
            )
        )
    if "page_size" in value:
        out["PageSize"] = value["page_size"]
    if "next_page_token" in value:
        out["NextPageToken"] = value["next_page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetReservationPurchaseRecommendationRequest:
    out: GetReservationPurchaseRecommendationRequest = {}  # type: ignore[typeddict-item]
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    if data.get("Service") is not None:
        out["service"] = data["Service"]
    else:
        out["service"] = ""
    if data.get("Filter") is not None:
        import capo_cost_explorer.types.expression

        out["filter"] = capo_cost_explorer.types.expression.deserialize_aws_json_1_1(
            data["Filter"]
        )
    if data.get("AccountScope") is not None:
        import capo_cost_explorer.types.account_scope

        out["account_scope"] = (
            capo_cost_explorer.types.account_scope.deserialize_aws_json_1_1(
                data["AccountScope"]
            )
        )
    if data.get("LookbackPeriodInDays") is not None:
        import capo_cost_explorer.types.lookback_period_in_days

        out["lookback_period_in_days"] = (
            capo_cost_explorer.types.lookback_period_in_days.deserialize_aws_json_1_1(
                data["LookbackPeriodInDays"]
            )
        )
    if data.get("TermInYears") is not None:
        import capo_cost_explorer.types.term_in_years

        out["term_in_years"] = (
            capo_cost_explorer.types.term_in_years.deserialize_aws_json_1_1(
                data["TermInYears"]
            )
        )
    if data.get("PaymentOption") is not None:
        import capo_cost_explorer.types.payment_option

        out["payment_option"] = (
            capo_cost_explorer.types.payment_option.deserialize_aws_json_1_1(
                data["PaymentOption"]
            )
        )
    if data.get("ServiceSpecification") is not None:
        import capo_cost_explorer.types.service_specification

        out["service_specification"] = (
            capo_cost_explorer.types.service_specification.deserialize_aws_json_1_1(
                data["ServiceSpecification"]
            )
        )
    if data.get("PageSize") is not None:
        out["page_size"] = data["PageSize"]
    if data.get("NextPageToken") is not None:
        out["next_page_token"] = data["NextPageToken"]
    return out
