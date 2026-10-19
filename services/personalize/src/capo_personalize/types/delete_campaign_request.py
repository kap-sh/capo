"""Generated from Smithy shape ``com.amazonaws.personalize#DeleteCampaignRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_personalize.types.arn


class DeleteCampaignRequest(TypedDict, closed=True):
    campaign_arn: "capo_personalize.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the campaign to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteCampaignRequest) -> dict:
    out: dict = {}
    out["campaignArn"] = value["campaign_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteCampaignRequest:
    out: DeleteCampaignRequest = {}  # type: ignore[typeddict-item]
    if data.get("campaignArn") is not None:
        out["campaign_arn"] = data["campaignArn"]
    else:
        out["campaign_arn"] = ""
    return out
