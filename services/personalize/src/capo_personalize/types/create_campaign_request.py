"""Generated from Smithy shape ``com.amazonaws.personalize#CreateCampaignRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_personalize.errors import DeserializationError

if TYPE_CHECKING:
    import capo_personalize.types.arn
    import capo_personalize.types.campaign_config
    import capo_personalize.types.name
    import capo_personalize.types.tags
    import capo_personalize.types.transactions_per_second


class CreateCampaignRequest(TypedDict, closed=True):
    name: "capo_personalize.types.name.Name"
    """<p>A name for the new campaign. The campaign name must be unique within your account.</p>"""
    solution_version_arn: "capo_personalize.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the trained model to deploy with the campaign. To specify the latest solution version of your solution, specify the ARN of your <i>solution</i> in <code>SolutionArn/$LATEST</code> format. You must use this format if you set <code>syncWithLatestSolutionVersion</code> to <code>True</code> in the <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_CampaignConfig.html">CampaignConfig</a>. </p> <p> To deploy a model that isn't the latest solution version of your solution, specify the ARN of the solution version. </p> <p> For more information about automatic campaign updates, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/campaigns.html#create-campaign-automatic-latest-sv-update">Enabling automatic campaign updates</a>. </p>"""
    min_provisioned_tps: NotRequired[
        "capo_personalize.types.transactions_per_second.TransactionsPerSecond"
    ]
    """<p>Specifies the requested minimum provisioned transactions (recommendations) per second that Amazon Personalize will support. A high <code>minProvisionedTPS</code> will increase your bill. We recommend starting with 1 for <code>minProvisionedTPS</code> (the default). Track your usage using Amazon CloudWatch metrics, and increase the <code>minProvisionedTPS</code> as necessary.</p>"""
    campaign_config: NotRequired[
        "capo_personalize.types.campaign_config.CampaignConfig"
    ]
    """<p>The configuration details of a campaign.</p>"""
    tags: NotRequired["capo_personalize.types.tags.Tags"]
    """<p>A list of <a href="https://docs.aws.amazon.com/personalize/latest/dg/tagging-resources.html">tags</a> to apply to the campaign.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateCampaignRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["solutionVersionArn"] = value["solution_version_arn"]
    if "min_provisioned_tps" in value:
        out["minProvisionedTPS"] = value["min_provisioned_tps"]
    if "campaign_config" in value:
        import capo_personalize.types.campaign_config

        out["campaignConfig"] = (
            capo_personalize.types.campaign_config.serialize_aws_json_1_1(
                value["campaign_config"]
            )
        )
    if "tags" in value:
        import capo_personalize.types.tags

        out["tags"] = capo_personalize.types.tags.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateCampaignRequest:
    out: CreateCampaignRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateCampaignRequest.name required")
    if data.get("solutionVersionArn") is not None:
        out["solution_version_arn"] = data["solutionVersionArn"]
    else:
        raise DeserializationError(
            "CreateCampaignRequest.solution_version_arn required"
        )
    if data.get("minProvisionedTPS") is not None:
        out["min_provisioned_tps"] = data["minProvisionedTPS"]
    if data.get("campaignConfig") is not None:
        import capo_personalize.types.campaign_config

        out["campaign_config"] = (
            capo_personalize.types.campaign_config.deserialize_aws_json_1_1(
                data["campaignConfig"]
            )
        )
    if data.get("tags") is not None:
        import capo_personalize.types.tags

        out["tags"] = capo_personalize.types.tags.deserialize_aws_json_1_1(data["tags"])
    return out
