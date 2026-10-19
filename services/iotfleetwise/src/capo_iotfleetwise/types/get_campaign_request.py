"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#GetCampaignRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotfleetwise.types.campaign_name


class GetCampaignRequest(TypedDict, closed=True):
    name: "capo_iotfleetwise.types.campaign_name.campaignName"
    """<p> The name of the campaign to retrieve information about. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetCampaignRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetCampaignRequest:
    out: GetCampaignRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    return out
