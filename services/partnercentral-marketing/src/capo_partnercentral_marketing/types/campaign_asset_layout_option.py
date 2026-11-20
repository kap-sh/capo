"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#CampaignAssetLayoutOption``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.asset_name
    import capo_partnercentral_marketing.types.layout_option_value
    import capo_partnercentral_marketing.types.layout_preview_list
    import capo_partnercentral_marketing.types.template_field_id_list


class CampaignAssetLayoutOption(TypedDict, closed=True):
    value: "capo_partnercentral_marketing.types.layout_option_value.LayoutOptionValue"
    """The value that selects this option."""
    label: NotRequired["capo_partnercentral_marketing.types.asset_name.AssetName"]
    """Display label."""
    field_ids: (
        "capo_partnercentral_marketing.types.template_field_id_list.TemplateFieldIdList"
    )
    """The fields this option uses: the FieldValues that stay in scope when it is selected. Lets a client show an option's form before selecting it."""
    layout_previews: NotRequired[
        "capo_partnercentral_marketing.types.layout_preview_list.LayoutPreviewList"
    ]
    """This option's pages, in page order."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CampaignAssetLayoutOption) -> dict:
    out: dict = {}
    out["Value"] = value["value"]
    if "label" in value:
        out["Label"] = value["label"]
    import capo_partnercentral_marketing.types.template_field_id_list

    out["FieldIds"] = (
        capo_partnercentral_marketing.types.template_field_id_list.serialize_cbor(
            value["field_ids"]
        )
    )
    if "layout_previews" in value:
        import capo_partnercentral_marketing.types.layout_preview_list

        out["LayoutPreviews"] = (
            capo_partnercentral_marketing.types.layout_preview_list.serialize_cbor(
                value["layout_previews"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> CampaignAssetLayoutOption:
    out: CampaignAssetLayoutOption = {}  # type: ignore[typeddict-item]
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    else:
        out["value"] = ""
    if data.get("Label") is not None:
        out["label"] = data["Label"]
    if data.get("FieldIds") is not None:
        import capo_partnercentral_marketing.types.template_field_id_list

        out["field_ids"] = (
            capo_partnercentral_marketing.types.template_field_id_list.deserialize_cbor(
                data["FieldIds"]
            )
        )
    else:
        out["field_ids"] = []
    if data.get("LayoutPreviews") is not None:
        import capo_partnercentral_marketing.types.layout_preview_list

        out["layout_previews"] = (
            capo_partnercentral_marketing.types.layout_preview_list.deserialize_cbor(
                data["LayoutPreviews"]
            )
        )
    return out
