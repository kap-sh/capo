"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#CampaignAssetFieldValue``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_partnercentral_marketing.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.campaign_asset_template_field
    import capo_partnercentral_marketing.types.template_field_value


class CampaignAssetFieldValue(TypedDict, closed=True):
    field: "capo_partnercentral_marketing.types.campaign_asset_template_field.CampaignAssetTemplateField"
    """The field schema (snapshot from the template)."""
    value: NotRequired[
        "capo_partnercentral_marketing.types.template_field_value.TemplateFieldValue"
    ]
    """The field's current value; the variant matches the field's type."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CampaignAssetFieldValue) -> dict:
    out: dict = {}
    import capo_partnercentral_marketing.types.campaign_asset_template_field

    out["Field"] = (
        capo_partnercentral_marketing.types.campaign_asset_template_field.serialize_cbor(
            value["field"]
        )
    )
    if "value" in value:
        import capo_partnercentral_marketing.types.template_field_value

        out["Value"] = (
            capo_partnercentral_marketing.types.template_field_value.serialize_cbor(
                value["value"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> CampaignAssetFieldValue:
    out: CampaignAssetFieldValue = {}  # type: ignore[typeddict-item]
    if data.get("Field") is not None:
        import capo_partnercentral_marketing.types.campaign_asset_template_field

        out["field"] = (
            capo_partnercentral_marketing.types.campaign_asset_template_field.deserialize_cbor(
                data["Field"]
            )
        )
    else:
        raise DeserializationError("CampaignAssetFieldValue.field required")
    if data.get("Value") is not None:
        import capo_partnercentral_marketing.types.template_field_value

        out["value"] = (
            capo_partnercentral_marketing.types.template_field_value.deserialize_cbor(
                data["Value"]
            )
        )
    return out


def redact_sensitive(value: CampaignAssetFieldValue) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "field" in value:
        import capo_partnercentral_marketing.types.campaign_asset_template_field

        out["field"] = (
            capo_partnercentral_marketing.types.campaign_asset_template_field.redact_sensitive(
                value["field"]
            )
        )
    if "value" in value:
        import capo_partnercentral_marketing.types.template_field_value

        out["value"] = (
            capo_partnercentral_marketing.types.template_field_value.redact_sensitive(
                value["value"]
            )
        )
    return out
