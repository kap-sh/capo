"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#TemplateFieldValue``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_partnercentral_marketing.errors import (
    DeserializationError,
    SerializationError,
)
from capo_partnercentral_marketing.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.asset_body_content
    import capo_partnercentral_marketing.types.campaign_asset_id
    import capo_partnercentral_marketing.types.campaign_asset_image_source
    import capo_partnercentral_marketing.types.file_reference


class TemplateFieldValueTextMember(TypedDict, closed=True):
    Text: "capo_partnercentral_marketing.types.asset_body_content.AssetBodyContent"


class TemplateFieldValueImageReferenceMember(TypedDict, closed=True):
    ImageReference: "capo_partnercentral_marketing.types.file_reference.FileReference"


class TemplateFieldValueLinkedAssetIdMember(TypedDict, closed=True):
    LinkedAssetId: (
        "capo_partnercentral_marketing.types.campaign_asset_id.CampaignAssetId"
    )


class TemplateFieldValueCampaignAssetImageMember(TypedDict, closed=True):
    CampaignAssetImage: "capo_partnercentral_marketing.types.campaign_asset_image_source.CampaignAssetImageSource"


TemplateFieldValue: TypeAlias = (
    TemplateFieldValueTextMember
    | TemplateFieldValueImageReferenceMember
    | TemplateFieldValueLinkedAssetIdMember
    | TemplateFieldValueCampaignAssetImageMember
    | UnknownUnionMember
)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TemplateFieldValue) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"TemplateFieldValue: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "Text" in value:
        return {"Text": value["Text"]}
    elif "ImageReference" in value:
        return {"ImageReference": value["ImageReference"]}
    elif "LinkedAssetId" in value:
        return {"LinkedAssetId": value["LinkedAssetId"]}
    elif "CampaignAssetImage" in value:
        import capo_partnercentral_marketing.types.campaign_asset_image_source

        return {
            "CampaignAssetImage": capo_partnercentral_marketing.types.campaign_asset_image_source.serialize_cbor(
                value["CampaignAssetImage"]
            )
        }
    else:
        raise SerializationError("TemplateFieldValue: no variant present")


def deserialize_cbor(data: dict) -> TemplateFieldValue:
    if data.get("Text") is not None:
        return {"Text": data["Text"]}
    elif data.get("ImageReference") is not None:
        return {"ImageReference": data["ImageReference"]}
    elif data.get("LinkedAssetId") is not None:
        return {"LinkedAssetId": data["LinkedAssetId"]}
    elif data.get("CampaignAssetImage") is not None:
        import capo_partnercentral_marketing.types.campaign_asset_image_source

        return {
            "CampaignAssetImage": capo_partnercentral_marketing.types.campaign_asset_image_source.deserialize_cbor(
                data["CampaignAssetImage"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("TemplateFieldValue: no recognized variant key")


def redact_sensitive(value: TemplateFieldValue) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "Text" in value:
        out["Text"] = "*** Sensitive Data Redacted ***"
    return out
