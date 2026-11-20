"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#CampaignAssetLayout``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.campaign_asset_layout_option_list
    import capo_partnercentral_marketing.types.layout_option_value


class CampaignAssetLayout(TypedDict, closed=True):
    selected: NotRequired[
        "capo_partnercentral_marketing.types.layout_option_value.LayoutOptionValue"
    ]
    """The selected option's value. An asset is created with its first option selected; an asset created before that rule, with none stored, reports and activates its first option."""
    options: "capo_partnercentral_marketing.types.campaign_asset_layout_option_list.CampaignAssetLayoutOptionList"
    """Every option the asset was created with, in authored order."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CampaignAssetLayout) -> dict:
    out: dict = {}
    if "selected" in value:
        out["Selected"] = value["selected"]
    import capo_partnercentral_marketing.types.campaign_asset_layout_option_list

    out["Options"] = (
        capo_partnercentral_marketing.types.campaign_asset_layout_option_list.serialize_cbor(
            value["options"]
        )
    )
    return out


def deserialize_cbor(data: dict) -> CampaignAssetLayout:
    out: CampaignAssetLayout = {}  # type: ignore[typeddict-item]
    if data.get("Selected") is not None:
        out["selected"] = data["Selected"]
    if data.get("Options") is not None:
        import capo_partnercentral_marketing.types.campaign_asset_layout_option_list

        out["options"] = (
            capo_partnercentral_marketing.types.campaign_asset_layout_option_list.deserialize_cbor(
                data["Options"]
            )
        )
    else:
        out["options"] = []
    return out
