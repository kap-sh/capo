"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#SubsidiaryAuthorizationLastModifiedDateFilterDateRange``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.date_time_iso8601


class SubsidiaryAuthorizationLastModifiedDateFilterDateRange(TypedDict, closed=True):
    after_value: NotRequired[
        "capo_marketplace_catalog.types.date_time_iso8601.DateTimeISO8601"
    ]
    """<p>The start date (inclusive) of the date range. The operation returns subsidiary authorizations last modified on or after this date.</p>"""
    before_value: NotRequired[
        "capo_marketplace_catalog.types.date_time_iso8601.DateTimeISO8601"
    ]
    """<p>The end date (inclusive) of the date range. The operation returns subsidiary authorizations last modified on or before this date.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: SubsidiaryAuthorizationLastModifiedDateFilterDateRange,
) -> dict:
    out: dict = {}
    if "after_value" in value:
        out["AfterValue"] = value["after_value"]
    if "before_value" in value:
        out["BeforeValue"] = value["before_value"]
    return out


def deserialize_json(
    data: dict,
) -> SubsidiaryAuthorizationLastModifiedDateFilterDateRange:
    out: SubsidiaryAuthorizationLastModifiedDateFilterDateRange = {}  # type: ignore[typeddict-item]
    if data.get("AfterValue") is not None:
        out["after_value"] = data["AfterValue"]
    if data.get("BeforeValue") is not None:
        out["before_value"] = data["BeforeValue"]
    return out
