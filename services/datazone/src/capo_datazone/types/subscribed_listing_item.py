"""Generated from Smithy shape ``com.amazonaws.datazone#SubscribedListingItem``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_datazone.types.subscribed_asset_listing
    import capo_datazone.types.subscribed_product_listing


class _SubscribedListingItem_assetListing(TypedDict, closed=True):
    assetListing: "capo_datazone.types.subscribed_asset_listing.SubscribedAssetListing"


class _SubscribedListingItem_productListing(TypedDict, closed=True):
    productListing: (
        "capo_datazone.types.subscribed_product_listing.SubscribedProductListing"
    )


SubscribedListingItem: TypeAlias = (
    _SubscribedListingItem_assetListing | _SubscribedListingItem_productListing
)


# --- restJson1 ser/de ---
def serialize_json(value: SubscribedListingItem) -> dict:
    if "assetListing" in value:
        import capo_datazone.types.subscribed_asset_listing

        return {
            "assetListing": capo_datazone.types.subscribed_asset_listing.serialize_json(
                value["assetListing"]
            )
        }
    elif "productListing" in value:
        import capo_datazone.types.subscribed_product_listing

        return {
            "productListing": capo_datazone.types.subscribed_product_listing.serialize_json(
                value["productListing"]
            )
        }
    else:
        raise SerializationError("SubscribedListingItem: no variant present")


def deserialize_json(data: dict) -> SubscribedListingItem:
    if data.get("assetListing") is not None:
        import capo_datazone.types.subscribed_asset_listing

        return {
            "assetListing": capo_datazone.types.subscribed_asset_listing.deserialize_json(
                data["assetListing"]
            )
        }
    elif data.get("productListing") is not None:
        import capo_datazone.types.subscribed_product_listing

        return {
            "productListing": capo_datazone.types.subscribed_product_listing.deserialize_json(
                data["productListing"]
            )
        }
    else:
        raise DeserializationError("SubscribedListingItem: no recognized variant key")


def redact_sensitive(value: SubscribedListingItem) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "assetListing" in value:
        import capo_datazone.types.subscribed_asset_listing

        out["assetListing"] = (
            capo_datazone.types.subscribed_asset_listing.redact_sensitive(
                value["assetListing"]
            )
        )
    if "productListing" in value:
        import capo_datazone.types.subscribed_product_listing

        out["productListing"] = (
            capo_datazone.types.subscribed_product_listing.redact_sensitive(
                value["productListing"]
            )
        )
    return out
