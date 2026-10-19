"""Generated from Smithy shape ``com.amazonaws.savingsplans#DescribeSavingsPlansOfferingRatesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_savingsplans.types.page_size
    import capo_savingsplans.types.pagination_token
    import capo_savingsplans.types.savings_plan_offering_rate_filters_list
    import capo_savingsplans.types.savings_plan_payment_option_list
    import capo_savingsplans.types.savings_plan_product_type_list
    import capo_savingsplans.types.savings_plan_rate_operation_list
    import capo_savingsplans.types.savings_plan_rate_service_code_list
    import capo_savingsplans.types.savings_plan_rate_usage_type_list
    import capo_savingsplans.types.savings_plan_type_list
    import capo_savingsplans.types.uui_ds


class DescribeSavingsPlansOfferingRatesRequest(TypedDict, closed=True):
    savings_plan_offering_ids: NotRequired["capo_savingsplans.types.uui_ds.UUIDs"]
    """<p>The IDs of the offerings.</p>"""
    savings_plan_payment_options: NotRequired[
        "capo_savingsplans.types.savings_plan_payment_option_list.SavingsPlanPaymentOptionList"
    ]
    """<p>The payment options.</p>"""
    savings_plan_types: NotRequired[
        "capo_savingsplans.types.savings_plan_type_list.SavingsPlanTypeList"
    ]
    """<p>The plan types.</p>"""
    products: NotRequired[
        "capo_savingsplans.types.savings_plan_product_type_list.SavingsPlanProductTypeList"
    ]
    """<p>The Amazon Web Services products.</p>"""
    service_codes: NotRequired[
        "capo_savingsplans.types.savings_plan_rate_service_code_list.SavingsPlanRateServiceCodeList"
    ]
    """<p>The services.</p>"""
    usage_types: NotRequired[
        "capo_savingsplans.types.savings_plan_rate_usage_type_list.SavingsPlanRateUsageTypeList"
    ]
    """<p>The usage details of the line item in the billing report.</p>"""
    operations: NotRequired[
        "capo_savingsplans.types.savings_plan_rate_operation_list.SavingsPlanRateOperationList"
    ]
    """<p>The specific Amazon Web Services operation for the line item in the billing report.</p>"""
    filters: NotRequired[
        "capo_savingsplans.types.savings_plan_offering_rate_filters_list.SavingsPlanOfferingRateFiltersList"
    ]
    """<p>The filters.</p>"""
    next_token: NotRequired["capo_savingsplans.types.pagination_token.PaginationToken"]
    """<p>The token for the next page of results.</p>"""
    max_results: NotRequired["capo_savingsplans.types.page_size.PageSize"]
    """<p>The maximum number of results to return with a single call. To retrieve additional results, make another call with the returned token value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeSavingsPlansOfferingRatesRequest) -> dict:
    out: dict = {}
    if "savings_plan_offering_ids" in value:
        import capo_savingsplans.types.uui_ds

        out["savingsPlanOfferingIds"] = capo_savingsplans.types.uui_ds.serialize_json(
            value["savings_plan_offering_ids"]
        )
    if "savings_plan_payment_options" in value:
        import capo_savingsplans.types.savings_plan_payment_option_list

        out["savingsPlanPaymentOptions"] = (
            capo_savingsplans.types.savings_plan_payment_option_list.serialize_json(
                value["savings_plan_payment_options"]
            )
        )
    if "savings_plan_types" in value:
        import capo_savingsplans.types.savings_plan_type_list

        out["savingsPlanTypes"] = (
            capo_savingsplans.types.savings_plan_type_list.serialize_json(
                value["savings_plan_types"]
            )
        )
    if "products" in value:
        import capo_savingsplans.types.savings_plan_product_type_list

        out["products"] = (
            capo_savingsplans.types.savings_plan_product_type_list.serialize_json(
                value["products"]
            )
        )
    if "service_codes" in value:
        import capo_savingsplans.types.savings_plan_rate_service_code_list

        out["serviceCodes"] = (
            capo_savingsplans.types.savings_plan_rate_service_code_list.serialize_json(
                value["service_codes"]
            )
        )
    if "usage_types" in value:
        import capo_savingsplans.types.savings_plan_rate_usage_type_list

        out["usageTypes"] = (
            capo_savingsplans.types.savings_plan_rate_usage_type_list.serialize_json(
                value["usage_types"]
            )
        )
    if "operations" in value:
        import capo_savingsplans.types.savings_plan_rate_operation_list

        out["operations"] = (
            capo_savingsplans.types.savings_plan_rate_operation_list.serialize_json(
                value["operations"]
            )
        )
    if "filters" in value:
        import capo_savingsplans.types.savings_plan_offering_rate_filters_list

        out["filters"] = (
            capo_savingsplans.types.savings_plan_offering_rate_filters_list.serialize_json(
                value["filters"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> DescribeSavingsPlansOfferingRatesRequest:
    out: DescribeSavingsPlansOfferingRatesRequest = {}  # type: ignore[typeddict-item]
    if data.get("savingsPlanOfferingIds") is not None:
        import capo_savingsplans.types.uui_ds

        out["savings_plan_offering_ids"] = (
            capo_savingsplans.types.uui_ds.deserialize_json(
                data["savingsPlanOfferingIds"]
            )
        )
    if data.get("savingsPlanPaymentOptions") is not None:
        import capo_savingsplans.types.savings_plan_payment_option_list

        out["savings_plan_payment_options"] = (
            capo_savingsplans.types.savings_plan_payment_option_list.deserialize_json(
                data["savingsPlanPaymentOptions"]
            )
        )
    if data.get("savingsPlanTypes") is not None:
        import capo_savingsplans.types.savings_plan_type_list

        out["savings_plan_types"] = (
            capo_savingsplans.types.savings_plan_type_list.deserialize_json(
                data["savingsPlanTypes"]
            )
        )
    if data.get("products") is not None:
        import capo_savingsplans.types.savings_plan_product_type_list

        out["products"] = (
            capo_savingsplans.types.savings_plan_product_type_list.deserialize_json(
                data["products"]
            )
        )
    if data.get("serviceCodes") is not None:
        import capo_savingsplans.types.savings_plan_rate_service_code_list

        out["service_codes"] = (
            capo_savingsplans.types.savings_plan_rate_service_code_list.deserialize_json(
                data["serviceCodes"]
            )
        )
    if data.get("usageTypes") is not None:
        import capo_savingsplans.types.savings_plan_rate_usage_type_list

        out["usage_types"] = (
            capo_savingsplans.types.savings_plan_rate_usage_type_list.deserialize_json(
                data["usageTypes"]
            )
        )
    if data.get("operations") is not None:
        import capo_savingsplans.types.savings_plan_rate_operation_list

        out["operations"] = (
            capo_savingsplans.types.savings_plan_rate_operation_list.deserialize_json(
                data["operations"]
            )
        )
    if data.get("filters") is not None:
        import capo_savingsplans.types.savings_plan_offering_rate_filters_list

        out["filters"] = (
            capo_savingsplans.types.savings_plan_offering_rate_filters_list.deserialize_json(
                data["filters"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    return out
