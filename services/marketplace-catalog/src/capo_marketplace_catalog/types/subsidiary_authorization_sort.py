"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#SubsidiaryAuthorizationSort``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.sort_order
    import capo_marketplace_catalog.types.subsidiary_authorization_sort_by


class SubsidiaryAuthorizationSort(TypedDict, closed=True):
    sort_by: NotRequired[
        "capo_marketplace_catalog.types.subsidiary_authorization_sort_by.SubsidiaryAuthorizationSortBy"
    ]
    """<p>The field to sort subsidiary authorizations by. Valid values are <code>EntityId</code>, <code>Status</code>, <code>ResourceId</code>, <code>SubsidiaryAccountId</code>, <code>CreatedDate</code>, and <code>LastModifiedDate</code>.</p>"""
    sort_order: NotRequired["capo_marketplace_catalog.types.sort_order.SortOrder"]
    """<p>The sorting order. Can be <code>ASCENDING</code> or <code>DESCENDING</code>. The default value is <code>DESCENDING</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SubsidiaryAuthorizationSort) -> dict:
    out: dict = {}
    if "sort_by" in value:
        import capo_marketplace_catalog.types.subsidiary_authorization_sort_by

        out["SortBy"] = (
            capo_marketplace_catalog.types.subsidiary_authorization_sort_by.serialize_json(
                value["sort_by"]
            )
        )
    if "sort_order" in value:
        import capo_marketplace_catalog.types.sort_order

        out["SortOrder"] = capo_marketplace_catalog.types.sort_order.serialize_json(
            value["sort_order"]
        )
    return out


def deserialize_json(data: dict) -> SubsidiaryAuthorizationSort:
    out: SubsidiaryAuthorizationSort = {}  # type: ignore[typeddict-item]
    if data.get("SortBy") is not None:
        import capo_marketplace_catalog.types.subsidiary_authorization_sort_by

        out["sort_by"] = (
            capo_marketplace_catalog.types.subsidiary_authorization_sort_by.deserialize_json(
                data["SortBy"]
            )
        )
    if data.get("SortOrder") is not None:
        import capo_marketplace_catalog.types.sort_order

        out["sort_order"] = capo_marketplace_catalog.types.sort_order.deserialize_json(
            data["SortOrder"]
        )
    return out
