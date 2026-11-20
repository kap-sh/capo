"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#ActivationIssue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.campaign_asset_id_list
    import capo_partnercentral_marketing.types.campaign_asset_state_reason
    import capo_partnercentral_marketing.types.campaign_setting
    import capo_partnercentral_marketing.types.partner_profile_field
    import capo_partnercentral_marketing.types.template_field_id


class ActivationIssue(TypedDict, closed=True):
    code: "capo_partnercentral_marketing.types.campaign_asset_state_reason.CampaignAssetStateReason"
    """What is wrong. Branch on this, not on `Message`."""
    field_id: NotRequired[
        "capo_partnercentral_marketing.types.template_field_id.TemplateFieldId"
    ]
    """The asset field to fix. Present for asset-level issues, except `SEND_MODE_MISSING` and a `CONTENT_REJECTED` that refused the asset's text as a whole rather than one field."""
    campaign_setting: NotRequired[
        "capo_partnercentral_marketing.types.campaign_setting.CampaignSetting"
    ]
    """The `UpdateCampaign` member to set. Present for campaign-level issues."""
    partner_profile_field: NotRequired[
        "capo_partnercentral_marketing.types.partner_profile_field.PartnerProfileField"
    ]
    """The partner-profile value to set or shorten, in AWS Partner Central, or the derived value whose input it is. Present on `PARTNER_PROFILE_FIELD_MISSING` and `PARTNER_PROFILE_FIELD_DOES_NOT_FIT`."""
    affected_asset_ids: NotRequired[
        "capo_partnercentral_marketing.types.campaign_asset_id_list.CampaignAssetIdList"
    ]
    """The assets this campaign-level issue blocks."""
    message: "str"
    """A description for display. Don't parse it."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ActivationIssue) -> dict:
    out: dict = {}
    import capo_partnercentral_marketing.types.campaign_asset_state_reason

    out["Code"] = (
        capo_partnercentral_marketing.types.campaign_asset_state_reason.serialize_cbor(
            value["code"]
        )
    )
    if "field_id" in value:
        out["FieldId"] = value["field_id"]
    if "campaign_setting" in value:
        import capo_partnercentral_marketing.types.campaign_setting

        out["CampaignSetting"] = (
            capo_partnercentral_marketing.types.campaign_setting.serialize_cbor(
                value["campaign_setting"]
            )
        )
    if "partner_profile_field" in value:
        import capo_partnercentral_marketing.types.partner_profile_field

        out["PartnerProfileField"] = (
            capo_partnercentral_marketing.types.partner_profile_field.serialize_cbor(
                value["partner_profile_field"]
            )
        )
    if "affected_asset_ids" in value:
        import capo_partnercentral_marketing.types.campaign_asset_id_list

        out["AffectedAssetIds"] = (
            capo_partnercentral_marketing.types.campaign_asset_id_list.serialize_cbor(
                value["affected_asset_ids"]
            )
        )
    out["Message"] = value["message"]
    return out


def deserialize_cbor(data: dict) -> ActivationIssue:
    out: ActivationIssue = {}  # type: ignore[typeddict-item]
    if data.get("Code") is not None:
        import capo_partnercentral_marketing.types.campaign_asset_state_reason

        out["code"] = (
            capo_partnercentral_marketing.types.campaign_asset_state_reason.deserialize_cbor(
                data["Code"]
            )
        )
    else:
        import typing

        out["code"] = typing.cast(
            "capo_partnercentral_marketing.types.campaign_asset_state_reason.CampaignAssetStateReason",
            "",
        )
    if data.get("FieldId") is not None:
        out["field_id"] = data["FieldId"]
    if data.get("CampaignSetting") is not None:
        import capo_partnercentral_marketing.types.campaign_setting

        out["campaign_setting"] = (
            capo_partnercentral_marketing.types.campaign_setting.deserialize_cbor(
                data["CampaignSetting"]
            )
        )
    if data.get("PartnerProfileField") is not None:
        import capo_partnercentral_marketing.types.partner_profile_field

        out["partner_profile_field"] = (
            capo_partnercentral_marketing.types.partner_profile_field.deserialize_cbor(
                data["PartnerProfileField"]
            )
        )
    if data.get("AffectedAssetIds") is not None:
        import capo_partnercentral_marketing.types.campaign_asset_id_list

        out["affected_asset_ids"] = (
            capo_partnercentral_marketing.types.campaign_asset_id_list.deserialize_cbor(
                data["AffectedAssetIds"]
            )
        )
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        out["message"] = ""
    return out
