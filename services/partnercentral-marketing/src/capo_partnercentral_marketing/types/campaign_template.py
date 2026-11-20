"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#CampaignTemplate``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.asset_language
    import capo_partnercentral_marketing.types.aws_services_list
    import capo_partnercentral_marketing.types.campaign_asset_template_list
    import capo_partnercentral_marketing.types.campaign_template_collection
    import capo_partnercentral_marketing.types.campaign_template_description
    import capo_partnercentral_marketing.types.campaign_template_id
    import capo_partnercentral_marketing.types.customer_segment_list
    import capo_partnercentral_marketing.types.industry
    import capo_partnercentral_marketing.types.reference_material_list
    import capo_partnercentral_marketing.types.template_name
    import capo_partnercentral_marketing.types.theme_list
    import capo_partnercentral_marketing.types.timestamp


class CampaignTemplate(TypedDict, closed=True):
    id: "capo_partnercentral_marketing.types.campaign_template_id.CampaignTemplateId"
    """The campaign template identifier."""
    name: "capo_partnercentral_marketing.types.template_name.TemplateName"
    """The display name."""
    industry: NotRequired["capo_partnercentral_marketing.types.industry.Industry"]
    """Target industry for filtering or categorization."""
    use_case: NotRequired["str"]
    """Campaign use case for filtering or categorization."""
    description: NotRequired[
        "capo_partnercentral_marketing.types.campaign_template_description.CampaignTemplateDescription"
    ]
    """A short overview of the campaign, as plain text in the template's language: no HTML and no character entities. Absent when the template has none; never an empty string."""
    language_code: NotRequired[
        "capo_partnercentral_marketing.types.asset_language.AssetLanguage"
    ]
    """Language the template is authored in, which a campaign created from it takes. A template has one language; the same content in another language is another template."""
    collection: "capo_partnercentral_marketing.types.campaign_template_collection.CampaignTemplateCollection"
    """The browsing context the template is listed in. Every template has exactly one."""
    aws_services: NotRequired[
        "capo_partnercentral_marketing.types.aws_services_list.AwsServicesList"
    ]
    """AWS services the template promotes."""
    customer_segments: NotRequired[
        "capo_partnercentral_marketing.types.customer_segment_list.CustomerSegmentList"
    ]
    """The customer segments the template is written for. Absent when the template names none, in which case it matches every `CustomerSegments` search filter."""
    themes: NotRequired["capo_partnercentral_marketing.types.theme_list.ThemeList"]
    """The template's marketing themes. Absent when the template names none, in which case it matches every `Themes` search filter."""
    setup_duration: NotRequired["str"]
    """Estimated setup time."""
    thumbnail_url: NotRequired["str"]
    """Thumbnail URL."""
    effective_date_begin: NotRequired[
        "capo_partnercentral_marketing.types.timestamp.Timestamp"
    ]
    """The instant the template becomes available to partners. Until then the template does not exist to a partner: SearchCampaignTemplates omits it and GetCampaignTemplate returns ResourceNotFoundException."""
    asset_templates: NotRequired[
        "capo_partnercentral_marketing.types.campaign_asset_template_list.CampaignAssetTemplateList"
    ]
    """The ordered asset blueprints. One call serves both template browsing and server-side copy-at-create."""
    reference_materials: NotRequired[
        "capo_partnercentral_marketing.types.reference_material_list.ReferenceMaterialList"
    ]
    """The template's reference materials: guides, briefs, copy blocks and other files a partner downloads and uses in their own channels. Kept apart from `AssetTemplates` because none of them can become a campaign asset — they have no editable field and nothing to activate — and listing them beside the blueprints invited a `BatchCreateCampaignAsset` that could only fail. Absent when the template has none."""
    created_at: NotRequired["capo_partnercentral_marketing.types.timestamp.Timestamp"]
    """Creation timestamp."""
    updated_at: NotRequired["capo_partnercentral_marketing.types.timestamp.Timestamp"]
    """Last update timestamp."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CampaignTemplate) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    out["Name"] = value["name"]
    if "industry" in value:
        import capo_partnercentral_marketing.types.industry

        out["Industry"] = capo_partnercentral_marketing.types.industry.serialize_cbor(
            value["industry"]
        )
    if "use_case" in value:
        out["UseCase"] = value["use_case"]
    if "description" in value:
        out["Description"] = value["description"]
    if "language_code" in value:
        import capo_partnercentral_marketing.types.asset_language

        out["LanguageCode"] = (
            capo_partnercentral_marketing.types.asset_language.serialize_cbor(
                value["language_code"]
            )
        )
    import capo_partnercentral_marketing.types.campaign_template_collection

    out["Collection"] = (
        capo_partnercentral_marketing.types.campaign_template_collection.serialize_cbor(
            value["collection"]
        )
    )
    if "aws_services" in value:
        import capo_partnercentral_marketing.types.aws_services_list

        out["AwsServices"] = (
            capo_partnercentral_marketing.types.aws_services_list.serialize_cbor(
                value["aws_services"]
            )
        )
    if "customer_segments" in value:
        import capo_partnercentral_marketing.types.customer_segment_list

        out["CustomerSegments"] = (
            capo_partnercentral_marketing.types.customer_segment_list.serialize_cbor(
                value["customer_segments"]
            )
        )
    if "themes" in value:
        import capo_partnercentral_marketing.types.theme_list

        out["Themes"] = capo_partnercentral_marketing.types.theme_list.serialize_cbor(
            value["themes"]
        )
    if "setup_duration" in value:
        out["SetupDuration"] = value["setup_duration"]
    if "thumbnail_url" in value:
        out["ThumbnailUrl"] = value["thumbnail_url"]
    if "effective_date_begin" in value:
        import capo_partnercentral_marketing.types.timestamp

        out["EffectiveDateBegin"] = (
            capo_partnercentral_marketing.types.timestamp.serialize_cbor(
                value["effective_date_begin"]
            )
        )
    if "asset_templates" in value:
        import capo_partnercentral_marketing.types.campaign_asset_template_list

        out["AssetTemplates"] = (
            capo_partnercentral_marketing.types.campaign_asset_template_list.serialize_cbor(
                value["asset_templates"]
            )
        )
    if "reference_materials" in value:
        import capo_partnercentral_marketing.types.reference_material_list

        out["ReferenceMaterials"] = (
            capo_partnercentral_marketing.types.reference_material_list.serialize_cbor(
                value["reference_materials"]
            )
        )
    if "created_at" in value:
        import capo_partnercentral_marketing.types.timestamp

        out["CreatedAt"] = capo_partnercentral_marketing.types.timestamp.serialize_cbor(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_partnercentral_marketing.types.timestamp

        out["UpdatedAt"] = capo_partnercentral_marketing.types.timestamp.serialize_cbor(
            value["updated_at"]
        )
    return out


def deserialize_cbor(data: dict) -> CampaignTemplate:
    out: CampaignTemplate = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Industry") is not None:
        import capo_partnercentral_marketing.types.industry

        out["industry"] = capo_partnercentral_marketing.types.industry.deserialize_cbor(
            data["Industry"]
        )
    if data.get("UseCase") is not None:
        out["use_case"] = data["UseCase"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("LanguageCode") is not None:
        import capo_partnercentral_marketing.types.asset_language

        out["language_code"] = (
            capo_partnercentral_marketing.types.asset_language.deserialize_cbor(
                data["LanguageCode"]
            )
        )
    if data.get("Collection") is not None:
        import capo_partnercentral_marketing.types.campaign_template_collection

        out["collection"] = (
            capo_partnercentral_marketing.types.campaign_template_collection.deserialize_cbor(
                data["Collection"]
            )
        )
    else:
        import typing

        out["collection"] = typing.cast(
            "capo_partnercentral_marketing.types.campaign_template_collection.CampaignTemplateCollection",
            "",
        )
    if data.get("AwsServices") is not None:
        import capo_partnercentral_marketing.types.aws_services_list

        out["aws_services"] = (
            capo_partnercentral_marketing.types.aws_services_list.deserialize_cbor(
                data["AwsServices"]
            )
        )
    if data.get("CustomerSegments") is not None:
        import capo_partnercentral_marketing.types.customer_segment_list

        out["customer_segments"] = (
            capo_partnercentral_marketing.types.customer_segment_list.deserialize_cbor(
                data["CustomerSegments"]
            )
        )
    if data.get("Themes") is not None:
        import capo_partnercentral_marketing.types.theme_list

        out["themes"] = capo_partnercentral_marketing.types.theme_list.deserialize_cbor(
            data["Themes"]
        )
    if data.get("SetupDuration") is not None:
        out["setup_duration"] = data["SetupDuration"]
    if data.get("ThumbnailUrl") is not None:
        out["thumbnail_url"] = data["ThumbnailUrl"]
    if data.get("EffectiveDateBegin") is not None:
        import capo_partnercentral_marketing.types.timestamp

        out["effective_date_begin"] = (
            capo_partnercentral_marketing.types.timestamp.deserialize_cbor(
                data["EffectiveDateBegin"]
            )
        )
    if data.get("AssetTemplates") is not None:
        import capo_partnercentral_marketing.types.campaign_asset_template_list

        out["asset_templates"] = (
            capo_partnercentral_marketing.types.campaign_asset_template_list.deserialize_cbor(
                data["AssetTemplates"]
            )
        )
    if data.get("ReferenceMaterials") is not None:
        import capo_partnercentral_marketing.types.reference_material_list

        out["reference_materials"] = (
            capo_partnercentral_marketing.types.reference_material_list.deserialize_cbor(
                data["ReferenceMaterials"]
            )
        )
    if data.get("CreatedAt") is not None:
        import capo_partnercentral_marketing.types.timestamp

        out["created_at"] = (
            capo_partnercentral_marketing.types.timestamp.deserialize_cbor(
                data["CreatedAt"]
            )
        )
    if data.get("UpdatedAt") is not None:
        import capo_partnercentral_marketing.types.timestamp

        out["updated_at"] = (
            capo_partnercentral_marketing.types.timestamp.deserialize_cbor(
                data["UpdatedAt"]
            )
        )
    return out


def redact_sensitive(value: CampaignTemplate) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "asset_templates" in value:
        import capo_partnercentral_marketing.types.campaign_asset_template_list

        out["asset_templates"] = (
            capo_partnercentral_marketing.types.campaign_asset_template_list.redact_sensitive(
                value["asset_templates"]
            )
        )
    return out
