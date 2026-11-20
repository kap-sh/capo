"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#AssetLinkFieldType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.campaign_asset_category
    import capo_partnercentral_marketing.types.template_field_id


class AssetLinkFieldType(TypedDict, closed=True):
    category: "capo_partnercentral_marketing.types.campaign_asset_category.CampaignAssetCategory"
    """The category of asset the field may name. The value must be an asset of this category on the same campaign; list the candidates with `ListCampaignAssets`."""
    label_field_id: NotRequired[
        "capo_partnercentral_marketing.types.template_field_id.TemplateFieldId"
    ]
    """The text field on the same asset whose copy names the linked asset, such as the "Solution Brief" in "Your Solution Brief is ready to download!". When the partner picks an asset, fill this field with the picked asset's `LinkLabel`, in a preview and in the same save, unless the partner has edited it. The field stays editable. The service does the same when a save changes the link without setting this field and the partner has never written it."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AssetLinkFieldType) -> dict:
    out: dict = {}
    import capo_partnercentral_marketing.types.campaign_asset_category

    out["Category"] = (
        capo_partnercentral_marketing.types.campaign_asset_category.serialize_cbor(
            value["category"]
        )
    )
    if "label_field_id" in value:
        out["LabelFieldId"] = value["label_field_id"]
    return out


def deserialize_cbor(data: dict) -> AssetLinkFieldType:
    out: AssetLinkFieldType = {}  # type: ignore[typeddict-item]
    if data.get("Category") is not None:
        import capo_partnercentral_marketing.types.campaign_asset_category

        out["category"] = (
            capo_partnercentral_marketing.types.campaign_asset_category.deserialize_cbor(
                data["Category"]
            )
        )
    else:
        import typing

        out["category"] = typing.cast(
            "capo_partnercentral_marketing.types.campaign_asset_category.CampaignAssetCategory",
            "",
        )
    if data.get("LabelFieldId") is not None:
        out["label_field_id"] = data["LabelFieldId"]
    return out
