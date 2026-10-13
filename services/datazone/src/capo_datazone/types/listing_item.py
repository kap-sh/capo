"""Generated from Smithy shape ``com.amazonaws.datazone#ListingItem``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_datazone.types.asset_listing
    import capo_datazone.types.data_product_listing


class _ListingItem_assetListing(TypedDict, closed=True):
    assetListing: "capo_datazone.types.asset_listing.AssetListing"


class _ListingItem_dataProductListing(TypedDict, closed=True):
    dataProductListing: "capo_datazone.types.data_product_listing.DataProductListing"


ListingItem: TypeAlias = _ListingItem_assetListing | _ListingItem_dataProductListing


# --- restJson1 ser/de ---
def serialize_json(value: ListingItem) -> dict:
    if "assetListing" in value:
        import capo_datazone.types.asset_listing

        return {
            "assetListing": capo_datazone.types.asset_listing.serialize_json(
                value["assetListing"]
            )
        }
    elif "dataProductListing" in value:
        import capo_datazone.types.data_product_listing

        return {
            "dataProductListing": capo_datazone.types.data_product_listing.serialize_json(
                value["dataProductListing"]
            )
        }
    else:
        raise SerializationError("ListingItem: no variant present")


def deserialize_json(data: dict) -> ListingItem:
    if data.get("assetListing") is not None:
        import capo_datazone.types.asset_listing

        return {
            "assetListing": capo_datazone.types.asset_listing.deserialize_json(
                data["assetListing"]
            )
        }
    elif data.get("dataProductListing") is not None:
        import capo_datazone.types.data_product_listing

        return {
            "dataProductListing": capo_datazone.types.data_product_listing.deserialize_json(
                data["dataProductListing"]
            )
        }
    else:
        raise DeserializationError("ListingItem: no recognized variant key")


def redact_sensitive(value: ListingItem) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "assetListing" in value:
        import capo_datazone.types.asset_listing

        out["assetListing"] = capo_datazone.types.asset_listing.redact_sensitive(
            value["assetListing"]
        )
    if "dataProductListing" in value:
        import capo_datazone.types.data_product_listing

        out["dataProductListing"] = (
            capo_datazone.types.data_product_listing.redact_sensitive(
                value["dataProductListing"]
            )
        )
    return out
