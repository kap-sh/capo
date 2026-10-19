"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#ListBillEstimateLineItemsFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bcm_pricing_calculator.types.list_bill_estimate_line_items_filter_name
    import capo_bcm_pricing_calculator.types.list_bill_estimate_line_items_filter_values
    import capo_bcm_pricing_calculator.types.match_option


class ListBillEstimateLineItemsFilter(TypedDict, closed=True):
    name: "capo_bcm_pricing_calculator.types.list_bill_estimate_line_items_filter_name.ListBillEstimateLineItemsFilterName"
    """<p> The name of the filter attribute. </p>"""
    values: "capo_bcm_pricing_calculator.types.list_bill_estimate_line_items_filter_values.ListBillEstimateLineItemsFilterValues"
    """<p> The values to filter by. </p>"""
    match_option: NotRequired[
        "capo_bcm_pricing_calculator.types.match_option.MatchOption"
    ]
    """<p> The match option for the filter (e.g., equals, contains). </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListBillEstimateLineItemsFilter) -> dict:
    out: dict = {}
    import capo_bcm_pricing_calculator.types.list_bill_estimate_line_items_filter_name

    out["name"] = (
        capo_bcm_pricing_calculator.types.list_bill_estimate_line_items_filter_name.serialize_aws_json_1_0(
            value["name"]
        )
    )
    import capo_bcm_pricing_calculator.types.list_bill_estimate_line_items_filter_values

    out["values"] = (
        capo_bcm_pricing_calculator.types.list_bill_estimate_line_items_filter_values.serialize_aws_json_1_0(
            value["values"]
        )
    )
    if "match_option" in value:
        import capo_bcm_pricing_calculator.types.match_option

        out["matchOption"] = (
            capo_bcm_pricing_calculator.types.match_option.serialize_aws_json_1_0(
                value["match_option"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListBillEstimateLineItemsFilter:
    out: ListBillEstimateLineItemsFilter = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        import capo_bcm_pricing_calculator.types.list_bill_estimate_line_items_filter_name

        out["name"] = (
            capo_bcm_pricing_calculator.types.list_bill_estimate_line_items_filter_name.deserialize_aws_json_1_0(
                data["name"]
            )
        )
    else:
        import typing

        out["name"] = typing.cast(
            "capo_bcm_pricing_calculator.types.list_bill_estimate_line_items_filter_name.ListBillEstimateLineItemsFilterName",
            "",
        )
    if data.get("values") is not None:
        import capo_bcm_pricing_calculator.types.list_bill_estimate_line_items_filter_values

        out["values"] = (
            capo_bcm_pricing_calculator.types.list_bill_estimate_line_items_filter_values.deserialize_aws_json_1_0(
                data["values"]
            )
        )
    else:
        out["values"] = []
    if data.get("matchOption") is not None:
        import capo_bcm_pricing_calculator.types.match_option

        out["match_option"] = (
            capo_bcm_pricing_calculator.types.match_option.deserialize_aws_json_1_0(
                data["matchOption"]
            )
        )
    return out
