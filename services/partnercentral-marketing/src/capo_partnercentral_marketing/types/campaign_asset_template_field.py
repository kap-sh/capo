"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#CampaignAssetTemplateField``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.campaign_setting
    import capo_partnercentral_marketing.types.field_type
    import capo_partnercentral_marketing.types.partner_profile_field
    import capo_partnercentral_marketing.types.template_field_description
    import capo_partnercentral_marketing.types.template_field_id
    import capo_partnercentral_marketing.types.template_field_label
    import capo_partnercentral_marketing.types.template_field_section


class CampaignAssetTemplateField(TypedDict, closed=True):
    field_id: "capo_partnercentral_marketing.types.template_field_id.TemplateFieldId"
    """The field identifier; matches a {{fieldId}} slot in the layout."""
    label: NotRequired[
        "capo_partnercentral_marketing.types.template_field_label.TemplateFieldLabel"
    ]
    """Human-readable name for the field, for display. Authored in the template policy, never derived from the field id or the source layout's field name: the id is a slug (`Page_2_Title`) and is not meant to be shown to a partner. Absent on fields imported before labels existed."""
    description: NotRequired[
        "capo_partnercentral_marketing.types.template_field_description.TemplateFieldDescription"
    ]
    """What belongs in this field, in English: its role in the asset and what good content for it is (for example "Headline that names the customer and leads with a source-backed statistic"). AWS-authored with the template; never written by a partner. Absent when the template carries none, never empty. Pinned onto the asset with the field, so a corrected description reaches assets created after the correction."""
    section: NotRequired[
        "capo_partnercentral_marketing.types.template_field_section.TemplateFieldSection"
    ]
    """Layout section the field belongs to."""
    page: NotRequired["int"]
    """One-based page number, for paginated layouts (print documents)."""
    required: NotRequired["bool"]
    """Whether the field must be filled before the asset can be activated. Derived from DG policy — never inherited from an upstream authoring system. Required for activation, not for saving: `UpdateCampaignAsset` accepts partial content and may clear a required field. An unfilled required field appears in the asset's `ActivationIssues` as `REQUIRED_FIELD_MISSING`, and activation refuses the asset with the same code. A text field is filled only by a non-blank value, and a rich-text field only by a value with non-blank text; a `Placeholder` never fills one. An image field is filled by the partner's image or by the template's `DefaultValue`. A field the campaign fills (`CampaignSetting`) or the partner's profile fills (`PartnerProfileField`) is never unfilled on the asset."""
    type: "capo_partnercentral_marketing.types.field_type.FieldType"
    """The field kind, with that kind's constraints, placeholder or default."""
    campaign_setting: NotRequired[
        "capo_partnercentral_marketing.types.campaign_setting.CampaignSetting"
    ]
    """The campaign setting this field shows, when it shows one: the partner sets it once on the campaign and every asset displays it. Present only on such fields. A client shows the field as "Set on the campaign", linking to the campaign, rather than as an input. `UpdateCampaignAsset` refuses a value for it with `FIELD_SET_ON_CAMPAIGN`, and on an asset the field carries no value: read it from the named member of `GetCampaign`'s `Campaign`."""
    partner_profile_field: NotRequired[
        "capo_partnercentral_marketing.types.partner_profile_field.PartnerProfileField"
    ]
    """The partner-profile value this field shows, when it shows one: the partner's AWS Partner Central profile supplies it, and every asset of every campaign displays it. Present only on such fields. A client shows the field as "From your Partner Central profile" rather than as an input. `UpdateCampaignAsset` refuses a value for it with `FIELD_FROM_PARTNER_PROFILE`. On a read the field carries the partner's resolved value — the logo as its URL, the name and website as text — so a slot renders from this list alone; `GetCampaign`'s `Campaign$PartnerProfile` carries the same three values."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CampaignAssetTemplateField) -> dict:
    out: dict = {}
    out["FieldId"] = value["field_id"]
    if "label" in value:
        out["Label"] = value["label"]
    if "description" in value:
        out["Description"] = value["description"]
    if "section" in value:
        import capo_partnercentral_marketing.types.template_field_section

        out["Section"] = (
            capo_partnercentral_marketing.types.template_field_section.serialize_cbor(
                value["section"]
            )
        )
    if "page" in value:
        out["Page"] = value["page"]
    if "required" in value:
        out["Required"] = value["required"]
    import capo_partnercentral_marketing.types.field_type

    out["Type"] = capo_partnercentral_marketing.types.field_type.serialize_cbor(
        value["type"]
    )
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
    return out


def deserialize_cbor(data: dict) -> CampaignAssetTemplateField:
    out: CampaignAssetTemplateField = {}  # type: ignore[typeddict-item]
    if data.get("FieldId") is not None:
        out["field_id"] = data["FieldId"]
    else:
        out["field_id"] = ""
    if data.get("Label") is not None:
        out["label"] = data["Label"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Section") is not None:
        import capo_partnercentral_marketing.types.template_field_section

        out["section"] = (
            capo_partnercentral_marketing.types.template_field_section.deserialize_cbor(
                data["Section"]
            )
        )
    if data.get("Page") is not None:
        out["page"] = data["Page"]
    if data.get("Required") is not None:
        out["required"] = data["Required"]
    if data.get("Type") is not None:
        import capo_partnercentral_marketing.types.field_type

        out["type"] = capo_partnercentral_marketing.types.field_type.deserialize_cbor(
            data["Type"]
        )
    else:
        out["type"] = {"$unknown": {"name": ""}}
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
    return out


def redact_sensitive(value: CampaignAssetTemplateField) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "type" in value:
        import capo_partnercentral_marketing.types.field_type

        out["type"] = capo_partnercentral_marketing.types.field_type.redact_sensitive(
            value["type"]
        )
    return out
