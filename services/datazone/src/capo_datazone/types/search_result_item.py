"""Generated from Smithy shape ``com.amazonaws.datazone#SearchResultItem``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError, SerializationError
from capo_datazone.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_datazone.types.asset_listing_item
    import capo_datazone.types.data_product_listing_item


class SearchResultItemAssetListingMember(TypedDict, closed=True):
    assetListing: "capo_datazone.types.asset_listing_item.AssetListingItem"


class SearchResultItemDataProductListingMember(TypedDict, closed=True):
    dataProductListing: (
        "capo_datazone.types.data_product_listing_item.DataProductListingItem"
    )


SearchResultItem: TypeAlias = (
    SearchResultItemAssetListingMember
    | SearchResultItemDataProductListingMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: SearchResultItem) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"SearchResultItem: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "assetListing" in value:
        import capo_datazone.types.asset_listing_item

        return {
            "assetListing": capo_datazone.types.asset_listing_item.serialize_json(
                value["assetListing"]
            )
        }
    elif "dataProductListing" in value:
        import capo_datazone.types.data_product_listing_item

        return {
            "dataProductListing": capo_datazone.types.data_product_listing_item.serialize_json(
                value["dataProductListing"]
            )
        }
    else:
        raise SerializationError("SearchResultItem: no variant present")


def deserialize_json(data: dict) -> SearchResultItem:
    if data.get("assetListing") is not None:
        import capo_datazone.types.asset_listing_item

        return {
            "assetListing": capo_datazone.types.asset_listing_item.deserialize_json(
                data["assetListing"]
            )
        }
    elif data.get("dataProductListing") is not None:
        import capo_datazone.types.data_product_listing_item

        return {
            "dataProductListing": capo_datazone.types.data_product_listing_item.deserialize_json(
                data["dataProductListing"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("SearchResultItem: no recognized variant key")


def redact_sensitive(value: SearchResultItem) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "assetListing" in value:
        import capo_datazone.types.asset_listing_item

        out["assetListing"] = capo_datazone.types.asset_listing_item.redact_sensitive(
            value["assetListing"]
        )
    if "dataProductListing" in value:
        import capo_datazone.types.data_product_listing_item

        out["dataProductListing"] = (
            capo_datazone.types.data_product_listing_item.redact_sensitive(
                value["dataProductListing"]
            )
        )
    return out
