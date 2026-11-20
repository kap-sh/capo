"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#CampaignAssetTemplate``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.asset_name
    import capo_partnercentral_marketing.types.campaign_asset_template_field_list
    import capo_partnercentral_marketing.types.campaign_asset_template_id_list
    import capo_partnercentral_marketing.types.campaign_asset_template_type
    import capo_partnercentral_marketing.types.id
    import capo_partnercentral_marketing.types.layout_preview_list
    import capo_partnercentral_marketing.types.platform


class CampaignAssetTemplate(TypedDict, closed=True):
    id: "capo_partnercentral_marketing.types.id.Id"
    """The template-local asset template identifier."""
    type: "capo_partnercentral_marketing.types.campaign_asset_template_type.CampaignAssetTemplateType"
    """The kind of asset this blueprint instantiates as."""
    label: "capo_partnercentral_marketing.types.asset_name.AssetName"
    """Display label; becomes the instantiated asset's name."""
    display_order: NotRequired["int"]
    """Ordering for preview and instantiation."""
    fields: NotRequired[
        "capo_partnercentral_marketing.types.campaign_asset_template_field_list.CampaignAssetTemplateFieldList"
    ]
    """The editable-field schema, copied and pinned onto each campaign asset at create. Fields the service fills itself are not listed."""
    layout_previews: NotRequired[
        "capo_partnercentral_marketing.types.layout_preview_list.LayoutPreviewList"
    ]
    """Previews of the AWS-authored layout skeleton."""
    prerequisite_asset_template_ids: NotRequired[
        "capo_partnercentral_marketing.types.campaign_asset_template_id_list.CampaignAssetTemplateIdList"
    ]
    """The asset templates this one embeds output from, such as an email's landing page. Each must be in the same `BatchCreateCampaignAsset` request or already an asset on the campaign, else the create is refused `PREREQUISITE_ASSET_MISSING`; include them when the partner picks this one. Absent when there are none. A link the partner chooses, such as a landing page's download button, is not listed here: it is an `AssetLink` field and needs nothing at create."""
    social_platform: NotRequired[
        "capo_partnercentral_marketing.types.platform.Platform"
    ]
    """SOCIAL_POST only: the platform an asset made from this blueprint posts to, which the asset reports as `SocialPlatform`. Fixed by the template, so a client can show which social connection the post needs before it is created. Absent for every other type."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CampaignAssetTemplate) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    import capo_partnercentral_marketing.types.campaign_asset_template_type

    out["Type"] = (
        capo_partnercentral_marketing.types.campaign_asset_template_type.serialize_cbor(
            value["type"]
        )
    )
    out["Label"] = value["label"]
    if "display_order" in value:
        out["DisplayOrder"] = value["display_order"]
    if "fields" in value:
        import capo_partnercentral_marketing.types.campaign_asset_template_field_list

        out["Fields"] = (
            capo_partnercentral_marketing.types.campaign_asset_template_field_list.serialize_cbor(
                value["fields"]
            )
        )
    if "layout_previews" in value:
        import capo_partnercentral_marketing.types.layout_preview_list

        out["LayoutPreviews"] = (
            capo_partnercentral_marketing.types.layout_preview_list.serialize_cbor(
                value["layout_previews"]
            )
        )
    if "prerequisite_asset_template_ids" in value:
        import capo_partnercentral_marketing.types.campaign_asset_template_id_list

        out["PrerequisiteAssetTemplateIds"] = (
            capo_partnercentral_marketing.types.campaign_asset_template_id_list.serialize_cbor(
                value["prerequisite_asset_template_ids"]
            )
        )
    if "social_platform" in value:
        import capo_partnercentral_marketing.types.platform

        out["SocialPlatform"] = (
            capo_partnercentral_marketing.types.platform.serialize_cbor(
                value["social_platform"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> CampaignAssetTemplate:
    out: CampaignAssetTemplate = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = ""
    if data.get("Type") is not None:
        import capo_partnercentral_marketing.types.campaign_asset_template_type

        out["type"] = (
            capo_partnercentral_marketing.types.campaign_asset_template_type.deserialize_cbor(
                data["Type"]
            )
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_partnercentral_marketing.types.campaign_asset_template_type.CampaignAssetTemplateType",
            "",
        )
    if data.get("Label") is not None:
        out["label"] = data["Label"]
    else:
        out["label"] = ""
    if data.get("DisplayOrder") is not None:
        out["display_order"] = data["DisplayOrder"]
    if data.get("Fields") is not None:
        import capo_partnercentral_marketing.types.campaign_asset_template_field_list

        out["fields"] = (
            capo_partnercentral_marketing.types.campaign_asset_template_field_list.deserialize_cbor(
                data["Fields"]
            )
        )
    if data.get("LayoutPreviews") is not None:
        import capo_partnercentral_marketing.types.layout_preview_list

        out["layout_previews"] = (
            capo_partnercentral_marketing.types.layout_preview_list.deserialize_cbor(
                data["LayoutPreviews"]
            )
        )
    if data.get("PrerequisiteAssetTemplateIds") is not None:
        import capo_partnercentral_marketing.types.campaign_asset_template_id_list

        out["prerequisite_asset_template_ids"] = (
            capo_partnercentral_marketing.types.campaign_asset_template_id_list.deserialize_cbor(
                data["PrerequisiteAssetTemplateIds"]
            )
        )
    if data.get("SocialPlatform") is not None:
        import capo_partnercentral_marketing.types.platform

        out["social_platform"] = (
            capo_partnercentral_marketing.types.platform.deserialize_cbor(
                data["SocialPlatform"]
            )
        )
    return out


def redact_sensitive(value: CampaignAssetTemplate) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "fields" in value:
        import capo_partnercentral_marketing.types.campaign_asset_template_field_list

        out["fields"] = (
            capo_partnercentral_marketing.types.campaign_asset_template_field_list.redact_sensitive(
                value["fields"]
            )
        )
    return out
