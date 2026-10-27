"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#SubsidiaryAuthorizationCreatedDateFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.subsidiary_authorization_created_date_filter_date_range


class SubsidiaryAuthorizationCreatedDateFilter(TypedDict, closed=True):
    date_range: NotRequired[
        "capo_marketplace_catalog.types.subsidiary_authorization_created_date_filter_date_range.SubsidiaryAuthorizationCreatedDateFilterDateRange"
    ]
    """<p>A date range to filter by. The operation returns subsidiary authorizations with creation dates that fall within this range.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SubsidiaryAuthorizationCreatedDateFilter) -> dict:
    out: dict = {}
    if "date_range" in value:
        import capo_marketplace_catalog.types.subsidiary_authorization_created_date_filter_date_range

        out["DateRange"] = (
            capo_marketplace_catalog.types.subsidiary_authorization_created_date_filter_date_range.serialize_json(
                value["date_range"]
            )
        )
    return out


def deserialize_json(data: dict) -> SubsidiaryAuthorizationCreatedDateFilter:
    out: SubsidiaryAuthorizationCreatedDateFilter = {}  # type: ignore[typeddict-item]
    if data.get("DateRange") is not None:
        import capo_marketplace_catalog.types.subsidiary_authorization_created_date_filter_date_range

        out["date_range"] = (
            capo_marketplace_catalog.types.subsidiary_authorization_created_date_filter_date_range.deserialize_json(
                data["DateRange"]
            )
        )
    return out
