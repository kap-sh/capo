"""Generated from Smithy shape ``com.amazonaws.costexplorer#GetSavingsPlansPurchaseRecommendationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cost_explorer.types.account_scope
    import capo_cost_explorer.types.expression
    import capo_cost_explorer.types.lookback_period_in_days
    import capo_cost_explorer.types.next_page_token
    import capo_cost_explorer.types.payment_option
    import capo_cost_explorer.types.recommendations_page_size
    import capo_cost_explorer.types.supported_savings_plans_type
    import capo_cost_explorer.types.term_in_years


class GetSavingsPlansPurchaseRecommendationRequest(TypedDict, closed=True):
    savings_plans_type: "capo_cost_explorer.types.supported_savings_plans_type.SupportedSavingsPlansType"
    """<p>The Savings Plans recommendation type that's requested.</p>"""
    term_in_years: "capo_cost_explorer.types.term_in_years.TermInYears"
    """<p>The savings plan recommendation term that's used to generate these recommendations.</p>"""
    payment_option: "capo_cost_explorer.types.payment_option.PaymentOption"
    """<p>The payment option that's used to generate these recommendations.</p>"""
    account_scope: NotRequired["capo_cost_explorer.types.account_scope.AccountScope"]
    """<p>The account scope that you want your recommendations for. Amazon Web Services calculates recommendations including the management account and member accounts if the value is set to <code>PAYER</code>. If the value is <code>LINKED</code>, recommendations are calculated for individual member accounts only.</p>"""
    next_page_token: NotRequired[
        "capo_cost_explorer.types.next_page_token.NextPageToken"
    ]
    """<p>The token to retrieve the next set of results. Amazon Web Services provides the token when the response from a previous call has more results than the maximum page size.</p>"""
    page_size: NotRequired[
        "capo_cost_explorer.types.recommendations_page_size.RecommendationsPageSize"
    ]
    """<p>The number of recommendations that you want returned in a single response object.</p>"""
    lookback_period_in_days: (
        "capo_cost_explorer.types.lookback_period_in_days.LookbackPeriodInDays"
    )
    """<p>The lookback period that's used to generate the recommendation.</p>"""
    filter: NotRequired["capo_cost_explorer.types.expression.Expression"]
    """<p>You can filter your recommendations by Account ID with the <code>LINKED_ACCOUNT</code> dimension. To filter your recommendations by Account ID, specify <code>Key</code> as <code>LINKED_ACCOUNT</code> and <code>Value</code> as the comma-separated Acount ID(s) that you want to see Savings Plans purchase recommendations for.</p> <p>For GetSavingsPlansPurchaseRecommendation, the <code>Filter</code> doesn't include <code>CostCategories</code> or <code>Tags</code>. It only includes <code>Dimensions</code>. With <code>Dimensions</code>, <code>Key</code> must be <code>LINKED_ACCOUNT</code> and <code>Value</code> can be a single Account ID or multiple comma-separated Account IDs that you want to see Savings Plans Purchase Recommendations for. <code>AND</code> and <code>OR</code> operators are not supported.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetSavingsPlansPurchaseRecommendationRequest) -> dict:
    out: dict = {}
    import capo_cost_explorer.types.supported_savings_plans_type

    out["SavingsPlansType"] = (
        capo_cost_explorer.types.supported_savings_plans_type.serialize_aws_json_1_1(
            value["savings_plans_type"]
        )
    )
    import capo_cost_explorer.types.term_in_years

    out["TermInYears"] = capo_cost_explorer.types.term_in_years.serialize_aws_json_1_1(
        value["term_in_years"]
    )
    import capo_cost_explorer.types.payment_option

    out["PaymentOption"] = (
        capo_cost_explorer.types.payment_option.serialize_aws_json_1_1(
            value["payment_option"]
        )
    )
    if "account_scope" in value:
        import capo_cost_explorer.types.account_scope

        out["AccountScope"] = (
            capo_cost_explorer.types.account_scope.serialize_aws_json_1_1(
                value["account_scope"]
            )
        )
    if "next_page_token" in value:
        out["NextPageToken"] = value["next_page_token"]
    if "page_size" in value:
        out["PageSize"] = value["page_size"]
    import capo_cost_explorer.types.lookback_period_in_days

    out["LookbackPeriodInDays"] = (
        capo_cost_explorer.types.lookback_period_in_days.serialize_aws_json_1_1(
            value["lookback_period_in_days"]
        )
    )
    if "filter" in value:
        import capo_cost_explorer.types.expression

        out["Filter"] = capo_cost_explorer.types.expression.serialize_aws_json_1_1(
            value["filter"]
        )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> GetSavingsPlansPurchaseRecommendationRequest:
    out: GetSavingsPlansPurchaseRecommendationRequest = {}  # type: ignore[typeddict-item]
    if data.get("SavingsPlansType") is not None:
        import capo_cost_explorer.types.supported_savings_plans_type

        out["savings_plans_type"] = (
            capo_cost_explorer.types.supported_savings_plans_type.deserialize_aws_json_1_1(
                data["SavingsPlansType"]
            )
        )
    else:
        import typing

        out["savings_plans_type"] = typing.cast(
            "capo_cost_explorer.types.supported_savings_plans_type.SupportedSavingsPlansType",
            "",
        )
    if data.get("TermInYears") is not None:
        import capo_cost_explorer.types.term_in_years

        out["term_in_years"] = (
            capo_cost_explorer.types.term_in_years.deserialize_aws_json_1_1(
                data["TermInYears"]
            )
        )
    else:
        import typing

        out["term_in_years"] = typing.cast(
            "capo_cost_explorer.types.term_in_years.TermInYears", ""
        )
    if data.get("PaymentOption") is not None:
        import capo_cost_explorer.types.payment_option

        out["payment_option"] = (
            capo_cost_explorer.types.payment_option.deserialize_aws_json_1_1(
                data["PaymentOption"]
            )
        )
    else:
        import typing

        out["payment_option"] = typing.cast(
            "capo_cost_explorer.types.payment_option.PaymentOption", ""
        )
    if data.get("AccountScope") is not None:
        import capo_cost_explorer.types.account_scope

        out["account_scope"] = (
            capo_cost_explorer.types.account_scope.deserialize_aws_json_1_1(
                data["AccountScope"]
            )
        )
    if data.get("NextPageToken") is not None:
        out["next_page_token"] = data["NextPageToken"]
    if data.get("PageSize") is not None:
        out["page_size"] = data["PageSize"]
    if data.get("LookbackPeriodInDays") is not None:
        import capo_cost_explorer.types.lookback_period_in_days

        out["lookback_period_in_days"] = (
            capo_cost_explorer.types.lookback_period_in_days.deserialize_aws_json_1_1(
                data["LookbackPeriodInDays"]
            )
        )
    else:
        import typing

        out["lookback_period_in_days"] = typing.cast(
            "capo_cost_explorer.types.lookback_period_in_days.LookbackPeriodInDays", ""
        )
    if data.get("Filter") is not None:
        import capo_cost_explorer.types.expression

        out["filter"] = capo_cost_explorer.types.expression.deserialize_aws_json_1_1(
            data["Filter"]
        )
    return out
