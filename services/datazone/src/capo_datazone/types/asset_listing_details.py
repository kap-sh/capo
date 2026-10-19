"""Generated from Smithy shape ``com.amazonaws.datazone#AssetListingDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.listing_id
    import capo_datazone.types.listing_status


class AssetListingDetails(TypedDict, closed=True):
    listing_id: "capo_datazone.types.listing_id.ListingId"
    """<p>The identifier of an asset published in an Amazon DataZone catalog. </p>"""
    listing_status: "capo_datazone.types.listing_status.ListingStatus"
    """<p>The status of an asset published in an Amazon DataZone catalog. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetListingDetails) -> dict:
    out: dict = {}
    out["listingId"] = value["listing_id"]
    import capo_datazone.types.listing_status

    out["listingStatus"] = capo_datazone.types.listing_status.serialize_json(
        value["listing_status"]
    )
    return out


def deserialize_json(data: dict) -> AssetListingDetails:
    out: AssetListingDetails = {}  # type: ignore[typeddict-item]
    if data.get("listingId") is not None:
        out["listing_id"] = data["listingId"]
    else:
        out["listing_id"] = ""
    if data.get("listingStatus") is not None:
        import capo_datazone.types.listing_status

        out["listing_status"] = capo_datazone.types.listing_status.deserialize_json(
            data["listingStatus"]
        )
    else:
        import typing

        out["listing_status"] = typing.cast(
            "capo_datazone.types.listing_status.ListingStatus", ""
        )
    return out
