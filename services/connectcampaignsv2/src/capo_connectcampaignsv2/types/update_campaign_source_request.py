"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#UpdateCampaignSourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.campaign_id
    import capo_connectcampaignsv2.types.source


class UpdateCampaignSourceRequest(TypedDict, closed=True):
    id: "capo_connectcampaignsv2.types.campaign_id.CampaignId"
    source: "capo_connectcampaignsv2.types.source.Source"


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCampaignSourceRequest) -> dict:
    out: dict = {}
    import capo_connectcampaignsv2.types.source

    out["source"] = capo_connectcampaignsv2.types.source.serialize_json(value["source"])
    return out


def deserialize_json(data: dict) -> UpdateCampaignSourceRequest:
    out: UpdateCampaignSourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("source") is not None:
        import capo_connectcampaignsv2.types.source

        out["source"] = capo_connectcampaignsv2.types.source.deserialize_json(
            data["source"]
        )
    else:
        out["source"] = {"$unknown": {"name": ""}}
    return out
