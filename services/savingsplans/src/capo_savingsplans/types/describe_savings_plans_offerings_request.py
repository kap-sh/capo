"""Generated from Smithy shape ``com.amazonaws.savingsplans#DescribeSavingsPlansOfferingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_savingsplans.types.currency_list
    import capo_savingsplans.types.durations_list
    import capo_savingsplans.types.page_size
    import capo_savingsplans.types.pagination_token
    import capo_savingsplans.types.savings_plan_descriptions_list
    import capo_savingsplans.types.savings_plan_offering_filters_list
    import capo_savingsplans.types.savings_plan_operation_list
    import capo_savingsplans.types.savings_plan_payment_option_list
    import capo_savingsplans.types.savings_plan_product_type
    import capo_savingsplans.types.savings_plan_service_code_list
    import capo_savingsplans.types.savings_plan_type_list
    import capo_savingsplans.types.savings_plan_usage_type_list
    import capo_savingsplans.types.uui_ds


class DescribeSavingsPlansOfferingsRequest(TypedDict, closed=True):
    offering_ids: NotRequired["capo_savingsplans.types.uui_ds.UUIDs"]
    """<p>The IDs of the offerings.</p>"""
    payment_options: NotRequired[
        "capo_savingsplans.types.savings_plan_payment_option_list.SavingsPlanPaymentOptionList"
    ]
    """<p>The payment options.</p>"""
    product_type: NotRequired[
        "capo_savingsplans.types.savings_plan_product_type.SavingsPlanProductType"
    ]
    """<p>The product type.</p>"""
    plan_types: NotRequired[
        "capo_savingsplans.types.savings_plan_type_list.SavingsPlanTypeList"
    ]
    """<p>The plan types.</p>"""
    durations: NotRequired["capo_savingsplans.types.durations_list.DurationsList"]
    """<p>The duration, in seconds.</p>"""
    currencies: NotRequired["capo_savingsplans.types.currency_list.CurrencyList"]
    """<p>The currencies.</p>"""
    descriptions: NotRequired[
        "capo_savingsplans.types.savings_plan_descriptions_list.SavingsPlanDescriptionsList"
    ]
    """<p>The descriptions.</p>"""
    service_codes: NotRequired[
        "capo_savingsplans.types.savings_plan_service_code_list.SavingsPlanServiceCodeList"
    ]
    """<p>The services.</p>"""
    usage_types: NotRequired[
        "capo_savingsplans.types.savings_plan_usage_type_list.SavingsPlanUsageTypeList"
    ]
    """<p>The usage details of the line item in the billing report.</p>"""
    operations: NotRequired[
        "capo_savingsplans.types.savings_plan_operation_list.SavingsPlanOperationList"
    ]
    """<p>The specific Amazon Web Services operation for the line item in the billing report.</p>"""
    filters: NotRequired[
        "capo_savingsplans.types.savings_plan_offering_filters_list.SavingsPlanOfferingFiltersList"
    ]
    """<p>The filters.</p>"""
    next_token: NotRequired["capo_savingsplans.types.pagination_token.PaginationToken"]
    """<p>The token for the next page of results.</p>"""
    max_results: NotRequired["capo_savingsplans.types.page_size.PageSize"]
    """<p>The maximum number of results to return with a single call. To retrieve additional results, make another call with the returned token value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeSavingsPlansOfferingsRequest) -> dict:
    out: dict = {}
    if "offering_ids" in value:
        import capo_savingsplans.types.uui_ds

        out["offeringIds"] = capo_savingsplans.types.uui_ds.serialize_json(
            value["offering_ids"]
        )
    if "payment_options" in value:
        import capo_savingsplans.types.savings_plan_payment_option_list

        out["paymentOptions"] = (
            capo_savingsplans.types.savings_plan_payment_option_list.serialize_json(
                value["payment_options"]
            )
        )
    if "product_type" in value:
        import capo_savingsplans.types.savings_plan_product_type

        out["productType"] = (
            capo_savingsplans.types.savings_plan_product_type.serialize_json(
                value["product_type"]
            )
        )
    if "plan_types" in value:
        import capo_savingsplans.types.savings_plan_type_list

        out["planTypes"] = (
            capo_savingsplans.types.savings_plan_type_list.serialize_json(
                value["plan_types"]
            )
        )
    if "durations" in value:
        import capo_savingsplans.types.durations_list

        out["durations"] = capo_savingsplans.types.durations_list.serialize_json(
            value["durations"]
        )
    if "currencies" in value:
        import capo_savingsplans.types.currency_list

        out["currencies"] = capo_savingsplans.types.currency_list.serialize_json(
            value["currencies"]
        )
    if "descriptions" in value:
        import capo_savingsplans.types.savings_plan_descriptions_list

        out["descriptions"] = (
            capo_savingsplans.types.savings_plan_descriptions_list.serialize_json(
                value["descriptions"]
            )
        )
    if "service_codes" in value:
        import capo_savingsplans.types.savings_plan_service_code_list

        out["serviceCodes"] = (
            capo_savingsplans.types.savings_plan_service_code_list.serialize_json(
                value["service_codes"]
            )
        )
    if "usage_types" in value:
        import capo_savingsplans.types.savings_plan_usage_type_list

        out["usageTypes"] = (
            capo_savingsplans.types.savings_plan_usage_type_list.serialize_json(
                value["usage_types"]
            )
        )
    if "operations" in value:
        import capo_savingsplans.types.savings_plan_operation_list

        out["operations"] = (
            capo_savingsplans.types.savings_plan_operation_list.serialize_json(
                value["operations"]
            )
        )
    if "filters" in value:
        import capo_savingsplans.types.savings_plan_offering_filters_list

        out["filters"] = (
            capo_savingsplans.types.savings_plan_offering_filters_list.serialize_json(
                value["filters"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> DescribeSavingsPlansOfferingsRequest:
    out: DescribeSavingsPlansOfferingsRequest = {}  # type: ignore[typeddict-item]
    if data.get("offeringIds") is not None:
        import capo_savingsplans.types.uui_ds

        out["offering_ids"] = capo_savingsplans.types.uui_ds.deserialize_json(
            data["offeringIds"]
        )
    if data.get("paymentOptions") is not None:
        import capo_savingsplans.types.savings_plan_payment_option_list

        out["payment_options"] = (
            capo_savingsplans.types.savings_plan_payment_option_list.deserialize_json(
                data["paymentOptions"]
            )
        )
    if data.get("productType") is not None:
        import capo_savingsplans.types.savings_plan_product_type

        out["product_type"] = (
            capo_savingsplans.types.savings_plan_product_type.deserialize_json(
                data["productType"]
            )
        )
    if data.get("planTypes") is not None:
        import capo_savingsplans.types.savings_plan_type_list

        out["plan_types"] = (
            capo_savingsplans.types.savings_plan_type_list.deserialize_json(
                data["planTypes"]
            )
        )
    if data.get("durations") is not None:
        import capo_savingsplans.types.durations_list

        out["durations"] = capo_savingsplans.types.durations_list.deserialize_json(
            data["durations"]
        )
    if data.get("currencies") is not None:
        import capo_savingsplans.types.currency_list

        out["currencies"] = capo_savingsplans.types.currency_list.deserialize_json(
            data["currencies"]
        )
    if data.get("descriptions") is not None:
        import capo_savingsplans.types.savings_plan_descriptions_list

        out["descriptions"] = (
            capo_savingsplans.types.savings_plan_descriptions_list.deserialize_json(
                data["descriptions"]
            )
        )
    if data.get("serviceCodes") is not None:
        import capo_savingsplans.types.savings_plan_service_code_list

        out["service_codes"] = (
            capo_savingsplans.types.savings_plan_service_code_list.deserialize_json(
                data["serviceCodes"]
            )
        )
    if data.get("usageTypes") is not None:
        import capo_savingsplans.types.savings_plan_usage_type_list

        out["usage_types"] = (
            capo_savingsplans.types.savings_plan_usage_type_list.deserialize_json(
                data["usageTypes"]
            )
        )
    if data.get("operations") is not None:
        import capo_savingsplans.types.savings_plan_operation_list

        out["operations"] = (
            capo_savingsplans.types.savings_plan_operation_list.deserialize_json(
                data["operations"]
            )
        )
    if data.get("filters") is not None:
        import capo_savingsplans.types.savings_plan_offering_filters_list

        out["filters"] = (
            capo_savingsplans.types.savings_plan_offering_filters_list.deserialize_json(
                data["filters"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    return out
