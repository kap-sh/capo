"""Generated from Smithy shape ``com.amazonaws.servicecatalog#SearchProductsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.accept_language
    import capo_service_catalog.types.page_size_max100
    import capo_service_catalog.types.page_token
    import capo_service_catalog.types.product_view_filters
    import capo_service_catalog.types.product_view_sort_by
    import capo_service_catalog.types.sort_order


class SearchProductsInput(TypedDict, closed=True):
    accept_language: NotRequired[
        "capo_service_catalog.types.accept_language.AcceptLanguage"
    ]
    """<p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>"""
    filters: NotRequired[
        "capo_service_catalog.types.product_view_filters.ProductViewFilters"
    ]
    """<p>The search filters. If no search filters are specified, the output includes all products to which the caller has access.</p>"""
    page_size: NotRequired["capo_service_catalog.types.page_size_max100.PageSizeMax100"]
    """<p>The maximum number of items to return with this call.</p>"""
    sort_by: NotRequired[
        "capo_service_catalog.types.product_view_sort_by.ProductViewSortBy"
    ]
    """<p>The sort field. If no value is specified, the results are not sorted.</p>"""
    sort_order: NotRequired["capo_service_catalog.types.sort_order.SortOrder"]
    """<p>The sort order. If no value is specified, the results are not sorted.</p>"""
    page_token: NotRequired["capo_service_catalog.types.page_token.PageToken"]
    """<p>The page token for the next set of results. To retrieve the first set of results, use null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SearchProductsInput) -> dict:
    out: dict = {}
    if "accept_language" in value:
        out["AcceptLanguage"] = value["accept_language"]
    if "filters" in value:
        import capo_service_catalog.types.product_view_filters

        out["Filters"] = (
            capo_service_catalog.types.product_view_filters.serialize_aws_json_1_1(
                value["filters"]
            )
        )
    if "page_size" in value:
        out["PageSize"] = value["page_size"]
    if "sort_by" in value:
        import capo_service_catalog.types.product_view_sort_by

        out["SortBy"] = (
            capo_service_catalog.types.product_view_sort_by.serialize_aws_json_1_1(
                value["sort_by"]
            )
        )
    if "sort_order" in value:
        import capo_service_catalog.types.sort_order

        out["SortOrder"] = capo_service_catalog.types.sort_order.serialize_aws_json_1_1(
            value["sort_order"]
        )
    if "page_token" in value:
        out["PageToken"] = value["page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SearchProductsInput:
    out: SearchProductsInput = {}  # type: ignore[typeddict-item]
    if data.get("AcceptLanguage") is not None:
        out["accept_language"] = data["AcceptLanguage"]
    if data.get("Filters") is not None:
        import capo_service_catalog.types.product_view_filters

        out["filters"] = (
            capo_service_catalog.types.product_view_filters.deserialize_aws_json_1_1(
                data["Filters"]
            )
        )
    if data.get("PageSize") is not None:
        out["page_size"] = data["PageSize"]
    if data.get("SortBy") is not None:
        import capo_service_catalog.types.product_view_sort_by

        out["sort_by"] = (
            capo_service_catalog.types.product_view_sort_by.deserialize_aws_json_1_1(
                data["SortBy"]
            )
        )
    if data.get("SortOrder") is not None:
        import capo_service_catalog.types.sort_order

        out["sort_order"] = (
            capo_service_catalog.types.sort_order.deserialize_aws_json_1_1(
                data["SortOrder"]
            )
        )
    if data.get("PageToken") is not None:
        out["page_token"] = data["PageToken"]
    return out
