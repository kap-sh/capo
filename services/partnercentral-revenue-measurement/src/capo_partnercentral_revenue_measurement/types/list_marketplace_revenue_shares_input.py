"""Generated from Smithy shape ``com.amazonaws.partnercentralrevenuemeasurement#ListMarketplaceRevenueSharesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_partnercentral_revenue_measurement.types.catalog_name
    import capo_partnercentral_revenue_measurement.types.marketplace_product_id_list
    import capo_partnercentral_revenue_measurement.types.marketplace_revenue_share_sort_by
    import capo_partnercentral_revenue_measurement.types.next_token
    import capo_partnercentral_revenue_measurement.types.product_code_list
    import capo_partnercentral_revenue_measurement.types.sort_order


class ListMarketplaceRevenueSharesInput(TypedDict, closed=True):
    catalog: "capo_partnercentral_revenue_measurement.types.catalog_name.CatalogName"
    """<p>The catalog to list marketplace revenue shares from.</p>"""
    product_ids: NotRequired[
        "capo_partnercentral_revenue_measurement.types.marketplace_product_id_list.MarketplaceProductIdList"
    ]
    """<p>Filter results to only include shares with these product identifiers.</p>"""
    product_codes: NotRequired[
        "capo_partnercentral_revenue_measurement.types.product_code_list.ProductCodeList"
    ]
    """<p>Filter results to only include shares with these product codes.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of results to return in a single call.</p>"""
    next_token: NotRequired[
        "capo_partnercentral_revenue_measurement.types.next_token.NextToken"
    ]
    """<p>Token for pagination. Use the value returned in the previous response to retrieve the next page.</p>"""
    sort_by: NotRequired[
        "capo_partnercentral_revenue_measurement.types.marketplace_revenue_share_sort_by.MarketplaceRevenueShareSortBy"
    ]
    """<p>The field to sort marketplace revenue shares by.</p>"""
    sort_order: NotRequired[
        "capo_partnercentral_revenue_measurement.types.sort_order.SortOrder"
    ]
    """<p>The direction to sort results.</p>"""
    created_after: NotRequired["datetime.datetime"]
    """<p>Filter results to only include marketplace revenue shares created after this timestamp.</p>"""
    created_before: NotRequired["datetime.datetime"]
    """<p>Filter results to only include marketplace revenue shares created before this timestamp.</p>"""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListMarketplaceRevenueSharesInput) -> dict:
    out: dict = {}
    import capo_partnercentral_revenue_measurement.types.catalog_name

    out["Catalog"] = (
        capo_partnercentral_revenue_measurement.types.catalog_name.serialize_cbor(
            value["catalog"]
        )
    )
    if "product_ids" in value:
        import capo_partnercentral_revenue_measurement.types.marketplace_product_id_list

        out["ProductIds"] = (
            capo_partnercentral_revenue_measurement.types.marketplace_product_id_list.serialize_cbor(
                value["product_ids"]
            )
        )
    if "product_codes" in value:
        import capo_partnercentral_revenue_measurement.types.product_code_list

        out["ProductCodes"] = (
            capo_partnercentral_revenue_measurement.types.product_code_list.serialize_cbor(
                value["product_codes"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "sort_by" in value:
        import capo_partnercentral_revenue_measurement.types.marketplace_revenue_share_sort_by

        out["SortBy"] = (
            capo_partnercentral_revenue_measurement.types.marketplace_revenue_share_sort_by.serialize_cbor(
                value["sort_by"]
            )
        )
    if "sort_order" in value:
        import capo_partnercentral_revenue_measurement.types.sort_order

        out["SortOrder"] = (
            capo_partnercentral_revenue_measurement.types.sort_order.serialize_cbor(
                value["sort_order"]
            )
        )
    if "created_after" in value:
        import capo_partnercentral_revenue_measurement.types._prelude.timestamp

        out["CreatedAfter"] = (
            capo_partnercentral_revenue_measurement.types._prelude.timestamp.serialize_cbor(
                value["created_after"]
            )
        )
    if "created_before" in value:
        import capo_partnercentral_revenue_measurement.types._prelude.timestamp

        out["CreatedBefore"] = (
            capo_partnercentral_revenue_measurement.types._prelude.timestamp.serialize_cbor(
                value["created_before"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> ListMarketplaceRevenueSharesInput:
    out: ListMarketplaceRevenueSharesInput = {}  # type: ignore[typeddict-item]
    if data.get("Catalog") is not None:
        import capo_partnercentral_revenue_measurement.types.catalog_name

        out["catalog"] = (
            capo_partnercentral_revenue_measurement.types.catalog_name.deserialize_cbor(
                data["Catalog"]
            )
        )
    else:
        import typing

        out["catalog"] = typing.cast(
            "capo_partnercentral_revenue_measurement.types.catalog_name.CatalogName", ""
        )
    if data.get("ProductIds") is not None:
        import capo_partnercentral_revenue_measurement.types.marketplace_product_id_list

        out["product_ids"] = (
            capo_partnercentral_revenue_measurement.types.marketplace_product_id_list.deserialize_cbor(
                data["ProductIds"]
            )
        )
    if data.get("ProductCodes") is not None:
        import capo_partnercentral_revenue_measurement.types.product_code_list

        out["product_codes"] = (
            capo_partnercentral_revenue_measurement.types.product_code_list.deserialize_cbor(
                data["ProductCodes"]
            )
        )
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("SortBy") is not None:
        import capo_partnercentral_revenue_measurement.types.marketplace_revenue_share_sort_by

        out["sort_by"] = (
            capo_partnercentral_revenue_measurement.types.marketplace_revenue_share_sort_by.deserialize_cbor(
                data["SortBy"]
            )
        )
    if data.get("SortOrder") is not None:
        import capo_partnercentral_revenue_measurement.types.sort_order

        out["sort_order"] = (
            capo_partnercentral_revenue_measurement.types.sort_order.deserialize_cbor(
                data["SortOrder"]
            )
        )
    if data.get("CreatedAfter") is not None:
        import capo_partnercentral_revenue_measurement.types._prelude.timestamp

        out["created_after"] = (
            capo_partnercentral_revenue_measurement.types._prelude.timestamp.deserialize_cbor(
                data["CreatedAfter"]
            )
        )
    if data.get("CreatedBefore") is not None:
        import capo_partnercentral_revenue_measurement.types._prelude.timestamp

        out["created_before"] = (
            capo_partnercentral_revenue_measurement.types._prelude.timestamp.deserialize_cbor(
                data["CreatedBefore"]
            )
        )
    return out
