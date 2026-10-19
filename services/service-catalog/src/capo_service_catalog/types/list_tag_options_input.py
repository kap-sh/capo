"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ListTagOptionsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.list_tag_options_filters
    import capo_service_catalog.types.page_size
    import capo_service_catalog.types.page_token


class ListTagOptionsInput(TypedDict, closed=True):
    filters: NotRequired[
        "capo_service_catalog.types.list_tag_options_filters.ListTagOptionsFilters"
    ]
    """<p>The search filters. If no search filters are specified, the output includes all TagOptions.</p>"""
    page_size: NotRequired["capo_service_catalog.types.page_size.PageSize"]
    """<p>The maximum number of items to return with this call.</p>"""
    page_token: NotRequired["capo_service_catalog.types.page_token.PageToken"]
    """<p>The page token for the next set of results. To retrieve the first set of results, use null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagOptionsInput) -> dict:
    out: dict = {}
    if "filters" in value:
        import capo_service_catalog.types.list_tag_options_filters

        out["Filters"] = (
            capo_service_catalog.types.list_tag_options_filters.serialize_aws_json_1_1(
                value["filters"]
            )
        )
    if "page_size" in value:
        out["PageSize"] = value["page_size"]
    if "page_token" in value:
        out["PageToken"] = value["page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagOptionsInput:
    out: ListTagOptionsInput = {}  # type: ignore[typeddict-item]
    if data.get("Filters") is not None:
        import capo_service_catalog.types.list_tag_options_filters

        out["filters"] = (
            capo_service_catalog.types.list_tag_options_filters.deserialize_aws_json_1_1(
                data["Filters"]
            )
        )
    if data.get("PageSize") is not None:
        out["page_size"] = data["PageSize"]
    if data.get("PageToken") is not None:
        out["page_token"] = data["PageToken"]
    return out
