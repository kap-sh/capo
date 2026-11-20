"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#CampaignTemplateSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.asset_language
    import capo_partnercentral_marketing.types.aws_services_list
    import capo_partnercentral_marketing.types.campaign_template_collection
    import capo_partnercentral_marketing.types.campaign_template_description
    import capo_partnercentral_marketing.types.campaign_template_id
    import capo_partnercentral_marketing.types.customer_segment_list
    import capo_partnercentral_marketing.types.industry
    import capo_partnercentral_marketing.types.template_name
    import capo_partnercentral_marketing.types.theme_list


class CampaignTemplateSummary(TypedDict, closed=True):
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
    """The campaign overview. See `CampaignTemplate$Description`."""
    language_code: NotRequired[
        "capo_partnercentral_marketing.types.asset_language.AssetLanguage"
    ]
    """Language the template is authored in. See `CampaignTemplate$LanguageCode`."""
    collection: "capo_partnercentral_marketing.types.campaign_template_collection.CampaignTemplateCollection"
    """The browsing context the template is listed in. See `CampaignTemplate$Collection`."""
    aws_services: NotRequired[
        "capo_partnercentral_marketing.types.aws_services_list.AwsServicesList"
    ]
    """AWS services the template promotes."""
    customer_segments: NotRequired[
        "capo_partnercentral_marketing.types.customer_segment_list.CustomerSegmentList"
    ]
    """The customer segments the template is written for. See `CampaignTemplate$CustomerSegments`."""
    themes: NotRequired["capo_partnercentral_marketing.types.theme_list.ThemeList"]
    """The template's marketing themes. See `CampaignTemplate$Themes`."""
    thumbnail_url: NotRequired["str"]
    """Thumbnail URL."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CampaignTemplateSummary) -> dict:
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
    if "thumbnail_url" in value:
        out["ThumbnailUrl"] = value["thumbnail_url"]
    return out


def deserialize_cbor(data: dict) -> CampaignTemplateSummary:
    out: CampaignTemplateSummary = {}  # type: ignore[typeddict-item]
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
    if data.get("ThumbnailUrl") is not None:
        out["thumbnail_url"] = data["ThumbnailUrl"]
    return out
