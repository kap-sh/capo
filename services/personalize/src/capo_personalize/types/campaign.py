"""Generated from Smithy shape ``com.amazonaws.personalize#Campaign``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_personalize.types.arn
    import capo_personalize.types.campaign_config
    import capo_personalize.types.campaign_update_summary
    import capo_personalize.types.date
    import capo_personalize.types.failure_reason
    import capo_personalize.types.name
    import capo_personalize.types.status
    import capo_personalize.types.transactions_per_second


class Campaign(TypedDict, closed=True):
    name: NotRequired["capo_personalize.types.name.Name"]
    """<p>The name of the campaign.</p>"""
    campaign_arn: NotRequired["capo_personalize.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the campaign. </p>"""
    solution_version_arn: NotRequired["capo_personalize.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the solution version the campaign uses.</p>"""
    min_provisioned_tps: NotRequired[
        "capo_personalize.types.transactions_per_second.TransactionsPerSecond"
    ]
    """<p>Specifies the requested minimum provisioned transactions (recommendations) per second. A high <code>minProvisionedTPS</code> will increase your bill. We recommend starting with 1 for <code>minProvisionedTPS</code> (the default). Track your usage using Amazon CloudWatch metrics, and increase the <code>minProvisionedTPS</code> as necessary.</p>"""
    campaign_config: NotRequired[
        "capo_personalize.types.campaign_config.CampaignConfig"
    ]
    """<p>The configuration details of a campaign.</p>"""
    status: NotRequired["capo_personalize.types.status.Status"]
    """<p>The status of the campaign.</p> <p>A campaign can be in one of the following states:</p> <ul> <li> <p>CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED</p> </li> <li> <p>DELETE PENDING > DELETE IN_PROGRESS</p> </li> </ul>"""
    failure_reason: NotRequired["capo_personalize.types.failure_reason.FailureReason"]
    """<p>If a campaign fails, the reason behind the failure.</p>"""
    creation_date_time: NotRequired["capo_personalize.types.date.Date"]
    """<p>The date and time (in Unix format) that the campaign was created.</p>"""
    last_updated_date_time: NotRequired["capo_personalize.types.date.Date"]
    """<p>The date and time (in Unix format) that the campaign was last updated.</p>"""
    latest_campaign_update: NotRequired[
        "capo_personalize.types.campaign_update_summary.CampaignUpdateSummary"
    ]
    """<p>Provides a summary of the properties of a campaign update. For a complete listing, call the <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeCampaign.html">DescribeCampaign</a> API.</p> <note> <p>The <code>latestCampaignUpdate</code> field is only returned when the campaign has had at least one <code>UpdateCampaign</code> call. </p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Campaign) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "campaign_arn" in value:
        out["campaignArn"] = value["campaign_arn"]
    if "solution_version_arn" in value:
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
    if "status" in value:
        out["status"] = value["status"]
    if "failure_reason" in value:
        out["failureReason"] = value["failure_reason"]
    if "creation_date_time" in value:
        import capo_personalize.types.date

        out["creationDateTime"] = capo_personalize.types.date.serialize_aws_json_1_1(
            value["creation_date_time"]
        )
    if "last_updated_date_time" in value:
        import capo_personalize.types.date

        out["lastUpdatedDateTime"] = capo_personalize.types.date.serialize_aws_json_1_1(
            value["last_updated_date_time"]
        )
    if "latest_campaign_update" in value:
        import capo_personalize.types.campaign_update_summary

        out["latestCampaignUpdate"] = (
            capo_personalize.types.campaign_update_summary.serialize_aws_json_1_1(
                value["latest_campaign_update"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Campaign:
    out: Campaign = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("campaignArn") is not None:
        out["campaign_arn"] = data["campaignArn"]
    if data.get("solutionVersionArn") is not None:
        out["solution_version_arn"] = data["solutionVersionArn"]
    if data.get("minProvisionedTPS") is not None:
        out["min_provisioned_tps"] = data["minProvisionedTPS"]
    if data.get("campaignConfig") is not None:
        import capo_personalize.types.campaign_config

        out["campaign_config"] = (
            capo_personalize.types.campaign_config.deserialize_aws_json_1_1(
                data["campaignConfig"]
            )
        )
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("failureReason") is not None:
        out["failure_reason"] = data["failureReason"]
    if data.get("creationDateTime") is not None:
        import capo_personalize.types.date

        out["creation_date_time"] = (
            capo_personalize.types.date.deserialize_aws_json_1_1(
                data["creationDateTime"]
            )
        )
    if data.get("lastUpdatedDateTime") is not None:
        import capo_personalize.types.date

        out["last_updated_date_time"] = (
            capo_personalize.types.date.deserialize_aws_json_1_1(
                data["lastUpdatedDateTime"]
            )
        )
    if data.get("latestCampaignUpdate") is not None:
        import capo_personalize.types.campaign_update_summary

        out["latest_campaign_update"] = (
            capo_personalize.types.campaign_update_summary.deserialize_aws_json_1_1(
                data["latestCampaignUpdate"]
            )
        )
    return out
